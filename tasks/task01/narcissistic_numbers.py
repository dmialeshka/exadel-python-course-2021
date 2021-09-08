

def get_digits_number(num: int) -> tuple[int, list[int]]:
    count = 0
    digits = []
    while num > 0:
        count += 1
        digits.append(num % 10)
        num = num // 10
    return count, digits


def is_narcissistic_num(num: int) -> bool:
    count, digits = get_digits_number(num)
    nth = 0
    for digit in digits:
        nth += digit ** count
    return num == nth


for i in range(1, 1001):
    if is_narcissistic_num(i):
        print(f'narcissistic number: {i}')

