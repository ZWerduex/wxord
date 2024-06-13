import PyQt6.QtCore as core
import PyQt6.QtWidgets as wid

import rsc

MAXIMUM_WEIGHT = 9999

class CharsetListItem(wid.QWidget):
    """Represents a entry in a charset, i.e. a line edit for the character and a spin box for its weight."""
    textEdited = core.pyqtSignal(object)
    editingFinished = core.pyqtSignal(object)

    def __init__(self, isLast: bool, char: str = None, weight: int = None) -> None: # type: ignore
        super().__init__()

        self.isLast = isLast
        
        char = char if char else ''
        weight = weight if weight and weight > 0 else 1
        
        self.charEntry = wid.QLineEdit(char)
        self.charEntry.textEdited.connect(lambda _: self.textEdited.emit(self))
        self.charEntry.editingFinished.connect(lambda: self.editingFinished.emit(self))
        
        self.weightEntry = wid.QSpinBox()
        self.weightEntry.setRange(1, MAXIMUM_WEIGHT)
        self.weightEntry.setValue(weight)
        self.weightEntry.setFixedWidth(
            self.weightEntry.fontMetrics().horizontalAdvance(str(MAXIMUM_WEIGHT)) + 25
        )

        layout = wid.QHBoxLayout()
        layout.setSpacing(rsc.Margins.CHARSETLIST)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.addWidget(self.charEntry)
        layout.addWidget(self.weightEntry)
        self.setLayout(layout)

    @property
    def char(self) -> str:
        return self.charEntry.text()
    
    @property
    def weight(self) -> int:
        value = self.weightEntry.value()
        return value if value > 0 else 1