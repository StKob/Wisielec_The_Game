import pygame.display

from Screen import Screen
from ScreenGame import ScreenGame
from Words import WordlistManager


class ScreenStart(Screen):

    def __init__(self):
        super().__init__()
        self.name = "Wisielec"
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption(self.name)
        self.foto = pygame.image.load('assets/images/hangman9.png')
        self.foto = pygame.transform.scale(self.foto, (self.width * 0.4, self.height * 0.6))
        self.text = "Wisielec"

    def run(self):
        active = True
        self.screen.fill(self.white)
        self.screen.blit(self.foto, (self.width /2-self.width*0.4/2, 0))
        large_text = pygame.font.SysFont(self.font_name, self.font_size_large)
        text_surf, text_rect = self.text_objects(self.text, large_text, self.black)
        text_rect.center = (self.width / 2, self.height * 0.7)
        self.screen.blit(text_surf, text_rect)

        while active:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    active = False
            pygame.display.update()
            self.button("Start", self.width / 2 - 100, self.height * 0.8, 200, 80, self.bright_blue, self.blue,
                        self.start_game)


    def start_game(self):
        file = WordlistManager("Wordlist.txt")
        file.read_file()
        word, category = file.get_random_word()

        scrgame = ScreenGame(word, category)
        pygame.time.delay(200)
        scrgame.run()
        pygame.quit()
