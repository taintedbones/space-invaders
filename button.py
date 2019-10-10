import pygame.font


class Button:
    def __init__(self, settings, screen, msg):
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.text = msg

        self.width, self.height = 200, 50
        self.button_color = settings.bg_color
        self.text_color = (255, 255, 255)
        #self.font = pygame.font.SysFont(None, 48)
        self.font = pygame.font.Font('Fonts/8-Bit Madness.ttf', 48)

        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center


    def prep_msg(self):
        self.msg_image = self.font.render(self.text, True, self.text_color, self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_button(self):
        self.prep_msg()
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)
