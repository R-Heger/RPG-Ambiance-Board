import sys
from PyQt5.QtWidgets import QApplication, QWidget

app = QApplication(sys.argv)

main_window = QWidget()
main_window.setGeometry(50, 50, 500, 500)
main_window.setWindowTitle("RPG Ambience Board")

main_window.show()

sys.exit(app.exec_())
