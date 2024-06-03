# Generated from Rows.g4 by ANTLR 4.13.1
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


def serializedATN():
    return [
        4,0,3,21,6,-1,2,0,7,0,2,1,7,1,2,2,7,2,1,0,1,0,1,0,1,0,1,1,3,1,13,
        8,1,1,1,1,1,1,2,4,2,18,8,2,11,2,12,2,19,0,0,3,1,1,3,2,5,3,1,0,1,
        2,0,9,10,13,13,22,0,1,1,0,0,0,0,3,1,0,0,0,0,5,1,0,0,0,1,7,1,0,0,
        0,3,12,1,0,0,0,5,17,1,0,0,0,7,8,5,9,0,0,8,9,1,0,0,0,9,10,6,0,0,0,
        10,2,1,0,0,0,11,13,5,13,0,0,12,11,1,0,0,0,12,13,1,0,0,0,13,14,1,
        0,0,0,14,15,5,10,0,0,15,4,1,0,0,0,16,18,8,0,0,0,17,16,1,0,0,0,18,
        19,1,0,0,0,19,17,1,0,0,0,19,20,1,0,0,0,20,6,1,0,0,0,3,0,12,19,1,
        6,0,0
    ]

class RowsLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    TAB = 1
    NL = 2
    STUFF = 3

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'\\t'" ]

    symbolicNames = [ "<INVALID>",
            "TAB", "NL", "STUFF" ]

    ruleNames = [ "TAB", "NL", "STUFF" ]

    grammarFileName = "Rows.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


