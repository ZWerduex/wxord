import antlr4
from grammar.PatternLexer import PatternLexer
from grammar.PatternParser import PatternParser
from grammar.PatternVisitor import PatternVisitor

import logging
LOGGER = logging.getLogger(__name__)

from grammar.CharSet import CharSet

class Generator:
    def __init__(self, charsets: list[CharSet]) -> None:
        self.charsets = charsets

    def setCharSets(self, charsets: list[CharSet]) -> None:
        self.charsets = charsets

    def generate(self, pattern: str, maxLength: int) -> str:
        input_stream = antlr4.InputStream(pattern)
        lexer = PatternLexer(input_stream)
        tokens = antlr4.CommonTokenStream(lexer)
        parser = PatternParser(tokens)
        tree = parser.pattern()
        if parser.getNumberOfSyntaxErrors() > 0:
            raise IOError('Syntax errors found in pattern')
        visitor = PatternVisitor(maxLength, self.charsets)
        return visitor.visit(tree)
    
    def generateMany(self, pattern: str, maxLength: int, count: int) -> set[str]:
        LOGGER.debug(f"Generating {count} words with pattern '{pattern}'")
        return {self.generate(pattern, maxLength) for _ in range(count)}