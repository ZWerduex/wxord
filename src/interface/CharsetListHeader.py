from PyQt6.QtCore import Qt
import PyQt6.QtWidgets as wid

from interface.CharsetList import CharsetList
import rsc

class CharsetListHeader(wid.QWidget):
    """Header of a CharsetList, with buttons to order a list by char or weight."""

    def __init__(self, number: int, linkedList: CharsetList) -> None:
        super().__init__()

        header = wid.QLabel(str(number))

        self.orderByCharButton = wid.QPushButton(rsc.Translator.tr('OrderByCharButton_text'))
        self.orderByCharButton.clicked.connect(lambda: linkedList.orderBy('char'))
        
        self.orderByWeightButton = wid.QPushButton(rsc.Translator.tr('OrderByWeightButton_text'))
        self.orderByWeightButton.clicked.connect(lambda: linkedList.orderBy('weight'))

        hbox = wid.QHBoxLayout()
        hbox.setSpacing(rsc.Margins.CHARSETLIST)
        hbox.setContentsMargins(0, 0, 0, 0)
        hbox.addWidget(self.orderByCharButton)
        hbox.addStretch(1)
        hbox.addWidget(self.orderByWeightButton)

        vbox = wid.QVBoxLayout()
        vbox.setSpacing(rsc.Margins.CHARSETLIST)
        vbox.setContentsMargins(0, 0, 0, 0)
        vbox.addWidget(header)
        vbox.addLayout(hbox)

        self.setLayout(vbox)

    def reloadTranslation(self) -> None:
        self.orderByCharButton.setText(rsc.Translator.tr('OrderByCharButton_text'))
        self.orderByWeightButton.setText(rsc.Translator.tr('OrderByWeightButton_text'))
        