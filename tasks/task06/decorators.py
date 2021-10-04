'''
Sometimes, for debugging or analysis purposes,  we need to measure the execution time of a function.
In Python, we can use decorators to implement execution time measurement in a nice way.
'''
from time import time, sleep


def measure_elapsed_time(fn):
    def wrapper(*args, **kwargs):
        print(f'calling {fn.__name__}')
        start = time()
        result = fn(*args, **kwargs)
        delta = round(time() - start, 1)
        print(f'{fn.__name__} call took {delta} seconds')
        return result

    return wrapper


@measure_elapsed_time
def my_fn1(arg1, arg2):
    sleep(0.5)
    return arg1 + arg2


@measure_elapsed_time
def my_fn2():
    sleep(0.8)
    print('I do nothing! What a life')


@measure_elapsed_time
def my_fn3(arg1, **kwargs):
    sleep(0.3)
    print(f'I also do nothing, but I have arg1 = {arg1} and kwargs = {kwargs}')


print('my_fn1 result:', my_fn1(1, 2))
my_fn2()
my_fn3(12, kwarg1='lol', kwarg2='kek')