import random
import exrex

import logging
LOGGER = logging.getLogger(__name__)

from model.CharSet import CharSet

class Generator:
    def __init__(self, charsets: list[CharSet]) -> None:
        self.charsets = charsets

    def setCharSets(self, charsets: list[CharSet]) -> None:
        self.charsets = charsets

    def generate(self, pattern: str, maxLength: int) -> str:
        formattedPattern = ''
        for char in pattern:
            if char.isdigit():
                digit = int(char)
                if digit == 0:
                    formattedPattern += random.choice(self.charsets).pick()
                else:
                    if digit - 1 >= len(self.charsets) or digit - 1 < 0:
                        raise ValueError(f'No charset {digit} found')
                    formattedPattern += self.charsets[digit - 1].pick()
            else:
                formattedPattern += char
        return exrex.getone(formattedPattern, limit = maxLength)
    
    def generateMany(self, pattern: str, maxLength: int, count: int) -> set[str]:
        LOGGER.debug(f"Generating {count} words with pattern '{pattern}'")
        return {self.generate(pattern, maxLength) for _ in range(count)}