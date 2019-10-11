from button import Button


class HighScoreScreen:
    def __init__(self, screen, settings):
        self.screen = screen
        self.settings = settings
        self.screen_rect = screen.get_rect()
        self.return_button = Button(settings, screen, "RETURN TO MENU", 48)
        self.title = Button(self.settings, self.screen, "HIGH SCORES", 80)

    def draw_title(self):
        self.title.text_color = (255, 255, 255)
        self.title.rect.center = self.screen_rect.center
        self.title.rect.left -= 60
        self.title.rect.top = self.screen_rect.top + 30
        self.title.draw_button()

    def create_scores_rect(self):
        left_spacing = 200
        font_size = 60
        index_num = []
        path = open(self.settings.high_score_file, 'r')
        score_list = path.readlines()

        for i in range(len(score_list)):
            data = score_list[i].split(' ')
            index_num.append(Button(self.settings, self.screen, str(i+1), font_size))
            current_score = Button(self.settings, self.screen, data[0], font_size)
            current_player = Button(self.settings, self.screen, data[1].strip('\n'), font_size)

            if i == 0:
                index_num[i].rect.top = self.screen_rect.top + 150
            else:
                index_num[i].rect.top = index_num[i-1].rect.bottom + 10
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
        self.return_button.rect.center = self.title.rect.center
        self.return_button.rect.bottom = self.screen_rect.bottom - 30
        self.return_button.draw_button()

    def draw(self):
        self.screen.fill(self.settings.bg_color)
        self.draw_title()
        self.create_scores_rect()
        self.draw_return_button()
