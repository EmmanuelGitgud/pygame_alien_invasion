import pygame

class Ship:
    """a class to manage the ship"""

    def __init__(self, ai_game):
        """initialize ship in its starting position"""
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        self.settings = ai_game.settings

        # Load ship image and get rect
        self.image = pygame.image.load('ship.png')
        self.rect = self.image.get_rect()

        # Start ship at the bottom of the screen
        self.rect.midbottom = self.screen_rect.midbottom

        self.x = float(self.rect.x)

        self.moving_right = False
        self.moving_left = False

    def update(self):
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed
        self.rect.x = self.x

    def blitme(self):
        """draw the ship at location"""
        self.screen.blit(self.image, self.rect)
    
