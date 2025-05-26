<template>
  <div class="max-w-2xl mx-auto p-4">
    <h2 class="text-2xl font-bold mb-4 text-center">Оформление заказа</h2>

    <!-- Индикатор шагов -->
    <ul class="steps steps-horizontal mb-6">
      <li :class="['step', currentStep > 1 ? 'step-primary' : 'step-neutral']">Корзина</li>
      <li :class="['step', currentStep > 2 ? 'step-primary' : (currentStep === 2 ? 'step-primary' : 'step-neutral')]">Данные</li>
      <li :class="['step', currentStep === 3 ? 'step-primary' : 'step-neutral']">Готово</li>
    </ul>

    <!-- Шаг 1: подтверждение товаров в корзине -->
    <div v-if="currentStep === 1" class="space-y-4">
      <div v-for="item in cartItems" :key="item.productId" class="flex justify-between items-center border-b pb-2">
        <span>{{ item.name }} (x{{ item.quantity }})</span>
        <span>{{ item.price * item.quantity }} ₽</span>
      </div>
      <div v-if="cartItems.length === 0" class="text-center text-gray-600">
        Ваша корзина пуста.
      </div>
      <button
          class="btn btn-primary mt-4 w-full"
          :disabled="cartItems.length === 0"
          @click="currentStep = 2">
        Подтвердить товары
      </button>
    </div>

    <!-- Шаг 2: форма с контактными данными -->
    <div v-if="currentStep === 2" class="space-y-4">
      <div v-if="!isAuth">
        <div class="alert alert-info text-center">
          Для оформления заказа нужно войти или зарегистрироваться
        </div>
        <div class="flex gap-2 justify-center">
          <NuxtLink to="/auth/login" class="btn btn-primary">Войти</NuxtLink>
          <NuxtLink to="/auth/register" class="btn btn-accent">Зарегистрироваться</NuxtLink>
        </div>
        <button class="btn btn-outline w-full mt-2" @click="currentStep = 1">← Назад в корзину</button>
      </div>
      <div v-else class="flex flex-col items-center gap-3">
        <div class="text-green-600 text-lg font-medium flex items-center gap-2">
          <span class="text-2xl">✅</span> Валидация подтверждена, вы можете оформить заказ!
        </div>
        <button class="btn btn-primary w-full mt-2" @click="submitOrder">Оформить заказ</button>
        <button class="btn btn-outline w-full" @click="currentStep = 1">← Назад в корзину</button>
      </div>
    </div>

    <!-- Шаг 3: подтверждение результата -->
    <div v-if="currentStep === 3" class="text-center space-y-4">
      <div v-if="orderSuccess" class="text-green-600 text-xl font-medium">
        ✅ {{ orderSuccess }}
      </div>
      <div v-if="orderError" class="text-error text-xl font-medium">
        ⚠️ {{ orderError }}
      </div>
      <!-- Кнопки навигации после заказа -->
      <div class="flex flex-col sm:flex-row sm:justify-center gap-2 mt-4">
        <NuxtLink to="/" class="btn">На главную</NuxtLink>
        <NuxtLink v-if="isAuth" to="/account/profile" class="btn">В профиль</NuxtLink>
        <NuxtLink to="/water" class="btn">К товарам</NuxtLink>
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
    orderSuccess.value = 'Заказ успешно оформлен! Спасибо за покупку.'
    cartItems.value = []
    if (process.client) localStorage.removeItem('cart')
  } catch (err: any) {
    orderError.value = 'Не удалось оформить заказ. ' + (err.response?.data?.message || err.message || '')
  } finally {
    currentStep.value = 3
  }
}
</script>

