from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

from gui.buttons import *


class MasterWidget(QWidget):
    def __init__(self):
        super().__init__()

        masterBox = QVBoxLayout()
        self.masterVolume = QSlider()
        masterBox.addWidget(self.masterVolume)
        self.masterVolume.move(self.rect().center())
        masterBox.addWidget(MuteButton())

        self.setLayout(masterBox)
