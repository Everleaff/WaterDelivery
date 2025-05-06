<template>
  <div class="bg-cyan-600 bg-[url(/img/boloto.jpg)] bg-center bg-cover bg-no-repeat min-h-screen ">
    <div class="text-white flex-row" >
      <div class="sticky top-0 flex justify-between z-10">
        <div class="navbar bg-teal-600 pr-4  opacity-90 z-10">
          <div class="navbar-start">
            <NuxtLink to="/" draggable="false">
               <button class="btn btn-ghost border-none hover:shadow-none hover:bg-teal-700 m-1 text-xl active:bg-teal-700">Доставка воды от Романа</button>
            </NuxtLink>
          </div>
          <div class="navbar-center lg:flex ">
            <NuxtLink to="/water" draggable="false" >
              <button  class="btn btn-ghost border-none hover:shadow-none hover:bg-teal-700 m-1 active:bg-teal-700">Товары</button>
            </NuxtLink>
            <NuxtLink to="/delivery" draggable="false">
              <button  class="btn btn-ghost border-none hover:shadow-none hover:bg-teal-700 m-1 active:bg-teal-700">Доставка</button>
            </NuxtLink>
            <NuxtLink to="/about" draggable="false">
              <button  class="btn btn-ghost border-none hover:shadow-none hover:bg-teal-700 m-1 active:bg-teal-700">О нас</button>
            </NuxtLink>
          </div>
          <div class="navbar-end">
<!--            Будет показываться, если человек прошел регистрацию/логин:-->
<!--            <div class="flex space-x-4">-->

<!--              <details class="dropdown dropdown-end">-->
<!--                <summary class="btn btn-ghost border-none hover:shadow-none hover:bg-teal-700 m-1">-->
<!--                  Профиль-->
<!--                </summary>-->
<!--                <ul class="menu dropdown-content bg-teal-800 opacity-90 rounded-box z-1 w-52 p-2 shadow-sm">-->
<!--                  <li><a>Просмотреть профиль</a></li>-->
<!--                  <li class="bg-red-900 rounded-b-md"><a>Выйти из аккаунта</a></li>-->
<!--                </ul>-->
<!--              </details>-->

<!--              <details class="dropdown dropdown-end">-->
<!--                <summary class="btn btn-ghost border-none hover:shadow-none hover:bg-teal-700 m-1">-->
<!--                  Профиль-->
<!--                </summary>-->
<!--                <ul class="menu dropdown-content bg-teal-800 opacity-90 rounded-box z-1 w-52 p-2 shadow-sm">-->
<!--                  <li><a>Просмотреть профиль</a></li>-->
<!--                  <li class="bg-red-900 rounded-b-md"><a>Выйти из аккаунта</a></li>-->
<!--                </ul>-->
<!--              </details>-->


<!--              <details class="dropdown ">-->
<!--                <summary class="btn btn-ghost border-none hover:shadow-none hover:bg-teal-700  m-1 ">-->

<!--                  <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24">&lt;!&ndash; Icon from Huge Icons by Hugeicons - undefined &ndash;&gt;<g fill="none" stroke="white" stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" color="white"><path d="m8 16l8.72-.727c2.729-.227 3.341-.823 3.643-3.544L21 6M6 6h16"/><circle cx="6" cy="20" r="2"/><circle cx="17" cy="20" r="2"/><path d="M8 20h7M2 2h.966c.945 0 1.768.625 1.997 1.515L7.94 15.076a1.96 1.96 0 0 1-.35 1.686L6.631 18"/></g></svg>-->
<!--                    Корзина-->
<!--                </summary>-->
<!--                <ul class="menu dropdown-content bg-teal-800 opacity-85 rounded-box z-1 w-52 p-2 shadow-sm">-->
<!--                  <li class=""><a>Просмотреть корзину</a></li>-->
<!--                  <li class="bg-red-900 rounded-b-md"><a>Очистить корзину</a></li>-->
<!--                </ul>-->
<!--              </details>-->
<!--              <div class="avatar">-->
<!--                <div class="w-12 rounded-md">-->
<!--                  <img src="https://img.daisyui.com/images/stock/photo-1534528741775-53994a69daeb.webp" />-->
<!--                </div>-->
<!--              </div>-->

