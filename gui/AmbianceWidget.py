from gui.buttons import *
from gui.TitleBarWidget import TitleBarWidget
from gui.MasterWidget import MasterWidget
from gui.AmbiancePlayerWidget import AmbiancePlayerWidget

class AmbianceWidget(QWidget):
    def __init__(self):
        super().__init__()

        outerVBox = QVBoxLayout()
        outerVBox.addWidget(TitleBarWidget(_('Ambiance')))
        hBox = QHBoxLayout()
        outerVBox.addLayout(hBox)

        soundBoxScroll = QScrollArea()

        hBox.addWidget(soundBoxScroll)

        self.soundHBox = QHBoxLayout()
        soundBox = QWidget()
        soundBox.setLayout(self.soundHBox)

        self.soundHBox.addWidget(AmbiancePlayerWidget())
        self.soundHBox.addWidget(AmbiancePlayerWidget())
        self.soundHBox.addWidget(AmbiancePlayerWidget())
        self.soundHBox.addWidget(AmbiancePlayerWidget())
        self.soundHBox.addWidget(AmbiancePlayerWidget())

        self.soundHBox.addStretch(1)
        soundBoxScroll.setWidget(soundBox)


        self.master = MasterWidget()
        hBox.addWidget(self.master)





        self.setLayout(outerVBox)