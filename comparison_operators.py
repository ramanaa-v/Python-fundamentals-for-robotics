# Equal to
print('10 == 10:', 10 == 10) # Outputs True

print('10 == 5:', 10 == 5) # Outputs False

# Not equal to
print('10 != 5:', 10 != 5) # Outputs True

# Less than
print('5 < 10:', 5 < 10) # Outputs True

# Greater than
print('5 > 10:', 5 > 10) # Outputs False

# Less than or equal to
print('5 <= 5:', 5 <= 5) # Outputs True

# Greater than or equal to
print('10 >= 5', 10 <= 5) # Outputs False


# Robot sensor threshold check
sensor_threshold = 10
sensor_reading = 12

if sensor_reading >= sensor_threshold:
    print('Sensor threshold exceeded, take action.')
else:
    print('Sensor levels normal, no action required.')


# Strin comparison
print("'abc' < 'def':", 'abc' < 'def') # Outputs True
