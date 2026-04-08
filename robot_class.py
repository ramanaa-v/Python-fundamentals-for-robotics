class Robot:
    def __init__(self, name, color):
        self.name = name
        self.color = color

    def introduce_self(self):
        print(f'Hello, my name is {self.name} and my color is {self.color}.')

r1 = Robot('RamanaaVijayakumar', 'Blue')
r1.introduce_self()