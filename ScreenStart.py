import pygame.display

black = (0, 0, 0)
white = (255, 255, 255)
blue = (0, 0, 204)
bright_blue = (0, 128, 255)


class ScreenStart:

    def __init__(self):
        self.name = "Wisielec"
        self.width = 1000
        self.height = 700
        self.screen_start = pygame.display.set_mode((self.width, self.height))  # wymiary z sceen
        pygame.display.set_caption(self.name)
        self.foto = pygame.image.load('foto.png')
        self.foto = pygame.transform.scale(self.foto, (self.width * 0.8, self.height * 0.6))  # wymiary wzgledem screen
        self.font = "comicsansms"  # do screen
        self.text = "Wisielec"
        self.font_size_large = 90  # do screen
        self.font_size_small = 30  # do screen

    def run(self):
        active = True
        while active:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    active = False
            self.screen_start.fill(white)

            self.screen_start.blit(self.foto, (self.width * 0.1, 0))
            large_text = pygame.font.SysFont(self.font, self.font_size_large)
            text_surf, text_rect = text_objects(self.text, large_text, black)
            text_rect.center = (self.width / 2, self.height * 0.7)
            self.screen_start.blit(text_surf, text_rect)
            self.button("Start", self.width / 2 - 100, self.height * 0.8, 200, 80, bright_blue, blue)

            pygame.display.update()

    def button(self, msg, x, y, w, h, unactive_color, active_color, action=None):
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        if x + w > mouse[0] > x and y + h > mouse[1] > y:
            pygame.draw.rect(self.screen_start, active_color, (x, y, w, h))

            if click[0] == 1 and action != None:
                action()
        else:
            pygame.draw.rect(self.screen_start, unactive_color, (x, y, w, h))

        button_text = pygame.font.SysFont(self.font, self.font_size_small)
        text_surf, text_rect = text_objects(msg, button_text, white)
        text_rect.center = ((x + (w / 2)), (y + (h / 2)))
        self.screen_start.blit(text_surf, text_rect)


def text_objects(text, font, color):
    text_surface = font.render(text, True, color)
    return text_surface, text_surface.get_rect()
