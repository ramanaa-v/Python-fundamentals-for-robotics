class Robot:
    def action(self):
        print('Performing a generic action')

class FlyingRobot(Robot):
    def action(self):
        print('Flying')
    
generic_robot = Robot()
generic_robot.action() # This calls the base (parent) class method

flying_robot = FlyingRobot()
flying_robot.action() # This calls the overriden method in the subclass
