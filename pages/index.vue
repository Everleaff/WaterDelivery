<template>
  <div class="w-full h-full text-white ">

<!--    Начало карточек товаров-->
    <div class="flex p-8">
      <div class="card bg-base-100 w-96 shadow-sm m-8">
        <figure>
          <img
              src="/img/voda1.jpg"
              alt="Туалетная вода" />
        </figure>
        <div class="card-body">
          <h2 class="card-title">
            Вода из раковины
            <div class="badge badge-secondary shadow-md shadow-teal-800 p-1 bg-teal-500">Новинка!</div>
          </h2>
          <p>Вкуснейшая вода прямиком из домашнего туалета. Попробуйте!</p>
          <div class="card-actions justify-end font-semibold space-x-1">
            <div class="badge badge-outline shadow-md shadow-emerald-800 hover:shadow-emerald-900 hover:bg-emerald-700 p-1 bg-emerald-500">Осмотреть</div>
            <div class="badge badge-outline shadow-md shadow-emerald-800 hover:shadow-emerald-900 hover:bg-emerald-700 p-1 bg-emerald-500">Добавить в корзину</div>
          </div>
        </div>
      </div>

      <div class="card bg-base-100 image-full w-96 shadow-sm m-8">
        <figure>
          <img
              src="/img/voda2.jpg"
              alt="Болотная вода" />
        </figure>
        <div class="card-body">
          <h2 class="card-title">Болотная вода</h2>
          <p>Вода, добытая прямиком из благовещенских болот, бодрит тело и разум!</p>
          <div class="card-actions justify-end">
            <button class="btn btn-ghost border-none shadow-md shadow-emerald-800 hover:shadow-emerald-900 hover:bg-emerald-700 p-1 bg-emerald-500">В корзину!</button>
          </div>
        </div>
      </div>
    </div>

  </div>
</template>