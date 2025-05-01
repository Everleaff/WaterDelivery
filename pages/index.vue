<template>
  <div class="w-full h-full text-white ">

<!--    Начало карточек товаров-->
    <div class="flex p-8 h-full justify-center">
      <div class="card bg-base-100  w-96 shadow-sm m-8 mb-20"   v-on:mouseover="hover=true" v-on:mouseleave="hover=false">
        <figure class="image-cover">
          <img
              src="/img/voda1.jpg"
              alt="Туалетная вода" />
        </figure>
        <div class="card-body">
          <h2 class="card-title">
            Вода из раковины
            <div class="badge badge-secondary shadow-md shadow-teal-800 p-1 bg-teal-500">Новинка!</div>
          </h2>
          <div v-if="hover===true">
            <p>Елки иголки, это вода такая крута, вот ее характеристики: Ржавчина - 50, магний - 20, вкуснота - 10</p>
          </div>
          <div v-else>
            <p>Вкуснейшая вода прямиком из домашнего туалета. Попробуйте!</p>
          </div>

          <p></p>
          <div class="card-actions justify-center font-semibold space-x-1">

            <button class="btn btn-ghost border-none shadow-md shadow-emerald-800 hover:shadow-emerald-900 hover:bg-emerald-700 p-2 bg-emerald-500 w-full">Добавить в корзину</button>
          </div>
        </div>
      </div>
      <div class="card bg-base-100 h-auto w-96 shadow-sm m-8 mb-20"   v-on:mouseover="hover=true" v-on:mouseleave="hover=false">
        <figure class="image-cover">
          <img
              src="/img/voda1.jpg"
              alt="Туалетная вода" />
        </figure>
        <div class="card-body">
          <h2 class="card-title">
            Вода из раковины
            <div class="badge badge-secondary shadow-md shadow-teal-800 p-1 bg-teal-500">Новинка!</div>
          </h2>
          <div v-if="hover===true">
            <p>Елки иголки, это вода такая крута, вот ее характеристики: Ржавчина - 50, магний - 20, вкуснота - 10</p>
          </div>
          <div v-else>
            <p>Вкуснейшая вода прямиком из домашнего туалета. Попробуйте!</p>
          </div>

          <p></p>
          <div class="card-actions justify-center font-semibold space-x-1">

            <button class="btn btn-ghost border-none shadow-md shadow-emerald-800 hover:shadow-emerald-900 hover:bg-emerald-700 p-2 bg-emerald-500 w-full">Добавить в корзину</button>
          </div>
        </div>
      </div>
      <div class="card bg-base-100 h-auto w-96 shadow-sm m-8 mb-20"   v-on:mouseover="hover=true" v-on:mouseleave="hover=false">
        <figure class="image-cover">
          <img
              src="/img/voda1.jpg"
              alt="Туалетная вода" />
        </figure>
        <div class="card-body">
          <h2 class="card-title">
            Вода из раковины
            <div class="badge badge-secondary shadow-md shadow-teal-800 p-1 bg-teal-500">Новинка!</div>
          </h2>
          <div v-if="hover===true">
            <p>Елки иголки, это вода такая крута, вот ее характеристики: Ржавчина - 50, магний - 20, вкуснота - 10</p>
          </div>
          <div v-else>
            <p>Вкуснейшая вода прямиком из домашнего туалета. Попробуйте!</p>
          </div>

          <p></p>
          <div class="card-actions justify-center font-semibold space-x-1">

            <button class="btn btn-ghost border-none shadow-md shadow-emerald-800 hover:shadow-emerald-900 hover:bg-emerald-700 p-2 bg-emerald-500 w-full">Добавить в корзину</button>
          </div>
        </div>
      </div>

<!--      <div class="card bg-base-100 image-full h-auto w-96 shadow-sm m-8 mb-20 shadow-sm">-->
<!--        <figure>-->
<!--          <img-->
<!--              src="/img/voda2.jpg"-->
<!--              alt="Болотная вода" />-->
<!--        </figure>-->
<!--        <div class="card-body" >-->
<!--          <h2 class="card-title">Болотная вода</h2>-->
<!--          <div v-if="hover===true">-->
<!--            <p>Елки иголки, это вода такая крута, вот ее характеристики: Ржавчина - 50, магний - 20, вкуснота - 10</p>-->
<!--          </div>-->
<!--          <div v-else>-->
<!--            <p>Вода, добытая прямиком из благовещенских болот, бодрит тело и разум!</p>-->
<!--          </div>-->


<!--          <div class="card-actions justify-end">-->
<!--            <button class="btn btn-ghost border-none shadow-md shadow-emerald-800 hover:shadow-emerald-900 hover:bg-emerald-700 p-1 bg-emerald-500 ">В корзину!</button>-->
<!--          </div>-->
<!--        </div>-->
<!--      </div>-->
    </div>

  </div>
</template>

<script>


export default {

  data() {
    return {
      hover: false
    }
  },

}
</script>