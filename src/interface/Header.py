import PyQt6.QtWidgets as wid
from PyQt6.QtCore import Qt

import rsc

class Header(wid.QWidget):

    def __init__(self) -> None:
        super().__init__()
        self.setStyleSheet(f'background-color: {rsc.Colors.HEADER_BACKGROUND};')

        title = wid.QLabel(rsc.Strings.APPLICATION_NAME)
        title.setFont(rsc.Fonts.TITLE)
        title.setStyleSheet(f'color: {rsc.Colors.WHITE};')
        title.setContentsMargins(25, 20, 25, 20)

        self.author = wid.QLabel(
            rsc.Translator.tr('HeaderAuthor_text').format(author = rsc.Strings.APPLICATION_AUTHOR)
        )
        self.author.setFont(rsc.Fonts.AUTHOR)
        self.author.setStyleSheet(f'color: {rsc.Colors.GRAY};')
        self.author.setContentsMargins(25, 0, 25, 31)
        self.author.setAlignment(Qt.AlignmentFlag.AlignBottom)

        layout = wid.QHBoxLayout()
        layout.addWidget(title)
        layout.addWidget(wid.QWidget(), 1)
        layout.addWidget(self.author)
        layout.setSpacing(0)
        layout.setContentsMargins(0, 0, 0, 0)
        self.setLayout(layout)

    def reloadTranslation(self) -> None:
        self.author.setText(
            rsc.Translator.tr('HeaderAuthor_text').format(author = rsc.Strings.APPLICATION_AUTHOR)
        )