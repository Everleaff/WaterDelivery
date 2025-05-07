
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
          <div class="grid grid-cols-1 md:grid-cols-3 gap-8">
            <div class="card h-150 image-full w-96 shadow-xl animate-fadeInUp hover:scale-105 transition-transform "
                 @mouseover="hover=true; blur_card='backdrop-blur-sm'"
                 @mouseleave="hover=false; blur_card=''"
                 data-aos-delay="200">
              <figure><img src="/img/voda1.jpg" alt="Вода" class="object-cover w-full h-full rounded-2xl" /></figure>
              <div class="card-body transition-all " :class="blur_card">
                <h2 class="card-title justify-center lg:text-[3rem] text-center animate-zoomIn text-teal-300">Вода из раковины</h2>
                <div class="border border-teal-600/50 rounded-full opacity-75 w-full my-4 animate-pulse"></div>
                <div class="flex justify-center mb-6">
                  <p v-if="hover" class="text-lg animate-slideUp text-gray-200">Ржавчина - 50, магний - 20, вкуснота - 10</p>
                  <p v-else class="text-lg animate-slideUp text-gray-200">Артезианская вода с природными минералами.</p>
                </div>
                <button class="btn btn-ghost border-none hover:shadow-xl hover:bg-teal-700 active:bg-teal-700 bg-teal-600 w-full animate-pulse text-white px-6 py-3 rounded-full shadow-lg transition-all ">Добавить в корзину</button>
              </div>
            </div>
          </div>
        </template>

        <template v-if="index === 4">
          <h2 class="text-5xl font-bold mb-12 animate-zoomIn text-transparent bg-clip-text bg-gradient-to-r from-teal-400 to-teal-500">Сайт и поставщики</h2>
          <p class="text-xl animate-slideUp text-gray-200">Мы сотрудничаем сами с собой, потому что мы самые крутые!</p>
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
