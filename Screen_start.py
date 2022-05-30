import pygame.display


class Screen_start:

    def __init__(self):
        self.name = "Okno startowe"
        win = pygame.display.set_mode((500,500))
        pygame.display.set_caption(self.name)


    def run(self):
        active = True
        while active:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    active = False

