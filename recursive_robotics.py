class Robot:
    def __init__(self, name):
        self.name = name
        self.sub_robots = []
    
    def add_sub_robot(self, sub_robot):
        self.sub_robots.append(sub_robot)

def count_robots(robot):
    """ Return the total count of robots in the hierarchy using recursion """
    if robot is None:
        return 0
    total = 1 # Count the current robot
    # Sum up all sub-robots

    for sub_robot in robot.sub_robots:
        total += count_robots(sub_robot) # Recursive call for each sub-robot
    return total

root_robot = Robot('Root')
child_robot1 = Robot('Child1')
child_robot2 = Robot('Child2')
sub_child_robot1 = Robot('SubChild1')

root_robot.add_sub_robot(child_robot1)
root_robot.add_sub_robot(child_robot2)
child_robot1.add_sub_robot(sub_child_robot1)

print('Total number of robots:', count_robots(root_robot))