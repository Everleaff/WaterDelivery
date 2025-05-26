<template>
  <div v-if="isAdmin" class="w-full p-4 pl-30 pr-30">
    <h2 class="text-2xl font-bold mb-4 text-center">Админ-панель</h2>
    <div class=" p-4">
      <!-- Кнопки отображения/взаимодействия -->
      <div class="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 gap-2 mb-6">
        <button class="btn btn-ghost bg-teal-600 border-none hover:shadow-none hover:bg-teal-700 m-1 active:bg-teal-700" @click="showSection('users')">👥 Пользователи</button>
        <button class="btn btn-ghost bg-teal-600 border-none hover:shadow-none hover:bg-teal-700 m-1 active:bg-teal-700" @click="showSection('products')">📦 Товары</button>
        <button class="btn btn-ghost bg-teal-600 border-none hover:shadow-none hover:bg-teal-700 m-1 active:bg-teal-700" @click="showSection('orders')">🛒 Заказы</button>
        <button class="btn btn-ghost bg-teal-600 border-none hover:shadow-none hover:bg-teal-700 m-1 active:bg-teal-700" @click="showSection('delivery')">🚚 Курьеры</button>
        <button class="btn btn-ghost bg-teal-600 border-none hover:shadow-none hover:bg-teal-700 m-1 active:bg-teal-700" @click="showSection('logs')" disabled>📑 Логи</button>
        <button class="btn btn-ghost bg-red-500/80 border-none hover:shadow-none hover:bg-red-900 m-1 active:bg-red-900" @click="logout">↩️ Выйти</button>
      </div>

      <!-- --- Пользователи --- -->
      <section v-if="section==='users'">
        <div class="flex justify-between items-center mb-4">
          <h3 class="text-xl font-bold">Пользователи</h3>
          <button class="btn btn-ghost bg-teal-600 border-none hover:shadow-none hover:bg-teal-700 m-1 active:bg-teal-700" @click="showFormUsers = !showFormUsers">➕ Создать пользователя</button>
        </div>
        <div v-if="showFormUsers" class="card bg-base-200 shadow p-4 mb-6">
          <form @submit.prevent="createUser" class="space-y-3">
            <input v-model="userForm.full_name" placeholder="ФИО" class="input w-full" required />
            <input v-model="userForm.email" type="email" placeholder="Email" class="input w-full" required />
            <input v-model="userForm.password" type="password" placeholder="Пароль (мин. 6)" class="input w-full" required minlength="6"/>
            <div class="flex gap-2 mt-2">
              <button type="submit" class="btn btn-ghost bg-teal-600 border-none hover:shadow-none hover:bg-teal-700 m-1 active:bg-teal-700">Создать</button>
              <button type="button" class="btn btn-ghost bg-red-500/80 border-none hover:shadow-none hover:bg-red-900 m-1 active:bg-red-900" @click="resetUserForm">Отмена</button>
            </div>
            <div v-if="userForm.success" class="alert alert-success">{{ userForm.success }}</div>
            <div v-if="userForm.error" class="alert alert-error">{{ userForm.error }}</div>
          </form>
        </div>
        <div v-if="users.length" class="overflow-x-auto">
          <table class="table w-full bg-base-100 shadow rounded-lg">
            <thead>
            <tr>
              <th>ФИО</th><th>Email</th><th>Действия</th>
            </tr>
            </thead>
            <tbody>
            <tr v-for="u in filteredUsers" :key="u.id">
              <td v-if="editingUserId !== u.id">{{ u.full_name }}</td>
              <td v-else>
                <input v-model="editUserForm.full_name" class="input input-sm w-full" />
              </td>
              <td v-if="editingUserId !== u.id">{{ u.email }}</td>
              <td v-else>
                <input v-model="editUserForm.email" class="input input-sm w-full" />
              </td>
              <td class="flex gap-2">
                <button class="btn btn-xs btn-ghost bg-teal-600 border-none hover:shadow-none hover:bg-teal-700 m-1 active:bg-teal-700"                            @click="startEditUser(u)" v-if="editingUserId !== u.id">✏️ Ред.</button>
                <button class="btn btn-xs btn-success text-white bg-emerald-600 border-none hover:shadow-none hover:bg-emerald-700 m-1 active:bg-emerald-700"   @click="saveEditUser(u)" v-if="editingUserId === u.id">💾 Сохранить</button>
                <button class="btn btn-xs btn-warning self-center border-none m-1"                                                                                      @click="cancelEditUser" v-if="editingUserId === u.id">❌</button>
                <button class="btn btn-xs btn-error bg-red-500/80 border-none hover:shadow-none hover:bg-red-900 m-1 active:bg-red-900"                          @click="deleteUser(u.id)">🗑️</button>
              </td>
            </tr>
            </tbody>
          </table>
        </div>
        <div v-else class="text-center text-base-content-secondary mt-2">Пользователей пока нет</div>
      </section>

      <!-- --- Товары --- -->
      <section v-if="section==='products'">
        <div class="flex justify-between items-center mb-4">
          <h3 class="text-xl font-bold">Товары</h3>
          <button class="btn btn-ghost bg-teal-600 border-none hover:shadow-none hover:bg-teal-700 m-1 active:bg-teal-700" @click="showFormProducts = !showFormProducts">➕ Создать товар</button>
        </div>
        <div v-if="showFormProducts" class="card bg-base-200 shadow p-4 mb-6">
          <form @submit.prevent="createProduct" class="space-y-3">
            <input v-model="productForm.name" placeholder="Название" class="input w-full" required maxlength="100"/>
            <textarea v-model="productForm.description" placeholder="Описание" class="textarea w-full" required></textarea>
            <input v-model="productForm.price" type="number" min="0.01" step="0.01" placeholder="Цена" class="input w-full" required />
            <input v-model="productForm.image_url" type="url" placeholder="URL картинки (опционально)" class="input w-full" />
            <div class="flex gap-2 mt-2">
              <button type="submit" class="btn btn-ghost bg-teal-600 border-none hover:shadow-none hover:bg-teal-700 m-1 active:bg-teal-700">Создать</button>
              <button type="button" class="btn btn-ghost bg-red-500/80 border-none hover:shadow-none hover:bg-red-900 m-1 active:bg-red-900" @click="resetProductForm">Отмена</button>
            </div>
            <div v-if="productForm.success" class="alert alert-success">{{ productForm.success }}</div>
            <div v-if="productForm.error" class="alert alert-error">{{ productForm.error }}</div>
          </form>
        </div>
        <div v-if="products.length" class="overflow-x-auto">
          <table class="table w-full bg-base-100 shadow rounded-lg">
            <thead>
            <tr>
              <th>Название</th><th>Описание</th><th >Цена</th><th>URL картинки</th><th>Действия</th>
            </tr>
            </thead>
            <tbody>
            <tr v-for="p in filteredProducts" :key="p.id">
              <td v-if="editingProductId !== p.id">{{ p.name }}</td>
              <td v-else>
                <input v-model="editProductForm.name" class="input input-sm w-full" />
              </td>
              <td v-if="editingProductId !== p.id">{{ p.description }}</td>
              <td v-else>
                <input v-model="editProductForm.description" class="input input-sm w-full" />
              </td>
              <td v-if="editingProductId !== p.id" >{{ p.price }}</td>
              <td v-else>
                <input v-model="editProductForm.price" type="number" class="input input-md w-30" />
              </td>
              <td v-if="editingProductId !== p.id">{{ p.image_url }}</td>
              <td v-else>
                <input v-model="editProductForm.image_url" class="input input-sm w-full" />
              </td>
              <td class="flex gap-2">
                <button class="btn btn-xs btn-ghost  bg-teal-600 border-none hover:shadow-none hover:bg-teal-700 m-1 active:bg-teal-700"                           @click="startEditProduct(p)" v-if="editingProductId !== p.id">✏️ Ред.</button>
                <button class="btn btn-xs btn-success text-white bg-emerald-600 border-none hover:shadow-none hover:bg-emerald-700 m-1 active:bg-emerald-700"     @click="saveEditProduct(p)" v-if="editingProductId === p.id">💾 Сохранить</button>
                <button class="btn btn-xs btn-warning self-center border-none m-1"                                                                                @click="cancelEditProduct" v-if="editingProductId === p.id">❌</button>
                <button class="btn btn-xs btn-error bg-red-500/80 border-none hover:shadow-none hover:bg-red-900 m-1 active:bg-red-900"                           @click="deleteProduct(p.id)">🗑️</button>
              </td>
            </tr>
            </tbody>
          </table>
        </div>
        <div v-else class="text-center text-base-content-secondary mt-2">Товаров пока нет</div>
      </section>

      <!-- --- Заказы --- -->
      <section v-if="section==='orders'">
        <div class="flex justify-between items-center mb-4">
          <h3 class="text-xl font-bold">Заказы</h3>
          <button class="btn btn-ghost bg-teal-600 border-none hover:shadow-none hover:bg-teal-700 m-1 active:bg-teal-700" @click="showFormOrders = !showFormOrders">➕ Создать заказ</button>
        </div>
        <div v-if="showFormOrders" class="card bg-base-200 shadow p-4 mb-6">
          <form @submit.prevent="createOrder" class="space-y-3">
            <select v-model.number="orderForm.user_id" class="input w-full" required>
              <option value="" disabled>Выберите пользователя</option>
              <option v-for="u in users" :key="u.id" :value="u.id">{{ u.full_name }} ({{ u.email }})</option>
            </select>
            <div v-for="(item, idx) in orderForm.items" :key="idx" class="flex gap-2 mb-2">
              <select v-model.number="item.product_id" class="input w-1/3" required>
                <option value="" disabled>Товар</option>
                <option v-for="p in products" :key="p.id" :value="p.id">{{ p.name }}</option>
              </select>
              <input v-model.number="item.quantity" type="number" min="1" class="input w-1/4" placeholder="Кол-во" required/>
              <input v-model.number="item.price" type="number" min="0.01" step="0.01" class="input w-1/4" placeholder="Цена" required/>
              <button class="btn btn-xs btn-ghost self-center bg-red-500/80 border-none hover:shadow-none hover:bg-red-900 m-1 active:bg-red-900" type="button" @click="removeOrderItem(idx)">🗑️</button>
            </div>
            <button type="button" class="btn btn-xs bg-emerald-600 border-none hover:shadow-none hover:bg-emerald-700 m-1 active:bg-emerald-700" @click="addOrderItem">+ Добавить товар</button>
            <div class="flex gap-2 mt-2">
              <button type="submit" class="btn btn-ghost bg-teal-600 border-none hover:shadow-none hover:bg-teal-700 m-1 active:bg-teal-700">Создать заказ</button>
              <button type="button" class="btn btn-ghost bg-red-500/80 border-none hover:shadow-none hover:bg-red-900 m-1 active:bg-red-900" @click="resetOrderForm">Отмена</button>
            </div>
            <div v-if="orderForm.success" class="alert alert-success">{{ orderForm.success }}</div>
            <div v-if="orderForm.error" class="alert alert-error">{{ orderForm.error }}</div>
          </form>
        </div>
        <!-- Таблица заказов -->
        <div v-if="orders.length" class="overflow-x-auto">
          <table class="table w-full bg-base-100 shadow rounded-lg">
            <thead>
            <tr>
              <th>ID</th><th>Пользователь</th><th>Статус</th><th>Создан</th><th>Товары</th><th>Действия</th>
            </tr>
            </thead>
            <tbody>
            <tr v-for="o in filteredOrders" :key="o.id">
              <td>{{ o.id }}</td>
              <td>{{ getUserName(o.user_id) }}</td>
              <td>{{ o.status }}</td>
              <td>{{ o.created_at }}</td>
              <td>
                <ul>
                  <li v-for="item in o.items" :key="item.id">
                    {{ getProductName(item.product_id) }} × {{ item.quantity }} ({{ item.price }})
                  </li>
                </ul>
              </td>
              <td>
                <button class="btn btn-xs btn-ghost self-center bg-red-500/80 border-none hover:shadow-none hover:bg-red-900 m-1 active:bg-red-900" @click="deleteOrder(o.id)">🗑️</button>
              </td>
            </tr>
            </tbody>
          </table>
        </div>
        <div v-else class="text-center text-base-content-secondary mt-2">Заказов пока нет</div>
      </section>

      <!-- --- Доставка/Курьеры --- -->
      <section v-if="section==='delivery'">
        <div class="flex justify-between items-center mb-4">
          <h3 class="text-xl font-bold">Курьеры</h3>
          <button class="btn btn-ghost bg-teal-600 border-none hover:shadow-none hover:bg-teal-700 m-1 active:bg-teal-700" @click="showFormDelivery = !showFormDelivery">➕ Создать курьера</button>
        </div>
        <div v-if="showFormDelivery" class="card bg-base-200 shadow p-4 mb-6">
          <form @submit.prevent="createCourier" class="space-y-3">
            <input v-model="courierForm.name" placeholder="Имя" class="input w-full" required />
            <input v-model="courierForm.phone" placeholder="Телефон" class="input w-full" required />
            <div class="flex gap-2 mt-2">
              <button type="submit" class="btn btn-ghost bg-teal-600 border-none hover:shadow-none hover:bg-teal-700 m-1 active:bg-teal-700">Создать</button>
              <button type="button" class="btn btn-ghost bg-red-500/80 border-none hover:shadow-none hover:bg-red-900 m-1 active:bg-red-900" @click="resetCourierForm">Отмена</button>
            </div>
            <div v-if="courierForm.success" class="alert alert-success">{{ courierForm.success }}</div>
            <div v-if="courierForm.error" class="alert alert-error">{{ courierForm.error }}</div>
          </form>
        </div>
        <div v-if="couriers.length" class="overflow-x-auto">
          <table class="table w-full bg-base-100 shadow rounded-lg">
            <thead>
            <tr>
              <th>Имя</th><th>Телефон</th><th>Действия</th>
            </tr>
            </thead>
            <tbody>
            <tr v-for="c in filteredDelivery" :key="c.id">
              <td v-if="editingCourierId !== c.id">{{ c.name }}</td>
              <td v-else>
                <input v-model="editCourierForm.name" class="input input-sm w-full" />
              </td>
              <td v-if="editingCourierId !== c.id">{{ c.phone }}</td>
              <td v-else>
                <input v-model="editCourierForm.phone" class="input input-sm w-full" />
              </td>
              <td class="flex gap-2">
                <button class="btn btn-xs btn-ghost bg-teal-600 border-none hover:shadow-none hover:bg-teal-700 m-1 active:bg-teal-700"                           @click="startEditCourier(c)" v-if="editingCourierId !== c.id">✏️ Ред.</button>
                <button class="btn btn-xs btn-success text-white bg-emerald-600 border-none hover:shadow-none hover:bg-emerald-700 m-1 active:bg-emerald-700"     @click="saveEditCourier(c)" v-if="editingCourierId === c.id">💾 Сохранить</button>
                <button class="btn btn-xs btn-warning self-center border-none m-1"                                                                                @click="cancelEditCourier" v-if="editingCourierId === c.id">❌</button>
                <button class="btn btn-xs btn-error bg-red-500/80 border-none hover:shadow-none hover:bg-red-900 m-1 active:bg-red-900"                           @click="deleteCourier(c.id)">🗑️</button>
              </td>
            </tr>
            </tbody>
          </table>
        </div>
        <div v-else class="text-center text-base-content-secondary mt-2">Курьеров пока нет</div>
      </section>

      <!-- --- Логи --- -->
      <section v-if="section==='logs'">
        <div class="text-center font-bold text-2xl text-red-600 text-base-content-secondary mt-2">Логи пока не реализованы</div>
      </section>

      <!-- --- Поисковик --- -->
      <div class="flex gap-2 mt-4 items-center justify-center" v-if="section !== null || '' ">
        <select v-model="selectedColumn"  class="select select-bordered w-40">
          <option value="">Все столбцы</option>
          <option v-for="col in filterColumns[section]" :key="col.value" :value="col.value">
            {{ col.label }}
          </option>
        </select>
        <button class="btn btn-sm bg-teal-600 border-none hover:shadow-none hover:bg-teal-700 m-1 active:bg-teal-700"  @click="applySearch">🔍 Поиск</button>
        <input v-model="searchQuery" type="text" class="input input-bordered w-60" :placeholder="`Поиск по ${selectedColumn ? filterColumns[section].find(col => col.value === selectedColumn).label : 'всем столбцам'}...`" />
        <button class="btn btn-sm btn-error text-white bg-red-500/80 border-none hover:shadow-none hover:bg-red-900 m-1 active:bg-red-900"  v-if="searchQuery" @click="clearSearch">✖️ Очистить</button>
        <button class="btn btn-xs  shadow-none hover:shadow-none border-none text-white bg-white/0 !active:bg-none hover:bg-none"  v-if="search_clear === false"  @click="search_clear = !search_clear">✅ Очищать поиск при смене выгрузки</button>
        <button class="btn btn-xs  shadow-none hover:shadow-none border-none text-white bg-white/0 !active:bg-none hover:bg-none"  v-else-if="search_clear === true"  @click="search_clear = !search_clear">✖️ Очищать поиск при смене выгрузки</button>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import {ref, reactive, onMounted, computed} from 'vue'
