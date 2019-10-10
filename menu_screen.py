from button import Button
import pygame
from alien import *


class Menu:
    def __init__(self, screen, settings):
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.settings = settings
        self.bg_color = settings.bg_color

        self.play_button = Button(settings, screen, "PLAY SPACE INVADERS", 48)
        self.high_score_button = Button(settings, screen, "HIGH SCORES", 48)

        self.score_rect = pygame.Rect(0, 0, 500, 500)
        self.border_rect = pygame.Rect(0, 0, self.score_rect.width + 10, self.score_rect.height + 10)

    def draw_alien_score(self):
        alien_spacing = 10
        alien1 = LowerAlien(self.settings, self.screen)
        alien2 = MiddleAlien(self.settings, self.screen)
        alien3 = UpperAlien(self.settings, self.screen)
        alien1_score = Button(self.settings, self.screen, "= " + str(alien1.points()) + " PTS", 48)
        alien2_score = Button(self.settings, self.screen, "= " + str(alien2.points()) + " PTS", 48)
        alien3_score = Button(self.settings, self.screen, "= " + str(alien3.points()) + " PTS", 48)

        alien1.rect.top = self.score_rect.top + 150
        alien1.rect.left = self.score_rect.left + 130
        alien1.draw()

        alien2.rect.top = alien1.rect.bottom + alien_spacing
        alien2.rect.left = alien1.rect.left
        alien2.draw()

        alien3.rect.top = alien2.rect.bottom + alien_spacing
        alien3.rect.left = alien1.rect.left
        alien3.draw()

        alien1_score.rect.left = alien1.rect.right
        alien1_score.rect.bottom = alien1.rect.bottom
        alien1_score.draw_button()

        alien2_score.rect.left = alien2.rect.right
        alien2_score.rect.bottom = alien2.rect.bottom
        alien2_score.draw_button()

        alien3_score.rect.left = alien3.rect.right
        alien3_score.rect.bottom = alien3.rect.bottom
        alien3_score.draw_button()

    def draw_buttons(self):
        self.high_score_button.rect.center = self.score_rect.center
        self.play_button.rect.center = self.score_rect.center
        self.high_score_button.rect.bottom = self.score_rect.bottom - 10
        self.play_button.rect.bottom = self.high_score_button.rect.top - 10

        self.high_score_button.draw_button()
        self.play_button.draw_button()

    def draw_title(self):
        font_size = 90
        title1 = Button(self.settings, self.screen, "SPACE", font_size)
        title2 = Button(self.settings, self.screen, "INVADERS", font_size)
        title1.text_color = (0, 255, 0)
        title2.text_color = (0, 255, 0)

        title1.rect.centery = self.score_rect.centery
        title1.rect.top = self.score_rect.top + 20
        title2.rect.centery = self.score_rect.centery
        title2.rect.top = title1.rect.bottom + 5

        title2.draw_button()
        title1.draw_button()

    def draw(self):
        self.score_rect.center = self.screen_rect.center
        self.border_rect.center = self.screen_rect.center

        self.screen.fill(self.settings.bg_color)
        pygame.draw.rect(self.screen, (255, 255, 255), self.border_rect)
        pygame.draw.rect(self.screen, self.bg_color, self.score_rect)
        self.draw_title()
        self.draw_buttons()
        self.draw_alien_score()