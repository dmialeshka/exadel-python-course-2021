import math


def get_values(data: str):
    values = data.split(' ')
    first_v = int(values[0])
    second_v = int(values[1])
    if len(values) == 2:
        return first_v, second_v
    return first_v, second_v, int(values[2])


def print_area(area):
    print(f'Area is: {area}')
    init_menu()


def base_calculate():
    data: str = input('Enter base and height: ')
    b, h = get_values(data)
    area = int(round((0.5 * b * h), 1))
    print_area(area)


def calculate_with_angle():
    data: str = input('Enter 2 sides and angle(degrees) between them: ')
    side_a, side_b, angle = get_values(data)
    area = int(round((0.5 * side_a * side_b * math.sin(math.radians(angle))), 1))
    print_area(area)


def close():
    print('Goodbye!')
    exit(0)


def init_menu():
    print("""
    Welcome to the triangle area calculation tool.
    
    Menu:
    1. Calculate triangle area by base and height
    2. Calculate triangle area by 2 sides and angle between them
    3. Exit
    """)
    number: int = int(input('Enter menu item number: '))
    operations = {
        1: base_calculate,
        2: calculate_with_angle,
        3: close
    }
    operation = operations.get(number)
    operation()


init_menu()
