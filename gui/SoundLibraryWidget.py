from PyQt5.QtWidgets import *
from PyQt5.QtGui import*
from PyQt5.QtCore import *


class SoundLibraryWidget(QWidget):
    def __init__(self):
        super().__init__()

        box = QHBoxLayout()
        frame = QFrame()
        frame.setStyleSheet("QWidget {background-color: silver}")
        box.addWidget(frame)
        self.setLayout(box)
