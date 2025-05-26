
<template>
  <div class="min-h-screen text-white overflow-hidden relative">

    <div class="fixed right-4 top-1/2 transform -translate-y-1/2 !z-5 flex flex-col space-y-4">
      <button
          v-for="(section, index) in sections"
          :key="index"
          @click="scrollToSection(index)"
          class="w-3 h-3 rounded-full transition-all "
          :class="currentSection === index ? 'bg-teal-500 scale-125' : 'bg-gray-500 opacity-50 hover:opacity-100'"
      ></button>
    </div>

    <section
        v-for="(section, index) in sections"
        :key="index"
        class="h-screen w-full absolute top-0 left-0 flex items-center justify-center transition-all ease-in-out"
        :class="currentSection === index ? normal_class : hidden_class"
        :data-aos="section.aos"
        :data-aos-delay="section.delay"
    >
      <div
          class="container mx-auto text-center p-8 rounded-lg bg-opacity-20 transform transition-all "
          :class="{ 'scale-105': currentSection === index }"
      >
        <template v-if="index === 0">
          <h1 class="text-6xl font-bold mb-6 animate-zoomIn text-transparent bg-clip-text bg-gradient-to-r from-teal-400 to-teal-500">Добро пожаловать!</h1>
          <p class="text-xl mb-6 animate-slideUp text-gray-200">Лучшая вода с доставкой прямо к вам домой.</p>
          <button class="btn btn-ghost border-none hover:shadow-xl hover:bg-teal-700 m-1 active:bg-teal-700 bg-teal-600 animate-pulse text-white px-6 py-3 rounded-full shadow-lg transition-all " v-on:click="open_auth_modal && open_auth_modal()">Зарегистрироваться</button>
        </template>

        <template v-if="index === 1">
          <h2 class="text-5xl font-bold mb-12 animate-zoomIn text-transparent bg-clip-text bg-gradient-to-r from-teal-400 to-teal-500">Почему нужно выбирать нас?</h2>
          <div class="grid grid-cols-1 md:grid-cols-3 gap-8">
            <div class="card bg-gray-800/40 border border-teal-600/40 border border-teal-600/50 rounded-3xl opacity-85 p-6 animate-fadeInUp hover:scale-105 transition-transform " data-aos="fade-up" data-aos-delay="100">
              <h3 class="text-3xl font-semibold mb-2 animate-slideUp text-teal-300">Наша команда</h3>
              <p class="text-lg text-white">Профессионалы, крутые и умелые.</p>
            </div>
            <div class="card bg-gray-800/40 border border-teal-600/40 border border-teal-600/50 rounded-3xl opacity-85 p-6 animate-fadeInUp hover:scale-105 transition-transform " data-aos="fade-up" data-aos-delay="100">
              <h3 class="text-3xl font-semibold mb-2 animate-slideUp text-teal-300">Наш сайт</h3>
              <p class="text-lg text-white">Удобный интерфейс и быстрая навигация.</p>
            </div>
            <div class="card bg-gray-800/40 border border-teal-600/40 rounded-3xl opacity-85 p-6 animate-fadeInUp hover:scale-105 transition-transform " data-aos="fade-up" data-aos-delay="100">
              <h3 class="text-3xl font-semibold mb-2 animate-slideUp text-teal-300">Эффективность доставки</h3>
              <p class="text-lg text-white">Доставляем быстро и в срок.</p>
            </div>
          </div>
        </template>

        <template v-if="index === 2">
          <h2 class="text-5xl font-bold mb-12 animate-zoomIn text-transparent bg-clip-text bg-gradient-to-r from-teal-400 to-teal-500">Наша эффективность</h2>
          <p class="text-xl animate-slideUp text-gray-200" data-aos-delay="100">Скорость доставки — нереальная</p>
          <p class="text-xl animate-slideUp text-gray-200" data-aos-delay="200">Удовлетворенность клиентов — 146% положительных отзывов.</p>
        </template>

        <template v-if="index === 3">
          <h2 class="text-5xl font-bold mb-12 animate-zoomIn text-transparent bg-clip-text bg-gradient-to-r from-teal-400 to-teal-500">Наши товары</h2>
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
        </template>

        <template v-if="index === 4">
          <h2 class="text-5xl font-bold mb-12 animate-zoomIn text-transparent bg-clip-text bg-gradient-to-r from-teal-400 to-teal-500">Сайт и поставщики</h2>
          <p class="text-xl animate-slideUp text-gray-200">Быстрая сборка заказа, опытные курьеры!</p>
          <p class="text-xl animate-slideUp text-gray-200">Обширная зона доставки!</p>
          <div class="flex justify-center mt-12 ">
            <img class="shadow shadow-black w-156 h-120" src="public/img/deliveryRadius.png"/>
          </div>

        </template>

        <template v-if="index === 5">
          <h2 class="text-5xl font-bold mb-12 animate-zoomIn text-transparent bg-clip-text bg-gradient-to-r from-teal-400 to-teal-500">Свяжитесь с нами</h2>
          <p class="text-xl mb-6 animate-slideUp text-gray-200">Email: ogo@mail.ru | Телефон: +7 (999) 888-77-66</p>
          <button class="btn btn-ghost border-none hover:shadow-xl hover:bg-teal-700 m-1 active:bg-teal-700 bg-teal-600 animate-pulse text-white px-6 py-3 rounded-full shadow-lg transition-all " v-on:click="open_auth_modal && open_auth_modal()">Зарегистрироваться</button>
        </template>
      </div>
    </section>
  </div>
