from fastapi import FastAPI
from db_tools import DBControler
from swagger_settings import description, tags_metadata
import models
from fastapi.middleware.cors import CORSMiddleware #для настройки CORS
from datetime import datetime


app = FastAPI(
    title="API для сайта с карточками",
    summary="API для реализации работы серверной части учета карточек, которые хотят люди, чтобы делать совместные покупки",
    description=description,
    version="0.0.1",
    openapi_tags=tags_metadata
    )

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


#получения списка желания карточек
@app.get("/wish", tags=["Список желания"])
def get_cards_in_wish() -> dict:
    result = []
    dbControler = DBControler()
    wish_cards = dbControler.makeQueri('SELECT * FROM CardOrders WHERE order_status != ?', sqlParams=(models.ORDERED,))

    for wc in wish_cards:
        result.append({
            'order_id': wc[0],
            'card_name_RU': wc[1],
            'card_name_EU': wc[2],
            'count': wc[3],
            'date_add': datetime.strptime(wc[4], '%Y-%m-%d %H:%M:%S.%f').strftime('%d.%m.%Y'),
            'user_name': wc[5],
            'order_status': wc[6]
        })
    
    del dbControler

    return {
        "cards": result
    }


#добавление карты в список желаемого
@app.post("/wish", tags=["Список желания"])
def add_card_to_wish(card: models.CardOrders) -> str:
    dbControler = DBControler()
    dbControler.makeQueri(
        sqlQueri=f'INSERT INTO CardOrders(card_name_RU, card_name_EU, count, date_add, user_name, order_status) values(?, ?, ?, ?, ?, ?)',
        sqlParams=(
            card.card_name_RU,
            card.card_name_EU,
            card.count,
            card.date_add,
            card.user_name,
            card.order_status
            ),
        changeState=True,
        resultState=False
        )
    del dbControler
    return f"card {card.card_name_RU} count = {card.count} from {card.user_name} add to wish"


#удаление карты из списка желаемого
@app.delete("/wish/{order_id}", tags=["Список желания"])
def delete_card_from_wish(order_id: int) -> str:
    dbControler = DBControler()
    dbControler.makeQueri(
        'DELETE FROM CardOrders WHERE order_id = ?', 
        sqlParams=(order_id,),
        changeState=True,
        resultState=False
        )
    del dbControler
    return f"card with id={order_id} is deleted"


#обновление карты из списка желаемого
@app.put("/wish/{order_id}", tags=["Список желания"])
def update_card_in_wish(card: models.CardOrders) -> str:
    dbControler = DBControler()
    dbControler.makeQueri(
        'UPDATE CardOrders SET card_name_RU=?, card_name_EU=?, count=?, date_add=?, user_name=?, order_status=? WHERE order_id=?',
        sqlParams=(card.card_name_RU, card.card_name_EU, card.count, card.date_add, card.user_name, card.order_status, card.order_id),
        changeState=True,
        resultState=False
    )
    del dbControler
    return f"card with id={card.order_id} is updated"


#заказ карты через обновление статуса
@app.put("/order/{order_id}", tags=["Заказать карту"])
def order_card(order_id: int) -> str:
    dbControler = DBControler()
    dbControler.makeQueri(
        'UPDATE CardOrders SET order_status=? WHERE order_id=?',
        sqlParams=(models.ORDERED, order_id),
        changeState=True,
        resultState=False
        )
    del dbControler
    return f"card with {order_id} is ordered"
        

#получени списка карт, которые уже заказаны
@app.get("/orders", tags=["Список статусов карт"])
def get_cards_in_orders() -> dict:
    result = []
    dbControler = DBControler()
    orderCards = dbControler.makeQueri(
        "SELECT * FROM CardOrders WHERE order_status=?",
        sqlParams=(models.ORDERED,)
        )
    
    for oc in orderCards:
        result.append({
            'order_id': oc[0],
            'card_name_RU': oc[1],
            'card_name_EU': oc[2],
            'count': oc[3],
            'date_add': oc[4],
            'user_name': oc[5],
            'order_status': oc[6]
        })

    del dbControler
    return {
        "cards": result
    }

#получение всех статусов карт
@app.get('/cards_status', tags=["Спиоск статусов карт"])
def get_cards_status() -> dict:
    return {
        "cards_status": models.CARDS_STATUS
    }