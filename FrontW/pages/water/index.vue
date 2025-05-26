<template>
  <div class="w-full h-full text-white ">
    <div class="flex flex-wrap justify-center p-8 h-auto">
      <div v-for="product in products" :key="product.id"
           class="card w-72 h-[400px] image-full shadow-sm m-6 mb-12 relative overflow-hidden group transition-all duration-200"
           v-on:mouseover="hoverCard = product.id" v-on:mouseleave="hoverCard = null">
        <figure>
          <img
              :src="product.image_url || '/img/voda1.jpg'"
              :alt="product.name"
              class="w-full h-48 object-cover rounded-t-md"
          />
        </figure>
        <div class="card-body transition-all duration-200"
             :class="hoverCard !== product.id ? 'opacity-100 z-2' : 'opacity-0 z-0 absolute top-0 left-0 w-full h-full'">
          <h2 class="card-title justify-center text-xl mb-2 text-center">
            {{ product.name }}
          </h2>
          <div class="border-1 border-teal-600/50 rounded-full opacity-75 w-full mb-6 mt-2"></div>
          <div class="flex-1 flex items-center justify-center text-center text-white/90 text-sm">
            {{ getFirstSentence(product.description) }}
          </div>
          <div class="card-actions justify-center font-semibold space-x-1 mt-4">
            <span class="text-lg text-emerald-100 font-bold">{{ product.price }} ₽</span>
            <button
                class="btn btn-ghost border-none shadow-md shadow-emerald-800 hover:shadow-emerald-900 hover:bg-emerald-700 p-2 bg-emerald-500 w-full mt-2"
                @click="addToCart(product)">
              Добавить в корзину
            </button>
          </div>
        </div>
        <div class="card-body absolute top-0 left-0 w-full h-full  backdrop-blur-sm flex flex-col justify-between
        opacity-0 group-hover:opacity-100 transition-all duration-300 z-5">
          <h2 class="card-title justify-center text-xl mb-2 text-center text-white">{{ product.name }}</h2>
          <div class="border-1 border-teal-400/70 rounded-full opacity-80 w-full mb-4"></div>
          <div class="flex-1 flex items-center justify-center text-center text-white/90 text-sm px-2">
            {{ product.description }}
          </div>
          <div class="card-actions justify-center font-semibold space-x-1 mt-2 ">
            <span class="text-lg text-emerald-100 font-bold ">{{ product.price }} ₽</span>
            <button
                class="btn btn-ghost border-none shadow-md shadow-emerald-800 hover:shadow-emerald-900 hover:bg-emerald-700 p-2 bg-emerald-500 w-full mt-2"
                @click="addToCart(product)">
              Добавить в корзину
            </button>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref, onMounted } from 'vue'
const products = ref([])
const hoverCard = ref<number | null>(null)
onMounted(async () => {
  try {
    products.value = await $fetch('http://0.0.0.0:80/products/')
  } catch (e) {
    products.value = []
  }
})
function getFirstSentence(text: string) {
  if (!text) return ''
  const m = text.match(/^.*?[.!?](?=\s|$)/)
  return m ? m[0] : text.split('\n')[0]
}
const addToCart = (product) => {
  let cart = []
  if (process.client) {
    cart = JSON.parse(localStorage.getItem('cart') || '[]')
    const found = cart.find(item => item.productId === product.id)
    if (found) {
      found.quantity++
      window.showToast && window.showToast('Ещё 1 шт. товара добавлено в корзину', 'info')
    } else {
      cart.push({
        productId: product.id,
        name: product.name,
        price: product.price,
        quantity: 1,
        picture: product.image_url || '/img/voda1.jpg',
        description: product.description,
      })
      window.showToast && window.showToast('Товар добавлен в корзину', 'success')
    }
    localStorage.setItem('cart', JSON.stringify(cart))
    window.refreshCart && window.refreshCart()
  }
}
</script>