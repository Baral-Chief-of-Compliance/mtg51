from pydantic import BaseModel
from datetime import datetime


#статусы карточек
REALLY_WANT = 'очень хочу'
WANT = 'хочу'
ORDERED = 'заказана'

#список всех статусов
CARDS_STATUS = [REALLY_WANT, WANT, ORDERED]

#модель для заказов
class CardOrders(BaseModel):
    order_id: int or None = None
    card_name_RU: str = 'Отсутствует'
    card_name_EU: str
    count: int
    date_add: datetime = datetime.today()
    user_name: str
    order_status: str