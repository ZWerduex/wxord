import PyQt6.QtWidgets as wid

import rsc

class Footer(wid.QWidget):

    def __init__(self):
        super().__init__()
        self.setStyleSheet(f'background-color: {rsc.Colors.HEADER_BACKGROUND};')

        self.statusTitle = wid.QLabel(rsc.Translator.tr('Status'))
        self.statusTitle.setContentsMargins(10, 10, 10, 10)
        self.statusTitle.setFont(rsc.Fonts.BASE)
        self.statusTitle.setStyleSheet(f'color: {rsc.Colors.GRAY};')

        self.status = wid.QLabel()
        self.status.setContentsMargins(10, 10, 10, 10)
        self.status.setFont(rsc.Fonts.BASE)
        self.status.setStyleSheet(f'color: {rsc.Colors.WHITE};')
        self.clearStatus()
        
        layout = wid.QHBoxLayout()
        layout.setSpacing(0)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.addWidget(self.statusTitle)
        layout.addWidget(self.status, 1)
        self.setLayout(layout)

    def setStatus(self, msg: str) -> None:
        self.status.setText(msg)
    
    def clearStatus(self) -> None:
        self.status.setText('-')

    def reloadTranslation(self) -> None:
        self.statusTitle.setText(rsc.Translator.tr('Status'))
        self.clearStatus()