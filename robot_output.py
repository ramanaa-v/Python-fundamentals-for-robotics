print("Hello, robot world!")

robot_name = 'ramanaavijayakumar'
task_status = 'active'

print('Robot Name:', robot_name,'- Status:', task_status)

battery_level = 85
print(f'Battery Level: {battery_level}%')

with open('log.txt', 'a') as file:
    print('An error occured', file=file)