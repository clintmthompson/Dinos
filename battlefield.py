from fleet import robot_fleet
from herd import dino_squad
import time
import fleet
import herd


class Battlefield:

    def __init__(self):

        self.fleet = []
        self.herd = []

    def compile_teams(self, team_robot, team_dino):
        self.fleet = team_robot
        self.herd = team_dino


battlefield = Battlefield()
battlefield.compile_teams(robot_fleet, dino_squad)


print(dino_squad.dinosaurs[0].health)
robot_fleet.robots[0].attack_dino(dino_squad.dinosaurs[0])
print(dino_squad.dinosaurs[0].health)

print(robot_fleet.robots[0].health)
dino_squad.dinosaurs[0].attack_robots(robot_fleet.robots[0])
print(robot_fleet.robots[0].health)


def dino_turn():
    i = 0
    while i < 3:
        if robot_fleet.robots[0].health > 0 and dino_squad.dinosaurs[0].health > 0:
            dino_squad.dinosaurs[i].attack_robots(robot_fleet.robots[0])
            i += 1
        elif robot_fleet.robots[0].health < 1 and robot_fleet.robots[1].health > 0 and dino_squad.dinosaurs[0].health > 0:
            dino_squad.dinosaurs[i].attack_robots(robot_fleet.robots[1])
            i += 1
        elif robot_fleet.robots[0].health < 1 and robot_fleet.robots[1].health < 1 and dino_squad.dinosaurs[0].health > 0:
            dino_squad.dinosaurs[i].attack_robots(robot_fleet.robots[2])
            i += 1
        else:
            pass
    print('The dinosaurs have attacked!!')
    print(f'Robot 1 Health ={robot_fleet.robots[0].health}')
    print(f'Robot 2 Health ={robot_fleet.robots[1].health}')
    print(f'Robot 3 Health ={robot_fleet.robots[2].health}')
    print('')


while robot_fleet.robots[2].health > 0:
    dino_turn()
    time.sleep(3)
