<template>
  <div class="max-w-2xl mx-auto p-4">
    <h2 class="text-2xl font-bold mb-4 text-center">Оформление заказа</h2>

    <!-- Индикатор шагов -->
    <ul class="steps steps-horizontal mb-6 w-full">
      <li :class="['step', currentStep > 1 ? 'step-success' : 'step-success']">Корзина</li>
      <li :class="['step', currentStep > 2 ? 'step-success' : (currentStep === 2 ? 'step-success' : 'step-neutral')]">Данные</li>
      <li :class="['step', currentStep === 3 ? 'step-success' : 'step-neutral']">Готово</li>

    </ul>


    <!-- Шаг 1: подтверждение товаров в корзине -->
    <div v-if="currentStep === 1" class="space-y-4">
      <div v-for="item in cartItems" :key="item.productId" class="flex justify-between items-center border-b pb-4 border-teal-600">
        <span class="font-semibold">{{ item.name }} (x{{ item.quantity }})</span>
        <span>{{ item.price * item.quantity }} ₽</span>
      </div>
      <div v-if="cartItems.length === 0" class="text-center text-gray-600">
        Ваша корзина пуста.
      </div>
      <button
          class="btn btn-block bg-teal-600 border-none hover:shadow-none hover:bg-teal-700 m-1 active:bg-teal-700 mt-4"
          :disabled="cartItems.length === 0"
          @click="currentStep = 2">
        Подтвердить товары
      </button>
    </div>

    <!-- Шаг 2: форма с контактными данными -->
    <div v-if="currentStep === 2" class="space-y-4">
      <div v-if="!isAuth">
        <div class="alert text-black font-semibold alert-warning place-content-center opacity-75">
         <p class="text-center">Для оформления заказа нужно войти или зарегистрироваться</p>
        </div>
        <div class="flex gap-2 m-1 justify-center">
          <button to="/auth/login" class="btn btn-ghost w-60 bg-teal-600 border-none hover:shadow-none hover:bg-teal-700 m-1 active:bg-teal-700 mt-8" v-on:click="open_login_modal && open_login_modal()">Войти</button>
          <button to="/auth/register" class="btn btn-ghost w-60 bg-teal-600 border-none hover:shadow-none hover:bg-teal-700 m-1 active:bg-teal-700 mt-8" v-on:click="open_auth_modal && open_auth_modal()">Зарегистрироваться</button>
        </div>
        <button class="btn btn-block bg-teal-600 border-none hover:shadow-none hover:bg-teal-700 active:bg-teal-700 mt-8" @click="currentStep = 1">Назад к оформлению</button>
      </div>
      <div v-else class="flex flex-col items-center gap-3">
        <div class="text-green-600 text-lg font-semibold  flex items-center gap-2">
          <span class="text-2xl">✅</span> Валидация подтверждена, вы можете оформить заказ!
        </div>
        <button class="btn btn-block bg-teal-600 border-none hover:shadow-none hover:bg-teal-700 m-1 active:bg-teal-700 mt-8" @click="submitOrder">Оформить заказ</button>
        <button class="btn btn-block bg-teal-600 border-none hover:shadow-none hover:bg-teal-700 m-1 active:bg-teal-700 mt-8" @click="currentStep = 1">Назад к оформлению</button>
      </div>
    </div>

    <!-- Шаг 3: подтверждение результата -->
    <div v-if="currentStep === 3" class="text-center space-y-4">
      <div v-if="orderSuccess" class="text-green-600 text-xl font-semibold">
        ✅ {{ orderSuccess }}

        <dialog id="orderSuccessModal" class="modal">
          <div class="modal-box">
            <h3 class="text-xl font-bold text-white">Спасибо за заказ, ожидайте!</h3>
            <p class="py-4 text-start font-medium text-white text-[16px]">Возврат тары осуществляется при следующей доставке.<br> Просто передайте пустые бутыли курьеру!</p>
            <div class="modal-action">
              <form method="dialog">
                <button class="btn btn-block bg-teal-600 border-none hover:shadow-none hover:bg-teal-700 m-1 active:bg-teal-700">Закрыть</button>
              </form>
            </div>
          </div>
        </dialog>

      </div>
      <div v-if="orderError" class="text-error text-xl font-medium">
        ⚠️ {{ orderError }}
      </div>
      <!-- Кнопки навигации после заказа -->
      <div class="flex flex-col sm:flex-row sm:justify-center gap-2 mt-4">
        <NuxtLink to="/" class="btn btn-ghost bg-teal-600 border-none hover:shadow-none hover:bg-teal-700 m-1 active:bg-teal-700 mt-8">На главную</NuxtLink>
        <NuxtLink v-if="isAuth" to="/account/profile" class="btn btn-ghost bg-teal-600 border-none hover:shadow-none hover:bg-teal-700 m-1 active:bg-teal-700 mt-8">В профиль</NuxtLink>
        <NuxtLink to="/water" class="btn btn-ghost bg-teal-600 border-none hover:shadow-none hover:bg-teal-700 m-1 active:bg-teal-700 mt-8">К товарам</NuxtLink>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref, computed, onMounted } from 'vue'
import { useRouter, useState } from '#app'

interface CartItem { productId: number; name: string; price: number; quantity: number }

const router = useRouter()
const currentStep = ref(1)
const cartItems = ref<CartItem[]>([])




const name = ref('')
const phone = ref('')
const email = ref('')
const orderSuccess = ref<string | null>(null)
const orderError = ref<string | null>(null)
const nameError = ref<string | null>(null)
const phoneError = ref<string | null>(null)
const emailError = ref<string | null>(null)

const user = useState('authUser')
const isAuth = computed(() => user.value && user.value.id)

onMounted(() => {
  if (process.client) {
    const saved = localStorage.getItem('cart')
    cartItems.value = saved ? JSON.parse(saved) : []
  }
  if (isAuth.value) {
    name.value = user.value.full_name || user.value.name || ''
    email.value = user.value.email || ''
  }
})



watch(orderSuccess, async (val) => {
  if (val) {
    await nextTick();
    const dlg = document.getElementById('orderSuccessModal');
    if (dlg) dlg.showModal();
  }
});

const total = computed(() => cartItems.value.reduce((acc, item) => acc + item.price * item.quantity, 0))

const submitOrder = async () => {
  orderSuccess.value = orderError.value = null
  // Проверяем, что пользователь точно залогинен (должно быть всегда на этом шаге)
  if (!isAuth.value) {
    orderError.value = 'Вы должны войти или зарегистрироваться для оформления заказа'
    return
  }
  try {
    const orderData = {
      user_id: user.value.id, // только id!
      items: cartItems.value.map(item => ({
        product_id: item.productId,
        quantity: item.quantity,
        price: item.price,
      }))
    }
    await $fetch('http://0.0.0.0:80/orders/', { method: 'POST', body: orderData })
    orderSuccess.value = 'Заказ успешно оформлен!'
    cartItems.value = []
    if (process.client) localStorage.removeItem('cart')
    window.refreshCart && window.refreshCart()
  } catch (err: any) {
    orderError.value = 'Не удалось оформить заказ. ' + (err.response?.data?.message || err.message || '')
  } finally {
    currentStep.value = 3
  }
}

const open_auth_modal = inject<() => void>('open_auth_modal')
const open_login_modal = inject<() => void>('open_login_modal')
</script>

