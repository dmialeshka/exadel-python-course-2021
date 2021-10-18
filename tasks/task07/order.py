import time
from uuid import uuid4


class Order:
    def __init__(self, client_id: uuid4, goods: list, order_date: time = time.strftime('%Y-%m-%d_%H:%M.%S')):
        self.order_id = uuid4()
        self.order_date = order_date
        self.client_id = client_id
        self.goods = goods
        self.total = goods

    def __repr__(self) -> str:
        return f'(order_id: {self.order_id} total: {self.total} order_date: {self.order_date})'

    @property
    def total(self):
        return self.__total
    
    @total.setter
    def total(self, goods):
        self.__total = 0
        for good in goods:
            self.__total += good.price
