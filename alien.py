import pygame
from pygame.sprite import Sprite
from timer import Timer
from pygame import time


class Alien(Sprite):
    def __init__(self, settings, screen):
        super(Alien, self).__init__()
        self.screen = screen
        self.settings = settings

        self.death_time = None
        self.move_frames = []
        explode_frames = []
        for frame in ['Images/Explosion-1.png', 'Images/Explosion-2.png',
            'Images/Explosion-3.png', 'Images/Explosion-4.png']:
            explode_frames.append(frame)

        self.image = pygame.image.load('Images/Lower-Alien-1.png')
        self.rect = self.image.get_rect()
        self.dead = False
        self.explosion = Timer(explode_frames, 250 / 4, loop_once=True)
        self.movement = Timer(self.move_frames, 250 / 2)

        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        self.x = float(self.rect.x)

    def blitme(self):
        if self.dead:
            self.screen.blit(self.explosion.image_rect(), self.rect)
        else:
            self.screen.blit(self.image, self.rect)

    def check_edges(self):
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True

    def update(self):
        if self.dead:
            self.image = pygame.image.load(self.explosion.image_rect())
            if self.explosion_finished():
                self.kill()
        else:
            self.image = pygame.image.load(self.movement.image_rect())
            self.x += (self.settings.alien_speed_factor * self.settings.fleet_direction)
            self.rect.x = self.x

    def draw(self):
        pygame.draw.rect(self.screen, self.settings.bg_color, self.rect)
        self.blitme()

    def explode(self):
        self.dead = True
        self.death_time = time.get_ticks()
        # play das sound

    def explosion_finished(self):
        return time.get_ticks() - self.death_time > 200

    def points(self):
        raise NotImplementedError


class LowerAlien(Alien):
    def __init__(self, settings, screen):
        super().__init__(settings, screen)
        self.move_frames.append('Images/Lower-Alien-1.png')
        self.move_frames.append('Images/Lower-Alien-2.png')
        self.image = pygame.image.load(self.move_frames[0])

    def points(self):
        return 10


class MiddleAlien(Alien):
    def __init__(self, settings, screen):
        super().__init__(settings, screen)
        self.move_frames.append('Images/Middle-Alien-1.png')
        self.move_frames.append('Images/Middle-Alien-2.png')
        self.image = pygame.image.load(self.move_frames[0])

    def points(self):
        return 20


class UpperAlien(Alien):
    def __init__(self, settings, screen):
        super().__init__(settings, screen)
        self.move_frames.append('Images/Upper-Alien-1.png')
        self.move_frames.append('Images/Upper-Alien-2.png')
        self.image = pygame.image.load(self.move_frames[0])

    def points(self):
        return 30
