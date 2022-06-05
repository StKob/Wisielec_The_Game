import pygame


class Screen:

    def __init__(self):
        self.font = None
        pygame.init()
        info_object = pygame.display.Info()
        self.x = info_object.current_w * 0.7
        self.y = info_object.current_h * 0.7
        self.disp = pygame.display.set_mode((int(self.x), int(self.y)))
        self.disp.fill((255, 255, 255))
        pygame.display.update()

    def set_font(self, font, size):
        self.font = pygame.font.Font(font, size)



