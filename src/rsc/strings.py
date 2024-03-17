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

    ENTER = os.path.join(Paths.IMG_DIR, 'enter.svg')
    VALID = os.path.join(Paths.IMG_DIR, 'valid.svg')

class Colors:

    WHITE = '#ffffff'
    LIGHT_GRAY = '#cccccc'
    GRAY = '#666666'
    DARK_GRAY = '#434952'

    METAL_BLUE = '#2A2F3D'
    DEEP_DARK_BLUE = '#131D37'
    DARK_BLUE = '#225a71'
    BLUE = '#3a93b7'

    DEFAULT_BACKGROUND = METAL_BLUE

    HEADER_BACKGROUND = DEEP_DARK_BLUE

    PATTERN_INPUT_BACKGROUND = DEFAULT_BACKGROUND
    PATTERN_INPUT_FOCUS = DARK_BLUE
    PATTERN_INPUT_HIGHLIGHT = BLUE

    LIST_ITEM_BACKGROUND = DEFAULT_BACKGROUND
    LIST_ITEM_BACKGROUND_HIGHLIGHT = BLUE
    LIST_ITEM_BACKGROUND_HOVER = DARK_BLUE

    WORD_LIST_BACKGROUND = LIST_ITEM_BACKGROUND
    WORD_LIST_SCROLLBAR_HANDLE = DARK_GRAY
    WORD_LIST_SCROLLBAR_BACKGROUND = LIGHT_GRAY

class Styles:

    SCROLLBAR = """
        QScrollBar {
            background: """ + Colors.WORD_LIST_SCROLLBAR_BACKGROUND + """;
        }
        QScrollBar::handle {
            background: """ + Colors.WORD_LIST_SCROLLBAR_HANDLE + """;
        }
        QScrollBar::add-line, QScrollBar::sub-line {
            height: 0px;
            background: none;
        }
        QScrollBar::add-page, QScrollBar::sub-page {
            background: none;
        }
    """

    PATTERN_INPUT = """
        QLineEdit {
            background: """ + Colors.PATTERN_INPUT_BACKGROUND + """;
            border: 3px solid """ + Colors.PATTERN_INPUT_BACKGROUND + """;
            border-radius: 22px;
            padding: 10px;

            color: """ + Colors.WHITE + """;
            letter-spacing: 2px;
            selection-background-color: """ + Colors.PATTERN_INPUT_HIGHLIGHT + """;
        }
        QLineEdit::hover {
            border: 3px solid """ + Colors.PATTERN_INPUT_FOCUS + """;
        }
        QLineEdit::focus {
            border: 3px solid """ + Colors.PATTERN_INPUT_HIGHLIGHT + """;
        }
    """

class Fonts:

    TITLE = gui.QFont('League Spartan', 36)
    AUTHOR = gui.QFont('League Spartan', 12)

    LIST_INDEX = gui.QFont('Montserrat', 8, gui.QFont.Weight.Light)

    BASE = gui.QFont('Montserrat', 12, gui.QFont.Weight.Normal)
    BOLD = gui.QFont('Montserrat', 12, gui.QFont.Weight.Bold)


for member in dir(Fonts):
    if not member.startswith('_'):
        getattr(Fonts, member).setHintingPreference(gui.QFont.HintingPreference.PreferNoHinting)