import {navigateTo, useState} from '#app'

const API_URL_USERS = 'http://0.0.0.0:80/users/'
const API_URL_PRODUCTS = 'http://0.0.0.0:80/products/'
const API_URL_ORDERS = 'http://0.0.0.0:80/orders/'
const API_URL_COURIERS = 'http://0.0.0.0:80/delivery/couriers/'

const section = ref('users')
const search_clear = ref(false)

function showSection(sec: string) {
  if (search_clear.value === false)
  {
    clearSearch()
  }
  section.value = sec
  if (sec === 'users') fetchUsers()
  if (sec === 'products') fetchProducts()
  if (sec === 'orders') fetchOrders()
  if (sec === 'delivery') fetchCouriers()
}
// =============== Поисковик ===============

const filterColumns = {
  users: [
    { value: 'full_name', label: 'Имя' },
    { value: 'email', label: 'Email' },
  ],
  products: [
    { value: 'name', label: 'Название' },
    { value: 'description', label: 'Описание' },
  ],
  orders: [
    { value: 'user_name', label: 'Имя пользователя' },
    { value: 'status', label: 'Статус' },
    { value: 'product_name', label: 'Товар' }
  ],
  delivery: [
    { value: 'name', label: 'Имя курьера' },
    { value: 'phone', label: 'Телефон' }
  ],
}

