<template>
  <div class="max-w-xl mx-auto p-4">
    <h2 class="text-2xl font-bold mb-4 text-center">Админ-панель</h2>
    <div class="max-w-2xl mx-auto p-4">
      <div class="flex justify-between items-center mb-6">
        <h2 class="text-xl font-bold">Пользователи</h2>
        <button class="btn btn-ghost" @click="showForm = !showForm">
          ➕ Создать пользователя
        </button>
      </div>

      <!-- Форма создания пользователя -->
      <div v-if="showForm" class="card bg-base-200 shadow p-4 mb-6">
        <form @submit.prevent="createUser" class="space-y-3">
          <div>
            <label class="label-text">Имя (полное):</label>
            <input v-model="fullName" type="text" class="input w-full" required />
          </div>
          <div>
            <label class="label-text">Email:</label>
            <input v-model="email" type="email" class="input w-full" required />
          </div>
          <div>
            <label class="label-text">Пароль:</label>
            <input v-model="password" type="password" class="input w-full" required />
          </div>
          <div class="flex gap-2 mt-2">
            <button type="submit" class="btn btn-primary">Создать</button>
            <button type="button" class="btn btn-ghost" @click="resetForm">Отмена</button>
          </div>
          <div v-if="formSuccess" class="alert alert-success mt-2">{{ formSuccess }}</div>
          <div v-if="formError" class="alert alert-error mt-2">{{ formError }}</div>
        </form>
      </div>

      <!-- Таблица пользователей -->
      <div v-if="users && users.length" class="overflow-x-auto">
        <table class="table w-full bg-base-100 shadow rounded-lg">
          <thead>
          <tr>
            <th>Имя</th>
            <th>Email</th>
            <th>Действия</th>
          </tr>
          </thead>
          <tbody>
          <tr v-for="u in users" :key="u.id">
            <td v-if="editingUserId !== u.id">{{ u.full_name }}</td>
            <td v-else>
              <input v-model="editFullName" class="input input-sm w-full" />
            </td>
            <td v-if="editingUserId !== u.id">{{ u.email }}</td>
            <td v-else>
              <input v-model="editEmail" class="input input-sm w-full" />
            </td>
            <td class="flex gap-2">
              <button class="btn btn-xs btn-accent" @click="startEdit(u)" v-if="editingUserId !== u.id">✏️ Ред.</button>
              <button class="btn btn-xs btn-success" @click="saveEdit(u)" v-if="editingUserId === u.id">💾 Сохранить</button>
              <button class="btn btn-xs btn-ghost" @click="cancelEdit" v-if="editingUserId === u.id">❌</button>
              <button class="btn btn-xs btn-error" @click="deleteUser(u.id)">🗑️</button>
            </td>
          </tr>
          </tbody>
        </table>
      </div>
      <div v-else class="mt-2 text-center text-base-content-secondary">Пользователей пока нет</div>
    </div>
    <div class="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 gap-4 mt-10">
      <NuxtLink to="/admin/users" class="btn btn-primary btn-lg">👥 Пользователи</NuxtLink>
      <NuxtLink to="/admin/products" class="btn btn-primary btn-lg">📦 Товары</NuxtLink>
      <NuxtLink to="/admin/orders" class="btn btn-primary btn-lg">🛒 Заказы</NuxtLink>
      <NuxtLink to="/admin/delivery" class="btn btn-primary btn-lg">🚚 Доставка</NuxtLink>
      <NuxtLink to="/admin/logs" class="btn btn-primary btn-lg">📑 Логи доставки</NuxtLink>
      <button @click="logout" class="btn btn-error btn-lg">↩️ Выйти</button>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref, onMounted } from 'vue'
import { navigateTo } from '#app'

const API_URL = 'http://0.0.0.0:80/users/'

const showForm = ref(false)
const fullName = ref('')
const email = ref('')
const password = ref('')
const formSuccess = ref('')
const formError = ref('')

const users = ref<any[]>([])

const editingUserId = ref<number | null>(null)
const editFullName = ref('')

// Сбросить форму
const resetForm = () => {
  showForm.value = false
  fullName.value = ''
  email.value = ''
  password.value = ''
  formSuccess.value = ''
  formError.value = ''
}

// Получить пользователей
const fetchUsers = async () => {
  try {
    users.value = await $fetch(API_URL)
  } catch (e) {
    users.value = []
  }
}

// Создание пользователя через API
const createUser = async () => {
  formError.value = ''
  formSuccess.value = ''
  try {
    const payload = {
      email: email.value,
      full_name: fullName.value,
      password: password.value,
    }
    await $fetch(API_URL, {
      method: 'POST',
      body: payload,
    })
    formSuccess.value = 'Пользователь успешно создан!'
    resetForm()
    showForm.value = false
    await fetchUsers()
  } catch (e: any) {
    formError.value = e?.data?.detail || e.message || 'Ошибка создания пользователя'
  }
}

// Удаление пользователя
const deleteUser = async (id: number) => {
  if (!confirm('Удалить пользователя?')) return
  try {
    await $fetch(API_URL + id, { method: 'DELETE' })
    await fetchUsers()
  } catch (e) {
    alert('Ошибка удаления')
  }
}

const editEmail = ref('')

// Начать редактирование
const startEdit = (user: any) => {
  editingUserId.value = user.id
  editFullName.value = user.full_name
  editEmail.value = user.email
}

// Сохранить изменения
const saveEdit = async (user: any) => {
  try {
    await $fetch(API_URL + user.id, {
      method: 'PUT',
      body: {
        full_name: editFullName.value,
        email: editEmail.value
      },
    })
    editingUserId.value = null
    editFullName.value = ''
    editEmail.value = ''
    await fetchUsers()
  } catch (e) {
    alert('Ошибка обновления')
  }
}

// Отмена редактирования
const cancelEdit = () => {
  editingUserId.value = null
  editFullName.value = ''
  editEmail.value = ''
}

const logout = async () => {
  try {
    await $fetch('/logout', { method: 'POST' })
  } catch (e) {}
  await navigateTo('/')
}

onMounted(fetchUsers)
</script>
