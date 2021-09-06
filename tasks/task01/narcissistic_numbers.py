import math

k = int(input('Please enter an integer: '))


def get_digits_number(num: int) -> int:
    return int(math.log(num, 10)) + 1


def is_narcissistic_num(num: int) -> bool:
    n: int = get_digits_number(num)
    nth: [int] = [int(digit) ** n for digit in str(num)]
    return num == sum(nth)


while 1 <= k <= 1000:
    if is_narcissistic_num(k):
        print(f'narcissistic number: {k}')
    k += 1
