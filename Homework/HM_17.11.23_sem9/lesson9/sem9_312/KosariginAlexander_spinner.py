""" Реализация спиннера. 

    Интересная статья на тему индикаторов: https://dtf.ru/flood/174240-progress-bar-ili-spinner-chto-i-kogda-ispolzovat?ysclid=lorrg51syv550654720
    Возможно, вам поможет circle_generator...
"""

def generate_circle_sequence(chars):
    length = len(chars)
    i = 0
    while True:
        yield chars[i]
        i += 1
        i = i%length

from typing import Iterable
from time import sleep, time


def wheel(time_limit: float, pause: float):
    """ Отрисовка спиннера.   (Имеется в виду анимация загрузки, как например при загрузке игры)

        Печатает на экран надпись: 'Thinking: <symbol>',
        где вместо <symbol> последовательно появляются знаки: \, |, /, -, 
        что создаёт эффект вращения.

        Вход:
            time_limit: float
                время (в секундах), в течение которого должна производиться отрисовка спиннера
            pause: float
                время (в секундах) задержки между сменой символов спиннера
        
        Выход:
            None
    """
    anim_msv = ["\\", "|", "/", "—"]
    symbol = generate_circle_sequence(anim_msv)
    i = 0
    time0 = time()
    while time() - time0 < time_limit:
        print( " Loading:", next(symbol), end="\r" )
        sleep(pause)
        i += 1
    print(" Loading complited", end="\r")
    pass

wheel(10, 0)

