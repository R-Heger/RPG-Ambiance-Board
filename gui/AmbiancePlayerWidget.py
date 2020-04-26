from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

from gui.Buttons import *
from application.AudioPlayer import *


class AmbiancePlayerWidget(QWidget):
    def __init__(self, title: str):
        super().__init__()

        self.title = QLabel(title)
        self.title.setAlignment(Qt.AlignCenter)

        self.player = AudioPlayer()

        outerVBox = QVBoxLayout()
        self.setLayout(outerVBox)
        outerVBox.addWidget(self.title)

        optionsButton = OptionsButton()
        playButton = PlayToggleButton()
        stopButton = StopButton()
        loopButton = SoundLoopToggleButton()

        transport = QVBoxLayout()
        transport.addWidget(playButton)
        transport.addWidget(stopButton)
        transport.addWidget(loopButton)
        transport.addStretch(1)
        transport.addWidget(optionsButton)

        outerHBox = QHBoxLayout()
        outerVBox.addLayout(outerHBox)

        volumeSlider = QSlider()
        outerHBox.addWidget(volumeSlider)

        outerHBox.addLayout(transport)

        playButton.clicked.connect(self.playClicked)
        stopButton.clicked.connect(self.stopClicked)

        volumeSlider.valueChanged.connect(self.adjustVolume)
        volumeSlider.setValue(defaultVolume)

    def openFileDialog(self):
        dialog = QFileDialog()
        filename = dialog.getOpenFileName(self, 'Add new Sound', 'D:\\Musik\\RPG Ambient', 'Soundfile (*.wav *.mp3)')
        self.title.setText(filename[0])

        self.player.setSound(filename[0])

    def playClicked(self):
        self.player.play()

    def pauseClicked(self):
        self.player.pause()

    def stopClicked(self):
        self.player.stop()

    def adjustVolume(self, vol):
        self.player.setVolume(vol)

    def sizeHint(self):
        return QSize(100, 150)
