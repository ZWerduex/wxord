from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    import interface as i

import glob
import json
import os

import logging
LOGGER = logging.getLogger(__name__)

import grammar as m
import rsc

class MainController:
    def __init__(self, window: i.MainWindow):
        self.window = window

    @property
    def charsets(self) -> dict[str, dict]:
        ext = 'json'
        cs = dict()
        files = glob.glob(os.path.join(rsc.Paths.CHARSETS_DIR, f'*.{ext}'))
        if len(files) == 0:
            LOGGER.info('No charsets file found')
        for file in files:
            lang = os.path.basename(file).replace(f'.{ext}', '')
            with open(file, 'r', encoding='utf-8') as f:
                cs[lang] = json.load(f)
        return cs
    
    # EVENTS

    def onGenerate(self, pattern: str):
        cs = self.charsets['basic_french']['charsets']
        tmp = []
        for d in cs:
            chars = []
            weights = []
            for key, value in d.items():
                chars.append(key)
                weights.append(value)
            tmp.append(m.CharSet(chars, weights))
        
        generated = m.Generator(tmp).generateMany(pattern, 20, 100)
        self.window.wordList.empty()

        if len(generated) > 0:
            words = {w[0].upper() + w[1:] for w in generated if len(w) > 0}
            self.window.wordList.populate(words)


    
