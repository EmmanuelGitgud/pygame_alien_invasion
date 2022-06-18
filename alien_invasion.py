import sys
import pygame
from settings import Settings
from ship import Ship

class AlienInvasion:
    """game assets and behavior"""
    def __init__(self):
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))

        pygame.display.set_caption("Alien Invasion")

        self.ship = Ship(self)

        # set bg color
        self.bg_color = self.settings.bg_color

    def run_game(self):
        """main loop of the game"""
        while True:
            self._check_events()
            self._update_screen()
            self.ship.update()

    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_keydown_events(self, event):
        """keypreses"""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True

    def _check_keyup_events(self, event):
        """keyup"""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False
           
    #           


    def _update_screen(self):
        """updates screen"""
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()

        #display latest frame
        pygame.display.flip()

if __name__ == '__main__':
    #run the game instance
    ai = AlienInvasion()
    ai.run_game()


