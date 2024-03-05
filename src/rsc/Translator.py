import glob
import json
import os

import logging
LOGGER = logging.getLogger(__name__)

import rsc

class Translator:

    PATH = rsc.Paths.LANG_DIR
    LANG = 'fr'
    DATA = {}

    @classmethod
    def tr(cls, key: str) -> str:
        if key not in cls.DATA[cls.LANG].keys():
            LOGGER.warning(f"Key '{key}' not found in language '{cls.LANG}'")
        return cls.DATA[cls.LANG].get(key, key)
    
    @classmethod
    def langs(cls) -> dict[str, str]:
        langs = dict()
        for lang in cls.DATA.keys():
            langs[lang] = cls.DATA[lang]['language_name']
        return langs
    
    @classmethod
    def setLang(cls, lang: str):
        if lang not in cls.langs().keys():
            raise ValueError(f"Language '{lang}' is not available")
        cls.LANG = lang

    @classmethod
    def load(cls):
        ext = 'json'
        # get all json files in lang directory
        files = glob.glob(os.path.join(cls.PATH, f'*.{ext}'))
        for file in files:
            # get lang from file name
            lang = os.path.basename(file).replace(f'.{ext}', '')
            # open file
            with open(file, 'r', encoding='utf-8') as f:
                # load json data
                cls.DATA[lang] = json.load(f)
        LOGGER.debug(f'Loaded {len(cls.DATA)} languages')
        
    