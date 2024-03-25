import PyQt6.QtCore as core
import PyQt6.QtWidgets as wid

import logging
LOGGER = logging.getLogger(__name__)

from interface.WordListItem import WordListItem
from interface.DefaultScrollArea import DefaultScrollArea
import control as c
import rsc

class WordList(DefaultScrollArea):
    itemClicked = core.pyqtSignal(object)
    itemIconClicked = core.pyqtSignal(object)

    def __init__(self) -> None:
        super().__init__()
        
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

    def _itemClicked(self, item: WordListItem) -> None:
        for index in self.items:
            index.unselect()
        item.select()
        self.itemClicked.emit(item.word)

    def _itemIconClicked(self, item: WordListItem) -> None:
        item.icon.validate()
        self.itemIconClicked.emit(item)

    def populate(self, words: list[str]) -> None:
        # Remove all widgets from the layout
        for index in reversed(range(self.grid.count())):
            self.grid.itemAt(index).widget().setParent(None) # type: ignore

        nb = 1
        self.items = set()
        for word in words:
            
            index = wid.QLabel(str(nb))
            index.setFont(rsc.Fonts.LIST_INDEX)
            index.setStyleSheet(f'color: {rsc.Colors.LIGHT_GRAY}; background-color: transparent;')
            index.setContentsMargins(rsc.Margins.WORDLIST, rsc.Margins.WORDLIST, rsc.Margins.WORDLIST, rsc.Margins.WORDLIST)
            self.grid.addWidget(index, nb - 1, 0)

            item = WordListItem(word)
            self.items.add(item)

            item.labelClicked.connect(self._itemClicked)
            item.iconClicked.connect(self._itemIconClicked)
            self.grid.addWidget(item, nb - 1, 1)
            nb += 1

    def empty(self) -> None:
        self.populate(list())