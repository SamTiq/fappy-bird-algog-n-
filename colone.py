from random import randint
import pygame

class Colone:
    def __init__(self):
        self.x = 10
        self.vitesse = 3
        self.trou = randint(1,399)
        self.taille_trou = 100
        self.rectUp = pygame.Rect((round(500*(self.x/10)), 0), (50, self.trou))
        self.rectDown = pygame.Rect((round(500*(self.x/10)), self.trou+self.taille_trou), (50, 500-self.trou-self.taille_trou))
        