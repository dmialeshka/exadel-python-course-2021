k = 1


def get_digits_number(num: int) -> int:
    count = 0
    while num > 0:
        count += 1
        num = num // 10
    return count


def is_narcissistic_num(num: int) -> bool:
    n: int = get_digits_number(num)
    nth: [int] = [int(digit) ** n for digit in str(num)]
    return num == sum(nth)


while 1 <= k <= 1000:
    if is_narcissistic_num(k):
        print(f'narcissistic number: {k}')
    k += 1
