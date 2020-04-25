import gettext
import sys
import ctypes
from PyQt5.QtWidgets import *
from PyQt5.QtGui import*
from PyQt5.QtCore import *

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        user32 = ctypes.windll.user32
        self.screenSize = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)
        self.windowScale = 0.75

        self.setWindowIcon(QIcon('../gui/icons/dragon_icon.png'))
        self.setWindowTitle("RPG Ambiance Board")

        windowSize = self.screenSize[0] * self.windowScale, self.screenSize[1] * self.windowScale
        windowPosition = (self.screenSize[0] - windowSize[0]) / 2, (self.screenSize[1] - windowSize[1]) / 2
        self.setGeometry(*windowPosition, *windowSize)

        self.init()

        self.show()

    def init(self):
        statusbar = self.statusBar().showMessage('This will become awesome!')
        exitMe = QAction(QIcon('../gui/icons/ab_icon.png'), _('&Exit'), self)
        exitMe.setShortcut('Ctrl+E')
        exitMe.setStatusTip('Exit')
        exitMe.triggered.connect(self.close)

        menubar = self.menuBar()
        file = menubar.addMenu(_('&File'))
        file.addAction(exitMe)
        menubar.addAction(exitMe)

        toolbar = self.addToolBar('Exit')
        toolbar.addAction(exitMe)


