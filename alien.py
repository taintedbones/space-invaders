import pygame
from pygame.sprite import Sprite
from timer import Timer


class Alien(Sprite):
    def __init__(self, settings, screen):
        super(Alien, self).__init__()
        self.screen = screen
        self.settings = settings

        self.move_frames = []
        self.hit_frames = ['Images/Explosion-1.png', 'Images/Explosion-2.png',
                           'Images/Explosion-3.png', 'Images/Explosion-4.png']
        self.image = pygame.image.load('Images/Lower-Alien-1.png')
        self.rect = self.image.get_rect()

        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        self.x = float(self.rect.x)

    def blitme(self):
        self.screen.blit(self.image, self.rect)

    def check_edges(self):
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True

    def update(self):
        self.x += (self.settings.alien_speed_factor * self.settings.fleet_direction)
        self.rect.x = self.x

        if self.x % 4 == 0:
            self.image = pygame.image.load('Images/' + self.move_frames[1])
        else:
            self.image = pygame.image.load('Images/' + self.move_frames[0])


    def explode(self):
        timer = Timer(self.hit_frames)
        self.image = pygame.image.load(timer.frame_index())


    def points(self):
        raise NotImplementedError


class LowerAlien(Alien):
    def __init__(self, settings, screen):
        super(LowerAlien, self).__init__(settings, screen)
        self.move_frames = ['Lower-Alien-1.png', 'Lower-Alien-2.png']
        self.image = pygame.image.load('Images/' + self.move_frames[0])

    def points(self):
        return 10


class MiddleAlien(Alien):
    def __init__(self, settings, screen):
        super(MiddleAlien, self).__init__(settings, screen)
        self.move_frames = ['Middle-Alien-1.png', 'Middle-Alien-2.png']
        self.image = pygame.image.load('Images/' + self.move_frames[0])

    def points(self):
        return 20


class UpperAlien(Alien):
    def __init__(self, settings, screen):
        super(UpperAlien, self).__init__(settings, screen)
        self.move_frames = ['Upper-Alien-1.png', 'Upper-Alien-2.png']
        self.image = pygame.image.load('Images/' +  self.move_frames[0])

    def points(self):
        return 30
