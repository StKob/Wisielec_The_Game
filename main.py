from ScreenFinal import ScreenFinal
from ScreenGame import ScreenGame
from ScreenStart import ScreenStart
from Words import WordlistManager


if __name__ == '__main__':
    file = WordlistManager("Wordlist.txt")
    file.read_file()

    screen_start = ScreenStart()
    screen_start.run()
    word, category = file.get_random_word()
    scrgame = ScreenGame(word, category)
    scrgame.run()

    screen_final = ScreenFinal("win")
    screen_final.run()

    screen_final = ScreenFinal("loss")
    screen_final.run()
