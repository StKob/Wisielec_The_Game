import pygame

from Screen import Screen


class ScreenGame(Screen):

    def __init__(self, word, category):
        super().__init__()
        self.category = category
        self.word = word
        self.length = len(word)
        self.masked_word = list(self.length * '_')
        self.guessed = 0
        self.word_rect = None
        self.category_rect = None

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
        for index, item in enumerate(self.word):
            if item == letter:
                self.guessed += 1
                self.masked_word[index] = letter

        self.show_masked_word()

    def disp_word_rectangle(self, text):
        if self.word_rect is not None:
            self.disp.blit(self.font.render(self.word*2, True, (255, 255, 255), (255, 255, 255)),
                           self.word_rect)
        self.word_rect = text.get_rect()
        self.word_rect.center = (self.x // 2, self.y // 2)
        self.disp.blit(text, self.word_rect)

    def disp_category_rectangle(self, text):
        self.category_rect = text.get_rect()
        self.category_rect.center = (self.x // 2, self.y // 4)
        self.disp.blit(text, self.category_rect)

