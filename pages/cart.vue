<template>
  <div class="w-full flex justify-center p-8 ">
    <div class="bg-accent-content/30 flex flex-col items-start w-1/2 rounded-md p-4 gap-4">
      <div class="font-bold text-lg text-shadow-md"><p>Корзина товаров</p></div>
      <div class="border-1 border-teal-600/50 rounded-full opacity-75 w-full"></div>
      <div class="font-semibold text-md text-shadow-md w-full">
        <p class="mb-2">Выбранные товары:</p>
        <div class="bg-black/20 rounded-md w-full p-4 flex flex-col gap-4">

<!--          Тут будет выгрузка карточек выбранных товаров-->
          <div class="w-full h-full bg-teal-600 flex flex-row opacity-95 rounded-md " v-for="water in water_cart" :key="water.productId">
            <img :src="water.picture" class="w-62 min-h-42 h-auto opacity-75 rounded-l-md" />
            <div class="flex flex-col justify-between bg-teal-600 w-full rounded-r-md">
              <div class="w-full flex flex-row p-4 justify-between">
                <div>
                  <p class="mb-2">{{water.name}}</p>
                  <p class="mb-2 font-medium text-white/80">{{water.description}}</p>
                </div>
                <div>
                  <p>{{ water.price }}</p>
                </div>

              </div>
              <div class="flex justify-between w-full p-2 ">
                <NuxtLink to="/water" class="btn btn-ghost bg-teal-600 border-none hover:shadow-none hover:bg-teal-700 p-2 active:bg-teal-700 text-sm ">Перейти</NuxtLink>
                <button class="btn btn-ghost bg-teal-600 border-none hover:shadow-none hover:bg-teal-700 p-2 active:bg-teal-700 text-sm " v-on:click="increment(water.productId)">+</button>
                <p class="self-center ">{{water.quantity}}</p>
                <button class="btn btn-ghost bg-teal-600 border-none hover:shadow-none hover:bg-teal-700 p-2 active:bg-teal-700 text-sm  max-w-fit" v-on:click="decrement(water.productId)">-</button>
                <button class="btn btn-ghost bg-teal-600 border-none hover:shadow-none hover:bg-red-900 p-2 active:bg-red-900 text-sm  max-w-fit" v-on:click="remove(water.productId)">Удалить</button>
              </div>
            </div>
          </div>


        </div>
      </div>
      <div class="flex justify-between w-full">
        <NuxtLink to="/order" class="btn btn-ghost bg-teal-600 border-none hover:shadow-none hover:bg-teal-700 p-2 active:bg-teal-700 text-sm  max-w-fit">Перейти к заказу</NuxtLink>
        <button class="btn btn-ghost bg-teal-600 border-none hover:shadow-none hover:bg-teal-700 p-2 active:bg-teal-700 text-sm  max-w-fit" v-on:click="clearCart">Очистить корзину</button>
      </div>
    </div>

  </div>
</template>
<script setup lang="ts">
import { ref, watch, onMounted } from 'vue'
interface Water {
  productId: number
  picture: string
  name: string
  description: string
  price: number
  quantity: number
}
const water_cart = ref<Water[]>([])
const loadCart = () => {
  if (process.client) {
    const saved = localStorage.getItem('cart')
    water_cart.value = saved ? JSON.parse(saved) : []
  }
}
watch(water_cart, (val) => {
  if (process.client) localStorage.setItem('cart', JSON.stringify(val))
  window.refreshCart && window.refreshCart()
}, { deep: true })
const increment = (productId: number) => {
  const item = water_cart.value.find(i => i.productId === productId)
  if (item) item.quantity++
}
const decrement = (productId: number) => {
  const item = water_cart.value.find(i => i.productId === productId)
  if (item && item.quantity > 1) item.quantity--
}
const remove = (productId: number) => {
  water_cart.value = water_cart.value.filter(i => i.productId !== productId)
  window.showToast && window.showToast('Товар удален', 'info')
}
const clearCart = () => {
  water_cart.value = []
  if (process.client) localStorage.removeItem('cart')
  window.showToast && window.showToast('Товары удалены', 'info')
}
onMounted(loadCart)
</script>