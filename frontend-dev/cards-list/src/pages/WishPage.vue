<template>
    <q-page padding>
        <div class="q-ma-md">
            <q-card class="my-card">
                <q-card-section>
                    <!-- таблица с картами в списке желаемого -->
                    <q-table
                        title="Карты в списке желаемого"
                        :rows="state.cards"
                        :columns="state.columns_table"
                        row-key="name"
                        :rows-per-page-options="[0]"
                    >

                        <!-- изменяем отображение столбца с название карты -->
                        <template v-slot:body-cell-card_name_EU="props">
                            <q-td :props="props">
                                <b>{{ props.row.card_name_EU}}</b>
                                </q-td>
                        </template>

                        <!-- изменяем отображение столбца с название карты -->
                        <template v-slot:body-cell-card_name_RU="props">
                            <q-td :props="props">
                                <b>{{ props.row.card_name_RU}}</b>
                            </q-td>
                        </template>

                        <!-- изменяем отображение столбца со статусом -->
                        <template v-slot:body-cell-order_status="props">
                            <q-td :props="props">
                                <q-chip :color="[props.row.order_status === 'хочу' ? 'primary' : 'green'] " text-color="white" :label="props.row.order_status" />
                            </q-td>
                        </template>

                        <!-- изменяем отображение столбца со кнопкой изменить -->
                        <template v-slot:body-cell-update="props">
                            <q-td :props="props">
                                <q-btn 
                                    @click="showUpdateCard(
                                        props.row.order_id,
                                        props.row.card_name_RU,
                                        props.row.card_name_EU,
                                        props.row.count,
                                        props.row.user_name,
                                        props.row.order_status
                                    )"
                                    color="orange" 
                                    icon="mode_edit" 
                                />
                            </q-td>
                        </template>

                        <!-- изменяем отображение столбца со кнопкой удалить -->
                        <template v-slot:body-cell-delete="props">
                            <q-td :props="props">
                                <q-btn color="red" icon="delete" @click="state.deleteCardId = props.row.order_id; state.deleteCard = true"/>
                            </q-td>
                        </template>

                        <!-- изменяем отображение столбца со кнопкой заказть карту -->
                        <template v-slot:body-cell-order="props">
                            <q-td :props="props">
                                <q-btn color="primary" icon="add" @click="showOrderCard(
                                    props.row.order_id,
                                    props.row.card_name_EU,
                                    props.row.card_name_RU,
                                    props.row.count,
                                    props.row.user_name
                                    )"/>
                            </q-td>
                        </template>


                        

                    </q-table>
                    <!-- конец таблицы с картами в списке желаемого -->
                </q-card-section>
                <q-card-section>

                    <!-- кнопка для добавления карт в список желаемого -->
                    <div class="column">
                        <q-btn color="primary" icon="add" label="Добавить карту" @click="state.addCard = true;" />
                    </div>
                    <!-- конец кнопки для добавления карт в список желемого -->


                    <!-- диалоговое окно для добавления карты в список желаемого -->
                    <q-dialog v-model="state.addCard" persistent>
                        <q-card>
                            <q-card-section class="row items-center">
                                <span class="q-ml-sm text-center text-h5">Добавить карту в список желаемого</span>

                                <!-- блок с полями для добавления карты в список желаемого -->
                                <div class="q-my-md col-12">
                                    <q-input class="q-my-sm" outlined  v-model="state.addCardNameRU" type="text" label="Название(RU)" />
                                    <q-input class="q-my-sm" outlined  v-model="state.addCardNameEU" type="text" label="Название(EU)" />
                                    <q-input class="q-my-sm" outlined  v-model="state.addCardCount" min="1" type="number" label="Количество" />
                                    <q-input autocomplete="on" class="q-my-sm" outlined  v-model="state.addCardUserName" type="text" label="Кто добавил" />
                                    <q-select class="q-my-sm" v-model="state.addCardStatus" :options="state.cardStatus" label="Статус" outlined />
                                </div>
                                <!-- конец блока с полями для добавления карты в список желаемого -->
                            </q-card-section>
                            <q-card-actions align="right">
                                <q-btn flat label="Отмена" color="red" v-close-popup />
                                <q-btn 
                                    v-if="
                                        state.addCardNameEU != null &
                                        state.addCardUserName != null &
                                        state.addCardStatus != null
                                    "
                                    flat label="Добавить карту" color="green" @click="addCardWish()" />
                            </q-card-actions>
                        </q-card>
                    </q-dialog>
                    <!-- конец диалового окна для добавления карт в список желаемого -->
                   
                    <!-- диалоговое окно для удаления карточки из списка желвемого -->
                    <q-dialog v-model="state.deleteCard" persistent>
                        <q-card>
                            <q-card-section class="items-center">
                                <div class="row">
                                    <q-avatar icon="delete" color="red" text-color="white" />
                                    <span class="q-ma-sm text-center text-h5">Вы точно хотите удалить эту карту?</span>
                                </div>
                                
                            </q-card-section>
                            <q-card-actions align="right">
                                <q-btn flat label="Нет" color="red" v-close-popup />
                                <q-btn flat label="Да" color="green" @click="deleteCardWish()" />
                            </q-card-actions>
                        </q-card>
                    </q-dialog>
                    <!-- конец диалогового окно для удаления карточки из списка желвемого -->


                    <!-- диалоговое окно для обновления информации о карточке -->
                    <q-dialog v-model="state.updateCard" persistent>
                        <q-card>
                            <q-card-section class="cloumn items-center">
                                <!-- название карточки -->
                                <div class="row">
                                    <q-avatar color="orange" icon="mode_edit" text-color="white" />
                                    <span class="q-ma-sm text-center text-h5">Изменить информацию о карте</span>
                                </div>

                                <!-- блок с полями для данных -->
                                <div class="q-my-md col-12">
                                    <q-input color="orange" class="q-my-sm" outlined  v-model="state.updateCardNameRU" type="text" label="Название(RU)" />
                                    <q-input color="orange" class="q-my-sm" outlined  v-model="state.updateCardNameEU" type="text" label="Название(EU)" />
                                    <q-input color="orange" class="q-my-sm" outlined  v-model="state.updateCardCount" min="1" type="number" label="Количество" />
                                    <q-input color="orange" autocomplete="on" class="q-my-sm" outlined  v-model="state.updateCardUserName" type="text" label="Кто добавил" />
                                    <q-select color="orange" class="q-my-sm" v-model="state.updateCardStatus" :options="state.cardStatus" label="Статус" outlined />
                                </div>
                                <!-- конец блока с полями для данных -->

                                
                            </q-card-section>
                            <q-card-actions align="right">
                                <q-btn flat label="Отмена" color="red" v-close-popup />
                                <q-btn flat label="Изменить" color="orange" @click="updateCardWish()" />
                            </q-card-actions>
                        </q-card>
                    </q-dialog>
                    <!-- конец диалогового окна для обновления информации о карточке -->

                    <!-- диалоговое окно для заказа карточки -->
                    <q-dialog v-model="state.orderCard" persistent>
                        <q-card>
                            <q-card-section class="column items-center">

                                <div class="row">
                                    <q-avatar icon="add" color="primary" text-color="white" />
                                    <span class="q-ma-sm text-h5">Вы точно заказаываете эту карту?</span>
                                </div>

                                <div class="column text-center">
                                    <q-list bordered>
                                        <q-item>
                                            <q-item-section avatar>
                                                <div>Название(RU):</div>
                                            </q-item-section>
                                            <q-item-section>
                                                <b>{{ state.orderCardNameRU }}</b>
                                            </q-item-section>
                                        </q-item>

                                        <q-item>
                                            <q-item-section avatar>
                                                <div>Название(EU):</div>
                                            </q-item-section>
                                            <q-item-section>
                                                <b>{{ state.orderCardNameEU }}</b>
                                            </q-item-section>
                                        </q-item>   

                                        <q-item>
                                            <q-item-section avatar>
                                                <div>Количество:</div>
                                            </q-item-section>
                                            <q-item-section>
                                                <b>{{ state.orderCardCount }}</b>
                                            </q-item-section>
                                        </q-item>   

                                        <q-item>
                                            <q-item-section avatar>
                                                <div>Кто добавил:</div>
                                            </q-item-section>
                                            <q-item-section>
                                                <b>{{ state.orderCardUser }}</b>
                                            </q-item-section>
                                        </q-item>   

                                    </q-list>
                                </div>

                            </q-card-section>
                            <q-card-actions align="right">
                                <q-btn flat label="Нет" color="red" v-close-popup />
                                <q-btn flat label="Да" color="green" @click="orderCardWish()" />
                            </q-card-actions>
                        </q-card>
                    </q-dialog>
                    <!-- конец диалового окна для добавления карточки -->
                </q-card-section>
            </q-card>
        </div>
    </q-page>
