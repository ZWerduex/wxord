import json, os

import logging
LOGGER = logging.getLogger(__name__)

import rsc

class Configuration:
    def __init__(self) -> None:
        self.config = {}
        self.load()

    def load(self) -> None:
        if not os.path.exists(rsc.Paths.CONFIG_FILE):
            LOGGER.warning("Configuration file not found")
            return

        with open(rsc.Paths.CONFIG_FILE, "r", encoding='utf-8') as file:
            self.config = json.load(file)
        
        if 'lang' not in self.config.keys():
            LOGGER.warning("Language not found in configuration file")

        if 'charset' not in self.config.keys():
            LOGGER.warning("Charset not found in configuration file")

    def save(self, data: dict) -> None:
        for key, value in data.items():
            self.config[key] = value
        with open(rsc.Paths.CONFIG_FILE, "w", encoding='utf-8') as file:
            json.dump(self.config, file)

    @property
    def lang(self) -> str | None:
        return self.config['lang'] if 'lang' in self.config.keys() else None
    
    @property
    def charset(self) -> dict[str, int] | None:
        return self.config['charset'] if 'charset' in self.config.keys() else None