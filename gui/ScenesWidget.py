from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

from gui.TitleBarWidget import TitleBarWidget
from gui.Buttons import *

class ScenesWidget(QWidget):
    def __init__(self):
        super().__init__()

        sceneBox = QVBoxLayout()

        titleBar = TitleBarWidget(_('Scenes'), False)
        sceneBox.addWidget(titleBar)

        self.sceneList = QListWidget()
        sceneBox.addWidget(self.sceneList)

        buttonBox = QHBoxLayout()
        buttonBox.addWidget(AddButton())
        buttonBox.addWidget(DelButton())
        sceneBox.addLayout(buttonBox)

        for i in range(10):
            self.sceneList.addItem('Scene ' + str(i))

        font = QFont()
        font.setPointSize(20)
        self.sceneList.setFont(font)

        self.setLayout(sceneBox)

        self.sceneList.addItem('TEST!!!')
