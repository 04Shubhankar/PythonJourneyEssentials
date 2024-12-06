import random

# Choose a random element from a sequence
my_list = [1, 2, 3, 4, 5]
random_element = random.choice(my_list)
print("Random element from list:", random_element)

# Generate a random floating-point number between 0.0 and 1.0
random_float = random.random()
print("Random float:", random_float)

# Generate a random integer within a specified range
random_integer = random.randint(1, 10)
print("Random integer:", random_integer)

# Generate a random floating-point number within a specified range
random_uniform = random.uniform(2.5, 5.0)
print("Random uniform:", random_uniform)

# Generate a random integer from a range with a specified step
random_range = random.randrange(2, 10, 2)  # Even numbers between 2 and 10
print("Random range:", random_range)
