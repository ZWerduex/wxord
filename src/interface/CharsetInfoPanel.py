import PyQt6.QtWidgets as wid

import control as c

class CharsetInfoPanel(wid.QWidget):
    def __init__(self, controller: c.MainController):
        super().__init__()
        self.controller = controller

    