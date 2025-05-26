<template>
  <div class="max-w-lg mx-auto rounded-md bg-teal-600/80 p-8 mt-12 text-center">
    <div v-if="!isAuth">
      <div class="alert alert-warning text-lg font-semibold mb-4 text-black text-center">
        Необходимо войти, чтобы просматривать профиль
      </div>
      <div class="flex  justify-between">
        <button class="btn btn-ghost bg-teal-600 border-none hover:shadow-none hover:bg-teal-700 mt-4 w-46"
                @click="open_login_modal && open_login_modal()">
          Войти
        </button>
        <button class="btn btn-ghost bg-teal-600 border-none hover:shadow-none hover:bg-teal-700 mt-4 w-56"
                @click="open_auth_modal && open_auth_modal()">
          Зарегистрироваться
        </button>
      </div>

    </div>

    <div v-else>
      <h2 class="text-2xl font-bold mb-2 text-white text-shadow-md">Профиль</h2>
      <div class="flex flex-col gap-3 items-center">
        <div class="avatar">
          <div class="w-24 rounded-full bg-teal-100 flex items-center justify-center">
            <span class="text-4xl text-teal-700">{{ initials }}</span>
          </div>
        </div>
        <div class="text-lg font-semibold mt-2">{{ user.full_name || user.name }}</div>
        <div class="text-white text-shadow-md">{{ user.email }}</div>
        <div v-if="isAdmin" class="mt-3">
          <NuxtLink to="/account/admin" class="btn btn-ghost bg-red-500/80 border-none hover:shadow-none hover:bg-red-900 m-1 active:bg-red-900" >
            Перейти в админ-панель
          </NuxtLink>
        </div>
        <div v-else class="mt-2">
          <span class="text-gray-400 text-shadow-md text-sm">Обычный пользователь</span>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { useState } from '#app'
import { computed } from 'vue'

const user = useState('authUser', () => null)
const isAuth = computed(() => user.value && user.value.id)
const isAdmin = computed(() => user.value && user.value.email === 'admin@mail.ru')

const initials = computed(() => {
  if (!user.value) return ''
  const parts = (user.value.full_name || user.value.name || '').split(' ')
  if (!parts.length) return ''
  if (parts.length === 1) return parts[0][0]
  return parts[0][0] + parts[1][0]
})

const open_login_modal = inject<() => void>('open_login_modal')
const open_auth_modal = inject<() => void>('open_auth_modal')
</script>
