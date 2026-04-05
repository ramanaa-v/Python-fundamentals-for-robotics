"""This module defines a simple Robot class for demonstration purposes"""


class Robot:
    """Simple robot class that can greet.
    """

    def __init__(self, name):
        self.name = name

    def greet(self):
        """Print a greeting from the robot.
        """
        print("Hello, my name is " + self.name)


myRobot = Robot("R2D2")
myRobot.greet()
