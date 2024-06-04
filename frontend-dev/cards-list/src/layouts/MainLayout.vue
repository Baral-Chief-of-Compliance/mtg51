<template>
  <q-layout view="lHh Lpr lFf">
    <!-- хедер вместе с навигационной панелью -->
    <q-header bordered  class="bg-grey-3 text-primary">
        <q-toolbar>
          <!-- <q-btn flat round dense icon="menu" class="q-mr-sm" />
          <q-avatar>
            <img src="https://cdn.quasar.dev/logo-v2/svg/logo-mono-white.svg">
          </q-avatar> -->

          <q-toolbar-title>МТГ51</q-toolbar-title>

          <!-- <q-btn flat round dense icon="whatshot" /> -->
        </q-toolbar>

        <q-tabs v-model="tab">
          <q-tab @click="router.push({name: 'Wish'})" name="wish" label="Список желаемого" />
          <q-tab @click="router.push({name: 'Orders'})" name="orders" label="Заказанные карты" />
          <!-- <q-tab @click="router.push({name: 'UsefulLinks'})" name="usefulLinks" label="Полезнные ссылки" /> -->
        </q-tabs>
    </q-header>
    <!-- конец хедера вместе с навигационной панелью -->

    <q-page-container>
      <router-view />
    </q-page-container>
  </q-layout>
</template>

<script setup>
import { useRouter } from 'vue-router'

//переменная для роутера
const router = useRouter()


defineOptions({
  name: 'MainLayout'
})

</script>
