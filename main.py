import pygame

from Screen import Screen
from Words import WordlistManager


def print_hi(name):
    print(f'Hi, {name}')


def working_loop():
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False


if __name__ == '__main__':
    print_hi('PyCharm')
    file = WordlistManager("Wordlist.txt")
    file.read_file()
    file.print_dict()
    scr = Screen()
    working_loop()

