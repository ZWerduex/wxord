import PyQt6.QtCore as core
import PyQt6.QtWidgets as wid

from interface.CharsetsPanelHeader import CharsetsPanelHeader
import interface as i
import rsc

class CharsetsPanel(wid.QWidget):

    def __init__(self,
            name: str = '',
            desc: str = '',
            suggested: list[str] | None = None,
            charsets: list[dict[str, int]] | None = None
        ) -> None:
        super().__init__()
        suggested = suggested if suggested else list()
        charsets = charsets if charsets else list()

        # Hardcoded-limit to 3 charsets per panel
        while len(charsets) < 3:
            charsets.append(dict())
        if len(charsets) > 3:
            charsets = charsets[:3]

        self.title = CharsetsPanelHeader(name, desc, suggested)

        self.charsetLists = list()
        listsLayout = wid.QHBoxLayout()
        listsLayout.setSpacing(0)
        listsLayout.setContentsMargins(0, 0, 0, 0)

        for charset in charsets:
            charsetWidget = i.CharsetList(charset)
            self.charsetLists.append(charsetWidget)
            listsLayout.addWidget(charsetWidget)

        main = wid.QVBoxLayout()
        main.setSpacing(0)
        main.setContentsMargins(0, 0, 0, 0)
        main.addWidget(self.title)
        main.addLayout(listsLayout)
        self.setLayout(main)

        self.reloadTranslation()

    def update(self,
            name: str = '',
            desc: str = '',
            suggested: list[str] | None = None,
            charsets: list[dict[str, int]] | None = None
        ) -> None:
        suggested = suggested if suggested else list()
        charsets = charsets if charsets else list()

        self.title.update(name, desc, suggested)
        for i, charset in enumerate(charsets):
            self.charsetLists[i].populate(charset)

    @property
    def charsets(self) -> list[dict[str, int]]:
        return [charset.charset for charset in self.charsetLists]

    def reloadTranslation(self) -> None:
        self.title.reloadTranslation()
        for charset in self.charsetLists:
            charset.reloadTranslation()