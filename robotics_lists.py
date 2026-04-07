# Sensor data list
sensor_readings = [20, 55, 75, 10]
print('Initial sensor readings:', sensor_readings)

# Accessing elements
print('First readings:', sensor_readings[0]) # 20
print('Most recent readings:', sensor_readings[-1]) # 10

# Updating a sensor reading
sensor_readings[2] = 80
print('Updated Readings:', sensor_readings)

# Adding a new sensor reading
sensor_readings.append(65)
print('Readings after append:', sensor_readings)


# Remove a sensor reading
del sensor_readings[0] # Removing the first sensor reading
print('Readings after deletion:', sensor_readings)

# Iterating through sensor readings
for reading in sensor_readings:
    print('Processing reading:', reading)