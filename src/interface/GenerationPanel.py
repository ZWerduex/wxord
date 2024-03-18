import PyQt6.QtCore as core
import PyQt6.QtWidgets as wid

from interface.SettingsPanel import SettingsPanel
import rsc

class GenerateButton(wid.QPushButton):

    def __init__(self) -> None:
        super().__init__()
        self.reloadTranslation()

    def reloadTranslation(self) -> None:
        self.setText(rsc.Translator.tr('GenerateButton_text'))

class PatternInput(wid.QLineEdit):

    def __init__(self) -> None:
        super().__init__()

        self.setStyleSheet(rsc.Styles.PATTERN_INPUT)
        self.setFont(rsc.Fonts.BASE)

        self.reloadTranslation()

    def reloadTranslation(self) -> None:
        self.setPlaceholderText(rsc.Translator.tr('PatternInput_placeholder'))

class GenerationPanel(wid.QWidget):
    # Arg order : pattern, maxLength, batchSize
    generated = core.pyqtSignal(object, object, object)
    patternEdited = core.pyqtSignal(object)

    def __init__(self) -> None:
        super().__init__()
        callback = lambda : self.generated.emit(
            self.patternInput.text(), self.settingsPanel.maxLength, self.settingsPanel.batchSize
        )

        self.patternInput = PatternInput()
        self.generateButton = GenerateButton()
        self.generateButton.clicked.connect(callback)
        self.patternInput.returnPressed.connect(callback)
        self.patternInput.textEdited.connect(self.patternEdited.emit)

        self.settingsPanel = SettingsPanel()

        hbox = wid.QVBoxLayout()
        hbox.setSpacing(rsc.Margins.BASE)
        hbox.setContentsMargins(0, 0, 0, 0)
        hbox.addWidget(self.patternInput)
        hbox.addWidget(self.settingsPanel)
        hbox.addWidget(self.generateButton)
        self.setLayout(hbox)

    def reloadTranslation(self) -> None:
        self.generateButton.reloadTranslation()
        self.patternInput.reloadTranslation()
        self.settingsPanel.reloadTranslation()

    def setPattern(self, pattern: str) -> None:
        self.patternInput.setText(pattern)