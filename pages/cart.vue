<template>
  <div class="w-full flex justify-center p-8 ">
    <div class="bg-accent-content/30 flex flex-col items-start w-1/2 rounded-md p-4 gap-4">
      <div class="font-bold text-lg text-shadow-md"><p>Корзина товаров</p></div>
      <div class="border-1 border-teal-600/50 rounded-full opacity-75 w-full"></div>
      <div class="font-semibold text-md text-shadow-md w-full  "><p class="mb-2">Выбранные товары:</p>
        <div class="bg-black/20 rounded-md w-full p-4 grid md:grid-cols-2 gap-4 xl:grid-cols-3 place-items-center ">
          <div class="w-64 h-full bg-cover flex flex-col justify-between opacity-95">
            <p class="bg-teal-600 p-2 rounded-t-md">*Название товара*</p>
            <img src="public/img/voda1.jpg" class="w-full h-52 opacity-75"/>
            <div class="flex justify-between bg-teal-600 rounded-b-md" >
              <button class="btn btn-ghost bg-teal-600 border-none hover:shadow-none hover:bg-teal-700 p-2 active:bg-teal-700 text-sm rounded-none max-w-fit rounded-b-md">Перейти</button>
              <button class="btn btn-ghost bg-teal-600 border-none hover:shadow-none hover:bg-teal-700 p-2 active:bg-teal-700 text-sm rounded-none max-w-fit">+</button>
              <p class="self-center ">1</p>
              <button class="btn btn-ghost bg-teal-600 border-none hover:shadow-none hover:bg-teal-700 p-2 active:bg-teal-700 text-sm rounded-none max-w-fit">-</button>
              <button class="btn btn-ghost bg-teal-600 border-none hover:shadow-none hover:bg-red-900 p-2 active:bg-teal-700 text-sm rounded-none max-w-fit rounded-b-md">Удалить</button>
            </div>
          </div>
          <div class="w-64 h-full bg-cover flex flex-col justify-between opacity-95">
            <p class="bg-teal-600 p-2 rounded-t-md">*Название товара*</p>
            <img src="public/img/voda1.jpg" class="w-full h-52 opacity-75"/>
            <div class="flex justify-between bg-teal-600 rounded-b-md" >
              <button class="btn btn-ghost bg-teal-600 border-none hover:shadow-none hover:bg-teal-700 p-2 active:bg-teal-700 text-sm rounded-none max-w-fit rounded-b-md">Перейти</button>
              <button class="btn btn-ghost bg-teal-600 border-none hover:shadow-none hover:bg-teal-700 p-2 active:bg-teal-700 text-sm rounded-none max-w-fit">+</button>
              <p class="self-center ">1</p>
              <button class="btn btn-ghost bg-teal-600 border-none hover:shadow-none hover:bg-teal-700 p-2 active:bg-teal-700 text-sm rounded-none max-w-fit">-</button>
              <button class="btn btn-ghost bg-teal-600 border-none hover:shadow-none hover:bg-red-900 p-2 active:bg-teal-700 text-sm rounded-none max-w-fit rounded-b-md">Удалить</button>
            </div>
          </div>
          <div class="w-64 h-full bg-cover flex flex-col justify-between opacity-95">
            <p class="bg-teal-600 p-2 rounded-t-md">*Название товара*</p>
            <img src="public/img/voda1.jpg" class="w-full h-52 opacity-75"/>
            <div class="flex justify-between bg-teal-600 rounded-b-md" >
              <button class="btn btn-ghost bg-teal-600 border-none hover:shadow-none hover:bg-teal-700 p-2 active:bg-teal-700 text-sm rounded-none max-w-fit rounded-b-md">Перейти</button>
              <button class="btn btn-ghost bg-teal-600 border-none hover:shadow-none hover:bg-teal-700 p-2 active:bg-teal-700 text-sm rounded-none max-w-fit">+</button>
              <p class="self-center ">1</p>
              <button class="btn btn-ghost bg-teal-600 border-none hover:shadow-none hover:bg-teal-700 p-2 active:bg-teal-700 text-sm rounded-none max-w-fit">-</button>
              <button class="btn btn-ghost bg-teal-600 border-none hover:shadow-none hover:bg-red-900 p-2 active:bg-teal-700 text-sm rounded-none max-w-fit rounded-b-md">Удалить</button>
            </div>
          </div>



        </div>
      </div>
      <div class="flex justify-between w-full">
        <button>Перейти к заказу</button>
        <button>Очистить корзину</button>
      </div>
    </div>

  </div>
</template>
<script setup lang="ts">
</script>