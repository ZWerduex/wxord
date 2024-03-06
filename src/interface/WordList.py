import PyQt6.QtCore as core
import PyQt6.QtGui as gui
import PyQt6.QtWidgets as wid

import logging
LOGGER = logging.getLogger(__name__)

import control as c
import rsc

class WordListItem(wid.QLabel):
    clicked = core.pyqtSignal(object)

    def __init__(self, word: str) -> None:
        super().__init__(word)
        self.unselect()

    def select(self) -> None:
        self.setFont(rsc.Fonts.BOLD)
        self.setStyleSheet(f'color: {rsc.Colors.WHITE}; background-color: {rsc.Colors.LIST_ITEM_BACKGROUND_HIGHLIGHT};')

    def unselect(self) -> None:
        self.setFont(rsc.Fonts.BASE)
        self.setStyleSheet(f'color: {rsc.Colors.WHITE}; background-color: transparent;')

    def mouseReleaseEvent(self, event: core.QEvent) -> None:
        self.clicked.emit(self)


class WordList(wid.QScrollArea):
    wordClicked = core.pyqtSignal(object)

    def __init__(self, controller: c.MainController) -> None:
        super().__init__()
        # Widget properties
        self.setWidgetResizable(True)
        self.setVerticalScrollBarPolicy(core.Qt.ScrollBarPolicy.ScrollBarAsNeeded)
        self.setHorizontalScrollBarPolicy(core.Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.setFrameStyle(wid.QFrame.Shape.NoFrame)
        self.setStyleSheet(f'background-color: {rsc.Colors.WORD_LIST_BACKGROUND};')
        # Scrollbar properties
        scrollbar: wid.QScrollBar = self.verticalScrollBar() # type: ignore
        scrollbar.setStyleSheet(
            """
            QScrollBar:vertical {
                background: """ + rsc.Colors.WORD_LIST_SCROLLBAR_BACKGROUND + """;
            }
            QScrollBar::handle:vertical {
                background: """ + rsc.Colors.WORD_LIST_SCROLLBAR_HANDLE + """;
            }
            QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {
                height: 0px;
                background: none;
            }
            QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {
                background: none;
            }
            """
        )

        self.controller = controller
        self.items = set()

        self.grid = wid.QGridLayout()
        self.grid.setSpacing(0)
        self.grid.setContentsMargins(0, 0, 0, 0)
        self.grid.setColumnStretch(1, 1)

        vbox = wid.QVBoxLayout()
        vbox.setSpacing(0)
        vbox.setContentsMargins(0, 0, 0, 0)
        vbox.addLayout(self.grid)
        vbox.addStretch(1)

        container = wid.QWidget()
        container.setLayout(vbox)
        self.setWidget(container)

    def highlightWord(self, item: WordListItem) -> None:
        for i in self.items:
            i.unselect()
        item.select()
        self.wordClicked.emit(item.text())

    def populate(self, words: list[str]) -> None:
        # Remove all widgets from the layout
        for i in reversed(range(self.grid.count())):
            self.grid.itemAt(i).widget().setParent(None) # type: ignore
        self.items = set()

        nb = 1
        for word in words:
            
            index = wid.QLabel(str(nb))
            index.setFont(rsc.Fonts.LIST_INDEX)
            index.setStyleSheet(f'color: {rsc.Colors.LIGHT_GRAY}; background-color: transparent;')
            index.setContentsMargins(10, 10, 10, 10)
            self.grid.addWidget(index, nb - 1, 0)

            item = WordListItem(word)
            self.items.add(item)

            item.clicked.connect(self.highlightWord)
            item.setContentsMargins(10, 10, 10, 10)
            self.grid.addWidget(item, nb - 1, 1)
            nb += 1

    def empty(self) -> None:
        self.populate(list())