const selectedColumn = ref('')
const searchQuery = ref('')

const filteredUsers = computed(() => {
  if (!searchQuery.value.trim()) return users.value
  const q = searchQuery.value.trim().toLowerCase()
  if (!selectedColumn.value){
    return users.value.filter(u =>
        (u.full_name && u.full_name.toLowerCase().includes(q)) ||
        (u.email && u.email.toLowerCase().includes(q))
    )
  }
  return users.value.filter(u =>
      (u[selectedColumn.value] && u[selectedColumn.value].toLowerCase().includes(q))
  )
})



const filteredProducts = computed(() => {
  if (!searchQuery.value.trim()) return products.value
  const q = searchQuery.value.trim().toLowerCase()
  if (!selectedColumn.value){
  return products.value.filter(p =>
      (p.name && p.name.toLowerCase().includes(q)) ||
      (p.description && p.description.toLowerCase().includes(q))
  )
  }
  return products.value.filter(p =>
      (p[selectedColumn.value] && p[selectedColumn.value].toLowerCase().includes(q))
  )
})

const filteredOrders = computed(() => {
  if (!searchQuery.value.trim()) return orders.value
  const q = searchQuery.value.trim().toLowerCase()
  if (!selectedColumn.value) {
    return orders.value.filter(o =>
        (getUserName(o.user_id) && getUserName(o.user_id).toLowerCase().includes(q)) ||
        (o.status && o.status.toLowerCase().includes(q)) ||
        (Array.isArray(o.items) && o.items.some(item => {
          const productName = getProductName(item.product_id)
          return productName && productName.toLowerCase().includes(q)
        }))
    )
  }
  if (selectedColumn.value === 'user_name') {
    return orders.value.filter(o => (getUserName(o.user_id) && getUserName(o.user_id).toLowerCase().includes(q)))
  }
  if (selectedColumn.value === 'status') {
    return orders.value.filter(o => (o.status && o.status.toLowerCase().includes(q)))
  }
  if (selectedColumn.value === 'product_name') {
    return orders.value.filter(o =>
            Array.isArray(o.items) && o.items.some(item => {
              const productName = getProductName(item.product_id)
              return productName && productName.toLowerCase().includes(q)
            })
    )
  }
  return orders.value
})

