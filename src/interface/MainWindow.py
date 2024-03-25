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
    def __init__(self, width: int, height: int) -> None:
        super().__init__()
        self.controller = c.MainController(self)

        # Load fonts
        for file in glob.glob(os.path.join(rsc.Paths.FONTS_DIR, '*.ttf')):
            gui.QFontDatabase.addApplicationFont(file)
            LOGGER.debug(f'Font {os.path.basename(file)} loaded')

        self.initWindow(width, height)
        self.buildWidgets()

        self.controller.completeInit()

    # WINDOW BAKING
    
    def initWindow(self, width: int, height: int) -> None:
        LOGGER.debug(f'Initializing {width}x{height} window')
        self.setWindowTitle(rsc.Strings.APPLICATION_NAME)
        self.setMinimumSize(width, height)
        
        # Centers window
        qr = self.frameGeometry()
        cp = self.screen().availableGeometry().center() # type: ignore
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def buildWidgets(self) -> None:
        self.header = i.Header()
        self.footer = i.Footer()
        self.footer.langChanged.connect(self.controller.onChangeLang)
        self.footer.comboBoxDroppedDown.connect(self.controller.onScanTranslationsFiles)

        self.wordList = i.WordList()
        self.wordList.itemClicked.connect(self.controller.onSendToClipboard)
        self.wordList.itemIconClicked.connect(self.controller.onSendToPatternInput)
        
        # Left panel
        self.generationPanel = i.GenerationPanel()
        self.generationPanel.generated.connect(self.controller.onGenerate)
        self.generationPanel.patternEdited.connect(self.controller.onPatternEdited)

        self.charsetsPanel = i.CharsetsPanel()

        leftPanel = wid.QWidget()
        leftPanel.setStyleSheet(f"background: {rsc.Colors.DEFAULT_BACKGROUND};")
        leftPanel.setMinimumWidth(400)

        leftLayout = wid.QVBoxLayout()
        leftLayout.setSpacing(rsc.Margins.BASE)
        leftLayout.setContentsMargins(rsc.Margins.BASE, rsc.Margins.BASE, rsc.Margins.BASE, rsc.Margins.BASE)
        leftLayout.addWidget(self.generationPanel)
        leftLayout.addWidget(self.wordList, 1)
        leftPanel.setLayout(leftLayout)

        main = wid.QHBoxLayout()
        main.setSpacing(0)
        main.setContentsMargins(0, 0, 0, 0)
        main.addWidget(leftPanel)
        main.addWidget(self.charsetsPanel, 1)

        vbox = wid.QVBoxLayout()
        vbox.setSpacing(0)
        vbox.setContentsMargins(0, 0, 0, 0)
        vbox.addWidget(self.header)
        vbox.addLayout(main, 1)
        vbox.addWidget(self.footer)

        container = wid.QWidget()
        container.setLayout(vbox)
        self.setCentralWidget(container)

    # HANDY METHODS
        
    def reloadTranslations(self) -> None:
        LOGGER.debug('Reloading translations')
        self.header.reloadTranslation()
        self.footer.reloadTranslation()
        self.generationPanel.reloadTranslation()
        self.charsetsPanel.reloadTranslation()
    
    def setPattern(self, pattern: str) -> None:
        self.generationPanel.setPattern(pattern)
