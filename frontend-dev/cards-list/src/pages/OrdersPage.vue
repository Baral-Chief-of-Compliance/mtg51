<template>
    <q-page padding>
        <q-card class="my-card">
                <q-card-section>
                    <q-table
                        title="Заказанные карты"
                        :rows="state.cards"
                        :columns="state.columns_table"
                        row-key="name"
                        :rows-per-page-options="[0]"
                    />
                </q-card-section>
        </q-card>
    </q-page>
</template>


<script setup>
import axios from 'axios';
import { reactive, onMounted } from 'vue';


//состояние страницы
const state = reactive({

    //список заказанных карт
    cards: [],

    //параметры для таблицы, которая отражает карты
    columns_table: [
        { name: 'card_name_RU', align: 'center', label: 'Название(RU)', field: row => row.card_name_RU, sortable: true },
        { name: 'card_name_EU', align: 'center', label: 'Название(EU)', field: row => row.card_name_EU, sortable: true },
        { name: 'count', align: 'center', label: 'Количество', field: row => row.count, sortable: true },
        { name: 'user_name', align: 'center', label: 'Кто добавил', field: row => row.user_name, sortable: true },
    ],

    //путь к бекенду
    backend_url: import.meta.env.VITE_BACKEND_ADDRESS
})

//получить список заказнных уже карт
function getOrderedCars(){
    axios.get(`${state.backend_url}/orders`)
    .then((res)=>{
        state.cards = res.data.cards;
    })
}

//функции при загрузке страницы
onMounted(()=>{
    getOrderedCars(); 
})

</script>