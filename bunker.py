import random
import pygame
from PIL import Image
from pygame.sprite import Sprite


class Bunker(Sprite):
    def __init__(self, settings, screen, x, y):
        super().__init__()
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.health = settings.bunker_health
        self.pixels = Image.open('Images/asteroid.png')
        self.width, self.height = self.pixels.size
        self.image = pygame.image.load('Images/asteroid.png')
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.bottom = y

    def damage(self):
        self.health -= 1
        destroyed = self.health < 1

        if destroyed:
            self.kill()
        else:
            for x in range(self.width):
                for y in range(self.height):
                    if random. random() < 0.1:
                        self.pixels.putpixel((x, y), (0, 0, 0, 0))
            self.update()

    def update(self):
        self.image = pygame.transform.scale(pygame.image.fromstring(self.pixels.tobytes(), (self.width, self.height), self.pixels.mode), (self.width, self.height))