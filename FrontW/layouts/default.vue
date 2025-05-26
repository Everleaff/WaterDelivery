<template>
  <div class="bg-cyan-600 bg-[url(/img/boloto.jpg)] bg-center bg-cover bg-no-repeat min-h-screen ">
    <div class="text-white flex-row">
      <div class="sticky top-0 flex justify-between z-10 ">
        <div class="navbar bg-teal-600 pr-4  opacity-90 z-10">
          <div class="navbar-start">
            <NuxtLink to="/" draggable="false" class="flex">
              <img v-if="route.path === '/delivery'" src="public/img/ЛоготипWaterDelivery1.png" class="w-20 h-14" />
              <img v-else src="public/img/ЛоготипWaterDelivery2.png" class="w-20 h-14" />
              <button
                  class="btn btn-ghost border-none hover:shadow-none hover:bg-teal-700 m-1 text-xl active:bg-teal-700">
                Water Delivery

              </button>
            </NuxtLink>
          </div>
          <div class="navbar-center lg:flex ">
            <NuxtLink to="/water" draggable="false">
              <button class="btn btn-ghost border-none hover:shadow-none hover:bg-teal-700 m-1 active:bg-teal-700">
                Товары
              </button>
            </NuxtLink>
            <NuxtLink to="/delivery" draggable="false">
              <button class="btn btn-ghost border-none hover:shadow-none hover:bg-teal-700 m-1 active:bg-teal-700">
                Доставка
              </button>
            </NuxtLink>
            <NuxtLink to="/about" draggable="false">
              <button class="btn btn-ghost border-none hover:shadow-none hover:bg-teal-700 m-1 active:bg-teal-700">О
                нас
              </button>
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

              <div class="indicator">
                <span v-if="cartCount"
                      class="indicator-item indicator-start sm:indicator-middle md:indicator-bottom lg:indicator-center xl:indicator-end badge badge-secondary w-4 bg-emerald-700 opacity-95">{{ cartCount }}</span>
                <NuxtLink to="/cart"
                          class="btn btn-ghost border-none hover:shadow-none hover:bg-teal-700 m-1 active:bg-teal-700">
                  Корзина
                </NuxtLink>
              </div>
              <div v-if="toastText" class="toast toast-center z-[9999] mb-6">
                <div class="text-white font-semibold" :class="['alert', toastType === 'success' ? 'alert-success' : 'alert-info']">
                  <span>{{ toastText }}</span>
                </div>
              </div>

              <div v-if="authUser && authUser.full_name" class="dropdown dropdown-end">
                <div tabindex="0" role="button" class="btn btn-ghost bg-teal-600 border-none hover:shadow-none hover:bg-teal-700 m-1 active:bg-teal-700">{{ authUser.full_name }}</div>
                <ul tabindex="0" class="menu dropdown-content bg-teal-700 rounded-box z-20 w-52 p-2 shadow-sm mt-2">
                  <li><NuxtLink to="/account/profile" class="btn btn-ghost bg-teal-600 border-none hover:shadow-none hover:bg-teal-700 m-1 active:bg-teal-700">Профиль</NuxtLink></li>
                  <li><a v-on:click="logout" class="btn btn-ghost bg-teal-600 border-none hover:shadow-none hover:bg-teal-700 m-1 active:bg-teal-700">Выйти</a></li>
                </ul>
              </div>
              <button v-else class="btn btn-ghost border-none hover:shadow-none hover:bg-teal-700 m-1 active:bg-teal-700"
                      v-on:click="log_reg_tab = !log_reg_tab; open_login_modal()">Аккаунт
              </button>

            </div>


          </div>

        </div>
        <div class="absolute !z-20 bg-black/40 h-screen w-screen place-items-center justify-center flex top-0 fixed"
             v-if="log_reg_tab===true" v-on:click.self="closeForm">
          <div class="absolute !z-30  h-full w-1/3 place-items-center justify-center flex fixed"
               v-if="log_reg_tab===true" v-on:dblclick.self="closeForm">
            <Tabs v-model="log_reg_modal_type" class="w-[400px] !z-30 ">
              <TabsList class="grid w-full grid-cols-2 bg-teal-600  gap-4 ">
                <TabsTrigger value="login"
                             class="!text-white border-none font-semibold data-[state=active]:bg-teal-700">
                  Логин
                </TabsTrigger>
                <TabsTrigger value="registration"
                             class="!text-white border-none font-semibold data-[state=active]:bg-teal-700">
                  Регистрация
                </TabsTrigger>
              </TabsList>
              <TabsContent value="login" class="">
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
                      <Label for="login">Почта</Label>
                      <Input id="login" v-model="form_log.email"
                             class="bg-teal-700 text-white border-none placeholder:text-white/50 focus:placeholder-transparent"
                             placeholder="Ваша почта"/>
                    </div>
                    <div class="space-y-1">
                      <Label for="password">Пароль</Label>
                      <div class="flex gap-2">
                        <Input id="password" v-model="form_log.password" :type="show_pass_log ? 'text' : 'password'"
                               class="bg-teal-700 text-white border-none focus:placeholder-transparent placeholder:text-white/50"
                               type="password" placeholder="Ваш пароль для входа"/>
                        <Button type="button" v-on:click="show_pass_log = !show_pass_log"
                                class=" bg-teal-500 hover:bg-teal-700 p-2 rounded-md">
                          <Icon :name="show_pass_log ? 'mdi:eye-off' : 'mdi:eye'" class="w-6 h-6 text-white"/>
                        </Button>
                      </div>
                    </div>
                  </CardContent>
                  <CardFooter>
                    <Button class="bg-teal-500 hover:bg-teal-700 text-white" v-on:click="loginUser">Войти</Button>
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
                      <Label for="name">ФИО</Label>
                      <Input id="name" v-model="form_reg.name"
                             class="bg-teal-700 text-white border-none focus:placeholder-transparent placeholder:text-white/50"
                             placeholder="Ваше ФИО. Для удобства обращения при заказе"/>
                    </div>
                    <!--                    <div class="space-y-1">-->
                    <!--                      <Label for="login">Логин</Label>-->
                    <!--                      <Input id="login" v-model="form_reg.login" class="bg-teal-700 text-white border-none focus:placeholder-transparent placeholder:text-white/50" type="text" placeholder="Ваш логин. По нему осуществляется вход на сайт" />-->
                    <!--                    </div>-->
                    <div class="space-y-1">
                      <Label for="email">Почта</Label>
                      <Input id="email" v-model="form_reg.email"
                             class="bg-teal-700 text-white border-none focus:placeholder-transparent placeholder:text-white/50"
                             type="email" placeholder="Ваша почта. Для безопасности аккаунта"/>
                    </div>
                    <!--                    <div class="space-y-1">-->
                    <!--                      <Label for="phone">Номер телефона</Label>-->
                    <!--                      <Input id="phone" v-model="form_reg.phone"  class="bg-teal-700 text-white border-none focus:placeholder-transparent placeholder:text-white/50" type="tel" placeholder="Ваш номер. Детали заказа по звонку"  />-->
                    <!--                    </div>-->
                    <div class="space-y-1">
                      <Label for="password">Пароль</Label>
                      <div class="flex gap-2">
                        <Input id="password" v-model="form_reg.password" :type="show_pass ? 'text' : 'password'"
                               class="bg-teal-700 text-white border-none focus:placeholder-transparent placeholder:text-white/50"
                               type="password" placeholder="Ваш пароль. Он будет использоваться для входа"/>
                        <Button type="button" v-on:click="show_pass = !show_pass"
                                class=" bg-teal-500 hover:bg-teal-700 p-2 rounded-md">
                          <Icon :name="show_pass ? 'mdi:eye-off' : 'mdi:eye'" class="w-6 h-6 text-white"/>
                        </Button>
                      </div>

                    </div>

                    <div class="space-y-1">
                      <Label for="password_conf">Повторный пароль</Label>
                      <div class="flex gap-2">
                        <Input id="password_conf" v-model="form_reg.password_conf"
                               :type="show_confirm ? 'text' : 'password'"
                               class="bg-teal-700 text-white border-none focus:placeholder-transparent placeholder:text-white/50"
                               type="password" placeholder="Повторный пароль. Для проверки"/>
                        <Button type="button" v-on:click="show_confirm = !show_confirm"
                                class="bg-teal-500 hover:bg-teal-700 p-2 rounded-md">
                          <Icon :name="show_confirm ? 'mdi:eye-off' : 'mdi:eye'" class="w-6 h-6 text-white"/>
                        </Button>
                      </div>
                    </div>

                  </CardContent>
                  <CardFooter>
                    <Button class="bg-teal-500 hover:bg-teal-700 text-white" v-on:click="registerUser">
                      Зарегистрироваться
                    </Button>
                  </CardFooter>
                </Card>
              </TabsContent>
            </Tabs>

          </div>
        </div>


      </div>

      <slot/>


    </div>
    <footer
        class="sticky mt-20  top-full flex  w-full  justify-between bg-teal-600 text-neutral-content p-10 opacity-90">
      <aside>
        <img src="public/img/ЛоготипWaterDelivery2.png" class="w-20 h-14" />
        <p>
          Water Delivery
          <br/>
          Лучшая доставка воды
          <br/>
          2025
        </p>
      </aside>
      <nav>
        <h6 class="footer-title">Медиа</h6>
        <div class="grid grid-flow-col gap-4">
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
        </div>
      </nav>
    </footer>
  </div>


