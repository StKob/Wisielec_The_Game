import pygame

from Screen import Screen
from ScreenFinal import ScreenFinal
from ScreenGame import ScreenGame
from ScreenStart import ScreenStart
from Words import WordlistManager


def print_hi(name):
    print(f'Hi, {name}')


def working_loop():
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            pygame.display.update()


if __name__ == '__main__':
    print_hi('PyCharm')
    file = WordlistManager("Wordlist.txt")
    file.read_file()

    screen_start = ScreenStart()
    screen_start.run()
    scrgame = ScreenGame("test", "TESTOWA")
    scrgame.set_font('freesansbold.ttf', 32)
    scrgame.show_masked_word()
    scrgame.show_category()
    scrgame.show_letter_if_present('t')
    working_loop()
    screen_final=ScreenFinal("win")
    screen_final.run()

    screen_final=ScreenFinal("loss")
    screen_final.run()




