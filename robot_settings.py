class Robot:
    def __init__(self, speed=0, battery=100):
        self._speed = speed
        self._battery = battery
    
    def get_speed(self):
        return self._speed
    
    def set_speed(self, value):
        if value < 0:
            raise ValueError('Speed cannot be negative')
        self._speed = value

    def get_battery(self):
        return self._battery
    
    def set_battery(self, value):
        if not (0 <= value <= 100):
            raise ValueError('Battery level must be between 0 and 100')
        self._battery = value


robot = Robot()
print('Initial speed:', robot.get_speed())

robot.set_speed(5)
print('Updated Speed:', robot.get_speed())

try:
    robot.set_battery(150)
except ValueError as e:
    print(e)