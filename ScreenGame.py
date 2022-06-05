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
        for index, item in enumerate(self.word):
            if item == letter:
                self.guessed += 1
                self.masked_word[index] = letter

        self.show_masked_word()

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

    def quit(self):
        pygame.quit()
        exit()
