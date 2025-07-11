from random import randint # generates random numbers

def get_random_number():
    return randint(1, 10)

# added a argument that will be of type Function
def add_number_and_random(num1, number_generator = get_random_number):
    # call the provided function
    return num1 + number_generator()


# usage
result = add_number_and_random(10)
print(f"result = {result}")
