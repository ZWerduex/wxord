import PyQt6.QtGui as gui

import os

class Strings:

    APPLICATION_NAME = 'Wxord'

class Paths:

    ROOT = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
    LANG_DIR = os.path.join(ROOT, 'lang')
    CHARSETS_DIR = os.path.join(ROOT, 'charsets')

    LOG_FILE = os.path.join(ROOT, Strings.APPLICATION_NAME.lower() + '.log')

class Colors:

    WHITE = '#ffffff'
    LIGHT_GRAY = '#cccccc'

    LIST_ITEM_BACKGROUND_EVEN = '#113799'
    LIST_ITEM_BACKGROUND_ODD = '#152D6C'
    LIST_ITEM_BACKGROUND_HIGHLIGHT = '#6c13e0'
    WORD_LIST_BACKGROUND = LIST_ITEM_BACKGROUND_EVEN
    WORD_LIST_SCROLLBAR_HANDLE = '#686fa1'
    WORD_LIST_SCROLLBAR_BACKGROUND = '#ffffff'

class Fonts:

    LIST_INDEX = gui.QFont('Arial', 8, gui.QFont.Weight.Light)

    BASE = gui.QFont('Arial', 12)
    BOLD = gui.QFont('Arial', 12, gui.QFont.Weight.Bold)
