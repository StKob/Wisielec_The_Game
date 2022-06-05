import pygame.display

from Screen import Screen


class ScreenStart(Screen):

    def __init__(self):
        super().__init__()
        self.name = "Wisielec"
        self.screen= pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption(self.name)
        self.foto = pygame.image.load('foto.png')
        self.foto = pygame.transform.scale(self.foto, (self.width * 0.8, self.height * 0.6))
        self.text = "Wisielec"

    def run(self):
        active = True
        while active:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    active = False

            self.screen.fill(self.white)
            self.screen.blit(self.foto, (self.width * 0.1, 0))
            large_text = pygame.font.SysFont(self.font, self.font_size_large)
            text_surf, text_rect = self.text_objects(self.text, large_text, self.black)
            text_rect.center = (self.width / 2, self.height * 0.7)
            self.screen.blit(text_surf, text_rect)
            self.button("Start", self.width / 2 - 100, self.height * 0.8, 200, 80, self.bright_blue, self.blue)

            pygame.display.update()




