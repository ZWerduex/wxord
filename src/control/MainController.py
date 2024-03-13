from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    import interface as i

import PyQt6.QtWidgets as wid

import glob
import json
import os

import logging
LOGGER = logging.getLogger(__name__)

import grammar as g
import rsc

class MainController:
    def __init__(self, window: i.MainWindow):
        self.window = window

        self.itemSentToPattern = None

    @property
    def charsets(self) -> dict[str, dict]:
        ext = 'json'
        cs = dict()
        files = glob.glob(os.path.join(rsc.Paths.CHARSETS_DIR, f'*.{ext}'))
        for file in files:
            lang = os.path.basename(file).replace(f'.{ext}', '')
            with open(file, 'r', encoding = 'utf-8') as f:
                cs[lang] = json.load(f)
        if len(files) == 0:
            LOGGER.info('No charsets file found')
        else:
            LOGGER.info(f'{len(files)} charsets file(s) found')
        return cs
    
    # EVENTS

    def onSendToClipboard(self, word: str) -> None:
        LOGGER.debug(f"Copying '{word}' to clipboard")
        wid.QApplication.clipboard().setText(word) # type: ignore

        self.window.footer.setStatus(
            rsc.Translator.tr('Status_WordSentToClipboard').format(word = word)
        )

    def onSendToPatternInput(self, item: i.WordListItem) -> None:
        self.itemSentToPattern = item
        pattern = item.word
        LOGGER.debug(f"Setting pattern to word '{pattern}'")
        self.window.footer.setStatus(rsc.Translator.tr('Status_WordSentToPatternInput').format(word = pattern))
        self.window.setPattern(pattern)

    def onPatternEdited(self, pattern: str) -> None:
        if self.itemSentToPattern is not None:
            self.itemSentToPattern.icon.unvalidate()
            self.itemSentToPattern = None

    def onGenerate(self, pattern: str) -> None:
        cs = self.charsets['basic_french']['charsets']
        tmp = []
        for d in cs:
            chars = []
            weights = []
            for key, value in d.items():
                chars.append(key)
                weights.append(value)
            tmp.append(g.CharSet(chars, weights))
        
        generated = sorted(g.Generator(tmp).generateMany(pattern, 20, 15))
        self.window.wordList.empty()

        if len(generated) > 0:
            words = [w[0].upper() + w[1:] for w in generated if len(w) > 0]
            self.window.wordList.populate(words)

            key = 'Status_GeneratedWords' if len(words) > 1 else 'Status_GeneratedWord'
            self.window.footer.setStatus(
                rsc.Translator.tr(key).format(nb = len(words))
            )
