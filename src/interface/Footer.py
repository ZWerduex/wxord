import PyQt6.QtCore as core
import PyQt6.QtWidgets as wid

from interface.LangComboBox import LangComboBox
import rsc

class Footer(wid.QWidget):
    comboBoxDroppedDown = core.pyqtSignal()
    langChanged = core.pyqtSignal(object, object)

    def __init__(self):
        super().__init__()
        self.setStyleSheet(f'background-color: {rsc.Colors.HEADER_BACKGROUND};')

        self.statusTitle = wid.QLabel(rsc.Translator.tr('Status'))
        self.statusTitle.setContentsMargins(rsc.Margins.BASE, rsc.Margins.BASE, rsc.Margins.BASE, rsc.Margins.BASE)
        self.statusTitle.setFont(rsc.Fonts.BASE)
        self.statusTitle.setStyleSheet(f'color: {rsc.Colors.GRAY};')

        self.status = wid.QLabel()
        self.status.setContentsMargins(rsc.Margins.BASE, rsc.Margins.BASE, rsc.Margins.BASE, rsc.Margins.BASE)
        self.status.setFont(rsc.Fonts.BASE)
        self.status.setStyleSheet(f'color: {rsc.Colors.DEFAULT_FONT};')
        self.clearStatus()

        self.langsCombo = LangComboBox()
        self.langsCombo.langChanged.connect(self.langChanged)
        self.langsCombo.arrowClicked.connect(self.comboBoxDroppedDown)

        container = wid.QWidget()
        container.setStyleSheet(f'background-color: {rsc.Colors.HEADER_BACKGROUND};')
        layout = wid.QHBoxLayout()
        layout.setSpacing(0)
        layout.setContentsMargins(rsc.Margins.BASE, rsc.Margins.BASE, rsc.Margins.BASE, rsc.Margins.BASE)
        layout.addWidget(self.langsCombo)
        container.setLayout(layout)
        
        layout = wid.QHBoxLayout()
        layout.setSpacing(0)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.addWidget(self.statusTitle)
        layout.addWidget(self.status, 1)
        layout.addWidget(container)
        self.setLayout(layout)

    def setStatus(self, msg: str) -> None:
        self.status.setText(msg)
    
    def clearStatus(self) -> None:
        self.status.setText('-')

    def reloadTranslation(self) -> None:
        self.statusTitle.setText(rsc.Translator.tr('Status'))
        self.clearStatus()