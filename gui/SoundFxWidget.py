from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

from gui.TitleBarWidget import TitleBarWidget
from gui.MasterWidget import MasterWidget

from gui.SoundFxPlayerWidget import SoundFxPlayerWidget

class SoundFxWidget(QWidget):
    def __init__(self):
        super().__init__()

        outerVBox = QVBoxLayout()
        self.setLayout(outerVBox)
        outerVBox.addWidget(TitleBarWidget(_('Sound Effects')))

        hBox = QHBoxLayout()
        outerVBox.addLayout(hBox)
        self.FxList = QListWidget()
        hBox.addWidget(self.FxList)

        self.FxList.setFlow(QListView.LeftToRight)
        self.FxList.setResizeMode(QListView.Adjust)
        self.FxList.setWrapping(True)

        self.master = MasterWidget()
        hBox.addWidget(self.master)

        # TODO add by button
        for i in range(20):
            self.addSoundFx()

    def addSoundFx(self):
        playerWidget = SoundFxPlayerWidget('Sound FX')
        playerWidgetItem = QListWidgetItem(self.FxList)
        playerWidgetItem.setSizeHint(playerWidget.sizeHint())
        self.FxList.setItemWidget(playerWidgetItem, playerWidget)
