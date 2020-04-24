import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QToolTip
from PyQt5.QtGui import QIcon, QFont, QKeyEvent
from PyQt5 import QtCore
from PyQt5.QtCore import Qt, QObject, pyqtSignal

class MyEvent(QObject):
    myEvent = pyqtSignal()



class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.init_me()

    def init_me(self):
        self.sig = MyEvent()
        self.sig.myEvent.connect(QtCore.QCoreApplication.instance().quit)
        QToolTip.setFont(QFont('Arial', 14))
        button = QPushButton('Drück mich!', self)
        button.setToolTip('Tooltiptext')
        button.clicked.connect(self.button_clicked)
        self.setGeometry(50, 50, 500, 500)
        self.setWindowTitle("RPG Ambience Board")
        self.setWindowIcon(QIcon('../icons/dragon_icon.png'))

        self.show()

    def button_clicked(self):
        print('button clicked')
        sender = self.sender()
        print(sender.text())
        self.sig.myEvent.emit()

    def keyPressEvent(self, key_event: QKeyEvent) -> None:
        if key_event.key() == Qt.Key_W:
            print('W')


app = QApplication(sys.argv)

main_window = Window()

sys.exit(app.exec_())