</template>

<style scoped>


section {
  background: transparent;
}

.animate-zoomIn {
  animation: zoomIn 1.2s cubic-bezier(0.68, -0.55, 0.27, 1.55);
}

@keyframes zoomIn {
  from { transform: scale(0.7) rotate(5deg); opacity: 0; }
  to { transform: scale(1) rotate(0deg); opacity: 1; }
}

.animate-slideUp {
  animation: slideUp 1s ease-out;
}

@keyframes slideUp {
  from { transform: translateY(50px); opacity: 0; }
  to { transform: translateY(0); opacity: 1; }
}

.animate-fadeInUp {
  animation: fadeInUp 1.5s ease-out;
}

@keyframes fadeInUp {
  from { transform: translateY(30px); opacity: 0; }
  to { transform: translateY(0); opacity: 1; }
}

.animate-pulse {
  animation: pulse 2s infinite ease-in-out;
}

@keyframes pulse {
  0% { transform: scale(1); box-shadow: 0 0 10px rgba(20, 184, 166, 0.5); }
  50% { transform: scale(1.1); box-shadow: 0 0 20px rgba(20, 184, 166, 0.8); }
  100% { transform: scale(1); box-shadow: 0 0 10px rgba(20, 184, 166, 0.5); }
}

.animate-fadeIn {
  animation: fadeIn 2s ease-in;
}

@keyframes fadeIn {
  from { opacity: 0; }
  to { opacity: 1; }
}
</style>

<script setup lang="ts">
import AOS from 'aos'
import 'aos/dist/aos.css'
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

const currentSection = ref(0)
const hover = ref(false)
const blur_card = ref('')

const normal_class = ref('opacity-100 z-0');
const hidden_class = ref('opacity-100 z-0 hidden pointer-events-none');


const sections = [
  { aos: 'fade-in', delay: 0 },
  { aos: 'fade-up', delay: 10, title: 'Почему выбирают нас' },
  { aos: 'fade-up', delay: 10, title: 'Наша эффективность' },
  { aos: 'fade-up', delay: 10, title: 'Наши товары' },
  { aos: 'fade-up', delay: 10, title: 'Сайт и поставщики' },
  { aos: 'fade-up', delay: 10, title: 'Контакты' }
]

const isScrolling = ref(false)

const overlayActive = ref(true)

function updateOverlay() {
  overlayActive.value = window.scrollY === 0
}

function scrollToSection(i: number) {
  if (!overlayActive.value) return
  if (i < 0 || i >= sections.length || isScrolling.value) return

  isScrolling.value = true
  currentSection.value = i
  setTimeout(() => (isScrolling.value = false), 200)
}

function handleWheel(e: WheelEvent) {
  if (!overlayActive.value) return
  e.preventDefault()
  scrollToSection(currentSection.value + Math.sign(e.deltaY))
}


function handleKey(e: KeyboardEvent) {
  if (!overlayActive.value) return
  const tag = (e.target as HTMLElement).tagName
  if (['INPUT', 'TEXTAREA', 'SELECT'].includes(tag)) return

  if (['ArrowDown', 'PageDown', ' ', 'Spacebar'].includes(e.key)) {
    if (currentSection.value < sections.length - 1) {
      e.preventDefault()
      scrollToSection(currentSection.value + 1)
    }
  } else if (['ArrowUp', 'PageUp'].includes(e.key)) {
    if (currentSection.value > 0) {
      e.preventDefault()
      scrollToSection(currentSection.value - 1)
    }
  }
}

function handleMiddleDown (e: MouseEvent) {
  if (e.button !== 1) return
  e.preventDefault()

  scrollToSection(currentSection.value + 1)
}

watch(currentSection, async () => {
  await nextTick()
  AOS.refreshHard()
})

onMounted(() => {
  AOS.init({ duration: 1200, once: false, mirror: true })

  window.addEventListener('wheel',   handleWheel,   { passive: false })
  window.addEventListener('keydown', handleKey,     { passive: false })
  window.addEventListener('scroll',  updateOverlay, { passive: true })
})
onUnmounted(() => {
  window.removeEventListener('wheel',   handleWheel)
  window.removeEventListener('keydown', handleKey)
  window.removeEventListener('scroll',  updateOverlay)
})

const open_auth_modal = inject<() => void>('open_auth_modal')

</script>
