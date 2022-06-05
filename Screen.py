import pygame


class Screen:

    def __init__(self):
        pygame.init()
        self.font = "comicsansms"
        self.width = 1000
        self.height = 700
        self.font_size_large = 90
        self.font_size_small = 30
        self.set_colors()
        self.disp = pygame.display.set_mode((int(self.width), int(self.height)))
        self.disp.fill(self.white)
        pygame.display.update()

    def set_font(self, font, size):
        self.font = pygame.font.Font(font, size)

    def set_colors(self):
        self.black = (0, 0, 0)
        self.white = (255, 255, 255)
        self.blue = (0, 0, 204)
        self.bright_blue = (0, 128, 255)
