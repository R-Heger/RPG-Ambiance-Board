import gettext
import sys
import ctypes
from PyQt5.QtWidgets import *
from PyQt5.QtGui import*
from PyQt5.QtCore import *

from gui.SoundBoardGui import  SoundBoardGui
from gui.SoundLibraryGui import  SoundLibraryGui
from gui.MainContentGui import  MainContentGui


class RPGABMainGUI(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowIcon(QIcon('../icons/dragon_icon.png'))
        self.setWindowTitle("RPG Ambiance Board")

        # init
        user32 = ctypes.windll.user32
        screenSize = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)
        windowScale = 0.75

        windowSize = screenSize[0] * windowScale, screenSize[1] * windowScale
        windowPosition = (screenSize[0] - windowSize[0]) / 2, (screenSize[1] - windowSize[1]) / 2
        self.setGeometry(*windowPosition, *windowSize)

        self.exitMain = QAction(QIcon('../icons/ab_icon.png'), _('&Exit'), self)
        self.exitMain.setStatusTip(_('Exit'))
        self.exitMain.triggered.connect(self.close)

        menubar = self.menuBar()
        file = menubar.addMenu(_('&File'))
        file.addAction(self.exitMain)

        statusbar = self.statusBar()
        statusbar.showMessage(_('Ready for some epic adventures'))

        self.mainContent = MainContentGui()

        self.setCentralWidget(self.mainContent)

        menubar.addAction(self.mainContent.showBoard)
        menubar.addAction(self.mainContent.showLibrary)

        self.show()



