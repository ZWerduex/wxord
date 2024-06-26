# Generated from ../Pattern.g4 by ANTLR 4.13.1
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


def serializedATN():
    return [
        4,0,6,25,6,-1,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,1,
        0,1,0,1,1,1,1,1,2,1,2,1,3,1,3,1,4,1,4,1,5,1,5,0,0,6,1,1,3,2,5,3,
        7,4,9,5,11,6,1,0,1,2,0,42,43,63,63,24,0,1,1,0,0,0,0,3,1,0,0,0,0,
        5,1,0,0,0,0,7,1,0,0,0,0,9,1,0,0,0,0,11,1,0,0,0,1,13,1,0,0,0,3,15,
        1,0,0,0,5,17,1,0,0,0,7,19,1,0,0,0,9,21,1,0,0,0,11,23,1,0,0,0,13,
        14,5,40,0,0,14,2,1,0,0,0,15,16,5,41,0,0,16,4,1,0,0,0,17,18,2,48,
        57,0,18,6,1,0,0,0,19,20,5,124,0,0,20,8,1,0,0,0,21,22,7,0,0,0,22,
        10,1,0,0,0,23,24,9,0,0,0,24,12,1,0,0,0,1,0,0
    ]

class PatternLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    DIGIT = 3
    OPERATOR = 4
    QUANTIFIER = 5
    OTHER = 6

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'('", "')'", "'|'" ]

    symbolicNames = [ "<INVALID>",
            "DIGIT", "OPERATOR", "QUANTIFIER", "OTHER" ]

    ruleNames = [ "T__0", "T__1", "DIGIT", "OPERATOR", "QUANTIFIER", "OTHER" ]

    grammarFileName = "Pattern.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


