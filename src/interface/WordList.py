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

    def mouseReleaseEvent(self, event: core.QEvent) -> None:
        self.clicked.emit(self)


class WordList(wid.QWidget):
    wordClicked = core.pyqtSignal(object)

    def __init__(self, controller: c.MainController) -> None:
        super().__init__()
        self.controller = controller
        self.items = set()

        self.grid = wid.QGridLayout()
        self.grid.setColumnStretch(1, 1)
        vbox = wid.QVBoxLayout()
        vbox.addLayout(self.grid)
        vbox.addStretch(1)
        self.setLayout(vbox)

    def highlightWord(self, item: WordListItem) -> None:
        for i in self.items:
            i.setFont(rsc.Fonts.BASE) # type: ignore
        item.setFont(rsc.Fonts.BOLD)
        self.wordClicked.emit(item.text())

    def populate(self, words: set[str]) -> None:
        # Remove all widgets from the layout
        for i in reversed(range(self.grid.count())):
            self.grid.itemAt(i).widget().setParent(None) # type: ignore
        self.items = set()

        nb = 1
        for word in words:
            item = WordListItem(word)

            index = wid.QLabel(str(nb))
            index.setFont(rsc.Fonts.LIST_INDEX)
            index.setStyleSheet(f'color: {rsc.Colors.LIST_INDEX}')
            self.grid.addWidget(index, nb - 1, 0)

            self.items.add(item)
            item.clicked.connect(self.highlightWord)
            item.setFont(rsc.Fonts.BASE)
            self.grid.addWidget(item, nb - 1, 1)
            nb += 1

    def empty(self) -> None:
        self.populate(set())