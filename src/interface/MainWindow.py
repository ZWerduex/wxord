import PyQt6.QtWidgets as wid
import PyQt6.QtGui as gui

import glob
import os

import logging
LOGGER = logging.getLogger(__name__)

import control as c
import interface as i
import rsc

class MainWindow(wid.QMainWindow):
    def __init__(self, width: int, height: int):
        super().__init__()
        self.controller = c.MainController(self)

        for file in glob.glob(os.path.join(rsc.Paths.FONTS_DIR, '*.ttf')):
            gui.QFontDatabase.addApplicationFont(file)

        self.initWindow(width, height)
        self.buildWidgets()

    # WINDOW BAKING
    
    def initWindow(self, width: int, height: int):
        LOGGER.debug(f'Initializing {width}x{height} window')
        self.setWindowTitle(rsc.Strings.APPLICATION_NAME)
        self.setMinimumSize(width, height)
        
        # Centers window
        qr = self.frameGeometry()
        cp = self.screen().availableGeometry().center() # type: ignore
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def buildWidgets(self):
        header = i.Header()

        self.wordList = i.WordList(self.controller)
        self.wordList.wordClicked.connect(self.setPattern)
        
        callback = lambda : self.controller.onGenerate(self.pattern)
        self.patternInput = i.PatternInput(callback)
        self.generateButton = i.GenerateButton(callback)

        leftPanel = wid.QVBoxLayout()
        leftPanel.setSpacing(0)
        leftPanel.setContentsMargins(0, 0, 0, 0)
        leftPanel.addWidget(self.patternInput)
        leftPanel.addWidget(self.generateButton)

        main = wid.QHBoxLayout()
        main.setSpacing(0)
        main.setContentsMargins(0, 0, 0, 0)
        main.addLayout(leftPanel)
        main.addWidget(self.wordList)

        vbox = wid.QVBoxLayout()
        vbox.setSpacing(0)
        vbox.setContentsMargins(0, 0, 0, 0)
        vbox.addWidget(header)
        vbox.addLayout(main, 1)

        container = wid.QWidget()
        container.setLayout(vbox)
        self.setCentralWidget(container)
        
    def reloadTranslations(self) -> None:
        self.patternInput.reloadTranslation()
        self.generateButton.reloadTranslation()

    # DATA FIELDS
    
    @property
    def pattern(self) -> str:
        return self.patternInput.text()
    
    def setPattern(self, pattern: str) -> None:
        self.patternInput.setText(pattern)