const filteredDelivery = computed(() => {
  if (!searchQuery.value.trim()) return couriers.value
  const q = searchQuery.value.trim().toLowerCase()
  return couriers.value.filter(d =>
      (d.name && d.name.toLowerCase().includes(q)) ||
      (d.phone && d.phone.toLowerCase().includes(q))
  )
})



const applySearch = () => { /* для дальнейших доработок, вдруг что нужно */ }
const clearSearch = () => { searchQuery.value = '' }




// =============== Пользователи ===============
const showFormUsers = ref(false)
const users = ref<any[]>([])
const userForm = reactive({ full_name: '', email: '', password: '', success: '', error: '' })
const editUserForm = reactive({ full_name: '', email: '', password: '' })
const editingUserId = ref<number|null>(null)

async function fetchUsers() {
  try { users.value = await $fetch(API_URL_USERS) } catch { users.value = [] }
}
function resetUserForm() { Object.assign(userForm, { full_name: '', email: '', password: '', success: '', error: '' }); showFormUsers.value = false }
async function createUser() {
  userForm.error = ''
  try {
    await $fetch(API_URL_USERS, { method: 'POST', body: { full_name: userForm.full_name, email: userForm.email, password: userForm.password } })
    userForm.success = 'Пользователь создан!'
    resetUserForm()
    await fetchUsers()
  } catch (e: any) { userForm.error = e?.data?.detail || e.message || 'Ошибка создания' }
}
function startEditUser(u: any) { editingUserId.value = u.id; editUserForm.full_name = u.full_name; editUserForm.email = u.email; editUserForm.password = '' }
function cancelEditUser() { editingUserId.value = null; editUserForm.full_name = ''; editUserForm.email = ''; editUserForm.password = '' }
async function saveEditUser(u: any) {
  try {
    await $fetch(API_URL_USERS + u.id, { method: 'PUT', body: { full_name: editUserForm.full_name, email: editUserForm.email, password: editUserForm.password || undefined } })
    editingUserId.value = null; await fetchUsers()
  } catch (e) { alert('Ошибка обновления') }
}
async function deleteUser(id: number) {
  if (!confirm('Удалить пользователя?')) return
  try { await $fetch(API_URL_USERS + id, { method: 'DELETE' }); await fetchUsers() } catch { alert('Ошибка удаления') }
}

