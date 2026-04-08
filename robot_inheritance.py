class Robot:
    def __init__(self, name):
        self._name = name

    def greet(self):
        print(f'Hello, I am {self._name}.')
    
class CleaningRobot(Robot):
    def clean(self):
        print('Cleaning in progress...')
    
my_robot = CleaningRobot('RobotCleaner')
my_robot.greet()
my_robot.clean()
