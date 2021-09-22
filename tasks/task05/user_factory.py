"""
Implement a function create_user(...) that supports the following semantics:
"""


def create_user(*args, age=42, **kwargs):
    return {
        'name': args[0],
        'surname': args[1],
        'age': age,
        'extra': kwargs
    }


assert create_user("John", "Doe") == \
       {
           "name": "John",
           "surname": "Doe",
           "age": 42,
           "extra": {}
       }

assert create_user("Bill", "Gates", age=65) == \
       {
           "name": "Bill",
           "surname": "Gates",
           "age": 65,
           "extra": {}
       }

assert create_user("Marie", "Curie", age=66, occupation="physicist", won_nobel=True) == \
       {
           "name": "Marie",
           "surname": "Curie",
           "age": 66,
           "extra": {
               "occupation": "physicist",
               "won_nobel": True
           }
       }
