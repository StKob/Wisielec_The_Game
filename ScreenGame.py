import pygame
import string

from Screen import Screen


class ScreenGame(Screen):

    def __init__(self, word, category):
        super().__init__()
        self.category = category
        self.word = word
        self.length = len(word)
        self.masked_word = list(self.length * '_')
        self.letter_list = list(string.ascii_lowercase)
        self.guessed = 0
        self.word_rect = None
        self.category_rect = None
        self.set_font(self.font_name, self.font_size_large)

    def run(self):
        running = True
        self.show_masked_word()
        self.show_category()

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            self.button("Wyjście", self.width / 2 + 250, self.height * 0.05, 200, 80, self.bright_blue, self.blue, quit)
            self.add_letter_buttons()
            pygame.display.update()

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
        if str(self.word).find(letter, 0):
            self.guessed += 1
        for index, item in enumerate(self.word):
            if item == letter:
                self.masked_word[index] = letter

        self.show_masked_word()

    def check_if_won(self):
        if self.guessed < 9 and str(self.masked_word) == self.word:
            return True

    def disp_word_rectangle(self, text):
        if self.word_rect is not None:
            self.screen.blit(self.font.render(self.word * 2, True, (255, 255, 255), (255, 255, 255)),
                             self.word_rect)
        self.word_rect = text.get_rect()
        self.word_rect.center = (self.width // 2, self.height // 2)
        self.screen.blit(text, self.word_rect)

    def disp_category_rectangle(self, text):
        self.category_rect = text.get_rect()
        self.category_rect.center = (self.width // 2, self.height // 4)
        self.screen.blit(text, self.category_rect)

    def add_letter_buttons(self):
        self.iter = 0
        self.mul = 0.7
        for i in self.letter_list:
            self.button(i, self.width // 2 - 450 + self.iter, self.height * self.mul, 60, 60, self.bright_blue,
                        self.blue, letter_action=self.on_letter_button_pressed)
            self.iter += 70
            if self.iter >= 700:
                self.iter = 0
                self.mul += 0.1

    def on_letter_button_pressed(self, letter):
        self.letter_list.remove(letter)
        pygame.draw.rect(self.screen, (255, 255, 255), (self.width // 2 - 450, self.height * 0.7, 800, 800))
        pygame.time.delay(100)

    def quit(self):
        pygame.quit()
        exit()




