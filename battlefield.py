from tkinter import *
from fleet import robot_fleet
from herd import dino_squad
import time
import fleet
import herd

root = Tk()
root.title('Dinos VS Robots')
root.config(bg='tan')


class Battlefield:

    def __init__(self):

        self.fleet = []
        self.herd = []

    def compile_teams(self, team_robot, team_dino):
        self.fleet = team_robot
        self.herd = team_dino


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


intro = Label(root, text="Dinosaur VS Robot Battle Simulator\n\nThis will simulate a turn based battle between 3 dinosaurs and 3 robots")
dino_victory_message = Label(root, text="The dinosaurs deliver a killing blow to the final robot! Dinos Win!!")
robot_victory_message = Label(root, text="The robots deliver a killing blow to the final dino! Robots Win!!")


def attack_with_dino():
    dino_turn()
    robot_health.config(text=f'Robot 1 Health: {robot_fleet.robots[0].health}\nRobot 2 Health: {robot_fleet.robots[1].health}\nRobot 3 Health: {robot_fleet.robots[2].health}')
    if robot_fleet.robots[2].health <= 0:
        dino_victory_message.grid(row=4, column=1, padx=40, pady=40)
    elif dino_squad.dinosaurs[2].health <= 0:
        robot_victory_message.grid(row=4, column=1, padx=40, pady=40)


def attack_with_robot():
    robot_turn()
    dino_health.config(text=f'Dino 1 Health: {dino_squad.dinosaurs[0].health}\nDino 2 Health: {dino_squad.dinosaurs[1].health}\nDino 3 Health: {dino_squad.dinosaurs[2].health}')
    if robot_fleet.robots[2].health <= 0:
        dino_victory_message.grid(row=4, column=1, padx=40, pady=40)
    elif dino_squad.dinosaurs[2].health <= 0:
        robot_victory_message.grid(row=4, column=1, padx=40, pady=40)


dino_button = Button(root, text="Attack with Dino", command=attack_with_dino)
robot_button = Button(root, text="Attack with Robots", command=attack_with_robot)

intro.grid(row=0, column=1, padx=0, pady=0)
dino_button.grid(row=3, column=2, padx=40, pady=40)
robot_button.grid(row=3, column=0, padx=40, pady=40)

robot_health = Label(root, text=f'Robot 1 Health: {robot_fleet.robots[0].health}\nRobot 2 Health: {robot_fleet.robots[1].health}\nRobot 3 Health: {robot_fleet.robots[2].health}')
dino_health = Label(root, text=f'Dino 1 Health: {dino_squad.dinosaurs[0].health}\nDino 2 Health: {dino_squad.dinosaurs[1].health}\nDino 3 Health: {dino_squad.dinosaurs[2].health}')

robot_health.grid(row=2, column=0, padx=40, pady=40)
dino_health.grid(row=2, column=2, padx=40, pady=40)

root.mainloop()
