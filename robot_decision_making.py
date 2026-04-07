# if-else statement for robot movement
obstacle_detected = True

if obstacle_detected:
    print('Stop or change direction.')
else:
    print('Continue moving forward.')

# Using elif for sensor-based conditions
sensor_reading = 'low_battery'

if sensor_reading == 'obstacle':
    print('Avoid obstacle.')
elif sensor_reading == 'low_battery':
    print('Return to charging station.')
else:  
    print('Normal operation.')


# Nested if-else for more detailed decision-making
if sensor_reading == 'obstacle':
    distance = 5 # distance to obstacle in meters
    if distance < 1:
        print('Immediate stop.')
    else:
        print('Prepare to change direction.')
else:
    print('Continue exploration')

# Logical operators for complex conditions
battery_level = 20 # percentage
if sensor_reading == 'obstacle' and battery_level > 50:
    print('Navigate around obstacle.')
elif sensor_reading == 'obstacle' and battery_level <= 50:
    print('Return to base for recharge.')
else:
    print('Continue on current path.')