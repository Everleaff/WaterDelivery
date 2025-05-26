<template>
  <div class="w-full flex justify-center p-8 ">
    <div class="bg-accent-content/30 flex flex-col items-start w-1/2 rounded-md p-4 gap-4">
      <div class="font-bold text-lg text-shadow-md"><p>Корзина товаров</p></div>
      <div class="border-1 border-teal-600/50 rounded-full opacity-75 w-full"></div>
      <div class="font-semibold text-md text-shadow-md w-full">
        <p class="mb-2">Выбранные товары:</p>
        <div class="bg-black/20 rounded-md w-full p-4 flex flex-col gap-4">

<!--          Тут будет выгрузка карточек выбранных товаров-->
          <div class="w-full h-full bg-teal-600 flex flex-row opacity-95 rounded-md " v-for="water in water_cart">
            <img :src="water.picture" class="w-62 min-h-42 h-auto opacity-75 rounded-l-md" />
            <div class="flex flex-col justify-between bg-teal-600 w-full rounded-r-md">
              <div class="w-full flex flex-row p-4 justify-between">
                <div>
                  <p class="mb-2">{{water.title}}</p>
                  <p class="mb-2 font-medium text-white/80">{{water.description}}</p>
                </div>
                <div>
                  <p>{{ water.price }}</p>
                </div>

              </div>
              <div class="flex justify-between w-full p-2 ">
                <button class="btn btn-ghost bg-teal-600 border-none hover:shadow-none hover:bg-teal-700 p-2 active:bg-teal-700 text-sm ">Перейти</button>
                <button class="btn btn-ghost bg-teal-600 border-none hover:shadow-none hover:bg-teal-700 p-2 active:bg-teal-700 text-sm " v-on:click="water.count++">+</button>
                <p class="self-center ">{{water.count}}</p>
                <button class="btn btn-ghost bg-teal-600 border-none hover:shadow-none hover:bg-teal-700 p-2 active:bg-teal-700 text-sm  max-w-fit" v-on:click="water.count > 1 ? water.count-- : water.count = 1">-</button>
                <button class="btn btn-ghost bg-teal-600 border-none hover:shadow-none hover:bg-red-900 p-2 active:bg-red-900 text-sm  max-w-fit" >Удалить</button>
              </div>
            </div>
          </div>


        </div>
      </div>
      <div class="flex justify-between w-full">
        <NuxtLink to="/order" class="btn btn-ghost bg-teal-600 border-none hover:shadow-none hover:bg-teal-700 p-2 active:bg-teal-700 text-sm  max-w-fit">Перейти к заказу</NuxtLink>
        <button class="btn btn-ghost bg-teal-600 border-none hover:shadow-none hover:bg-teal-700 p-2 active:bg-teal-700 text-sm  max-w-fit">Очистить корзину</button>
      </div>
    </div>

  </div>
</template>
<script setup lang="ts">
import { ref, reactive, watch } from 'vue'
import { useRouter } from 'vue-router'

interface Water {
  productId: number
  picture: string
  title: string
  description: string
  price: number
  count: number
}

const router = useRouter()

const water_cart = ref<Water[]>([])

const loadCart = () => {
  if (process.client) {
    const saved = localStorage.getItem('cart')
    water_cart.value = saved ? JSON.parse(saved) : []
  }
}

// Сохранять корзину при изменениях
watch(water_cart, (val) => {
  if (process.client) localStorage.setItem('cart', JSON.stringify(val))
}, { deep: true })

// Изменить количество товара
const increment = (idx: number) => { water_cart.value[idx].count++ }
const decrement = (idx: number) => {
  if (water_cart.value[idx].count > 1) water_cart.value[idx].count--
}
// Удалить товар
const remove = (idx: number) => { water_cart.value.splice(idx, 1) }
// Очистить корзину полностью
const clearCart = () => { water_cart.value = []; if (process.client) localStorage.removeItem('cart') }
// Перейти к оформлению заказа
const goToOrder = () => router.push('/order')

onMounted(loadCart)
</script>
