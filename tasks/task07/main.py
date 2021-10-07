'''
Imagine you are implementing a backend for an online shop. Now you need to implement order storage.

Implement the following classes:
Good  - a good that user can buy. It has fields like id, name, price.
Order - a class representing an order in your application. It has fields like order_id, order_date, client_id, goods: List[Good], price (might be a computed property).
OrderRepository - an abstraction over some underlying storage that supports CRUD (Create Read Update Delete) operations over a collection of Order.
Use list or dict to store the data internally. OrderRepository should have methods like:
add(order: Order) - add order
get(order_id: UUID) -> Order - get one order by its id
list(n_latest:int = None) -> List[Order] - get n_latest orders or all orders if n_latest is None
delete(order_id: UUID)

Use assert to test your implementation, your testing flow can look like:
Add several records
List them, assert
'''
from uuid import uuid4
from faker import Faker
from good import Good
from order import Order
from order_repository import OrderRepository

fake = Faker()

def create_order() -> Order:
    goods = set(Good(fake.name(), fake.unique.random_int(min=1000, max=9999)) for i in range(5))
    return Order(uuid4(), goods)

order1 = create_order()
order2 = create_order()
order3 = create_order()

repository = OrderRepository()
assert len(repository.list()) == 0
repository.add(order1)
repository.add(order2)
repository.add(order3)
assert len(repository.list()) == 3
repository.delete(order2.order_id)

assert len(repository.list()) == 2