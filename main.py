import gettext
import sys
import compiled_resources

from PyQt5.QtWidgets import *
from PyQt5.QtGui import*
from PyQt5.QtCore import *

from gui.RPGABMainWindow import RPGABMainWindow

lang = 'en'
appStyle = 'gui/stylesheets/dark_blue/style.qss'


def main():
    print('RPG AMBIANCE BOARD is starting...')

    # set language
    if lang == 'en':
        en = gettext.translation('main', localedir='locales', languages=['en'])
        en.install()
        _ = gettext
    elif lang == 'de':
        de = gettext.translation('main', localedir='locales', languages=['de'])
        de.install()
        _ = de.gettext

    # start the GUI
    app = QApplication(sys.argv)
    main_window = RPGABMainWindow()
    with open(appStyle, 'r') as style:
        main_window.setStyleSheet(style.read())
    sys.exit(app.exec_())
    # nothing will be executed from here


if __name__ == "__main__":
    main()

