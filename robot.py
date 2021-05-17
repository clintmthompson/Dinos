
from weapon import Weapon

bot_weapon = Weapon()
bot_weapon.get_weapon('shotgun', 15)


class Robot:

    def __init__(self):
        self.name = "Robot"
        self.power_level = 100
        self.health = 120
        self.weapon = bot_weapon

    def get_robot(self, name):
        self.name = name

    def attack_dino(self, dino):
        dino.health = dino.health - self.weapon.attack_power
