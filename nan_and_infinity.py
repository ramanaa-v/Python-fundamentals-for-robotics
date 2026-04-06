# Positive infinity
positive_infinity = float('inf')
print('Positive Infinity:', positive_infinity)

# Negative infinity
negative_infinity = float('-inf')
print('Negative Infinity:', negative_infinity)

# NaN example
not_a_number = float('nan')
print('Example of NaN:', not_a_number)

# Operations with NaN
print('NaN added to a number:', not_a_number + 5)
print('NaN multiplied by a number:', not_a_number * 2)

# Checking if a value is NaN
print('Is NaN equal to NaN?:', not_a_number == not_a_number)

import math
print('Using math.isnan() to check NaN:', math.isnan(not_a_number))