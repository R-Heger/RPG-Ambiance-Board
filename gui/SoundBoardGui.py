from PyQt5.QtWidgets import *
from PyQt5.QtGui import*
from PyQt5.QtCore import *

from gui.AmbiancePlayerGui import AmbiancePlayerWidget


class SoundBoardGui(QWidget):
    def __init__(self):
        super().__init__()

        outerVBox = QVBoxLayout()
        outerVBox.addWidget(QFrame())
        boardSplitter = QSplitter(Qt.Vertical)
        outerVBox.addWidget(boardSplitter)

        hBox = QHBoxLayout()
        hBox.addWidget(AmbiancePlayerWidget())
        hBox.addWidget(AmbiancePlayerWidget())
        hBox.addStretch(1)
        outerVBox.addLayout(hBox)

        self.setLayout(outerVBox)
