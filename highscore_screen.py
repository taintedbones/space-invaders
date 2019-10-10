import pygame
from button import Button

class HighScoreScreen:
    def __init__(self, screen, settings):
        self.screen = screen
        self.settings = settings
        self.screen_rect = screen.get_rect()
        self.file = 'high_scores.txt'
        self.return_button = Button(settings, screen, "RETURN TO MENU", 48)
        self.clicked = False

    def draw_title(self):
        title = Button(self.settings, self.screen, "HIGH SCORES", 60)
        title.text_color = (255, 255, 255)
        title.rect.centery = self.screen_rect.centery
        title.rect.top = self.screen_rect.top + 30
        title.draw_button()

    def create_scores_rect(self):
        left_spacing = 200
        index_num = []
        path = open(self.file, 'r')
        score_list = path.readlines()

        for i in range(len(score_list)):
            data = score_list[i].split(' ')
            index_num.append(Button(self.settings, self.screen, str(i+1), 48))
            current_score = Button(self.settings, self.screen, data[0], 48)
            current_player = Button(self.settings, self.screen, data[1].strip('\n'), 48)

            if i == 0:
                index_num[i].rect.top = self.screen_rect.top + 100
            else:
                index_num[i].rect.top = index_num[i-1].rect.bottom
            index_num[i].rect.left = self.screen_rect.left + left_spacing

            current_player.rect.y = index_num[i].rect.y
            current_player.rect.right = self.screen_rect.right - left_spacing

            current_score.rect.y = index_num[i].rect.y
            current_score.rect.right = current_player.rect.left

            index_num[i].draw_button()
            current_score.draw_button()
            current_player.draw_button()

        path.close()

    def draw_return_button(self):
        self.return_button.rect.centery = self.screen_rect.centery
        self.return_button.rect.bottom = self.screen_rect.bottom - 30
        self.return_button.draw_button()

    def draw(self):
        self.screen.fill(self.settings.bg_color)
        self.draw_title()
        self.create_scores_rect()
        self.draw_return_button()
