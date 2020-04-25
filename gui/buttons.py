from PyQt5.QtWidgets import *
from PyQt5.QtGui import *


class AddButton(QPushButton):
    def __init__(self):
        super().__init__('+')


class DelButton(QPushButton):
    def __init__(self):
        super().__init__('-')


class OptionsButton(QPushButton):
    def __init__(self):
        super().__init__()
        self.setIcon(QIcon(':dragon.png'))


class MuteButton(QPushButton):
    def __init__(self):
        super().__init__('M')


class PlayToggleButton(QPushButton):
    def __init__(self):
        super().__init__('|>')


class StopButton(QPushButton):
    def __init__(self):
        super().__init__('[]')


class NextButton(QPushButton):
    def __init__(self):
        super().__init__('>|')


class PrevButton(QPushButton):
    def __init__(self):
        super().__init__('|<')


class RndToggleButton(QPushButton):
    def __init__(self):
        super().__init__('R')


class LoopToggleButton(QPushButton):
    def __init__(self):
        super().__init__('L')
