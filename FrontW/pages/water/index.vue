<template>
  <div class="w-full h-full text-white ">

    <!--    Начало карточек товаров-->
    <div class="flex p-8 h-auto  justify-center">
      <div class="card h-150 lg:text-xs  image-full w-96 shadow-sm m-8 mb-20" v-on:mouseover="hover=true; blur_card = 'backdrop-blur-xs'" v-on:mouseleave="hover=false; blur_card = '' ">
        <figure>
          <img
              src="/img/voda1.jpg"
              alt="Туалетная вода" />
        </figure>
        <div class="card-body" :class="blur_card">
          <h2 class="card-title justify-center lg:text-[2.5rem] sm:text-[1.5rem] text-center 2xl:text-nowrap ">Вода из раковины</h2>
          <div class="border-1 border-teal-600/50 rounded-full opacity-75 w-full mb-10 mt-2 "></div>
          <div class="flex justify-center mb-10 ">
            <div v-if="hover===true">
              <p>Елки иголки, это вода такая крута, вот ее характеристики: Ржавчина - 50, магний - 20, вкуснота - 10</p>
            </div>
            <div v-else>
              <p>Артезианская питьевая вода, добытая из природных глубин, обладает исключительной чистотой и мягким вкусом. <br> <br>Насыщенная природными минералами, она идеально подходит для ежедневного употребления, освежает организм и укрепляет здоровье. <br><br> Вода добывается из защищенного подземного источника, благодаря чему сохраняет первозданную чистоту и баланс микроэлементов, даруя заряд энергии и жизненных сил каждый день.

                <br> <br>Подходит для всей семьи, идеально утоляет жажду и сохраняет натуральный вкус.</p>

            </div>



          </div>
          <p></p>
          <div class="card-actions justify-center font-semibold space-x-1">

            <button class="btn btn-ghost border-none shadow-md shadow-emerald-800 hover:shadow-emerald-900 hover:bg-emerald-700 p-2 bg-emerald-500 w-full">Добавить в корзину</button>
          </div>


        </div>
      </div>
      <div class="card h-150 lg:text-xs  image-full w-96 shadow-sm m-8 mb-20" v-on:mouseover="hover=true; blur_card = 'backdrop-blur-xs'" v-on:mouseleave="hover=false; blur_card = '' ">
        <figure>
          <img
              src="/img/voda1.jpg"
              alt="Туалетная вода" />
        </figure>
        <div class="card-body" :class="blur_card">
          <h2 class="card-title justify-center lg:text-[2.5rem] sm:text-[1.5rem] text-center 2xl:text-nowrap ">Вода из раковины</h2>
          <div class="border-1 border-teal-600/50 rounded-full opacity-75 w-full mb-10 mt-2 "></div>
          <div class="flex justify-center mb-10 ">
            <div v-if="hover===true">
              <p>Елки иголки, это вода такая крута, вот ее характеристики: Ржавчина - 50, магний - 20, вкуснота - 10</p>
            </div>
            <div v-else>
              <p>Артезианская питьевая вода, добытая из природных глубин, обладает исключительной чистотой и мягким вкусом. <br> <br>Насыщенная природными минералами, она идеально подходит для ежедневного употребления, освежает организм и укрепляет здоровье. <br><br> Вода добывается из защищенного подземного источника, благодаря чему сохраняет первозданную чистоту и баланс микроэлементов, даруя заряд энергии и жизненных сил каждый день.

                <br> <br>Подходит для всей семьи, идеально утоляет жажду и сохраняет натуральный вкус.</p>

            </div>



          </div>
          <p></p>
          <div class="card-actions justify-center font-semibold space-x-1">

            <button class="btn btn-ghost border-none shadow-md shadow-emerald-800 hover:shadow-emerald-900 hover:bg-emerald-700 p-2 bg-emerald-500 w-full">Добавить в корзину</button>
          </div>


        </div>
      </div>
      <div class="card h-150 lg:text-xs  image-full w-96 shadow-sm m-8 mb-20" v-on:mouseover="hover=true; blur_card = 'backdrop-blur-xs'" v-on:mouseleave="hover=false; blur_card = '' ">
        <figure>
          <img
              src="/img/voda1.jpg"
              alt="Туалетная вода" />
        </figure>
        <div class="card-body" :class="blur_card">
          <h2 class="card-title justify-center lg:text-[2.5rem] sm:text-[1.5rem] text-center 2xl:text-nowrap ">Вода из раковины</h2>
          <div class="border-1 border-teal-600/50 rounded-full opacity-75 w-full mb-10 mt-2 "></div>
          <div class="flex justify-center mb-10 ">
            <div v-if="hover===true">
              <p>Елки иголки, это вода такая крута, вот ее характеристики: Ржавчина - 50, магний - 20, вкуснота - 10</p>
            </div>
            <div v-else>
              <p>Артезианская питьевая вода, добытая из природных глубин, обладает исключительной чистотой и мягким вкусом. <br> <br>Насыщенная природными минералами, она идеально подходит для ежедневного употребления, освежает организм и укрепляет здоровье. <br><br> Вода добывается из защищенного подземного источника, благодаря чему сохраняет первозданную чистоту и баланс микроэлементов, даруя заряд энергии и жизненных сил каждый день.

                <br> <br>Подходит для всей семьи, идеально утоляет жажду и сохраняет натуральный вкус.</p>

            </div>



          </div>
          <p></p>
          <div class="card-actions justify-center font-semibold space-x-1">

            <button class="btn btn-ghost border-none shadow-md shadow-emerald-800 hover:shadow-emerald-900 hover:bg-emerald-700 p-2 bg-emerald-500 w-full">Добавить в корзину</button>
          </div>


        </div>
      </div>
    </div>

  </div>
</template>

<script setup lang="ts">

const hover = ref(false)
const blur_card = ref("")

// export default {
//
//   data() {
//     return {
//       hover: false
//     }
//   },
//
// }
</script>