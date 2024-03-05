import PyQt6.QtWidgets as wid

import typing

import rsc

class GenerateButton(wid.QPushButton):

    def __init__(self, onGenerate: typing.Callable[[], None]) -> None:
        super().__init__('Generate')
        self.clicked.connect(onGenerate)
        self.reloadTranslation()

    def reloadTranslation(self) -> None:
        self.setText(rsc.Translator.tr('GenerateButton_text'))