</template>

<script setup>
import axios from 'axios';
import { reactive, onMounted } from 'vue';

//состояние страницы
const state = reactive({

    //статусы карт
    cardStatus: [],

    //карты в списке желаемого
    cards: [],

    //состояние для карточки добавления карты
    addCard: false,

    // параметры для добавления карты
    addCardNameRU: null,
    addCardNameEU: null,
    addCardCount: 1,
    addCardUserName: null,
    addCardStatus: null,


    //состояние для карточки обновления данных карты
    updateCard: false,

    // параметры для обновления карт карты
    updateCardId: null,
    updateCardNameRU: null,
    updateCardNameEU: null,
    updateCardCount: 1,
    updateCardUserName: null,
    updateCardStatus: null,


    //состояние для карточки удаления карты
    deleteCard: false,
    
    //параметры для удаление карты
    deleteCardId: null,

    //состояние для карточки добавления карты в заказнные
    orderCard: false,

    //параметры для заказа карты
    orderCardId: null,
    orderCardNameRU: null,
    orderCardNameEU: null,
    orderCardCount: null,
    orderCardUser: null,

    //параметры для таблицы, которая отражает карты
    columns_table: [
        { name: 'card_name_RU', align: 'center', label: 'Название(RU)', field: row => row.card_name_RU, sortable: true },
        { name: 'card_name_EU', align: 'center', label: 'Название(EU)', field: row => row.card_name_EU, sortable: true },
        { name: 'count', align: 'center', label: 'Количество', field: row => row.count, sortable: true },
        { name: 'date_add', align: 'center', label: 'Дата добавления', field: row => row.date_add, sortable: true },
        { name: 'user_name', align: 'center', label: 'Кто добавил', field: row => row.user_name, sortable: true },
        { name: 'order_status', align: 'center', label: 'Статус', field: row => row.order_status, sortable: true },

        //кнопки для манипуляции с данными
        { name: 'update', align: 'center', label: 'Изменение данных' },
        { name: 'delete', align: 'center', label: 'Удаление карты' },
        { name: 'order', align: 'center', label: 'Заказть карту' }

    ],

    //путь к бекенду
    backend_url: import.meta.env.VITE_BACKEND_ADDRESS
})

