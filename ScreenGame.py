import pygame
import pygame_textinput
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
        self.letter_button_size = 60
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
        self.letter_list_temp = dict()
        for i in self.letter_list:
            self.letter_list_temp[i] = self.blue
        self.letter_list = self.letter_list_temp

    def run(self):
        running = True

        textinput = pygame_textinput.TextInputVisualizer()
        textinput.cursor_blink_interval = 500

        while running:
            self.screen.fill((255, 255, 255))
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    running = False
            self.show_masked_word()
            self.show_word_or_category(self.category)
            self.button("Koniec", self.window_center_width + 350, self.height * 0.8, 200, 80, self.bright_blue,
                        self.blue, quit)
            self.add_letter_buttons()
            self.show_hangman()
            self.text_input(textinput, events, running)
            if self.check_if_won():
                self.win(running)
            if self.check_if_fail():
                self.fail(running)
            pygame.display.update()

    def fail(self, running):
        running = False
        screen_final = ScreenFinal("loss", self.word)
        screen_final.run()
        return running

    def win(self, running):
        running = False
        screen_final = ScreenFinal("win", self.word)
        screen_final.run()
        return running

    def load_images(self):
        images = []
        directory = Path(__file__).parent.absolute() / "assets" / "images"
        for i in range(len(os.listdir(directory))):
            img = pygame.image.load(str(directory / "hangman") + str(i) + ".png")
            images.append(img)
        return images

    def show_word_or_category(self, data):
        text = self.font.render(data, True, self.black, self.white)
        if data == self.word:
            self.disp_word_rectangle(text)

        if data == self.category:
            self.disp_category_rectangle(text)

    def show_masked_word(self):
        text = self.font.render(' '.join(self.masked_word), True, self.black, self.white)
        self.disp_word_rectangle(text)

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
            self.screen.blit(self.font.render(self.word + 7 * "A", True, self.white, self.white),
                             self.word_rect)
        self.word_rect = text.get_rect()
        self.word_rect.center = (self.window_one_third_width, self.window_center_height - 50)
        self.screen.blit(text, self.word_rect)

    def disp_category_rectangle(self, text):
        self.category_rect = text.get_rect()
        self.category_rect.center = (self.window_one_third_width, self.window_center_height / 2 - 50)
        self.screen.blit(text, self.category_rect)

    def add_letter_buttons(self):
        iteration = 0
        mul = 0.7
        for i in self.letter_list:
            if self.letter_list[i] == self.grey:
                self.button(i, self.window_center_width - 600 + iteration, self.height * mul, self.letter_button_size,
                            self.letter_button_size, self.letter_list[i], self.letter_list[i],
                            letter_action=self.on_letter_button_pressed)
            else:
                self.button(i, self.window_center_width - 600 + iteration, self.height * mul, self.letter_button_size,
                            self.letter_button_size, self.bright_blue, self.blue,
                            letter_action=self.on_letter_button_pressed)
            iteration += 70
            if iteration >= 800:
                iteration = 0
                mul += 0.1

    def on_letter_button_pressed(self, letter):
        # self.letter_list.remove(letter)
        if self.letter_list[letter] != self.grey:
            self.show_letter_if_present(letter)
        self.letter_list[letter] = self.grey
        pygame.draw.rect(self.screen, self.white, (self.window_center_width - 600,
                                                   self.height - self.window_one_third_height, 850, 800))
        pygame.time.delay(100)

    def show_hangman(self):
        if -1 < self.failed_clicks < 10:
            self.screen.blit(self.images[self.failed_clicks], (self.window_center_width + 190, 100))

    def text_input(self, textinput, events, running_state):
        textinput.update(events)
        pygame.draw.rect(self.screen, self.black, (self.window_one_third_width - 60,
                                                   self.window_center_height + 70, 300, 50), 2)
        text = self.font.render("słowo:", True, self.black, self.white)
        text_rectangle = text.get_rect()
        text_rectangle.center = (self.window_one_third_width - 160, self.window_center_height + 87)
        self.screen.blit(text, text_rectangle)

        for event in events:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                if textinput.value == self.word:
                    self.win(running_state)
                else:
                    self.failed_clicks += 1
                textinput.value = ""
        self.screen.blit(textinput.surface, (self.window_one_third_width - 50, self.window_center_height + 80))

    def quit(self):
        pygame.quit()
        exit()
