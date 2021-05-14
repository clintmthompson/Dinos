import dinosaur
from dinosaur import Dinosaur

dino = Dinosaur()
dino2 = Dinosaur()
dino3 = Dinosaur()


class Herd:

    def __init__(self):
        self.dinosaurs = []

    def create_herd(self, dino_one, dino_two, dino_three):
        self.dinosaurs = [dino_one, dino_two, dino_three]


dino_squad = Herd()

dino_squad.create_herd(dino, dino2, dino3)


