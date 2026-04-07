# Creating a dictionary
robot_parts = {'wheels': 4, 'motors': 2, 'sensors': 5}
print('Robot Parts Dictionary:', robot_parts)
print('')

# Dictionary with various data types
robot_specs = {
    'name': 'RamanaaVijayakumar',
    'parts': robot_parts,
    'features': ['autonomous', 'solar_powered', 'waterproof'],
    'dimensions': {'height': 120, 'width': 75, 'weight': 150}
}

print('Robot specifications dictionary:', robot_specs)
print('')

# Accessing and modifying dictionary values
print('Robot Height:', robot_specs['dimensions']['height'])
print('')
robot_specs['speed'] = '25 km/h'
print('')
print('Updated Robot Specifications:', robot_specs)
print('')

# Removing an item
del robot_specs['speed']
print('After deletion:', robot_specs)
print('')

# Looping through a dictionary
for key, value in robot_parts.items():
    print(key, ':', value)