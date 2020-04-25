from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

from gui.buttons import *


class TitleBarWidget(QWidget):
    def __init__(self, title: str):
        super().__init__()

        titleBox = QHBoxLayout()
        titleBox.addWidget(QLabel(title))
        titleBox.addStretch(1)
        titleBox.addWidget(AddButton())
        titleBox.addWidget(DelButton())
        titleBox.addWidget(OptionsButton())

        self.setLayout(titleBox)
