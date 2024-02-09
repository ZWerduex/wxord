import PyQt6.QtWidgets as wid

import logging
LOGGER = logging.getLogger(__name__)

import control as c
import rsc

class WordList(wid.QListWidget):
    def __init__(self, controller: c.MainController) -> None:
        super().__init__()
        self.controller = controller
        self.itemClicked.connect(self.onWordClicked)

    def onWordClicked(self, item: wid.QListWidgetItem) -> None:
        for i in range(self.count()):
            self.item(i).setFont(rsc.Fonts.BASE) # type: ignore
        item.setFont(rsc.Fonts.BOLD)
        self.controller.onWordClicked(item.text())

    def populate(self, words: list[str]) -> None:
        for i in range(self.count()):
            self.item(i).setFont(rsc.Fonts.BASE) # type: ignore
        self.addItems(words)

    def empty(self) -> None:
        self.clear()