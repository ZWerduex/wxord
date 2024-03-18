import PyQt6.QtWidgets as wid

import rsc

class CharsetsPanel(wid.QWidget):

    def __init__(self) -> None:
        super().__init__()

        self.reloadTranslation()

    def reloadTranslation(self) -> None:
        pass