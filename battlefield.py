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


def dino_turn():
    i = 0
    while i < 3:
        if robot_fleet.robots[0].health > 0 and dino_squad.dinosaurs[i].health > 0:
            dino_squad.dinosaurs[i].attack_robots(robot_fleet.robots[0])
            i += 1
        elif robot_fleet.robots[0].health < 1 and robot_fleet.robots[1].health > 0 and dino_squad.dinosaurs[i].health > 0:
            dino_squad.dinosaurs[i].attack_robots(robot_fleet.robots[1])
            i += 1
        elif robot_fleet.robots[0].health < 1 and robot_fleet.robots[1].health < 1 and dino_squad.dinosaurs[i].health > 0:
            dino_squad.dinosaurs[i].attack_robots(robot_fleet.robots[2])
            i += 1
        else:
            i += 1
            pass
    print('The Dinos have attacked!!')
    print(f'Robot 1 Health ={robot_fleet.robots[0].health}')
    print(f'Robot 2 Health ={robot_fleet.robots[1].health}')
    print(f'Robot 3 Health ={robot_fleet.robots[2].health}')
    print('')


def robot_turn():
    i = 0
    while i < 3:
        if dino_squad.dinosaurs[0].health > 0 and robot_fleet.robots[i].health > 0:
            robot_fleet.robots[i].attack_dino(dino_squad.dinosaurs[0])
            i += 1
        elif dino_squad.dinosaurs[0].health < 1 and dino_squad.dinosaurs[1].health > 0 and robot_fleet.robots[i].health > 0:
            robot_fleet.robots[i].attack_dino(dino_squad.dinosaurs[1])
            i += 1
        elif dino_squad.dinosaurs[0].health < 1 and dino_squad.dinosaurs[1].health < 1 and robot_fleet.robots[i].health > 0:
            robot_fleet.robots[i].attack_dino(dino_squad.dinosaurs[2])
            i += 1
        else:
            i += 1
            pass

    print('The robots have attacked!!')
    print(f'Dino 1 Health ={dino_squad.dinosaurs[0].health}')
    print(f'Dino 2 Health ={dino_squad.dinosaurs[1].health}')
    print(f'Dino 3 Health ={dino_squad.dinosaurs[2].health}')
    print('')

def to_battle():
    while robot_fleet.robots[2].health > 0 and dino_squad.dinosaurs[2].health > 0:
        dino_turn()
        time.sleep(3)
        robot_turn()
        time.sleep(3)
        if robot_fleet.robots[2].health <= 0:
            print("The dinosaurs deliver a killing blow to the final robot! Dinos Win!!")
        elif dino_squad.dinosaurs[2].health <= 0:
            print("The robots deliver a killing blow to the final dino! Robots Win!!")