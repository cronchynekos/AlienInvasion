from pygame.sysfont import SysFont
from pygame import display, time, image

class EnemyDisplay:
    def __init__(self, ai_settings, screen, y_start):
        self.settings = ai_settings
        self.aliens = []
        self.screen = screen
        images = [
            image.load('images/alien1.png'),
            image.load('images/alien2.png'),
            image.load('images/alien3.png'),
            image.load('images/alien4.png')
        ]

class Menu:
    def __int__(self, settings, game_stats, screen):
        self.game_stats = game_stats
        self.screen = screen
        self.settings = settings

        self.GameTitle