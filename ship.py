import pygame
from timer import Timer
from pygame.sprite import Sprite
from pygame import time


class Ship(Sprite):
    def __init__(self, screen, settings):
        super(Ship, self).__init__()
        self.screen = screen

        self.move_frames = []
        self.move_frames.append('Images/Ship-1.png')
        self.move_frames.append('Images/Ship-2.png')
        self.explode_frames = []
        for frame in ['Images/Explosion-1.png', 'Images/Explosion-2.png',
            'Images/Explosion-3.png', 'Images/Explosion-4.png']:
            self.explode_frames.append(frame)
        self.image = pygame.image.load('Images/Ship-1.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        r, sr = self.rect, self.screen_rect
        r.centerx = sr.centerx
        r.bottom = sr.bottom

        self.death_time = None
        self.dead = False
        self.explosion = Timer(self.explode_frames, 250 / 4, loop_once=True)
        self.movement = Timer(self.move_frames, 250 / 2)
        self.moving_right = False
        self.moving_left = False
        self.settings = settings
        self.center = float(r.centerx)

    def update(self):
        if self.dead:
            self.image = pygame.image.load(self.explosion.image_rect())
            if self.explosion_finished():
                self.kill()
        else:
            self.image = pygame.image.load(self.movement.image_rect())
            if self.moving_right and self.rect.right < self.screen_rect.width:
                self.center += self.settings.ship_speed_factor
            if self.moving_left and self.rect.left > 0:
                self.center -= self.settings.ship_speed_factor

        self.rect.centerx = self.center

    def blitme(self):
        self.screen.blit(self.image, self.rect)

    def center_ship(self):
        self.center = self.screen_rect.centerx

    def explode(self):
        self.dead = True
        self.death_time = time.get_ticks()

    def explosion_finished(self):
        return time.get_ticks() - self.death_time > 200