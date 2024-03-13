import PyQt6.QtGui as gui

import os

class Strings:

    APPLICATION_NAME = 'Wxord'
    APPLICATION_AUTHOR = 'Z-WX'

class Paths:

    ROOT = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
    CHARSETS_DIR = os.path.join(ROOT, 'charsets')
    FONTS_DIR = os.path.join(ROOT, 'fonts')
    IMG_DIR = os.path.join(ROOT, 'img')
    LANG_DIR = os.path.join(ROOT, 'lang')

    LOG_FILE = os.path.join(ROOT, Strings.APPLICATION_NAME.lower() + '.log')

class Images:

    ENTER = os.path.join(Paths.IMG_DIR, 'enter.png')
    VALID = os.path.join(Paths.IMG_DIR, 'valid.png')

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
    WORD_LIST_SCROLLBAR_BACKGROUND = LIGHT_GRAY

class Fonts:

    TITLE = gui.QFont('League Spartan', 36)
    AUTHOR = gui.QFont('League Spartan', 12)

    LIST_INDEX = gui.QFont('Montserrat', 8, gui.QFont.Weight.Light)

    BASE = gui.QFont('Montserrat', 12, gui.QFont.Weight.Normal)
    BOLD = gui.QFont('Montserrat', 12, gui.QFont.Weight.Bold)


for member in dir(Fonts):
    if not member.startswith('_'):
        getattr(Fonts, member).setHintingPreference(gui.QFont.HintingPreference.PreferNoHinting)