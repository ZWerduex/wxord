import antlr4
import antlr4.tree
import antlr4.tree.Tree

from grammar.PatternLexer import PatternLexer
from grammar.PatternParser import PatternParser
from grammar.PatternExpanderVisitor import PatternExpanderVisitor
from grammar.PatternGeneratorVisitor import PatternGeneratorVisitor
from grammar.PatternMinLengthVisitor import PatternMinLengthVisitor
from grammar.PatternSimplifierVisitor import PatternSimplifierVisitor

import logging
LOGGER = logging.getLogger(__name__)

from grammar.CharSet import CharSet

class Generator:

    def __init__(self, charsets: list[CharSet]) -> None:
        self.charsets = charsets
        self.lastPattern = ''
        self.generatedWords = dict()

    def tree(self, pattern: str) -> PatternParser.PatternContext:
        input_stream = antlr4.InputStream(pattern)
        lexer = PatternLexer(input_stream)
        tokens = antlr4.CommonTokenStream(lexer)
        parser = PatternParser(tokens)

        if parser.getNumberOfSyntaxErrors() > 0:
            raise IOError('Syntax errors found in pattern')
        
        return parser.pattern()
    
    def generate(self, pattern: str, minLength: int, maxLength: int, count: int) -> set[str]:
        LOGGER.debug(f"Generating {count} words with pattern '{pattern}'")
        if pattern == '':
            return set()
        
        # Get simplified pattern and count how many additional patterns there are
        simplified, additionalPatterns = PatternSimplifierVisitor().visit(self.tree(pattern))

        
        # Reset the generated words if the pattern has changed
        if self.lastPattern != simplified:
            self.lastPattern = simplified
            self.generatedWords = dict()

        words = set()

        for _ in range(count):
            # Get the minimum length of the pattern
            tree = self.tree(simplified)
            length = PatternMinLengthVisitor(self.charsets).visit(tree)
            expanded = simplified
            
            # LOGGER.debug(f"Simplified '{pattern}' (wanted minlen = {minLength}) to '{simplified}' (len={length})")
            # LOGGER.debug(f"Additional patterns: {additionalPatterns}")

            # Expand the pattern until the minimum length is reached while it is possible to do so
            while length < minLength and additionalPatterns > 0:
                
                expanded, additionalPatterns = PatternExpanderVisitor(
                    additionalPatterns
                ).visit(
                    self.tree(expanded)
                )
                length = PatternMinLengthVisitor(self.charsets).visit(
                    self.tree(expanded)
                )
                # LOGGER.debug(f"Expanded to '{expanded}' (len={length})")
                # LOGGER.debug(f"Additional patterns: {additionalPatterns}")

            self.generatedWords[expanded] = self.generatedWords.get(expanded, 0) + 1

            generator = PatternGeneratorVisitor(maxLength, self.charsets)
            words.add(generator.visit(self.tree(expanded)))

        LOGGER.debug(self.generatedWords)

        # visitor = PatternGeneratorVisitor(maxLength, self.charsets)
        return words