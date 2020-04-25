from PyQt5.QtWidgets import *
from PyQt5.QtGui import*
from PyQt5.QtCore import *

from gui.SoundBoardWidget import  SoundBoardWidget
from gui.SoundLibraryWidget import  SoundLibraryWidget


class MainContentWidget(QWidget):
    def __init__(self):
        super().__init__()

        self.soundBoard = SoundBoardWidget()
        self.soundLibrary = SoundLibraryWidget()

        self.content = QStackedLayout()
        self.content.addWidget(self.soundBoard)
        self.content.addWidget(self.soundLibrary)

        self.setLayout(self.content)
        self.content.setCurrentWidget(self.soundBoard)

        self.showBoard = QAction(_('&Soundboard'), self)
        self.showBoard.setStatusTip(_('Go to the Soundboard'))
        self.showBoard.triggered.connect(self.showTheBoard)

        self.showLibrary = QAction(_('&Library'), self)
        self.showLibrary.setStatusTip(_('Go to the Library'))
        self.showLibrary.triggered.connect(self.showTheLibrary)

    def showTheBoard(self):
        self.content.setCurrentWidget(self.soundBoard)

    def showTheLibrary(self):
        self.content.setCurrentWidget(self.soundLibrary)

