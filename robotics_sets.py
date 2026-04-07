# Creating a set of unique sensor IDs

sensor_ids = {101, 102, 103, 104}
print('Unique sensor IDs:', sensor_ids)

# Attempting to add duplicate sensor IDs
sensor_ids.update([102, 103, 105])
print('Updated sensor IDs:', sensor_ids)

# Managing sensor data
sensor_ids.add(106)
print('After adding:', sensor_ids)
 
sensor_ids.discard(101)
print('After discarding:', sensor_ids)

# Set operations with sensor data
another_set = {104, 105, 107}
print('Union:', sensor_ids.union(another_set))
print('Intersection:', sensor_ids.intersection(another_set))

