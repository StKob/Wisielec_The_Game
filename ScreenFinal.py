import pygame

from Screen import Screen


class ScreenFinal(Screen):

    def __init__(self, mode, word):
        super().__init__()
        self.text="Coś poszło nie tak"
        self.text2=" "
        self.name="Error"
        self.button_name="Koniec"
        self.set_mode_style(mode)
        self.screen=pygame.display.set_mode((self.width, self.height))
        self.word =word

    def set_mode_style(self, mode):
        if mode== "win":
            self.text="Gratulacje zgadłeś słowo !!!"
            self.text2 = "Zagraj jeszcze raz."
            self.name="Wygrana"
        if mode== "loss":
            self.text = "Niestety nie udało ci się zgadnąć słowa. "
            self.text2="Spróbuj jeszcze raz."
            self.name = "Przegrana"

    def run(self):
        active = True
        self.screen.fill(self.white)
        text1 = pygame.font.SysFont(self.font, self.font_size_medium)
        text_surf, text_position = self.text_objects(self.text, text1, self.black)
        text_position.center = (self.window_center_width, 100)
        self.screen.blit(text_surf, text_position)

        text2 = pygame.font.SysFont(self.font, self.font_size_medium)
        text_surf, text_position = self.text_objects(self.text2, text2, self.black)
        text_position.center = (self.window_center_width, self.height -self.window_one_third_height)
        self.screen.blit(text_surf, text_position)

        word = pygame.font.SysFont(self.font, self.font_size_large*2)
        text_surf, text_position = self.text_objects(self.word, word, self.red)
        text_position.center = (self.window_center_width, self.window_center_height-50)
        self.screen.blit(text_surf, text_position)
        while active:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    active = False

            self.button(self.button_name, self.window_center_width - 100, self.height *0.8, 200, 80, self.bright_blue, self.blue,quit)
            pygame.display.update()
    def quit(self):
        pygame.quit()
        exit()