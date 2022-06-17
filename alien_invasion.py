import sys
import pygame
from settings import Settings

class AlienInvasion:
    """game assets and behavior"""
    def __init__(self):
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")

        # set bg color
        self.bg_color = (230,230,230)

    def run_game(self):
        """main loop of the game"""
        while True:
            #mouse and keyboard event listener
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            #redraw screen each pass
            self.screen.fill(self.settings.bg_color)

            #display latest frame
            pygame.display.flip()

if __name__ == '__main__':
    #run the game instance
    ai = AlienInvasion()
    ai.run_game()


