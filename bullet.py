import pygame
from settings import Settings
from pygame.sprite import Sprite 

class Bullet(Sprite):
    """class to manage bullets"""

    def __init_subclass__(self, ai_game):
        """create bullet fired from the ship"""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.bullet_color

        self.rect = pygame.Rect(0, 0, self.settings.bullet_width, self.bullet_height)
        self.rect.midtop = ai_game.ship.rect.midtop

        self.y = float(self.rect.y)

    def update(self):
        """move bullet up screen"""
        #update decimal position of the bullet
        self.y -= self.settings.bullet_speed
        #update the rect position
        self.rect.y = self.y

    def draw_bullet(self):
        """draw bullet on the screen"""
        pygame.draw.rect(self.screen, self.color, self.rect)   