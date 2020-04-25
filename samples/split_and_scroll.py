import gettext
import sys
import ctypes
from PyQt5.QtWidgets import *
from PyQt5.QtGui import*
from PyQt5.QtCore import *


class MainWindow(QTabWidget):
    def __init__(self):
        super().__init__()

        user32 = ctypes.windll.user32
        self.screenSize = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)
        self.windowScale = 0.5

        self.setWindowIcon(QIcon('../gui/icons/dragon_icon.png'))
        self.setWindowTitle("RPG Ambiance Board")

        windowSize = self.screenSize[0] * self.windowScale, self.screenSize[1] * self.windowScale
        windowPosition = (self.screenSize[0] - windowSize[0]) / 2, (self.screenSize[1] - windowSize[1]) / 2
        self.setGeometry(*windowPosition, *windowSize)

        self.tab1 = QWidget()
        self.tab2 = QWidget()
        self.init()

        self.show()

    def init(self):
        self.addTab(self.tab1, 'Tab A')
        self.addTab(self.tab2, 'Tab B')

        splitter = QSplitter(Qt.Horizontal)

        tabHorizontal = QHBoxLayout()
        tabHorizontal.addWidget(splitter)
        self.tab1.setLayout(tabHorizontal)

        filesList = QScrollArea()
        # filesList.setMinimumWidth(150)
        splitter.setSizes([200, 200])
        filesList.setWidgetResizable(True)
        splitter.addWidget(filesList)
        splitter.addWidget(QFrame())

        filesListContent = QWidget()
        filesListLayout = QVBoxLayout(filesListContent)

        for i in range(50):
            filesListLayout.addWidget(QLabel('very_long_file_' + str(i)))

        filesList.setWidget(filesListContent)


app = QApplication(sys.argv)
main_window = MainWindow()
sys.exit(app.exec_())