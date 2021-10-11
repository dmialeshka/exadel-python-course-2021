from uuid import uuid4


class Good:
    def __init__(self, name: str, price: int):
        self.id = uuid4()
        self.name = name
        self.price = price

    def __str__(self):
        return f"good_id: {self.good_id}; name: {self.name}; price: {self.price}"

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        if value > 0:
            self.__price = value
        else:
            self.__price = 0
