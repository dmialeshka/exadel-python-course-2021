from uuid import uuid4


class Good:
    def __init__(self, name: str, price: int):
        self.id = uuid4()
        self.name = name
        self.price = price

    def info(self):
        return self.id, self.name, self.price
