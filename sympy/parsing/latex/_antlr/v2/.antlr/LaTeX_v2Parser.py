# Generated from /home/user/sympy-grammar-modifications/sympy/parsing/latex/_antlr/v2/LaTeX_v2.g4 by ANTLR 4.8
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3%")
        buf.write("\7\4\2\t\2\3\2\3\2\3\2\2\2\3\2\2\2\2\5\2\4\3\2\2\2\4\5")
        buf.write("\7$\2\2\5\3\3\2\2\2\2")
        return buf.getvalue()


class LaTeX_v2Parser ( Parser ):

    grammarFileName = "LaTeX_v2.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'('", "')'", "'{'", "'}'", "'['", "']'", 
                     "';'", "','", "'.'", "'='", "'>'", "'<'", "'!'", "'~'", 
                     "'?'", "':'", "'=='", "'<='", "'>='", "'!='", "'&&'", 
                     "'||'", "'++'", "'--'", "'+'", "'-'", "'*'", "'/'", 
                     "'&'", "'|'", "'^'", "'%'" ]

    symbolicNames = [ "<INVALID>", "LPAREN", "RPAREN", "LBRACE", "RBRACE", 
                      "LBRACK", "RBRACK", "SEMI", "COMMA", "DOT", "ASSIGN", 
                      "GT", "LT", "BANG", "TILDE", "QUESTION", "COLON", 
                      "EQUAL", "LE", "GE", "NOTEQUAL", "AND", "OR", "INC", 
                      "DEC", "ADD", "SUB", "MUL", "DIV", "BITAND", "BITOR", 
                      "CARET", "MOD", "WS", "INT", "FloatingPointLiteral" ]

    RULE_expression = 0

    ruleNames =  [ "expression" ]

    EOF = Token.EOF
    LPAREN=1
    RPAREN=2
    LBRACE=3
    RBRACE=4
    LBRACK=5
    RBRACK=6
    SEMI=7
    COMMA=8
    DOT=9
    ASSIGN=10
    GT=11
    LT=12
    BANG=13
    TILDE=14
    QUESTION=15
    COLON=16
    EQUAL=17
    LE=18
    GE=19
    NOTEQUAL=20
    AND=21
    OR=22
    INC=23
    DEC=24
    ADD=25
    SUB=26
    MUL=27
    DIV=28
    BITAND=29
    BITOR=30
    CARET=31
    MOD=32
    WS=33
    INT=34
    FloatingPointLiteral=35

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.8")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ExpressionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT(self):
            return self.getToken(LaTeX_v2Parser.INT, 0)

        def getRuleIndex(self):
            return LaTeX_v2Parser.RULE_expression




    def expression(self):

        localctx = LaTeX_v2Parser.ExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2
            self.match(LaTeX_v2Parser.INT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





