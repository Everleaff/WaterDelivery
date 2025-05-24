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
        <button class="btn btn-ghost bg-teal-600 border-none hover:shadow-none hover:bg-teal-700 p-2 active:bg-teal-700 text-sm  max-w-fit">Перейти к заказу</button>
        <button class="btn btn-ghost bg-teal-600 border-none hover:shadow-none hover:bg-teal-700 p-2 active:bg-teal-700 text-sm  max-w-fit">Очистить корзину</button>
      </div>
    </div>

  </div>
</template>
<script setup lang="ts">

const water_cart = reactive([
  {picture:"img/voda1.jpg", title: "Вода крутая", description:"Это нереально крутая вода", price: 16 + " " + "руб.", count: 1  },
  {picture:"img/voda2.jpg", title: "Вода чистая", description:"Это реально чистая вода", price: 36 + " " + "руб.", count: 1  },
  {picture:"img/voda1.jpg", title: "Вода красивая", description:"Красота, а не вода", price: 26 + " " + "руб.", count: 1  },
  {picture:"img/voda2.jpg", title: "Вода замурчательная", description:"Мур-мур-мур, водичка льется в пасть", price: 116 + " " + "руб.", count: 1  },

])

// function waterCount( count: number, waterCount :) {
//   water_cart.forEach((item) => {item.count ++})
//   return count;
// }


</script>