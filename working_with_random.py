import random

# Generate a random integer between 1 and 10
random_integer = random.randint(1, 10)
print('Random integer between 1 and 10:', random_integer)

# Generate a random float
random_float = random.random()
print('Random float between 0.0 and 1.0:', random_float)

# Generate a random float between 0.0 and 5.0
random_float_in_range = random.random() * 5
print('Random float between 0.0 and 5.0:', random_float_in_range)

# Pick a random element from a list
colors = ['saffron', 'white', 'green']
random_color = random.choice(colors)
print('Random color selected:', random_color)

random.shuffle(colors)
print('Shuffled colors:', colors)