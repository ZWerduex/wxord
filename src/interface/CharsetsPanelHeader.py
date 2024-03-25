import PyQt6.QtCore as core
import PyQt6.QtWidgets as wid

import rsc

class CharsetsPanelHeader(wid.QWidget):
    patternSelected = core.pyqtSignal(object)

    def __init__(self, name: str, desc:str, suggested: list[str]) -> None:
        super().__init__()

        self.name = wid.QLabel(name)
        self.desc = wid.QLabel(desc)

        self.suggestedCombo = wid.QComboBox()
        self.suggestedCombo.addItems(suggested)
        self.suggestedCombo.currentTextChanged.connect(self.patternSelected.emit)

        left = wid.QVBoxLayout()
        left.setSpacing(0)
        left.setContentsMargins(0, 0, 0, 0)
        left.addWidget(self.name)
        left.addWidget(self.desc)

        right = wid.QVBoxLayout()
        right.setSpacing(0)
        right.setContentsMargins(0, 0, 0, 0)
        right.addWidget(self.suggestedCombo)

        layout = wid.QHBoxLayout()
        layout.setSpacing(0)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.addLayout(left)
        layout.addLayout(right)
        self.setLayout(layout)

        self.reloadTranslation()

    def update(self, name: str, desc: str, suggested: list[str]) -> None:
        self.name.setText(name)
        self.desc.setText(desc)
        self.suggestedCombo.clear()
        self.suggestedCombo.addItems(suggested)

    def reloadTranslation(self) -> None:
        self.suggestedCombo.setPlaceholderText(rsc.Translator.tr('SuggestedPatterns_placeholder'))