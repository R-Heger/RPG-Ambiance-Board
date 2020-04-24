from PyQt5.QtWidgets import *
from PyQt5.QtGui import*
from PyQt5.QtCore import *

from gui.SoundBoardGui import  SoundBoardGui
from gui.SoundLibraryGui import  SoundLibraryGui


class MainContentGui(QWidget):
    def __init__(self):
        super().__init__()

        self.soundBoard = SoundBoardGui()
        self.soundLibrary = SoundLibraryGui()

        mainBox = QHBoxLayout()
        mainBox.addWidget(self.soundBoard)
        mainBox.addWidget(self.soundLibrary)

        self.setLayout(mainBox)
        self.soundLibrary.hide()

        self.showBoard = QAction(_('&Soundboard'), self)
        self.showBoard.setStatusTip(_('Go to the Soundboard'))
        self.showBoard.triggered.connect(self.showTheBoard)

        self.showLibrary = QAction(_('&Library'), self)
        self.showLibrary.setStatusTip(_('Go to the Library'))
        self.showLibrary.triggered.connect(self.showTheLibrary)

    def showTheBoard(self):
        self.soundBoard.show()
        self.soundLibrary.hide()

    def showTheLibrary(self):
        self.soundLibrary.show()
        self.soundBoard.hide()

