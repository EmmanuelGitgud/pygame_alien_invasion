import imp
from json import load
from turtle import Screen
import pygame
from pygame.sprite import Sprite
class Alien(Sprite):
    def __init__(self, ai_game):
        """start alin in it's starting position"""
        super().__init__()
        self.screen = ai_game.screen

        self.image = pygame.image.load('alien.png')
        self.rect = self.image.get_rect()

        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        self.x = float(self.rect.x)

        
