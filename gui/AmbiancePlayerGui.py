
from PyQt5.QtWidgets import *
from PyQt5.QtGui import*
from PyQt5.QtCore import *

from application.AudioPlayer import *



class AmbiancePlayerWidget(QWidget):
    def __init__(self):
        super().__init__()

        self.player = AudioPlayer()

        fileButton = QPushButton('Open File')
        playButton = QPushButton('Play')
        pauseButton = QPushButton('Pause')
        stopButton = QPushButton('Stop')

        transport = QVBoxLayout()
        transport.addWidget(playButton)
        transport.addWidget(pauseButton)
        transport.addWidget(stopButton)
        transport.addStretch(1)
        transport.addWidget(fileButton)

        outerVBox = QVBoxLayout()
        self.setLayout(outerVBox)

        self.soundTitle = QLabel('Title')
        outerVBox.addWidget(self.soundTitle)

        outerHBox = QHBoxLayout()
        outerVBox.addLayout(outerHBox)

        volumeSlider = QSlider()
        outerHBox.addWidget(volumeSlider)

        outerHBox.addLayout(transport)

        fileButton.clicked.connect(self.openFileDialog)
        playButton.clicked.connect(self.playClicked)
        pauseButton.clicked.connect(self.pauseClicked)
        stopButton.clicked.connect(self.stopClicked)

        volumeSlider.valueChanged.connect(self.adjustVolume)
        volumeSlider.setValue(defaultVolume)

        self.setMaximumWidth(100)

    def openFileDialog(self):
        dialog = QFileDialog()
        filename = dialog.getOpenFileName(self, 'Add new Sound', 'D:\\Musik\\RPG Ambient', 'Soundfile (*.wav *.mp3)')
        self.soundTitle.setText(filename[0])

        self.player.setSound(filename[0])

    def playClicked(self):
        self.player.play()

    def pauseClicked(self):
        self.player.pause()

    def stopClicked(self):
        self.player.stop()

    def adjustVolume(self, vol):
        self.player.setVolume(vol)
