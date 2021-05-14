
from robot import Robot

robot_fighter = Robot()
robot_fighter2 = Robot()
robot_fighter3 = Robot()


class Fleet:

    def __init__(self):
        self.fleet_name = 'Kill Fleet'
        self.robots = []

    def create_fleet(self, robot_one, robot_two, robot_three):
        self.robots = [robot_one, robot_two, robot_three]


robot_fleet = Fleet()

robot_fleet.create_fleet(robot_fighter, robot_fighter2, robot_fighter3)
