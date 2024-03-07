import PyQt6.QtGui as gui

import os

class Strings:

    APPLICATION_NAME = 'Wxord'
    APPLICATION_AUTHOR = 'Z-WX'

class Paths:

    ROOT = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
    LANG_DIR = os.path.join(ROOT, 'lang')
    CHARSETS_DIR = os.path.join(ROOT, 'charsets')
    FONTS_DIR = os.path.join(ROOT, 'fonts')

    LOG_FILE = os.path.join(ROOT, Strings.APPLICATION_NAME.lower() + '.log')

class Colors:

    WHITE = '#ffffff'
    LIGHT_GRAY = '#cccccc'
    GRAY = '#666666'

    HEADER_BACKGROUND = '#131D37'

    LIST_ITEM_BACKGROUND = '#2A2F3D'
    LIST_ITEM_BACKGROUND_HIGHLIGHT = '#3a93b7'
    LIST_ITEM_BACKGROUND_HOVER = '#225a71'
    WORD_LIST_BACKGROUND = LIST_ITEM_BACKGROUND
    WORD_LIST_SCROLLBAR_HANDLE = '#434952'
    WORD_LIST_SCROLLBAR_BACKGROUND = WHITE

class Fonts:

    TITLE = gui.QFont('League Spartan', 36, gui.QFont.Weight.Normal)
    AUTHOR = gui.QFont('League Spartan', 12, gui.QFont.Weight.Light)

    LIST_INDEX = gui.QFont('Arial', 8, gui.QFont.Weight.Light)

    BASE = gui.QFont('Arial', 12)
    BOLD = gui.QFont('Arial', 12, gui.QFont.Weight.Bold)
