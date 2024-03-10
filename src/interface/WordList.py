import PyQt6.QtCore as core
import PyQt6.QtWidgets as wid

import logging
LOGGER = logging.getLogger(__name__)

from interface.WordListItem import WordListItem
import control as c
import rsc


class WordList(wid.QScrollArea):
    wordClicked = core.pyqtSignal(object)
    wordCopied = core.pyqtSignal(object)

    def __init__(self, controller: c.MainController) -> None:
        super().__init__()
        # Widget properties
        self.setWidgetResizable(True)
        self.setVerticalScrollBarPolicy(core.Qt.ScrollBarPolicy.ScrollBarAsNeeded)
        self.setHorizontalScrollBarPolicy(core.Qt.ScrollBarPolicy.ScrollBarAsNeeded)
        self.setFrameStyle(wid.QFrame.Shape.NoFrame)
        self.setStyleSheet(f'background-color: {rsc.Colors.WORD_LIST_BACKGROUND};')
        # Scrollbar properties
        style = """
            QScrollBar {
                background: """ + rsc.Colors.WORD_LIST_SCROLLBAR_BACKGROUND + """;
            }
            QScrollBar::handle {
                background: """ + rsc.Colors.WORD_LIST_SCROLLBAR_HANDLE + """;
            }
            QScrollBar::add-line, QScrollBar::sub-line {
                height: 0px;
                background: none;
            }
            QScrollBar::add-page, QScrollBar::sub-page {
                background: none;
            }
            """
        self.verticalScrollBar().setStyleSheet(style) # type: ignore
        self.horizontalScrollBar().setStyleSheet(style) # type: ignore

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
        for index in self.items:
            index.unselect()
        item.select()
        self.wordClicked.emit(item.word)

    def populate(self, words: list[str]) -> None:
        # Remove all widgets from the layout
        for index in reversed(range(self.grid.count())):
            self.grid.itemAt(index).widget().setParent(None) # type: ignore
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
            item.copied.connect(lambda item: self.wordCopied.emit(item.word))
            self.grid.addWidget(item, nb - 1, 1)
            nb += 1

    def empty(self) -> None:
        self.populate(list())