import sys
import pygame

import game_function as gf
from settings import Settings
from ship import Ship
from alien import Alien
from pygame.sprite import Group
from game_stats import GameStats
from button import Button
from scoreboard import Scoreboard

# PYTHON CRASH COURSE - Ch 12 has references for ship img, shooting bullets,


def run_game():
    pygame.init()
    settings = Settings()
    screen = pygame.display.set_mode(settings.dims())
    pygame.display.set_caption('Alien Invasion')

    play_button = Button(settings, screen, "Play")

    # Create an instance to store game statistics and create a scoreboard
    stats = GameStats(settings)
    sb = Scoreboard(settings, screen, stats)
    ship = Ship(screen, settings)

    bullets = Group()
    aliens = Group()

    gf.create_fleet(settings, screen, ship, aliens)

    while True:
        gf.check_events(settings, screen, stats, sb, play_button, ship, aliens, bullets)

        if stats.game_active:
            ship.update()
            gf.update_bullets(settings, screen, stats, sb, ship, aliens, bullets)
            gf.update_aliens(settings, stats, screen, sb, ship, aliens, bullets)

        gf.update_screen(settings, screen, stats, sb, ship, aliens, bullets, play_button)

        screen.fill(settings.bg_color)
        ship.blitme()

    sys.exit()


run_game()
