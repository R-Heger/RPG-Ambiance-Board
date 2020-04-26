from gui.Buttons import *
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

        self.soundBoxList = QListWidget(self)
        hBox.addWidget(self.soundBoxList)
        self.soundBoxList.setFlow(QListView.LeftToRight)
        self.soundBoxList.setStyleSheet('background:transparent')

        self.master = MasterWidget()
        hBox.addWidget(self.master)

        self.setLayout(outerVBox)

        # TODO triggered by button
        self.addAmbianceSound()
        self.addAmbianceSound()
        self.addAmbianceSound()
        self.addAmbianceSound()
        self.addAmbianceSound()
        self.addAmbianceSound()
        self.addAmbianceSound()
        self.addAmbianceSound()
        self.addAmbianceSound()

    def addAmbianceSound(self):
        playerWidget = AmbiancePlayerWidget('Ambiance Sound')
        playerWidgetItem = QListWidgetItem(self.soundBoxList)
        playerWidgetItem.setSizeHint(playerWidget.sizeHint())
        self.soundBoxList.setItemWidget(playerWidgetItem, playerWidget)
