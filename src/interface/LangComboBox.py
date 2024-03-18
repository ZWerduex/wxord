import PyQt6.QtCore as core
import PyQt6.QtGui as gui
import PyQt6.QtWidgets as wid

import logging
LOGGER = logging.getLogger(__name__)

import rsc

class LangComboBox(wid.QComboBox):
    arrowClicked = core.pyqtSignal()
    langChanged = core.pyqtSignal(object, object)

    def __init__(self):
        super().__init__()
        self.setStyleSheet(rsc.Styles.COMBO_BOX)
        self.setFont(rsc.Fonts.SMALL)

        self.setEditable(False)
        
        self.activated.connect(
            lambda _: self.langChanged.emit(self.currentData(), self.currentText())
        )

    def mousePressEvent(self, event: gui.QMouseEvent):
        super().mousePressEvent(event)
        opt = wid.QStyleOptionComboBox()
        self.initStyleOption(opt)
        sc = self.style().hitTestComplexControl( # type: ignore
            wid.QStyle.ComplexControl.CC_ComboBox, opt, event.pos(), self
        ) 
        if sc == wid.QStyle.SubControl.SC_ComboBoxArrow:
            self.arrowClicked.emit()

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