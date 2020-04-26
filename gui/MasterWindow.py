from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

from gui.MasterWidget import MasterWidget


class MasterWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.master = MasterWidget()
        self.setCentralWidget(self.master)
        self.setFixedSize(50, 200)
        self.setWindowFlags(Qt.FramelessWindowHint)

        closeMaster = QPushButton('x')
        closeMaster.clicked.connect(self.close)
        masterMenubar = self.menuBar()
        masterMenubar.setCornerWidget(closeMaster, Qt.TopRightCorner)

    def showMe(self):
        self.move(QCursor.pos() - QPoint(int(self.width() / 2), 0))
        self.show()
