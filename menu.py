from os import system
from msvcrt import getch


# general class-definitions for menu-systems


def clr_scr():
    system('cls')


print_fcn = print  # change this if u wanna use your own printer function
getch_fcn = getch  # change this if u wanna use your own keypress catcher function
cls_fcn = clr_scr  # change this if u wanna use your own clear-screen function


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
