<template>
  <div class="max-w-3xl mx-auto bg-teal-600/80 rounded-md p-8 shadow-md mt-8">
    <div class="flex flex-col sm:flex-row gap-6 items-center">
      <div class="flex flex-col">
        <p class="font-bold self-center mb-2 text-shadow-md">Water Delivery</p>
        <img src="public/img/ЛоготипWaterDelivery2.png" alt="Доставка воды" class="w-60 rounded-lg shadow-lg mb-4 sm:mb-0" />
      </div>

      <div>
        <h2 class="text-3xl font-bold mb-2 text-white text-shadow-md">Доставка воды</h2>
        <ul class="list-disc list-inside text-teal-900 font-medium space-y-2">
          <li>
            <span class="font-bold text-white text-shadow-md">Время работы: </span>
            <span class="text-white text-shadow-md">Пн-Сб 9:00 – 20:00, Вс — выходной</span>
          </li>
          <li>
            <span class="font-bold text-white text-shadow-md">Доставка по городу: </span>
            <span class="text-green-500 font-bold  text-shadow-md">БЕСПЛАТНО</span>
            <span class="text-white text-shadow-md"> в зеленую зону</span>
          </li>
          <li>
            <span class="font-bold text-white text-shadow-md">В желтую зону: </span>
            <span class="text-amber-500 font-bold text-shadow-md">+200 ₽ к заказу</span>
          </li>
          <li>
            <span class="font-bold text-white text-shadow-md">В красную зону: </span>
            <span class="text-red-600 font-bold text-shadow-sm">Доставка не осуществляется</span> <br>
            <span class="text-gray-300"> (слишком далеко от города)</span>
          </li>
          <li>
            <span class="font-bold text-white text-shadow-md">Если у вас дом без лифта: </span>
            <span class="text-red-600 font-bold text-shadow-md">+100 ₽</span>
            <span class="text-white text-shadow-md"> за каждый этаж подъёма</span>
          </li>
        </ul>
        <div class="mt-4">
          <img src="public/img/deliveryRadius.png" alt="Зоны доставки" class="w-full max-w-md rounded border" />
          <div class="text-xs text-gray-300 mt-2 text-shadow-md">Схема зон — уточняйте адрес у оператора при заказе</div>
        </div>
      </div>
    </div>
  </div>
</template>
<script setup lang="ts">
</script>