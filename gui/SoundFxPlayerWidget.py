from PyQt5.QtCore import *

from gui.Buttons import *

class SoundFxPlayerWidget(QWidget):
    def __init__(self, title: str):
        super().__init__()

        self.title = QLabel(title)
        self.title.setAlignment(Qt.AlignCenter)

        outerVBox = QVBoxLayout()
        self.setLayout(outerVBox)

        outerVBox.addWidget(self.title)
        playButton = PlayToggleButton()
        outerVBox.addWidget(playButton)
        hBox = QHBoxLayout()
        outerVBox.addLayout(hBox)
        hBox.addStretch()
        hBox.addWidget(OptionsButton())