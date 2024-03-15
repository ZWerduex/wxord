import PyQt6.QtWidgets as wid

import logging
LOGGER = logging.getLogger(__name__)

import rsc

class SettingWidget(wid.QWidget):
    def __init__(self, translationKey: str, baseValue: int):
        super().__init__()
        self.translationKey = translationKey

        self.label = wid.QLabel(rsc.Translator.tr(translationKey))

        self.input = wid.QSpinBox()
        self.input.setMinimum(1)
        self.input.setMinimumWidth(80)
        if baseValue > 0:
            self.input.setValue(baseValue)
        else:
            LOGGER.warning(f"Base value for setting '{translationKey}' is not greater than 0")
        
        hbox = wid.QHBoxLayout()
        hbox.setSpacing(0)
        hbox.setContentsMargins(0, 0, 0, 0)
        hbox.addWidget(self.label)
        hbox.addWidget(self.input)
        self.setLayout(hbox)

    def reloadTranslation(self) -> None:
        self.label.setText(rsc.Translator.tr(self.translationKey))
        
    @property
    def value(self) -> int:
        return self.input.value()

class SettingsPanel(wid.QWidget):
    def __init__(self):
        super().__init__()

        self.maxLengthInput = SettingWidget('MaxLengthInput_label', 20)
        self.batchSizeInput = SettingWidget('BatchSizeInput_label', 20)
        
        hbox = wid.QHBoxLayout()
        hbox.setSpacing(0)
        hbox.setContentsMargins(0, 0, 0, 0)
        hbox.addStretch(1)
        hbox.addWidget(self.maxLengthInput)
        hbox.addStretch(1)
        hbox.addWidget(self.batchSizeInput)
        hbox.addStretch(1)
        self.setLayout(hbox)

    def reloadTranslation(self) -> None:
        self.maxLengthInput.reloadTranslation()
        self.batchSizeInput.reloadTranslation()

    @property
    def batchSize(self) -> int:
        return self.batchSizeInput.value
        
    @property
    def maxLength(self) -> int:
        return self.maxLengthInput.value