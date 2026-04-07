# Simple for loop with a list
colors = ['red', 'green', 'blue', 'yellow']
for color in colors:
    print('Color:', color)

# For loop with range
for i in range(4): # Generates numbers from 0 to 3
    print('Number:', i)

# Iterating over a sting
for char in 'robotics':
    print('Character:', char)

# Looping through a dictionary
robot_parts = {'wheels': 4, 'motors': 2, 'sensors': 5}
for part, quantity in robot_parts.items():
    print('Part:', part, 'Quantity:', quantity)

# Nested for loops
for outer in range(3):
    for inner in range(3):
        print('Position:', outer, inner)

