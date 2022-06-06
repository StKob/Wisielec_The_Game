import pygame
import string
import os
import locale
from pathlib import Path

from Screen import Screen
from ScreenFinal import ScreenFinal


class ScreenGame(Screen):

    def __init__(self, word, category):
        super().__init__()
        locale.setlocale(locale.LC_ALL, "")
        self.category = category
        self.word = word
        self.length = len(word)
        self.masked_word = list(self.length * '_')
        self.letter_list = list(string.ascii_lowercase)
        self.letter_list.extend(['ą', 'ć', 'ę', 'ł', 'ń', 'ó', 'ś', 'ź', 'ż'])
        self.letter_list.sort(key=locale.strxfrm)
        self.failed_clicks = -1
        self.word_rect = None
        self.category_rect = None
        self.set_font(self.font_name, self.font_size_medium)
        self.images = self.load_images()

    def run(self):
        running = True
        self.show_masked_word()
        self.show_category()

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            self.button("Wyjście", self.width / 2 + 250, self.height * 0.7, 200, 80, self.bright_blue, self.blue, quit)
            self.add_letter_buttons()
            self.show_hangman()
            if self.check_if_won():
                running = False
                screen_final = ScreenFinal("win")
                screen_final.run()
            if self.check_if_fail():
                running = False
                screen_final = ScreenFinal("loss")
                screen_final.run()
            pygame.display.update()

    def load_images(self):
        images = []
        directory = Path(__file__).parent.absolute() / "assets" / "images"
        for i in range(len(os.listdir(directory))):
            img = pygame.image.load(str(directory / "hangman") + str(i) + ".png")
            images.append(img)
        return images

    def show_word(self):
        text = self.font.render(self.word, True, (0, 0, 0), (255, 255, 255))
        self.disp_word_rectangle(text)

    def show_category(self):
        text = self.font.render(self.category, True, (0, 0, 0), (255, 255, 255))
        self.disp_category_rectangle(text)

    def show_masked_word(self):
        text = self.font.render(' '.join(self.masked_word), True, (0, 0, 0), (255, 255, 255))
        self.disp_word_rectangle(text)
        pygame.display.update()

    def show_letter_if_present(self, letter):
        if str(self.word).find(letter, 0) == -1:
            self.failed_clicks += 1
        for index, item in enumerate(self.word):
            if item == letter:
                self.masked_word[index] = letter

        self.show_masked_word()

    def check_if_won(self):
        if self.failed_clicks < 9 and ''.join(self.masked_word) == self.word:
            return True
        else:
            return False

    def check_if_fail(self):
        if self.failed_clicks >= 9:
            return True
        else:
            return False

    def disp_word_rectangle(self, text):
        if self.word_rect is not None:
            self.screen.blit(self.font.render(self.word * 2, True, (255, 255, 255), (255, 255, 255)),
                             self.word_rect)
        self.word_rect = text.get_rect()
        self.word_rect.center = (self.width // 3, self.height // 2)
        self.screen.blit(text, self.word_rect)

    def disp_category_rectangle(self, text):
        self.category_rect = text.get_rect()
        self.category_rect.center = (self.width // 3, self.height // 4)
        self.screen.blit(text, self.category_rect)

    def add_letter_buttons(self):
        self.iter = 0
        self.mul = 0.7
        for i in self.letter_list:
            self.button(i, self.width // 2 - 600 + self.iter, self.height * self.mul, 60, 60, self.bright_blue,
                        self.blue, letter_action=self.on_letter_button_pressed)
            self.iter += 70
            if self.iter >= 800:
                self.iter = 0
                self.mul += 0.1

    def on_letter_button_pressed(self, letter):
        self.letter_list.remove(letter)
        self.show_letter_if_present(letter)
        pygame.draw.rect(self.screen, (255, 255, 255), (self.width // 2 - 600, self.height * 0.7, 800, 800))
        pygame.time.delay(100)

    def show_hangman(self):
        if -1 < self.failed_clicks < 10:
            self.screen.blit(self.images[self.failed_clicks], (self.width // 2 + 190, 50))

    def quit(self):
        pygame.quit()
        exit()




