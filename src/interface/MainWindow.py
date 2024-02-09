import PyQt6.QtWidgets as wid

import logging
LOGGER = logging.getLogger(__name__)

import control as c
import interface as i
import rsc

class MainWindow(wid.QMainWindow):
    def __init__(self, minWidth: int, minHeight: int):
        super().__init__()
        self.controller = c.MainController(self)

        self.initWindow(minWidth, minHeight)
        self.buildWidgets()
    
    def initWindow(self, minWidth: int, minHeight: int):
        LOGGER.debug(f'Initializing {minWidth}x{minHeight} window')
        self.setWindowTitle(rsc.Strings.APPLICATION_NAME)
        self.setMinimumSize(minWidth, minHeight)
        
        # Centers window
        qr = self.frameGeometry()
        cp = self.screen().availableGeometry().center() # type: ignore
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def buildWidgets(self):
        
        words = i.WordList(self.controller)
        words.populate(['word', 'another word', 'chtulhu', 'chicken', 'object'])

        hbox = wid.QHBoxLayout()
        hbox.addWidget(words)
        container = wid.QWidget()
        container.setLayout(hbox)
        self.setCentralWidget(container)