import gettext
import sys

from PyQt5.QtWidgets import *
from PyQt5.QtGui import*
from PyQt5.QtCore import *

from gui.RPGABMainGUI import RPGABMainGUI

lang = 'en'


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
    main_window = RPGABMainGUI()
    sys.exit(app.exec_())
    # nothing will be executed from here


if __name__ == "__main__":
    main()

