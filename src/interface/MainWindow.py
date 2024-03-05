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

    # WINDOW BAKING
    
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
        self.wordList = i.WordList(self.controller)
        self.wordList.onWordClicked.connect(self.setPattern)
        
        callback = lambda : self.controller.onGenerate(self.pattern)
        self.patternInput = i.PatternInput(callback)
        self.generateButton = i.GenerateButton(callback)

        vbox = wid.QVBoxLayout()
        vbox.addWidget(self.wordList)
        vbox.addWidget(self.patternInput)
        vbox.addWidget(self.generateButton)

        container = wid.QWidget()
        container.setLayout(vbox)
        self.setCentralWidget(container)
        
    def reloadTranslations(self) -> None:
        self.patternInput.reloadTranslation()

    # DATA FIELDS
    
    @property
    def pattern(self) -> str:
        return self.patternInput.text()
    
    def setPattern(self, pattern: str) -> None:
        self.patternInput.setText(pattern)