<!--            </div>-->

            <div class="flex space-x-4">
              <button class="btn btn-ghost border-none hover:shadow-none hover:bg-teal-700 m-1 active:bg-teal-700" v-on:click="log_reg_tab = !log_reg_tab">Аккаунт</button>
            </div>


          </div>

        </div>
        <div class="absolute !z-20 bg-black/40 h-screen w-screen place-items-center justify-center flex top-0 fixed" v-if="log_reg_tab===true"  v-on:dblclick.self="log_reg_tab = false">
          <Tabs default-value="login" class="w-[400px] z-30 ">
            <TabsList class="grid w-full grid-cols-2 bg-teal-600  gap-4 ">
              <TabsTrigger value="login" class="!text-white font-semibold data-[state=active]:bg-teal-700">
                Логин
              </TabsTrigger>
              <TabsTrigger value="registration" class="!text-white font-semibold data-[state=active]:bg-teal-700">
                Регистрация
              </TabsTrigger>
            </TabsList>
            <TabsContent value="login"  class="" >
              <Card class="bg-teal-600 text-white border-none">
                <CardHeader>
                  <CardTitle>Вход</CardTitle>
                  <CardDescription class="text-white/50">
                    <p>Здесь вы можете войти в свой аккаунт.</p>
                    <p>Заполните поля ниже</p>
                  </CardDescription>
                </CardHeader>
                <CardContent class="space-y-2">
                  <div class="space-y-1">
                    <Label for="login">Логин</Label>
                    <Input id="login" v-model="form_log.login" class="bg-teal-700 text-white border-none placeholder:text-white/50 focus:placeholder-transparent" placeholder="Ваш логин"  />
                  </div>
                  <div class="space-y-1">
                    <Label for="password">Пароль</Label>
                     <div class="flex gap-2">
                        <Input id="password" v-model="form_log.password" :type="show_pass_log ? 'text' : 'password'" class="bg-teal-700 text-white border-none focus:placeholder-transparent placeholder:text-white/50" type="password" placeholder="Ваш пароль для входа"  />
                        <Button type="button" v-on:click="show_pass_log = !show_pass_log" class=" bg-teal-500 hover:bg-teal-700 p-2 rounded-md">
                          <Icon :name="show_pass_log ? 'mdi:eye-off' : 'mdi:eye'" class="w-6 h-6 text-white"/>
                        </Button>
                      </div>
                  </div>
                </CardContent>
                <CardFooter>
                  <Button class="bg-teal-500 hover:bg-teal-700 text-white">Войти</Button>
                </CardFooter>
              </Card>
            </TabsContent>
            <TabsContent value="registration">
              <Card class="bg-teal-600 text-white border-none">
                <CardHeader>
                  <CardTitle>Регистрация</CardTitle>
                  <CardDescription class="text-white/50">
                    <p>Здесь вы можете создать новый аккаунт.</p>
                    <p>Заполните поля ниже</p>
                  </CardDescription>
                </CardHeader>
                <CardContent class="space-y-2">
                  <div class="space-y-1">
                    <Label for="name">Имя</Label>
                    <Input id="name" v-model="form_reg.name" class="bg-teal-700 text-white border-none focus:placeholder-transparent placeholder:text-white/50" placeholder="Ваше имя. Так к Вам будут обращаться при заказе" />
                  </div>
                  <div class="space-y-1">
                    <Label for="login">Логин</Label>
                    <Input id="login" v-model="form_reg.login" class="bg-teal-700 text-white border-none focus:placeholder-transparent placeholder:text-white/50" type="text" placeholder="Ваш логин. По нему осуществляется вход на сайт" />
                  </div>
                  <div class="space-y-1">
                    <Label for="email">Почта</Label>
                    <Input id="email" v-model="form_reg.email" class="bg-teal-700 text-white border-none focus:placeholder-transparent placeholder:text-white/50" type="email" placeholder="Ваша почта. Для безопасности аккаунта" />
                  </div>
                  <div class="space-y-1">
                    <Label for="phone">Номер телефона</Label>
                    <Input id="phone" v-model="form_reg.phone"  class="bg-teal-700 text-white border-none focus:placeholder-transparent placeholder:text-white/50" type="tel" placeholder="Ваш номер. Детали заказа по звонку"  />
                  </div>
                  <div class="space-y-1">
                    <Label for="password"  >Пароль</Label>
                    <div class="flex gap-2">
                      <Input id="password" v-model="form_reg.password" :type="show_pass ? 'text' : 'password'" class="bg-teal-700 text-white border-none focus:placeholder-transparent placeholder:text-white/50" type="password" placeholder="Ваш пароль. Он будет использоваться для входа"  />
                      <Button type="button" v-on:click="show_pass = !show_pass" class=" bg-teal-500 hover:bg-teal-700 p-2 rounded-md">
                        <Icon :name="show_pass ? 'mdi:eye-off' : 'mdi:eye'" class="w-6 h-6 text-white"/>
                      </Button>
                    </div>

                  </div>

                  <div class="space-y-1">
                    <Label for="password_conf">Повторный пароль</Label>
                    <div class="flex gap-2">
                      <Input id="password_conf" v-model="form_reg.password_conf" :type="show_confirm ? 'text' : 'password'" class="bg-teal-700 text-white border-none focus:placeholder-transparent placeholder:text-white/50" type="password" placeholder="Повторный пароль. Для проверки"  />
                      <Button type="button" v-on:click="show_confirm = !show_confirm" class="bg-teal-500 hover:bg-teal-700 p-2 rounded-md">
                        <Icon :name="show_confirm ? 'mdi:eye-off' : 'mdi:eye'" class="w-6 h-6 text-white"/>
                      </Button>
                    </div>
                  </div>

                </CardContent>
                <CardFooter>
                  <Button class="bg-teal-500 hover:bg-teal-700 text-white">Зарегистрироваться</Button>
                </CardFooter>
              </Card>
            </TabsContent>
          </Tabs>
        </div>



      </div>

      <slot/>


    </div>
    <footer class="sticky mt-20  top-full flex  w-full  justify-between bg-teal-600 text-neutral-content p-10 opacity-90">
      <aside>
        <svg
            width="50"
            height="50"
            viewBox="0 0 24 24"
            xmlns="http://www.w3.org/2000/svg"
            fill-rule="evenodd"
            clip-rule="evenodd"
            class="fill-current">
          <path
              d="M22.672 15.226l-2.432.811.841 2.515c.33 1.019-.209 2.127-1.23 2.456-1.15.325-2.148-.321-2.463-1.226l-.84-2.518-5.013 1.677.84 2.517c.391 1.203-.434 2.542-1.831 2.542-.88 0-1.601-.564-1.86-1.314l-.842-2.516-2.431.809c-1.135.328-2.145-.317-2.463-1.229-.329-1.018.211-2.127 1.231-2.456l2.432-.809-1.621-4.823-2.432.808c-1.355.384-2.558-.59-2.558-1.839 0-.817.509-1.582 1.327-1.846l2.433-.809-.842-2.515c-.33-1.02.211-2.129 1.232-2.458 1.02-.329 2.13.209 2.461 1.229l.842 2.515 5.011-1.677-.839-2.517c-.403-1.238.484-2.553 1.843-2.553.819 0 1.585.509 1.85 1.326l.841 2.517 2.431-.81c1.02-.33 2.131.211 2.461 1.229.332 1.018-.21 2.126-1.23 2.456l-2.433.809 1.622 4.823 2.433-.809c1.242-.401 2.557.484 2.557 1.838 0 .819-.51 1.583-1.328 1.847m-8.992-6.428l-5.01 1.675 1.619 4.828 5.011-1.674-1.62-4.829z"></path>
        </svg>
        <p>
          ACME Industries Ltd.
          <br />
          Providing reliable tech since 1992
        </p>
      </aside>
      <nav>
        <h6 class="footer-title">Social</h6>
        <div class="grid grid-flow-col gap-4">
          <a>
            <svg
                xmlns="http://www.w3.org/2000/svg"
                width="24"
                height="24"
                viewBox="0 0 24 24"
                class="fill-current">
              <path
                  d="M24 4.557c-.883.392-1.832.656-2.828.775 1.017-.609 1.798-1.574 2.165-2.724-.951.564-2.005.974-3.127 1.195-.897-.957-2.178-1.555-3.594-1.555-3.179 0-5.515 2.966-4.797 6.045-4.091-.205-7.719-2.165-10.148-5.144-1.29 2.213-.669 5.108 1.523 6.574-.806-.026-1.566-.247-2.229-.616-.054 2.281 1.581 4.415 3.949 4.89-.693.188-1.452.232-2.224.084.626 1.956 2.444 3.379 4.6 3.419-2.07 1.623-4.678 2.348-7.29 2.04 2.179 1.397 4.768 2.212 7.548 2.212 9.142 0 14.307-7.721 13.995-14.646.962-.695 1.797-1.562 2.457-2.549z"></path>
            </svg>
          </a>
          <a>
            <svg
                xmlns="http://www.w3.org/2000/svg"
                width="24"
                height="24"
                viewBox="0 0 24 24"
                class="fill-current">
              <path
                  d="M19.615 3.184c-3.604-.246-11.631-.245-15.23 0-3.897.266-4.356 2.62-4.385 8.816.029 6.185.484 8.549 4.385 8.816 3.6.245 11.626.246 15.23 0 3.897-.266 4.356-2.62 4.385-8.816-.029-6.185-.484-8.549-4.385-8.816zm-10.615 12.816v-8l8 3.993-8 4.007z"></path>
            </svg>
          </a>
          <a>
            <svg
                xmlns="http://www.w3.org/2000/svg"
                width="24"
                height="24"
                viewBox="0 0 24 24"
                class="fill-current">
              <path
                  d="M9 8h-3v4h3v12h5v-12h3.642l.358-4h-4v-1.667c0-.955.192-1.333 1.115-1.333h2.885v-5h-3.808c-3.596 0-5.192 1.583-5.192 4.615v3.385z"></path>
            </svg>
          </a>
        </div>
      </nav>
    </footer>
  </div>




</template>

<script setup lang="ts">

const log_reg_tab = ref(false)

const form_reg = reactive({
  name:     '',
  login:    '',
  email:    '',
  phone:    '',
  password: '',
  password_conf:  '',
})

const form_log = reactive({
  login:    '',
  password: '',
})

const show_pass    = ref(false)
const show_pass_log    = ref(false)
const show_confirm = ref(false)

const passwordsMatch = computed(
    () => form_reg.password !== '' && form_reg.password === form_reg.password_conf
)


function open_auth_modal() {
  log_reg_tab.value = true
}

provide('open_auth_modal', open_auth_modal)

</script>