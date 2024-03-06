import PyQt6.QtWidgets as wid

import rsc

class Header(wid.QWidget):

    def __init__(self) -> None:
        super().__init__()
        self.setStyleSheet(f'background-color: {rsc.Colors.HEADER_BACKGROUND};')

        title = wid.QLabel(rsc.Strings.APPLICATION_NAME)
        title.setContentsMargins(25, 20, 25, 20)
        title.setFont(rsc.Fonts.TITLE)
        title.setStyleSheet(f'color: {rsc.Colors.WHITE};')

        layout = wid.QHBoxLayout()
        layout.addWidget(title)
        layout.setContentsMargins(0, 0, 0, 0)
        self.setLayout(layout)