import PyQt6.QtGui as gui

import os

class Strings:

    APPLICATION_NAME = 'Wxord'

class Paths:

    ROOT = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
    LANG_DIR = os.path.join(ROOT, 'lang')
    CHARSETS_DIR = os.path.join(ROOT, 'charsets')

    LOG_FILE = os.path.join(ROOT, Strings.APPLICATION_NAME.lower() + '.log')

class Fonts:

    BASE = gui.QFont('Arial', 12)
    BOLD = gui.QFont('Arial', 12, gui.QFont.Weight.Bold)
