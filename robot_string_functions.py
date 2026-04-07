message = 'Hello, RamanaaVijayakumar!'
print(len(message))
print(message.upper())
print(message.lower())

command_str = 'MOVE:FORWARD'
command, parameter = command_str.split(':')
print('Command:', command)
print('Parameter:', parameter)

distance_str = '12.6 m'
distance_str = distance_str.strip('m')
distance = float(distance_str)
print('Distance:', distance)

status_message = 'Error: Sensor disconnected'
status_message = status_message.replace('Error', 'Warning')
print(status_message)
