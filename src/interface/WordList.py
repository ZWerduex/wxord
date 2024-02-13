import PyQt6.QtWidgets as wid
import PyQt6.QtCore as core

import logging
LOGGER = logging.getLogger(__name__)

import control as c
import rsc

class WordList(wid.QListWidget):
    onWordClicked = core.pyqtSignal(object)

    def __init__(self, controller: c.MainController) -> None:
        super().__init__()
        self.controller = controller
        self.itemClicked.connect(self.highlightWord)

    def highlightWord(self, item: wid.QListWidgetItem) -> None:
        for i in range(self.count()):
            self.item(i).setFont(rsc.Fonts.BASE) # type: ignore
        item.setFont(rsc.Fonts.BOLD)
        self.onWordClicked.emit(item.text())

    def populate(self, words: set[str]) -> None:
        self.addItems(words)
        for i in range(self.count()):
            self.item(i).setFont(rsc.Fonts.BASE) # type: ignore

    def empty(self) -> None:
        self.clear()