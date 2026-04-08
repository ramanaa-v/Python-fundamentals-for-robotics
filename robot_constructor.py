class Robot:
    def __init__(self, name, type, sensor_count):
        self.name = name
        self.type = type
        self.sensor_count = sensor_count
        print(f'Robot created: {self.name}, a {self.type} robot with {self.sensor_count} sensors')

r1 = Robot('Atlas', 'Humanoid', 5)
r2 = Robot('Spot', 'Quadruped', 4)
