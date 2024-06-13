import PyQt6.QtCore as core
import PyQt6.QtWidgets as wid

import logging
LOGGER = logging.getLogger(__name__)

from interface.CharsetListItem import CharsetListItem
from interface.DefaultScrollArea import DefaultScrollArea
import rsc

class CharsetList(DefaultScrollArea):
    """Lists every character of a charset, with its weight. The last item is a blank one, to add new characters. Includes a header."""

    def __init__(self, charset: dict[str, int]) -> None:
        super().__init__()
        
        self.list = wid.QVBoxLayout()
        self.list.setSpacing(rsc.Margins.CHARSETLIST)
        self.list.setContentsMargins(rsc.Margins.CHARSETLIST, rsc.Margins.CHARSETLIST, rsc.Margins.CHARSETLIST, rsc.Margins.CHARSETLIST)
        
        layout = wid.QVBoxLayout()
        layout.setSpacing(0)
        layout.setContentsMargins(0, 0, 0, 0)
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
            # Add a new blank item at the last position
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