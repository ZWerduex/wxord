import PyQt6.QtWidgets as wid
import PyQt6.QtGui as gui
import PyQt6.QtCore as core

import rsc

class WordListItemLabel(wid.QLabel):
    clicked = core.pyqtSignal()

    def __init__(self, word: str) -> None:
        super().__init__(word)
        self.setStyleSheet(f'color: {rsc.Colors.WHITE};')
        self.setContentsMargins(10, 10, 10, 10)
        self.setCursor(gui.QCursor(core.Qt.CursorShape.PointingHandCursor))

    def mouseReleaseEvent(self, event: gui.QMouseEvent) -> None:
        self.clicked.emit()

class WordListClipboardIcon(wid.QLabel):
    clicked = core.pyqtSignal()

    def __init__(self) -> None:
        super().__init__()
        
        iconSize = 20
        self.valid = gui.QPixmap(rsc.Images.VALID).scaled(
            iconSize, iconSize,
            core.Qt.AspectRatioMode.KeepAspectRatio,
            core.Qt.TransformationMode.SmoothTransformation
        )
        self.clipboard = gui.QPixmap(rsc.Images.CLIPBOARD).scaled(
            iconSize, iconSize,
            core.Qt.AspectRatioMode.KeepAspectRatio,
            core.Qt.TransformationMode.SmoothTransformation
        )
        self.setPixmap(self.clipboard)

        self.setCursor(gui.QCursor(core.Qt.CursorShape.PointingHandCursor))

        self.setContentsMargins(10, 10, 10, 10)

    def validate(self) -> None:
        self.setPixmap(self.valid)
        core.QTimer.singleShot(5000, lambda : self.setPixmap(self.clipboard))

    def mouseReleaseEvent(self, event: gui.QMouseEvent) -> None:
        self.clicked.emit()

class WordListItem(wid.QWidget):
    clicked = core.pyqtSignal(object)
    copied = core.pyqtSignal(object)

    def __init__(self, word: str) -> None:
        super().__init__()

        self.label = WordListItemLabel(word)
        self.label.clicked.connect(lambda : self.clicked.emit(self))

        self.icon = WordListClipboardIcon()
        self.icon.clicked.connect(self.iconClicked)

        layout = wid.QHBoxLayout()
        layout.setSpacing(0)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.addWidget(self.label, 1)
        layout.addWidget(self.icon, 0)
        self.setLayout(layout)

        self.unselect()

    def iconClicked(self) -> None:
        self.icon.validate()
        self.copied.emit(self)

    def enterEvent(self, event: core.QEvent) -> None:
        if not self.selected:
            self.hover()

    def leaveEvent(self, event: core.QEvent) -> None:
        if not self.selected:
            self.unselect()
    
    def hover(self) -> None:
        if not self.selected:
            self.icon.setVisible(True)
            self.label.setFont(rsc.Fonts.BASE)
            self.setStyleSheet(f'background-color: {rsc.Colors.LIST_ITEM_BACKGROUND_HOVER};')

    def select(self) -> None:
        self.selected = True
        self.icon.setVisible(True)
        self.label.setFont(rsc.Fonts.BOLD)
        self.setStyleSheet(f'background-color: {rsc.Colors.LIST_ITEM_BACKGROUND_HIGHLIGHT};')

    def unselect(self) -> None:
        self.selected = False
        self.icon.setVisible(False)
        self.label.setFont(rsc.Fonts.BASE)
        self.setStyleSheet(f'background-color: {rsc.Colors.LIST_ITEM_BACKGROUND};')

    @property
    def word(self) -> str:
        return self.label.text()