// =============== Товары ===============
const showFormProducts = ref(false)
const products = ref<any[]>([])
const productForm = reactive({ name: '', description: '', price: '', image_url: '', success: '', error: '' })
const editProductForm = reactive({ name: '', description: '', price: '', image_url: '' })
const editingProductId = ref<number|null>(null)

async function fetchProducts() { try { products.value = await $fetch(API_URL_PRODUCTS) } catch { products.value = [] } }
function resetProductForm() { Object.assign(productForm, { name: '', description: '', price: '', image_url: '', success: '', error: '' }); showFormProducts.value = false }
async function createProduct() {
  productForm.error = ''
  try {
    await $fetch(API_URL_PRODUCTS, { method: 'POST', body: { name: productForm.name, description: productForm.description, price: productForm.price, image_url: productForm.image_url || null } })
    productForm.success = 'Товар создан!'
    resetProductForm()
    await fetchProducts()
  } catch (e: any) { productForm.error = e?.data?.detail || e.message || 'Ошибка создания' }
}
function startEditProduct(p: any) { editingProductId.value = p.id; editProductForm.name = p.name; editProductForm.description = p.description; editProductForm.price = p.price; editProductForm.image_url = p.image_url }
function cancelEditProduct() { editingProductId.value = null; editProductForm.name = ''; editProductForm.description = ''; editProductForm.price = ''; editProductForm.image_url = '' }
async function saveEditProduct(p: any) {
  try {
    await $fetch(API_URL_PRODUCTS + p.id, { method: 'PUT', body: { name: editProductForm.name, description: editProductForm.description, price: editProductForm.price, image_url: editProductForm.image_url || null } })
    editingProductId.value = null; await fetchProducts()
  } catch (e) { alert('Ошибка обновления') }
}
async function deleteProduct(id: number) {
  if (!confirm('Удалить товар?')) return
  try { await $fetch(API_URL_PRODUCTS + id, { method: 'DELETE' }); await fetchProducts() } catch { alert('Ошибка удаления') }
}

