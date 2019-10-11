import sys
from bullet import Bullet
from alien import *
from bunker import Bunker
from time import sleep


def change_fleet_direction(settings, aliens):
    for alien in aliens.sprites():
        alien.rect.y += settings.fleet_drop_speed
    settings.fleet_direction *= -1


def check_aliens_bottom(settings, stats, screen, sb, ship, aliens, bullets):
    screen_rect = screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
            ship_hit(settings, stats, screen, sb, ship, aliens, bullets)
            break


def check_bullet_alien_collisions(settings, screen, stats, sb, ship, aliens, bullets):
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, False)

    if collisions:
        for aliens in collisions.values():
            # stats.score += settings.alien_points * len(aliens)
            # sb.prep_score()
            for alien in aliens:
                alien.explode()
                stats.score += settings.alien_points * len(aliens)
                sb.prep_score()
        # check_high_score(stats, sb)

    if len(aliens) == 0:
        # If entire fleet destroyed, start new level
        bullets.empty()
        settings.increase_speed()

        # Increase level
        stats.level += 1
        sb.prep_level()

        create_fleet(settings, screen, ship, aliens)


def check_bullet_bunker_collision(bunkers, bullets):
    collisions = pygame.sprite.groupcollide(bullets, bunkers, True, False)
    if collisions:
        for bunkers_hit in collisions.values():
            for bunker in bunkers_hit:
                bunker.damage()


def check_buttons(settings, screen, stats, sb, menu, score_screen, ship, aliens, bullets, mouse_x, mouse_y):
    check_play_button(settings, screen, stats, sb, menu, ship, aliens, bullets, mouse_x, mouse_y)
    check_high_score_button(stats, menu, mouse_x, mouse_y)
    check_return_button(stats, menu, score_screen, mouse_x, mouse_y)


def check_events(settings, screen, stats, sb, menu, ship, aliens, bullets, score_screen):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_buttons(settings, screen, stats, sb, menu, score_screen, ship, aliens, bullets, mouse_x,
                          mouse_y)
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, settings, screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                ship.moving_right = False
            elif event.key == pygame.K_LEFT:
                ship.moving_left = False


def check_keydown_events(event, settings, screen, ship, bullets):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    if event.key == pygame.K_SPACE:
        fire_bullet(settings, screen, ship, bullets)


def check_fleet_edges(settings, aliens):
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(settings, aliens)
            break


def check_high_score(stats, sb):
    if stats.score > stats.high_score:
        stats.high_score = stats.score
        sb.prep_high_score()

    sb.check_high_score()


def check_play_button(settings, screen, stats, sb, menu, ship, aliens, bullets, mouse_x, mouse_y):
    # Start new game when player clicks play
    button_clicked = menu.play_button.rect.collidepoint(mouse_x, mouse_y)
    if button_clicked and not stats.game_active:
        # Reset game settings
        settings.initialize_dynamic_settings()

        # Hide the mouse cursor
        pygame.mouse.set_visible(False)
        stats.reset_stats()
        stats.game_active = True

        # Reset scoreboard images
        sb.prep_score()
        sb.prep_high_score()
        sb.prep_level()
        sb.prep_ships()

        # Empty the list of aliens and bullets
        aliens.empty()
        bullets.empty()

        create_fleet(settings, screen, ship, aliens)
        ship.center_ship()


def check_high_score_button(stats, menu, mouse_x, mouse_y):
    hs_button_clicked = menu.high_score_button.rect.collidepoint(mouse_x, mouse_y)
    if hs_button_clicked and not stats.game_active:
        menu.high_score_button.clicked = True


def check_return_button(stats, menu, score_screen, mouse_x, mouse_y):
    return_button_clicked = score_screen.return_button.rect.collidepoint(mouse_x, mouse_y)
    if return_button_clicked and not stats.game_active:
        menu.high_score_button.clicked = False


def create_alien(settings, screen, aliens, alien_type, alien_number, row_number):
    if alien_type == 0:
        alien = UpperAlien(settings, screen)
    elif alien_type == 1:
        alien = MiddleAlien(settings, screen)
    else:
        alien = LowerAlien(settings, screen)

    alien_width = alien.rect.width
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
    aliens.add(alien)


def create_bunkers(settings, screen, bunkers):
    screen_rect = screen.get_rect()
    x, y = 150, screen_rect.height - 100

    for bunker_num in range(4):
        bunker = Bunker(settings, screen, x, y)
        bunkers.add(bunker)
        x += 300


def create_fleet(settings, screen, ship, aliens):
    alien = Alien(settings, screen)
    alien_width = alien.rect.width
    number_aliens_x = get_number_aliens_x(settings, alien_width)
    number_rows = get_number_rows(settings, ship.rect.height, alien.rect.height)

    for row_number in range(number_rows):
        for alien_number in range(number_aliens_x):
            create_alien(settings, screen, aliens, row_number, alien_number, row_number)


def fire_bullet(settings, screen, ship, bullets):
    if len(bullets) < settings.bullets_allowed:
        new_bullet = Bullet(settings, screen, ship)
        bullets.add(new_bullet)


def get_number_aliens_x(settings, alien_width):
    available_space_x = settings.screen_width - 2 * alien_width
    number_aliens_x = int(available_space_x / (2 * alien_width))
    return number_aliens_x


def get_number_rows(settings, ship_height, alien_height):
    available_space_y = (settings.screen_height - (3 * alien_height) - ship_height)
    number_rows = int(available_space_y / (2 * alien_height))
    return number_rows


def ship_hit(settings, stats, screen, sb, ship, aliens, bullets):
    if stats.ships_left > 0:
        stats.ships_left -= 1

        ship.explode()
        sb.prep_ships()

        aliens.empty()
        bullets.empty()

        create_fleet(settings, screen, ship, aliens)
        ship.center_ship()

        sleep(0.5)
    else:
        stats.game_active = False
        pygame.mouse.set_visible(True)


def update_aliens(settings, stats, screen, sb, ship, aliens, bullets):
    check_fleet_edges(settings, aliens)
    aliens.update()

    if pygame.sprite.spritecollideany(ship, aliens):
        ship_hit(settings, stats, screen, sb, ship, aliens, bullets)

    check_aliens_bottom(settings, stats, screen, sb, ship, aliens, bullets)


def update_bullets(settings, screen, stats, sb, ship, aliens, bullets, bunkers):
    bullets.update()

    # Deletes bullets that have disappeared
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)

    check_bullet_alien_collisions(settings, screen, stats, sb, ship, aliens, bullets)
    check_bullet_bunker_collision(bunkers, bullets)


def update_screen(settings, screen, stats, sb, ship, aliens, bullets, menu, score_screen, bunkers):
    if not stats.game_active:
        if not menu.high_score_button.clicked or score_screen.return_button.clicked:
            menu.draw()
        elif not score_screen.return_button.clicked:
            score_screen.draw()
    else:
        screen.fill(settings.bg_color)
        for bullet in bullets.sprites():
            bullet.draw_bullet()
        ship.blitme()
        aliens.draw(screen)
        bunkers.draw(screen)

        sb.show_score()

    pygame.display.flip()
