from PyQt5.QtWidgets import *
from PyQt5.QtGui import*
from PyQt5.QtCore import *

from gui.ScenesWidget import ScenesWidget
from gui.SoundFxWidget import SoundFxWidget
from gui.MusicWidget import MusicWidget
from gui.AmbianceWidget import AmbianceWidget


class SoundBoardWidget(QSplitter):
    def __init__(self):
        super().__init__()

        self.setOrientation(Qt.Horizontal)

        scenes = ScenesWidget()
        self.addWidget(scenes)

        outerVSplitter = QSplitter(Qt.Vertical)
        self.addWidget(outerVSplitter)
        self.setSizes([100, 1000])

        soundFx = SoundFxWidget()
        mixerSplitter = QSplitter(Qt.Horizontal)
        outerVSplitter.addWidget(soundFx)
        outerVSplitter.addWidget(mixerSplitter)
        outerVSplitter.setSizes([2, 1])

        music = MusicWidget()
        ambiance = AmbianceWidget()
        mixerSplitter.addWidget(music)
        mixerSplitter.addWidget(ambiance)
        mixerSplitter.setSizes([150, 1200])

