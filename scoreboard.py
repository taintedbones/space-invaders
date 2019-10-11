import pygame.font
from pygame.sprite import Group
from ship import Ship


class Scoreboard:
    def __init__(self, settings, screen, stats):
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.settings = settings
        self.stats = stats

        # Font settings for scoring information
        self.text_color = (255, 255, 255)
        self.font = pygame.font.Font(settings.default_font, 48)

        # Prepare the initial score image
        self.prep_score()
        self.prep_high_score()
        self.prep_level()
        self.prep_ships()

    def get_high_scores(self):
        path = self.settings.high_score_file
        scores = []
        file = open(path, 'r')

        list = file.readlines()
        for i in range(len(list)):
            data = list[i].split(' ')
            data[1].rstrip()
            scores.append(data)

        file.close()
        return scores

    def check_high_score(self):
        score_list = self.get_high_scores()
        insert_index = -1
        player_initials = 'TST'

        for i in range(len(score_list)):
            if self.stats.high_score > int(score_list[1][0]):
                insert_index = i

        add_needed = insert_index > -1
        if add_needed:
            score_list.insert(insert_index, [self.stats.high_score, player_initials])
            self.rewrite_score_file(score_list)

    def rewrite_score_file(self, score_list):
        path = self.settings.high_score_file
        file = open(path, 'w')
        lines = []

        for i in range(len(score_list)):
            lines.append(score_list[0] + " " + score_list[1])

        file.writelines(lines)

        file.close()



    def prep_score(self):
        rounded_score = int(round(self.stats.score, -1))
        score_str = "{:,}".format(rounded_score)
        self.score_image = self.font.render(score_str, True, self.text_color, self.settings.bg_color)

        # Display the score at the top right of the screen
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20

    def prep_high_score(self):
        high_score = int(round(self.stats.high_score, -1))
        high_score_str = "{:,}".format(high_score)
        self.high_score_image = self.font.render(high_score_str, True, self.text_color, self.settings.bg_color)

        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = self.score_rect.top

    def prep_level(self):
        self.level_image = self.font.render(str(self.stats.level), True, self.text_color, self.settings.bg_color)

        # Posiition level below the score
        self.level_rect = self.level_image.get_rect()
        self.level_rect.right = self.score_rect.right
        self.level_rect.top = self.score_rect.bottom + 10

    def prep_ships(self):
        self.ships = Group()
        for ship_number in range(self.stats.ships_left):
            ship = Ship(self.screen, self.settings)
            ship.rect.x = 10 + ship_number * ship.rect.width
            ship.rect.y = 10
            self.ships.add(ship)

    def show_score(self):
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)
        self.screen.blit(self.level_image, self.level_rect)
        self.ships.draw(self.screen)
