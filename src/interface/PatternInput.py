import PyQt6.QtWidgets as wid

import typing

import rsc

class PatternInput(wid.QLineEdit):

    def __init__(self) -> None:
        super().__init__()
        self.reloadTranslation()

    def reloadTranslation(self) -> None:
        self.setPlaceholderText(rsc.Translator.tr('PatternInput_placeholder'))