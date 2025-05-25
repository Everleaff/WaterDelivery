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
      <div class="form-control">
        <label class="label"><span class="label-text">Имя</span></label>
        <input type="text" v-model="name" :class="['input w-full', nameError && 'input-error']" />
        <span v-if="nameError" class="text-error text-sm">{{ nameError }}</span>
      </div>
      <div class="form-control">
        <label class="label"><span class="label-text">Телефон</span></label>
        <input type="tel" v-model="phone" :class="['input w-full', phoneError && 'input-error']" placeholder="+7 ___ ___ __ __" />
        <span v-if="phoneError" class="text-error text-sm">{{ phoneError }}</span>
      </div>
      <div class="form-control">
        <label class="label"><span class="label-text">Email</span></label>
        <input type="email" v-model="email" :class="['input w-full', emailError && 'input-error']" />
        <span v-if="emailError" class="text-error text-sm">{{ emailError }}</span>
      </div>
      <button class="btn btn-primary w-full mt-2" @click="submitOrder">Оформить заказ</button>
      <button class="btn btn-outline w-full" @click="currentStep = 1">← Назад в корзину</button>
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
        <NuxtLink to="/water/products" class="btn">К товарам</NuxtLink>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref, onMounted } from 'vue'
import { navigateTo, useState } from '#app'

interface CartItem { productId: number; name: string; price: number; quantity: number }

const currentStep = ref(1)
const cartItems = ref<CartItem[]>([])

// Инициализируем поля формы (если пользователь авторизован, заполним позже)
const name = ref('')
const phone = ref('')
const email = ref('')

// Переменные для сообщений/состояния заказа
const orderSuccess = ref<string | null>(null)
const orderError = ref<string | null>(null)

// Переменные для сообщений об ошибках полей шага 2
const nameError = ref<string | null>(null)
const phoneError = ref<string | null>(null)
const emailError = ref<string | null>(null)

// Проверка авторизации и автозаполнение
const user = useState('authUser')  // глобальное состояние авторизованного пользователя
const isAuth = computed(() => user.value && user.value.id)
onMounted(() => {
  // Получаем корзину из localStorage (на клиенте)
  if (process.client) {
    const saved = localStorage.getItem('cart')
    cartItems.value = saved ? JSON.parse(saved) : []
  }
  // Если пользователь авторизован, заполняем данные из профиля
  if (isAuth.value) {
    name.value = user.value.name || ''
    email.value = user.value.email || ''
  }
})

// Функция отправки заказа (шаг 2 -> шаг 3)
const submitOrder = async () => {
  // Очистка сообщений предыдущего шага
  nameError.value = phoneError.value = emailError.value = null
  orderSuccess.value = orderError.value = null

  // Валидация полей
  if (!name.value.trim()) {
    nameError.value = 'Укажите имя'
  }
  if (!phone.value.trim()) {
    phoneError.value = 'Укажите телефон'
  }
  const emailPattern = /^[^\\s@]+@[^\\s@]+\\.[^\\s@]+$/
  if (!email.value.trim() || !emailPattern.test(email.value)) {
    emailError.value = 'Некорректный email'
  }
  if (nameError.value || phoneError.value || emailError.value) {
    return  // не переходим к следующему шагу, если есть ошибки
  }

  try {
    // Формируем данные для API
    const orderData = {
      user_id: isAuth.value ? user.value.id : null,
      name: name.value,
      phone: phone.value,
      email: email.value,
      items: cartItems.value.map(item => ({
        product_id: item.productId,
        quantity: item.quantity
      }))
    }
    const response = await $fetch('/orders/', { method: 'POST', body: orderData })
    orderSuccess.value = 'Заказ успешно оформлен! Спасибо за покупку.'
    // Опционально: можно обработать response (например, получить номер заказа)
    // Очистка корзины
    cartItems.value = []
    if (process.client) {
      localStorage.removeItem('cart')
    }
  } catch (err: any) {
    orderError.value = 'Не удалось оформить заказ. ' + (err.response?.data?.message || err.message || '')
  } finally {
    currentStep.value = 3
  }
}
</script>
