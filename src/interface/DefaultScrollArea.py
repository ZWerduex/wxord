import PyQt6.QtCore as core
import PyQt6.QtWidgets as wid

import rsc

class DefaultScrollArea(wid.QScrollArea):

    def __init__(self) -> None:
        super().__init__()
        
        # Widget properties
        self.setWidgetResizable(True)
        self.setVerticalScrollBarPolicy(core.Qt.ScrollBarPolicy.ScrollBarAsNeeded)
        self.setHorizontalScrollBarPolicy(core.Qt.ScrollBarPolicy.ScrollBarAsNeeded)
        self.setFrameStyle(wid.QFrame.Shape.NoFrame)
        self.setStyleSheet(rsc.Styles.SCROLLAREA)
        # Scrollbar properties
        self.verticalScrollBar().setStyleSheet(rsc.Styles.SCROLLBAR) # type: ignore
        self.verticalScrollBar().setCursor(core.Qt.CursorShape.PointingHandCursor) # type: ignore
        self.horizontalScrollBar().setStyleSheet(rsc.Styles.SCROLLBAR) # type: ignore
        self.horizontalScrollBar().setCursor(core.Qt.CursorShape.PointingHandCursor) # type: ignore