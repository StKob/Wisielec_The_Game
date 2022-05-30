import pygame


class Screen:

    def __init__(self):
        pygame.init()
        info_object = pygame.display.Info()
        disp = pygame.display.set_mode((info_object.current_w * 0.7, info_object.current_h * 0.7))
        disp.fill((255, 255, 255))
        pygame.display.update()


