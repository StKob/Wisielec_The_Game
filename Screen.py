import pygame


class Screen:

    def __init__(self):
        pygame.init()
        self.font_name = "comicsansms"
        self.font = None
        self.width = 1280
        self.height = 800
        self.font_size_large = 90
        self.font_size_medium = 60
        self.font_size_small = 30
        self.set_colors()
        self.screen = pygame.display.set_mode((int(self.width), int(self.height)))
        self.screen.fill(self.white)
        pygame.display.update()

    def set_font(self, font, size):
        self.font = pygame.font.SysFont(font, size)

    def set_colors(self):
        self.black = (0, 0, 0)
        self.white = (255, 255, 255)
        self.blue = (0, 0, 204)
        self.bright_blue = (0, 128, 255)

    def button(self, msg, x, y, w, h, inactive_color, active_color, action=None, letter_action=None):
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        pygame.draw.rect(self.screen, inactive_color, (x, y, w, h))

        button_text = pygame.font.SysFont(self.font_name, self.font_size_small)
        text_surf, text_rect = self.text_objects(msg, button_text, self.white)
        text_rect.center = ((x + (w / 2)), (y + (h / 2)))

        if x + w > mouse[0] > x and y + h > mouse[1] > y:
            pygame.draw.rect(self.screen, active_color, (x, y, w, h))

            if click[0] == 1 and action is not None:
                action()
                return
            if click[0] == 1 and letter_action is not None:
                letter_action(msg)
        else:
            pygame.draw.rect(self.screen, inactive_color, (x, y, w, h))

        self.screen.blit(text_surf, text_rect)



    @staticmethod
    def text_objects(text, font, color):
        text_surface = font.render(text, True, color)
        return text_surface, text_surface.get_rect()
