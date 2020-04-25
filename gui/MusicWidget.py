from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

from gui.buttons import *


class MusicWidget(QWidget):
    def __init__(self):
        super().__init__()

        outerVBox = QVBoxLayout()
        titleBar = QHBoxLayout()
        titleBar.addWidget(QLabel(_('Music')))
        titleBar.addStretch(1)
        titleBar.addWidget(OptionsButton())

        outerVBox.addLayout(titleBar)
        playerBox = QHBoxLayout()
        outerVBox.addLayout(playerBox)

        playlistBox = QVBoxLayout()
        playerBox.addLayout(playlistBox)
        playlistScroll = QScrollArea()
        playlistBox.addWidget(playlistScroll)

        buttonBox = QHBoxLayout()
        buttonBox.addWidget(AddButton())
        buttonBox.addWidget(DelButton())
        playlistBox.addLayout(buttonBox)

        playerControlBox = QVBoxLayout()
        playerBox.addLayout(playerControlBox)
        sliderBox = QHBoxLayout()
        playerControlBox.addLayout(sliderBox)
        self.musicVolumeSlider = QSlider()
        sliderBox.addStretch(1)
        sliderBox.addWidget(self.musicVolumeSlider)
        sliderBox.addStretch(1)


        transportBox1 = QHBoxLayout()
        playerControlBox.addLayout(transportBox1)
        transportBox2 = QHBoxLayout()
        playerControlBox.addLayout(transportBox2)
        transportBox2.addWidget(PrevButton())
        transportBox1.addWidget(StopButton())
        transportBox1.addWidget(PlayToggleButton())
        transportBox2.addWidget(NextButton())



        rndBox = QHBoxLayout()
        playerControlBox.addLayout(rndBox)
        rndBox.addWidget(RndToggleButton())
        rndBox.addWidget(LoopToggleButton())

        self.setLayout(outerVBox)



