from PyQt5.QtWidgets import *
from PyQt5.QtGui import*
from PyQt5.QtCore import *


class SoundLibraryWidget(QWidget):
    def __init__(self):
        super().__init__()

        box = QHBoxLayout()
        frame = QFrame()
        frame.setStyleSheet("QWidget {background-color: #555}")
        box.addWidget(frame)
        self.setLayout(box)
