from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

from gui.Buttons import *


class TitleBarWidget(QWidget):
    def __init__(self, title: str, showAddAndDel=True):
        super().__init__()

        titleBox = QHBoxLayout()
        titleBox.addWidget(QLabel(title))
        titleBox.addStretch(1)
        self.addButton = AddButton()
        self.delButton = DelButton()
        titleBox.addWidget(self.addButton)
        titleBox.addWidget(self.delButton)
        if not showAddAndDel:
            self.addButton.hide()
            self.delButton.hide()

        titleBox.addWidget(OptionsButton())

        self.setLayout(titleBox)
