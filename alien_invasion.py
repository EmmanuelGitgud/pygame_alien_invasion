import sys
import pygame

class AlienInvasion:
    """game assets and behavior"""
    def __init__(self):
        pygame.init()

        self.screen = pygame.display.set_mode((1200,800))
        pygame.display.set_caption("Alien Invasion")

    def run_game(self):
        """main loop of the game"""
        while True:
            #mouse and keyboard event listener
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            #display latest frame
            pygame.display.flip()

if __name__ == '__main__':
    #run the game instance
    ai = AlienInvasion()
    ai.run_game()
