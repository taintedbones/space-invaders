import pygame


class Settings:
    def __init__(self):
        self.screen_width = 1200
        self.screen_height = 700
        self.dimensions = 1200, 700
        self.bg_color = pygame.Color('#404040')
        self.default_font = 'Fonts/8-Bit Madness.ttf'

        # Ship settings
        self.ship_speed_factor = 1.5
        self.ship_limit = 3

        # Bullet settings
        self.bullet_speed_factor = 3
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 255, 255, 255
        self.bullets_allowed = 15

        # Alien settings
        self.alien_speed_factor = 1
        self.fleet_drop_speed = 10

        # How quickly game speeds up
        self.speedup_scale = 1.1
        # How quickly alien point values increase
        self.score_scale = 1.5

        self.initialize_scale = 1.1
        self.initialize_dynamic_settings()

        # fleet_direction of 1 represents right; -1 represents left
        self.fleet_direction = 1

    def dims(self):
        return self.dimensions

    def initialize_dynamic_settings(self):
        self.ship_speed_factor = 1.5
        self.bullet_speed_factor = 3
        self.alien_speed_factor = 1

        self.fleet_direction = 1

        # Scoring
        self.alien_points = 50

    def increase_speed(self):
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale

        self.alien_points = int(self.alien_points * self.score_scale)
        print(self.alien_points)