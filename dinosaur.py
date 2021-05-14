

class Dinosaur:

    def __init__(self):
        self.type = 'Raptor'
        self.energy = 80
        self.attack_power = 15
        self.health = 100

    def attack_robots(self, robot):
        robot.health = robot.health - self.attack_power
