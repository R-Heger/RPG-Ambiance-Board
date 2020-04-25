import gettext
import sys
import ctypes
from PyQt5.QtWidgets import *
from PyQt5.QtGui import*
from PyQt5.QtCore import *

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        user32 = ctypes.windll.user32
        self.screenSize = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)
        self.windowScale = 0.75

        self.setWindowIcon(QIcon('../gui/icons/dragon_icon.png'))
        self.setWindowTitle("RPG Ambiance Board")

        windowSize = self.screenSize[0] * self.windowScale, self.screenSize[1] * self.windowScale
        windowPosition = (self.screenSize[0] - windowSize[0]) / 2, (self.screenSize[1] - windowSize[1]) / 2
        self.setGeometry(*windowPosition, *windowSize)

        self.init()

        self.show()

    def init(self):
        upvote = QPushButton('Upvote')
        abo = QPushButton('Do the Abo!')

        vertical = QVBoxLayout()
        self.setLayout(vertical)

        grid = QGridLayout()
        buttons = [QPushButton(str(i)) for i in range(1, 10)]
        positions = [(i, j) for i in range(3) for j in range(3)]

        for pos, button in zip(positions, buttons):
            button.setCheckable(True)
            grid.addWidget(button, *pos)

        vertical.addLayout(grid)

        vertical.addStretch(1)
        horizontal = QHBoxLayout()

        vertical.addLayout(horizontal)

        horizontal.addStretch(2)
        horizontal.addWidget(upvote)
        horizontal.addWidget(abo)
        horizontal.addStretch(1)




