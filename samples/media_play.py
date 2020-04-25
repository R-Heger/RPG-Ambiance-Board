import gettext
import sys
import ctypes
from PyQt5.QtWidgets import *
from PyQt5.QtGui import*
from PyQt5.QtCore import *

import vlc



class MainWindow(QTabWidget):
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

        self.player = vlc.MediaPlayer()

        fileButton = QPushButton('Open File')
        playButton = QPushButton('Play')
        pauseButton = QPushButton('Pause')
        stopButton = QPushButton('Stop')

        transport = QHBoxLayout()

        transport.addWidget(playButton)
        transport.addWidget(pauseButton)
        transport.addWidget(stopButton)

        self.songTitle = QLabel('Song Title')

        vertical = QVBoxLayout()
        self.setLayout(vertical)
        vertical.addStretch(1)
        vertical.addWidget(self.songTitle)
        vertical.addLayout(transport)
        vertical.addStretch(1)
        horizontal = QHBoxLayout()
        vertical.addLayout(horizontal)
        horizontal.addStretch(1)

        horizontal.addWidget(fileButton)

        fileButton.clicked.connect(self.openFileDialog)
        playButton.clicked.connect(self.playClicked)
        pauseButton.clicked.connect(self.pauseClicked)
        stopButton.clicked.connect(self.stopClicked)



        self.show()

    def openFileDialog(self):
        dialog = QFileDialog()
        filename = dialog.getOpenFileName(self, 'Add new Sound', 'D:\\Musik\\RPG Ambient', 'Soundfile (*.wav *.mp3)')
        self.songTitle.setText(filename[0])

        self.player = vlc.MediaPlayer(filename[0])

    def playClicked(self):
        self.player.play()

    def pauseClicked(self):
        self.player.pause()

    def stopClicked(self):
        self.player.stop()
