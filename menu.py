from os import system
from msvcrt import getch


# general class-definitions for menu-systems


def clr_scr():
    system('cls')


class MenuItem():
    def load(self):
        pass


class MenuPoint(MenuItem):
    def __init__(self):
        pass

    def load(self):
        pass


class Menu(MenuItem):
    def __init__(self):
        pass

    def load(self):
        pass
