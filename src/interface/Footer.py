import PyQt6.QtWidgets as wid
import PyQt6.QtGui as gui

import rsc

class Footer(wid.QWidget):
    def __init__(self):
        super().__init__()
        self.setStyleSheet(f'background-color: {rsc.Colors.HEADER_BACKGROUND};')
        self.setFixedHeight(30)
        
    def paintEvent(self, event: gui.QPaintEvent) -> None:
        painter = gui.QPainter(self)
        painter.setPen(gui.QColor(rsc.Colors.LIGHT_GRAY))
        painter.drawLine(0, 0, self.width(), 0)
        painter.end()