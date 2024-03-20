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

        rsc.Translator.load()

    def completeInit(self) -> None:
        # Init the language combo box
        self.window.footer.langsCombo.populate(rsc.Translator.langs())
        # Read config file to set the last used language
        if os.path.exists(rsc.Paths.CONFIG_FILE):
            with open(rsc.Paths.CONFIG_FILE, 'r', encoding = 'utf-8') as f:
                data = json.load(f)
                if 'lang' in data:
                    try:
                        rsc.Translator.setLang(data['lang'])
                        LOGGER.info(f"Last used language : '{data['lang']}'")
                        self.window.reloadTranslations()
                    except ValueError as e:
                        LOGGER.error(f"{e} : {data['lang']} is missing in translations files")
        # Update the language combo box
        self.window.footer.langsCombo.setLang(rsc.Translator.LANG)

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
        LOGGER.debug(f"Setting pattern to word '{item.word}'")
        self.itemSentToPattern = item
        self.window.setPattern(item.word)
        
        self.window.footer.setStatus(
            rsc.Translator.tr('Status_WordSentToPatternInput').format(word = item.word)
        )

    def onPatternEdited(self, pattern: str) -> None:
        if self.itemSentToPattern is not None:
            self.itemSentToPattern.icon.unvalidate()
            self.itemSentToPattern = None

    def onChangeLang(self, lang: str, name: str) -> None:
        LOGGER.debug(f"Changing language to '{lang}' ({name})")
        # Set the new language
        rsc.Translator.setLang(lang)
        # Reload translations
        self.window.reloadTranslations()
        # Update the last used language
        with open(rsc.Paths.CONFIG_FILE, 'w', encoding = 'utf-8') as f:
            json.dump({'lang': lang}, f)

    def onScanTranslationsFiles(self) -> None:
        LOGGER.debug('Scanning translations files')
        rsc.Translator.load()
        self.window.footer.langsCombo.populate(rsc.Translator.langs())
        self.window.footer.langsCombo.setLang(rsc.Translator.LANG)

    def onGenerate(self, pattern: str, maxLength: int, batchSize: int) -> None:
        cs = self.charsets['basic_french']['charsets']
        tmp = []
        for d in cs:
            chars = []
            weights = []
            for key, value in d.items():
                chars.append(key)
                weights.append(value)
            tmp.append(g.CharSet(chars, weights))
        
        if len(pattern) == 0:
            self.window.footer.setStatus(rsc.Translator.tr('Status_PatternIsEmptyNoWordGenerated'))
            return
        
        generated = sorted(g.Generator(tmp).generateMany(
            pattern, maxLength, batchSize
        ))
        self.window.wordList.empty()

        if len(generated) > 0:
            words = [w[0].upper() + w[1:] for w in generated if len(w) > 0]
            self.window.wordList.populate(words)

            key = 'Status_GeneratedWords' if len(words) > 1 else 'Status_GeneratedWord'
            self.window.footer.setStatus(
                rsc.Translator.tr(key).format(nb = len(words))
            )
        else:
            raise RuntimeError(f"Pattern '{pattern}' generated no word")