//функция для получения карт в списке
function getCardsWish(){
    axios.get(`${state.backend_url}/wish`)
    .then((res)=>{
        state.cards = res.data.cards;
    })
}

//функция для получение статусов для карт
function getCardStatus(){
    axios.get(`${state.backend_url}/cards_status`)
    .then((res)=>{
        state.cardStatus = res.data.cards_status;
    })
}

//функция для добавления карт в список
function addCardWish(){
    if (state.addCardNameRU === null){
        state.addCardNameRU = 'Отсутствует'
    }
    axios.post(`${state.backend_url}/wish`, {
        card_name_RU: state.addCardNameRU,
        card_name_EU: state.addCardNameEU,
        count: state.addCardCount,
        user_name: state.addCardUserName,
        order_status: state.addCardStatus
    }).then(()=>{
        state.addCardNameRU = null;
        state.addCardNameEU = null;
        state.addCardCount = 1;
        state.addCardUserName = null;
        state.addCardStatus = null;
        state.addCard = false;
        getCardsWish();
    })
}

//функция удаления карты из списка
function deleteCardWish(){
    axios.delete(`${state.backend_url}/wish/${state.deleteCardId}`)
    .then(()=>{
        state.deleteCardId = null;
        state.deleteCard = false;
        getCardsWish();
    })
}   


//функция для показа карты с обновлением информации о карточке
function showUpdateCard(
    CardId,
    CardNameRU,
    CardNameEU,
    CardCount,
    CardUserName,
    CardStatus,
){
    state.updateCardId = CardId;
    state.updateCardNameRU = CardNameRU;
    state.updateCardNameEU = CardNameEU;
    state.updateCardCount = CardCount;
    state.updateCardUserName = CardUserName;
    state.updateCardStatus = CardStatus;
    state.updateCard = true;
}

//функция для обновления данных о карте
function updateCardWish(){
    axios.put(`${state.backend_url}/wish/${state.deleteCardId}`,{
        order_id: state.updateCardId,
        card_name_RU: state.updateCardNameRU,
        card_name_EU: state.updateCardNameEU,
        count: state.updateCardCount,
        user_name: state.updateCardUserName,
        order_status: state.updateCardStatus
    }).then((res)=>{
        getCardsWish();
        state.updateCard = false;
    })
}

//функция для показа диалового окна для заказ карты
function showOrderCard(
    orderId,
    orderNameEU,
    orderNameRU,
    orderCount,
    orderUserName
){
    state.orderCardId = orderId;
    state.orderCardNameEU = orderNameEU;
    state.orderCardNameRU = orderNameRU;
    state.orderCardCount = orderCount;
    state.orderCardUser = orderUserName;
    state.orderCard = true;
}

//функция для заказа карты
function orderCardWish(){
    axios.put(`${state.backend_url}/order/${state.orderCardId}`)
    .then((res)=>{
        getCardsWish();
        state.orderCard = false;
    })
}


//при загрузке страницы
onMounted(()=>{
    getCardsWish();
    getCardStatus();
});

</script>