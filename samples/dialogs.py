import gettext
import sys
import ctypes
from PyQt5.QtWidgets import *
from PyQt5.QtGui import*
from PyQt5.QtCore import *

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        user32 = ctypes.windll.user32
        self.screenSize = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)
        self.windowScale = 0.5

        self.setWindowIcon(QIcon('../gui/icons/dragon_icon.png'))
        self.setWindowTitle("RPG Ambiance Board")

        windowSize = self.screenSize[0] * self.windowScale, self.screenSize[1] * self.windowScale
        windowPosition = (self.screenSize[0] - windowSize[0]) / 2, (self.screenSize[1] - windowSize[1]) / 2
        self.setGeometry(*windowPosition, *windowSize)

        self.init()

        self.show()

    def init(self):
        fileButton = QPushButton('Open File')

        inputButton = QPushButton('Input')


        vertical = QVBoxLayout()
        self.setLayout(vertical)

        vertical.addStretch(1)
        horizontal = QHBoxLayout()
        vertical.addLayout(horizontal)
        horizontal.addStretch(1)
        horizontal.addWidget(fileButton)
        horizontal.addWidget(inputButton)

        fileButton.clicked.connect(self.openFileDialog)
        inputButton.clicked.connect(self.openInputDialog)

    def openFileDialog(self):
        dialog = QFileDialog()
        filename = dialog.getOpenFileName(self, 'Add new Sound', 'D:\\Musik\\RPG Ambient', 'Soundfile (*.wav *.mp3)')


        print('filename:', filename)

    def openInputDialog(self):
        dialog = QInputDialog()
        text, accepted = dialog.getText(self, 'A', 'B')

        print('text:', text, 'accepted:', accepted)