</template>

<script setup lang="ts">

const log_reg_tab = ref(false)
const authUser = useState('authUser', () => null)
import { useRoute } from 'vue-router'
const route = useRoute()

import { ref, computed, onMounted } from 'vue'

const cartCount = ref(0)
function getCartCount() {
  if (process.client) {
    // ВАЖНО! — теперь считаем уникальные товары
    const cart = JSON.parse(localStorage.getItem('cart') || '[]')
    cartCount.value = cart.length
  }
}
function refreshCart() {
  getCartCount()
}
onMounted(() => {
  getCartCount()
  window.addEventListener('storage', getCartCount)
})
const toastText = ref('')
const toastType = ref('info')
function showToast(text, type = 'info') {
  toastText.value = text
  toastType.value = type
  setTimeout(() => toastText.value = '', 1800)
}
if (process.client) {
  window.showToast = showToast
  window.refreshCart = refreshCart
}

function closeForm() {
  log_reg_tab.value = false
  resetForms();
}
const form_reg = reactive({
  name: '',
  email: '',
  password: '',
  password_conf: '',
})
function resetForms() {
  form_reg.name = ''
  form_reg.email = ''
  form_reg.password = ''
  form_reg.password_conf = ''
}
const form_log = reactive({
  email: '',
  password: '',
})
const show_pass = ref(false)
const show_pass_log = ref(false)
const show_confirm = ref(false)
const passwordsMatch = computed(
    () => form_reg.password !== '' && form_reg.password === form_reg.password_conf
)
const log_reg_modal_type = ref("login")
function open_login_modal() {
  log_reg_modal_type.value = "login"
  log_reg_tab.value = true
}
function open_auth_modal() {
  log_reg_modal_type.value = "registration"
  log_reg_tab.value = true
}
async function registerUser() {
  if (!form_reg.name.trim() || !form_reg.email.trim() || !form_reg.password.trim()) {
    alert('Пожалуйста, заполните все поля');
    return;
  }
  if (form_reg.password !== form_reg.password_conf) {
    alert('Пароли не совпадают');
    return;
  }
  try {
    const response = await $fetch('http://0.0.0.0:80/auth/register', {
      method: 'POST',
      body: {
        full_name: form_reg.name,
        email: form_reg.email,
        password: form_reg.password,
      }
    });
    authUser.value = response;
    log_reg_tab.value = false;
    resetForms();
  } catch (e: any) {
    alert(e.data?.message || e.message || 'Ошибка регистрации');
  }
}
async function loginUser() {
  if (!form_log.email.trim() || !form_log.password.trim()) {
    alert('Введите логин и пароль');
    return;
  }
  try {
    const body = new URLSearchParams();
    body.append('username', form_log.email);
    body.append('password', form_log.password);
    const response = await $fetch('http://0.0.0.0:80/auth/login', {
      method: 'POST',
      body,
      headers: {
        'Content-Type': 'application/x-www-form-urlencoded'
      }
    });
    const accessToken = response.access_token;
    const user = await $fetch('http://0.0.0.0:80/users/me', {
      headers: {
        Authorization: `Bearer ${accessToken}`
      }
    });
    authUser.value = user;
    log_reg_tab.value = false;
    resetForms();
  } catch (e: any) {
    alert(e.data?.message || e.message || 'Ошибка входа');
  }
}
function logout(){
  { authUser.value = null }
}
provide('open_auth_modal', open_auth_modal)
provide('open_login_modal', open_login_modal)

</script>