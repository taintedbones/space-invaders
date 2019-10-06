import pygame
from pygame.sprite import Sprite


class Ship(Sprite):
    def __init__(self, screen, settings):
        super(Ship, self).__init__()
        self.screen = screen

        self.image = pygame.image.load('Images/ship.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        r, sr = self.rect, self.screen_rect
        r.centerx = sr.centerx
        r.bottom = sr.bottom

        self.moving_right = False
        self.moving_left = False
        self.settings = settings
        self.center = float(r.centerx)

    def update(self):
        if self.moving_right:
            self.center += self.settings.ship_speed_factor
        if self.moving_left:
            self.center -= self.settings.ship_speed_factor

        self.rect.centerx = self.center

    def blitme(self):
        self.screen.blit(self.image, self.rect)

    def center_ship(self):
        self.center = self.screen_rect.centerx
