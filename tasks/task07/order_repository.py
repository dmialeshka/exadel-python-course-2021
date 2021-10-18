from order import Order
import uuid

class OrderRepository:
    def __init__(self):
        self.orders = []

    def add(self, order: Order):
        self.orders.append(order)

    def get(self, order_id: uuid) -> Order:
        return next(x for x in self.orders if x.order_id == order_id)

    def orders_list(self, n_latest:int = None) -> list:
        if n_latest is None or n_latest > len(self.order_list):
            return self.orders
        else:
            return self.orders[-n_latest:]

    def delete(self, order_id: uuid):
        self.orders = [x for x in self.orders if x.order_id != order_id]
