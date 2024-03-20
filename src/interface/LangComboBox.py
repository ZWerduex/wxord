import PyQt6.QtCore as core
import PyQt6.QtGui as gui
import PyQt6.QtWidgets as wid

import logging
LOGGER = logging.getLogger(__name__)

import rsc

class LangComboBox(wid.QComboBox):
    droppedDown = core.pyqtSignal()
    langChanged = core.pyqtSignal(object, object)

    def __init__(self):
        super().__init__()
        self.setStyleSheet(rsc.Styles.COMBO_BOX)
        self.setFont(rsc.Fonts.SMALL)
        self.setCursor(gui.QCursor(core.Qt.CursorShape.PointingHandCursor))
        self.view().setCursor(gui.QCursor(core.Qt.CursorShape.PointingHandCursor)) # type: ignore

        self.setEditable(False)
        
        self.activated.connect(
            lambda _: self.langChanged.emit(self.currentData(), self.currentText())
        )

    def showPopup(self) -> None:
        super().showPopup()
        self.droppedDown.emit()

    def setLang(self, lang: str) -> None:
        index = self.findData(lang)
        if index == -1:
            LOGGER.warning(f"Language '{lang}' not found in combo box")
            return
        self.setCurrentIndex(index)

    def populate(self, langs: dict[str, str]) -> None:
        self.clear()
        for lang, name in langs.items():
            self.addItem(name, lang)