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
    DROP_DOWN = os.path.join(Paths.IMG_DIR, 'drop_down.svg')

class Colors:

    WHITE = '#ffffff'
    LIGHT_GRAY = '#a9a9b5'
    GRAY = '#666666'
    DARK_GRAY = '#434952'

    METAL_BLUE = '#2A2F3D'
    DEEP_DARK_BLUE = '#131D37'
    DARK_BLUE = '#225a71'
    BLUE = '#3a93b7'

    LIGHT_GREEN = '#1da73b'
    GREEN = '#1a7f2c'
    DARK_GREEN = '#0f5b1f'

    DEFAULT_BACKGROUND = METAL_BLUE
    DEFAULT_FONT = WHITE

    HEADER_BACKGROUND = DEEP_DARK_BLUE

    INPUT_BACKGROUND = DARK_GRAY
    INPUT_FOCUS = BLUE
    INPUT_HIGHLIGHT = DARK_BLUE

    GENERATE_BUTTON_BACKGROUND = DARK_GREEN
    GENERATE_BUTTON_HIGHLIGHT = GREEN
    GENERATE_BUTTON_FOCUS = LIGHT_GREEN

    LIST_ITEM_BACKGROUND = DEFAULT_BACKGROUND
    LIST_ITEM_BACKGROUND_HIGHLIGHT = BLUE
    LIST_ITEM_BACKGROUND_HOVER = DARK_BLUE

    SCROLLAREA_BACKGROUND = DEFAULT_BACKGROUND

    SCROLLBAR_HANDLE = DARK_GRAY
    SCROLLBAR_BACKGROUND = LIGHT_GRAY

class Styles:

    SCROLLBAR = """
        QScrollBar {
            background: """ + Colors.SCROLLBAR_BACKGROUND + """;
        }
        QScrollBar::handle {
            background: """ + Colors.SCROLLBAR_HANDLE + """;
        }
        QScrollBar::add-line, QScrollBar::sub-line {
            height: 0px;
            background: none;
        }
        QScrollBar::add-page, QScrollBar::sub-page {
            background: none;
        }
    """

    COMBO_BOX = """
        QComboBox {
            background: """ + Colors.INPUT_BACKGROUND + """;
            border: 2px solid """ + Colors.INPUT_BACKGROUND + """;
            padding-left: 7px;
            padding-right: 18px;
            padding-top: 5px;
            padding-bottom: 5px;

            color: """ + Colors.DEFAULT_FONT + """;
        }
        QComboBox::hover {
            border: 2px solid """ + Colors.INPUT_HIGHLIGHT + """;
        }
        QComboBox::focus, QComboBox::on {
            border: 2px solid """ + Colors.INPUT_FOCUS + """;
        }
        QComboBox::drop-down {
            border: 0px;
        }
        QComboBox::down-arrow {
            image: url(img/drop_down.svg);
            width: 10px;
            height: 10px;
            margin-right: 7px;
        }
        QComboBox QAbstractItemView {
            background: """ + Colors.INPUT_BACKGROUND + """;
            padding: 5px;
            padding-left: 6px;
            outline: 0px;
            
            color: """ + Colors.DEFAULT_FONT + """;
        }
        QComboBox QAbstractItemView::item:hover, QComboBox QAbstractItemView::item:focus {
            background: """ + Colors.LIST_ITEM_BACKGROUND_HIGHLIGHT + """;
        }
    """

    GENERATE_BUTTON = """
        QPushButton {
            background: """ + Colors.GENERATE_BUTTON_BACKGROUND + """;
            border-radius: 16px;
            padding: 6px;

            color: """ + Colors.DEFAULT_FONT + """;
            letter-spacing: 1px;
        }
        QPushButton::hover {
            border: 3px solid """ + Colors.GENERATE_BUTTON_HIGHLIGHT + """;
        }
        QPushButton::focus {
            border: 3px solid """ + Colors.GENERATE_BUTTON_FOCUS + """;
        }
        QPushButton::pressed {
            background: """ + Colors.GENERATE_BUTTON_FOCUS + """;
        }
    """

    PATTERN_INPUT = """
        QLineEdit {
            background: """ + Colors.INPUT_BACKGROUND + """;
            border: 3px solid """ + Colors.INPUT_BACKGROUND + """;
            border-radius: 22px;
            padding: 10px;

            color: """ + Colors.DEFAULT_FONT + """;
            letter-spacing: 2px;
            selection-background-color: """ + Colors.INPUT_FOCUS + """;
        }
        QLineEdit::hover {
            border: 3px solid """ + Colors.INPUT_HIGHLIGHT + """;
        }
        QLineEdit::focus {
            border: 3px solid """ + Colors.INPUT_FOCUS + """;
        }
    """

    SCROLLAREA = """
        QScrollArea {
            background: """ + Colors.SCROLLAREA_BACKGROUND + """;
        }            
    """

    LEFT_PANEL = """
        QWidget {
            background: """ + Colors.DEFAULT_BACKGROUND + """;
        }
    """

class Margins:

    BASE = 10
    WORDLIST = 5

class Fonts:

    TITLE = gui.QFont('League Spartan', 36)
    AUTHOR = gui.QFont('League Spartan', 12)

    LIST_INDEX = gui.QFont('Montserrat', 7, gui.QFont.Weight.Light)
    SETTING = gui.QFont('Montserrat', 9)

    BASE = gui.QFont('Montserrat', 12, gui.QFont.Weight.Normal)
    BOLD = gui.QFont('Montserrat', 12, gui.QFont.Weight.Bold)
    SMALL = gui.QFont('Montserrat', 10, gui.QFont.Weight.Normal)


for member in dir(Fonts):
    if not member.startswith('_'):
        getattr(Fonts, member).setHintingPreference(gui.QFont.HintingPreference.PreferNoHinting)