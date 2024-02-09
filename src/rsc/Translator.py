import glob
import json
import os

import logging
LOGGER = logging.getLogger(__name__)

import rsc

class Singleton(object):
    _instances = {}
    def __new__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__new__(cls, *args, **kwargs)
        return cls._instances[cls]

class Translator(Singleton):
    def __init__(self):
        self.ext = '.json'
        self.path = rsc.Paths.LANG_DIR
        self.lang = 'fr'
        self.data = {}
        self.load()

    def tr(self, key: str) -> str:
        if key not in self.data[self.lang].keys():
            LOGGER.warning(f"Key '{key}' not found in language '{self.lang}'")
        return self.data[self.lang].get(key, key)
    
    @property
    def langs(self) -> dict[str, str]:
        langs = dict()
        for lang in self.data.keys():
            langs[lang] = self.data[lang]['language_name']
        return langs
    
    def setLang(self, lang: str):
        if lang not in self.langs.keys():
            raise ValueError(f"Language '{lang}' is not available")
        self.lang = lang

    def load(self):
        # get all json files in lang directory
        files = glob.glob(os.path.join(self.path, '*' + self.ext))
        for file in files:
            # get lang from file name
            lang = os.path.basename(file).replace(self.ext, '')
            # open file
            with open(file, 'r', encoding='utf-8') as f:
                # load json data
                self.data[lang] = json.load(f)
        LOGGER.debug(f'Loaded {len(self.data)} languages')
        
    