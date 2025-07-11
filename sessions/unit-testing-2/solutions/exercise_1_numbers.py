from random import randint

def add_two_numbers(a, b):
    return a + b

def get_random_number():
    return randint(1, 10)

def add_number_with_random_number(a, get_random_number):
    return a + get_random_number()

def add_two_random_numbers(get_random_number):
    return get_random_number() + get_random_number()

def get_random_number_di(randint):
    return randint(1, 10)
