import pygame

from Screen import Screen


class ScreenFinal(Screen):

    def __init__(self, mode):
        super().__init__()
        self.text="Coś poszło nie tak"
        self.text2=" "
        self.name="Error"
        self.button_name="Nowa gra"
        self.set_mode_style(mode)
        self.width=self.width*0.6
        self.height=self.height*0.6
        self.screen=pygame.display.set_mode((self.width, self.height))

    def set_mode_style(self, mode):
        if(mode=="win"):
            self.text="Gratulacje zgadłeś słowo !!!"
            self.text2 = "Zagraj jeszcze raz."
            self.name="Wygrana"
        if(mode=="loss"):
            self.text = "Niestety nie udało ci się zgadnąć słowa. "
            self.text2="Spróbuj jeszcze raz."
            self.name = "Przegrana"

    def run(self):
        active = True
        self.screen.fill(self.white)
        text1 = pygame.font.SysFont(self.font, self.font_size_small)
        text_surf, text_position = self.text_objects(self.text, text1, self.black)
        text_position.center = (self.width / 2, self.height / 4)
        self.screen.blit(text_surf, text_position)

        text2 = pygame.font.SysFont(self.font, self.font_size_small)
        text_surf, text_position = self.text_objects(self.text2, text2, self.black)
        text_position.center = (self.width / 2, self.height / 3)
        self.screen.blit(text_surf, text_position)

        while active:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    active = False

            self.button(self.button_name, self.width / 2 - 100, self.height /2+50, 200, 80, self.bright_blue, self.blue)
            pygame.display.update()
