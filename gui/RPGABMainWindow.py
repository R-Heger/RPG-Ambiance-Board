import gettext
import sys
import ctypes
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

from gui.SoundBoardWidget import  SoundBoardWidget
from gui.SoundLibraryWidget import  SoundLibraryWidget
from gui.MainContentWidget import  MainContentWidget



class RPGABMainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowIcon(QIcon(':dragon.png'))
        self.setWindowTitle("RPG Ambiance Board")

        # init
        user32 = ctypes.windll.user32
        screenSize = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)
        windowScale = 0.85

        windowSize = screenSize[0] * windowScale, screenSize[1] * windowScale
        windowPosition = (screenSize[0] - windowSize[0]) / 2, (screenSize[1] - windowSize[1]) / 2
        self.setGeometry(*windowPosition, *windowSize)

        self.exitMain = QAction(_('&Exit'), self)
        self.exitMain.setStatusTip(_('Exit'))
        self.exitMain.triggered.connect(self.close)

        self.mainContent = MainContentWidget()
        self.setCentralWidget(self.mainContent)

        statusbar = self.statusBar()
        statusbar.showMessage(_('Ready for some epic adventures!'))

        menubarLeft = self.menuBar()

        file = menubarLeft.addMenu(_('&File'))
        file.addAction(self.exitMain)

        menubarLeft.addAction(self.mainContent.showBoard)
        menubarLeft.addAction(self.mainContent.showLibrary)

        self.setFullscreen = QAction('[  ]', self)
        self.setFullscreen.setStatusTip(_('Fullscreen'))
        self.setFullscreen.triggered.connect(self.toggleFullscreen)

        menubarRight = QMenuBar(menubarLeft)
        menubarLeft.setCornerWidget(menubarRight, Qt.TopRightCorner)
        menubarRight.addAction(self.setFullscreen)

        self.show()

    def toggleFullscreen(self):
        if self.isFullScreen():
            self.showNormal()
        else:
            self.showFullScreen()
