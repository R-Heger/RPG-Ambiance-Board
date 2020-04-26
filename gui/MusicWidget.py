from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

from gui.Buttons import *
from gui.TitleBarWidget import TitleBarWidget
from gui.MasterWidget import MasterWidget


class MusicWidget(QWidget):
    def __init__(self):
        super().__init__()

        outerVBox = QVBoxLayout()
        titleBar = TitleBarWidget(_('Music'), False)

        outerVBox.addWidget(titleBar)
        playerBox = QHBoxLayout()
        outerVBox.addLayout(playerBox)

        playlistBox = QVBoxLayout()
        playerBox.addLayout(playlistBox)
        self.playlist = QListWidget()
        playlistBox.addWidget(self.playlist)

        buttonBox = QHBoxLayout()
        buttonBox.addWidget(AddButton())
        buttonBox.addWidget(DelButton())
        playlistBox.addLayout(buttonBox)

        playerControlBox = QHBoxLayout()
        playerBox.addLayout(playerControlBox)

        self.master = MasterWidget()
        playerControlBox.addWidget(self.master)

        transportButtonBox = QVBoxLayout()
        transportButtonBox.addWidget(PrevButton())
        transportButtonBox.addWidget(StopButton())
        transportButtonBox.addWidget(PlayToggleButton())
        transportButtonBox.addWidget(NextButton())
        transportButtonBox.addStretch(1)
        transportButtonBox.addWidget(RndToggleButton())
        transportButtonBox.addWidget(PlaylistLoopToggleButton())

        playerControlBox.addLayout(transportButtonBox)


        self.playlist.addItems(['Track_' + str(i) for i in range(30)])

        self.setLayout(outerVBox)



