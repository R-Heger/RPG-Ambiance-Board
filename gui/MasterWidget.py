from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

from gui.Buttons import *


class MasterWidget(QWidget):
    def __init__(self):
        super().__init__()

        masterBox = QVBoxLayout()
        sliderBox = QHBoxLayout()
        sliderBox.addStretch(1)
        self.masterVolume = QSlider()
        sliderBox.addWidget(self.masterVolume)
        sliderBox.addStretch(1)
        masterBox.addLayout(sliderBox)

        self.muteButton = MuteButton()
        masterBox.addWidget(self.muteButton)

        self.setLayout(masterBox)

        self.setFixedWidth(50)