// =============== Заказы ===============
const showFormOrders = ref(false)
const orders = ref<any[]>([])
const orderForm = reactive({ user_id: '', items: [], success: '', error: '' })
function resetOrderForm() { Object.assign(orderForm, { user_id: '', items: [], success: '', error: '' }); showFormOrders.value = false }
function addOrderItem() { orderForm.items.push({ product_id: '', quantity: 1, price: 0 }) }
function removeOrderItem(idx: number) { orderForm.items.splice(idx, 1) }
async function fetchOrders() { try { orders.value = await $fetch(API_URL_ORDERS) } catch { orders.value = [] } }
async function createOrder() {
  orderForm.error = ''
  try {
    await $fetch(API_URL_ORDERS, { method: 'POST', body: { user_id: orderForm.user_id, items: orderForm.items } })
    orderForm.success = 'Заказ создан!'
    resetOrderForm()
    await fetchOrders()
  } catch (e: any) { orderForm.error = e?.data?.detail || e.message || 'Ошибка создания заказа' }
}
async function deleteOrder(id: number) {
  if (!confirm('Удалить заказ?')) return
  try { await $fetch(API_URL_ORDERS + id, { method: 'DELETE' }); await fetchOrders() } catch { alert('Ошибка удаления заказа') }
}
function getUserName(id: number) { return users.value.find(u => u.id === id)?.full_name || '' }
function getProductName(id: number) { return products.value.find(p => p.id === id)?.name || '' }

