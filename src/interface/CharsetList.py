import PyQt6.QtCore as core
import PyQt6.QtWidgets as wid

import logging
LOGGER = logging.getLogger(__name__)

from interface.DefaultScrollArea import DefaultScrollArea
import rsc

MAXIMUM_WEIGHT = 9999

class CharsetListItem(wid.QWidget):
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
        return self.weightEntry.value()


class CharsetList(DefaultScrollArea):

    def __init__(self, charset: dict[str, int]) -> None:
        super().__init__()

        self.orderByCharButton = wid.QPushButton(rsc.Translator.tr('OrderByCharButton_text'))
        self.orderByCharButton.clicked.connect(lambda: self.orderBy('char'))
        
        self.orderByWeightButton = wid.QPushButton(rsc.Translator.tr('OrderByWeightButton_text'))
        self.orderByWeightButton.clicked.connect(lambda: self.orderBy('weight'))
        
        self.list = wid.QVBoxLayout()
        self.list.setSpacing(rsc.Margins.CHARSETLIST)
        self.list.setContentsMargins(rsc.Margins.CHARSETLIST, rsc.Margins.CHARSETLIST, rsc.Margins.CHARSETLIST, rsc.Margins.CHARSETLIST)

        headerSection = wid.QHBoxLayout()
        headerSection.setSpacing(rsc.Margins.CHARSETLIST)
        headerSection.setContentsMargins(0, 0, 0, 0)
        headerSection.addWidget(self.orderByCharButton)
        headerSection.addStretch(1)
        headerSection.addWidget(self.orderByWeightButton)
        
        layout = wid.QVBoxLayout()
        layout.setSpacing(0)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.addLayout(headerSection)
        layout.addLayout(self.list)
        layout.addStretch(1)

        container = wid.QWidget()
        container.setLayout(layout)
        self.setWidget(container)

        self.populate(charset)

    @property
    def charset(self) -> dict[str, int]:
        return {item.char: item.weight for item in self.items if not item.isLast and item.char != ''}

    def itemEdited(self, item: CharsetListItem) -> None:
        # Last item, the blank one, is being edited
        if item.isLast and item.char != '':
            item.isLast = False
            # Add a new blank item
            blank = CharsetListItem(True)
            blank.textEdited.connect(self.itemEdited)
            blank.editingFinished.connect(self.editingFinished)
            self.items.append(blank)
            self.list.addWidget(blank)
    
    def editingFinished(self, item: CharsetListItem) -> None:
        if not item.isLast and item.char == '':
            self.items.remove(item)
            self.list.removeWidget(item)
            item.setParent(None)

    def populate(self, charset: dict[str, int]) -> None:
        # Remove all widgets from the layout
        for index in reversed(range(self.list.count())):
            self.list.itemAt(index).widget().setParent(None) # type: ignore

        self.items = []
        for char, weight in charset.items():
            item = CharsetListItem(False, char, weight)
            item.textEdited.connect(self.itemEdited)
            item.editingFinished.connect(self.editingFinished)
            self.items.append(item)
            self.list.addWidget(item)

        blank = CharsetListItem(True)
        blank.textEdited.connect(self.itemEdited)
        blank.editingFinished.connect(self.editingFinished)
        self.items.append(blank)
        self.list.addWidget(blank)

    def orderBy(self, mode: str) -> None:
        LOGGER.debug(f"Ordering charset by '{mode}'")
        
        if mode not in ['char', 'weight']:
            raise ValueError(f"Invalid mode '{mode}', mode must be 'char' or 'weight'")
        blank = self.items.pop()
        self.items = sorted(
                self.items,
                key = lambda item: getattr(item, mode),
                reverse = mode == 'weight'
            )
        self.items.append(blank)

        for item in self.items:
            self.list.removeWidget(item)
            self.list.addWidget(item)

    def clear(self) -> None:
        self.populate(dict())

    def reloadTranslation(self) -> None:
        self.orderByCharButton.setText(rsc.Translator.tr('OrderByCharButton_text'))
        self.orderByWeightButton.setText(rsc.Translator.tr('OrderByWeightButton_text'))