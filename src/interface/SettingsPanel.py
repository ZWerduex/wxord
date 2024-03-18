import PyQt6.QtCore as core
import PyQt6.QtGui as gui
import PyQt6.QtWidgets as wid

import logging
LOGGER = logging.getLogger(__name__)

import rsc

MAXIMUM_INPUT = 100

class SettingWidgetLabel(wid.QLabel):
    clicked = core.pyqtSignal()

    def __init__(self, translationKey: str):
        super().__init__(rsc.Translator.tr(translationKey))
        self.setFont(rsc.Fonts.SETTING)

        self.translationKey = translationKey

    def reloadTranslation(self) -> None:
        self.setText(rsc.Translator.tr(self.translationKey))

    def mouseReleaseEvent(self, ev: gui.QMouseEvent | None) -> None:
        self.clicked.emit()

class SettingWidget(wid.QWidget):
    def __init__(self, translationKey: str, baseValue: int):
        super().__init__()

        self.input = wid.QSpinBox()
        self.input.setFont(rsc.Fonts.SETTING)
        self.input.setFixedWidth(self.fontMetrics().horizontalAdvance(str(MAXIMUM_INPUT)) + 30)
        self.input.setMinimum(1)
        self.input.setMaximum(MAXIMUM_INPUT)
        if baseValue > 0:
            self.input.setValue(baseValue)
        else:
            LOGGER.warning(f"Base value for setting '{translationKey}' is not greater than 0")

        self.label = SettingWidgetLabel(translationKey)
        self.label.clicked.connect(self.input.setFocus)
        
        hbox = wid.QHBoxLayout()
        hbox.setSpacing(rsc.Margins.BASE)
        hbox.setContentsMargins(0, 0, 0, 0)
        hbox.addWidget(self.label)
        hbox.addWidget(self.input)
        self.setLayout(hbox)

    def reloadTranslation(self) -> None:
        self.label.reloadTranslation()
        
    @property
    def value(self) -> int:
        return self.input.value()

class SettingsPanel(wid.QWidget):
    def __init__(self):
        super().__init__()

        self.maxLengthInput = SettingWidget('MaxLengthInput_label', 20)
        self.batchSizeInput = SettingWidget('BatchSizeInput_label', 20)
        
        hbox = wid.QHBoxLayout()
        hbox.setSpacing(rsc.Margins.BASE)
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