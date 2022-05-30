import pygame


class Screen:

    def __init__(self):
        pygame.init()
        info_object = pygame.display.Info()
        pygame.display.set_mode((info_object.current_h * 0.7, info_object.current_h * 0.7))


