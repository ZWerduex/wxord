import PyQt6.QtWidgets as wid

import typing

import rsc

class GenerateButton(wid.QPushButton):

    def __init__(self) -> None:
        super().__init__()
        self.reloadTranslation()

    def reloadTranslation(self) -> None:
        self.setText(rsc.Translator.tr('GenerateButton_text'))
