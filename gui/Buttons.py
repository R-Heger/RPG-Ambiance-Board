from PyQt5.QtWidgets import *
from PyQt5.QtGui import *


class ToggleButton(QPushButton):
    def __init__(self, text=''):
        super().__init__(text)


class AddButton(QPushButton):
    def __init__(self):
        super().__init__()
        self.setIcon(QIcon(':plus.png'))


class DelButton(QPushButton):
    def __init__(self):
        super().__init__()
        self.setIcon(QIcon(':minus.png'))


class OptionsButton(QPushButton):
    def __init__(self):
        super().__init__()
        self.setIcon(QIcon(':options.png'))


class MuteButton(QPushButton):
    def __init__(self):
        super().__init__('M')


class PlayToggleButton(ToggleButton):
    def __init__(self):
        super().__init__()
        self.setIcon(QIcon(':play.png'))


class StopButton(QPushButton):
    def __init__(self):
        super().__init__()
        self.setIcon(QIcon(':stop.png'))


class NextButton(QPushButton):
    def __init__(self):
        super().__init__()
        self.setIcon(QIcon(':next.png'))


class PrevButton(QPushButton):
    def __init__(self):
        super().__init__()
        self.setIcon(QIcon(':prev.png'))


class RndToggleButton(ToggleButton):
    def __init__(self):
        super().__init__()
        self.setIcon(QIcon(':rnd.png'))


class SoundLoopToggleButton(ToggleButton):
    def __init__(self):
        super().__init__('L')


class PlaylistLoopToggleButton(ToggleButton):
    def __init__(self):
        super().__init__('L')


