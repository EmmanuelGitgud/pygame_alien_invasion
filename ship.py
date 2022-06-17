import pygame

class Ship:
    """a class to manage the ship"""

    def __init__(self, ai_game):
        """initialize ship in its starting position"""
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        # Load ship image and get rect
        self.image = pygame.image.load('ship.png')
        self.rect = self.image.get_rect()

        # Start ship at the bottom of the screen
        self.rect.midbottom = self.screen_rect.midbottom

    def blitme(self):
        """draw the ship at location"""
        self.screen.blit(self.image, self.rect)
    
