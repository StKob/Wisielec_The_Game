from ScreenStart import ScreenStart
from Words import WordlistManager
import pygame
def print_hi(name):
    print(f'Hi, {name}')


if __name__ == '__main__':
    print_hi('PyCharm')
    file = WordlistManager("Wordlist.txt")
    file.read_file()
    #file.print_dict()
    pygame.init()
    screen_start = ScreenStart()
    screen_start.run()

