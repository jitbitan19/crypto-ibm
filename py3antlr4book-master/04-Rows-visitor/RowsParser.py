# Generated from Rows.g4 by ANTLR 4.13.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,3,18,2,0,7,0,2,1,7,1,1,0,1,0,1,0,4,0,8,8,0,11,0,12,0,9,1,1,1,
        1,4,1,14,8,1,11,1,12,1,15,1,1,0,0,2,0,2,0,0,17,0,7,1,0,0,0,2,13,
        1,0,0,0,4,5,3,2,1,0,5,6,5,2,0,0,6,8,1,0,0,0,7,4,1,0,0,0,8,9,1,0,
        0,0,9,7,1,0,0,0,9,10,1,0,0,0,10,1,1,0,0,0,11,12,5,3,0,0,12,14,6,
        1,-1,0,13,11,1,0,0,0,14,15,1,0,0,0,15,13,1,0,0,0,15,16,1,0,0,0,16,
        3,1,0,0,0,2,9,15
    ]

class RowsParser ( Parser ):

    grammarFileName = "Rows.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'\\t'" ]

    symbolicNames = [ "<INVALID>", "TAB", "NL", "STUFF" ]

    RULE_rows = 0
    RULE_row = 1

    ruleNames =  [ "rows", "row" ]

    EOF = Token.EOF
    TAB=1
    NL=2
    STUFF=3

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None



    @property
    def column(self):
        return self._col

    @column.setter
    def column(self, value):
        self._col = value




    class RowsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def row(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(RowsParser.RowContext)
            else:
                return self.getTypedRuleContext(RowsParser.RowContext,i)


        def NL(self, i:int=None):
            if i is None:
                return self.getTokens(RowsParser.NL)
            else:
                return self.getToken(RowsParser.NL, i)

        def getRuleIndex(self):
            return RowsParser.RULE_rows

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRows" ):
                listener.enterRows(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRows" ):
                listener.exitRows(self)




    def rows(self):

        localctx = RowsParser.RowsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_rows)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 7 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 4
                self.row()
                self.state = 5
                self.match(RowsParser.NL)
                self.state = 9 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==3):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RowContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.i = 0
            self._STUFF = None # Token

        def STUFF(self, i:int=None):
            if i is None:
                return self.getTokens(RowsParser.STUFF)
            else:
                return self.getToken(RowsParser.STUFF, i)

        def getRuleIndex(self):
            return RowsParser.RULE_row

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRow" ):
                listener.enterRow(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRow" ):
                listener.exitRow(self)




    def row(self):

        localctx = RowsParser.RowContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_row)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 13 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 11
                localctx._STUFF = self.match(RowsParser.STUFF)

                localctx.i = localctx.i + 1
                if localctx.i == self.column:
                    print((None if localctx._STUFF is None else localctx._STUFF.text))

                self.state = 15 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==3):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





