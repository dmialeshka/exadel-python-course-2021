"""
Implement a console program to calculate triangle area.

Support at least 2 formulas:
By base and height
By 2 sides and the angle between them.

The program must have a menu in which the user can select a formula or exit the program.
The menu must be looped: when the calculation is done, the user is back to the menu and can select another menu option.
"""
import math


def get_values(data: str):
    return map(int, data.split())


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
    if operation is None:
        init_menu()
    operation()


init_menu()
