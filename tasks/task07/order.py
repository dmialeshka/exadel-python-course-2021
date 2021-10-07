import time
from uuid import uuid4


class Order:
    def __init__(self, client_id: uuid4, goods: list, order_date=time.strftime('%Y-%m-%d_%H:%M.%S')):
        self.order_id = uuid4()
        self.order_date = order_date
        self.client_id = client_id
        self.goods = goods
        self.total = 0

        for good in self.goods:
            self.total += good.price

    def info(self):
         return self.order_id, self.order_date, self.client_id, self.goods, self.total