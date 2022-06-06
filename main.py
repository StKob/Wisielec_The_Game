from ScreenFinal import ScreenFinal
from ScreenStart import ScreenStart


if __name__ == '__main__':

    screen_start = ScreenStart()
    screen_start.run()

    screen_final = ScreenFinal("win")
    screen_final.run()

    screen_final = ScreenFinal("loss")
    screen_final.run()




