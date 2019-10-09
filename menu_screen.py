from button import Button
import pygame
from alien import *


class Menu:
    def __init__(self, screen, settings):
        self.screen = screen
        self.width = settings.screen_width
        self.height = settings.screen_height
        self.bg_color = settings.bg_color
        self.play_button = Button(settings, screen, "Play Space Invaders")
        self.high_score_button = Button(settings, screen, "High Scores")

        self.title = "SPACE INVADERS"

    def draw_alien_scores(self):
        score_rect = pygame.Rect(0, 0, 100, 100)
        alien1 = LowerAlien()
        alien2 = MiddleAlien()
        alien3 = UpperAlien()