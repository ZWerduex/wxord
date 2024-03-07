import PyQt6.QtWidgets as wid
import PyQt6.QtGui as gui

import rsc

class Footer(wid.QWidget):

    def __init__(self):
        super().__init__()
        self.setStyleSheet(f'background-color: {rsc.Colors.HEADER_BACKGROUND};')

        statusTitle = wid.QLabel(rsc.Translator.tr('Status_Title'))
        statusTitle.setContentsMargins(10, 10, 10, 10)
        statusTitle.setFont(rsc.Fonts.BASE)
        statusTitle.setStyleSheet(f'color: {rsc.Colors.GRAY};')

        self.status = wid.QLabel()
        self.status.setContentsMargins(10, 10, 10, 10)
        self.status.setFont(rsc.Fonts.BASE)
        self.status.setStyleSheet(f'color: {rsc.Colors.WHITE};')
        
        layout = wid.QHBoxLayout()
        layout.setSpacing(0)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.addWidget(statusTitle)
        layout.addWidget(self.status, 1)
        self.setLayout(layout)

    def setStatus(self, msg: str) -> None:
        self.status.setText(msg)
    
    def clearStatus(self) -> None:
        self.status.setText('')