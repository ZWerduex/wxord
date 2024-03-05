import PyQt6.QtWidgets as wid

import typing

import rsc

class PatternInput(wid.QLineEdit):

    def __init__(self, onGenerate: typing.Callable[[], None]) -> None:
        super().__init__()
        self.returnPressed.connect(onGenerate)
        self.reloadTranslation()

    def reloadTranslation(self) -> None:
        self.setPlaceholderText(rsc.Translator.tr('PatternInput_placeholder'))