# Creating a tuple
coordinates = (10, 20, 30)
print('Coordinates:', coordinates)

# Accessing tuple elements
print('X-coordinate:', coordinates[0])
print('Z-coordinate:', coordinates[-1])

# Tuple with mixed data types unpacking
info_tuple = ('Item', 150, 23.99)
name, quantity, price = info_tuple
print('Unpacked:', name, quantity, price)