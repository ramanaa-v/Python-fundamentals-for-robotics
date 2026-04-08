class Robot:
    def __init__(self, name):
        self._name = name
        
    def perform_task(self):
        print(f'{self.name} performs a generic task')


class CleaningRobot(Robot):
    def perform_task(self):
        print(f'{self._name} is cleaning the area.')


class PaintingRobot(Robot):
    def perform_task(self):
        print(f'{self._name} is painting the wall.')


robots = [CleaningRobot("Cleany"), PaintingRobot("Painty")]
for robot in robots:
    robot.perform_task()