// =============== Доставка / Курьеры ===============
const showFormDelivery = ref(false)
const couriers = ref<any[]>([])
const courierForm = reactive({ name: '', phone: '', success: '', error: '' })
const editCourierForm = reactive({ name: '', phone: '' })
const editingCourierId = ref<number|null>(null)

async function fetchCouriers() { try { couriers.value = await $fetch(API_URL_COURIERS) } catch { couriers.value = [] } }
function resetCourierForm() { Object.assign(courierForm, { name: '', phone: '', success: '', error: '' }); showFormDelivery.value = false }
async function createCourier() {
  courierForm.error = ''
  try {
    await $fetch(API_URL_COURIERS, { method: 'POST', body: { name: courierForm.name, phone: courierForm.phone } })
    courierForm.success = 'Курьер создан!'
    resetCourierForm()
    await fetchCouriers()
  } catch (e: any) { courierForm.error = e?.data?.detail || e.message || 'Ошибка создания курьера' }
}
function startEditCourier(c: any) { editingCourierId.value = c.id; editCourierForm.name = c.name; editCourierForm.phone = c.phone }
function cancelEditCourier() { editingCourierId.value = null; editCourierForm.name = ''; editCourierForm.phone = '' }
async function saveEditCourier(c: any) {
  try {
    await $fetch(API_URL_COURIERS + c.id, { method: 'PUT', body: { name: editCourierForm.name, phone: editCourierForm.phone } })
    editingCourierId.value = null; await fetchCouriers()
  } catch (e) { alert('Ошибка обновления') }
}
async function deleteCourier(id: number) {
  if (!confirm('Удалить курьера?')) return
  try { await $fetch(API_URL_COURIERS + id, { method: 'DELETE' }); await fetchCouriers() } catch { alert('Ошибка удаления курьера') }
}

// =============== Логи (пока не реализовано) ===============
// Не забыть добавить секцию для логов

async function logout() {
  try { await $fetch('/logout', { method: 'POST' }) } catch {}
  await navigateTo('/')
}

const user = useState('authUser', () => null)
const isAdmin = computed(() => user.value && user.value.email === 'admin@mail.ru')

onMounted(() => {
  fetchUsers()
  fetchProducts()
  fetchOrders()
  fetchCouriers()
})

watch(section, () => {
    selectedColumn.value = ''
})
</script>
