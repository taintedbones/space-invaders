import sys
import pygame

import game_function as gf
from settings import Settings
from ship import Ship
from pygame.sprite import Group
from game_stats import GameStats
from scoreboard import Scoreboard
from menu_screen import Menu
from highscore_screen import HighScoreScreen


def run_game():
    pygame.init()
    settings = Settings()
    screen = pygame.display.set_mode(settings.dims())
    pygame.display.set_caption('Alien Invasion')
    pygame.mixer.music.load('Sounds/pumpitup.wav')
    pygame.mixer.music.play(-1)

    # Create an instance to store game statistics and create a scoreboard
    stats = GameStats(settings)
    sb = Scoreboard(settings, screen, stats)
    ship = Ship(screen, settings)
    menu = Menu(screen, settings)
    score_screen = HighScoreScreen(screen, settings)

    bullets = Group()
    aliens = Group()
    bunkers = Group()

    gf.create_fleet(settings, screen, ship, aliens)
    gf.create_bunkers(settings, screen, bunkers)

    while True:
        gf.check_events(settings, screen, stats, sb, menu, ship, aliens, bullets, score_screen)

        if stats.game_active:
            ship.update()
            gf.update_bullets(settings, screen, stats, sb, ship, aliens, bullets, bunkers)
            gf.update_aliens(settings, stats, screen, sb, ship, aliens, bullets)

        gf.update_screen(settings, screen, stats, sb, ship, aliens, bullets, menu, score_screen, bunkers)

        if not stats.game_active:
            gf.check_high_score(stats, sb)

        screen.fill(settings.bg_color)
        ship.blitme()

    sys.exit()


run_game()