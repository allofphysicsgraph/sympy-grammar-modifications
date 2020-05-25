# Generated from /home/user/sympy-grammar-modifications/sympy/parsing/latex/LaTeX.g4 by ANTLR 4.7.1
# encoding: utf-8
from __future__ import print_function
from antlr4 import *
from io import StringIO
import sys

def serializedATN():
    with StringIO() as buf:
        buf.write(u"\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3")
        buf.write(u"S\u01c7\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t")
        buf.write(u"\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write(u"\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4")
        buf.write(u"\23\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30")
        buf.write(u"\t\30\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t")
        buf.write(u"\35\4\36\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$")
        buf.write(u"\t$\4%\t%\4&\t&\4\'\t\'\3\2\3\2\3\3\3\3\3\4\3\4\3\5\3")
        buf.write(u"\5\3\5\3\5\3\5\5\5Z\n\5\3\5\5\5]\n\5\3\5\3\5\3\5\3\5")
        buf.write(u"\7\5c\n\5\f\5\16\5f\13\5\3\6\3\6\3\6\3\6\3\7\3\7\3\b")
        buf.write(u"\3\b\3\b\3\b\3\b\3\b\7\bt\n\b\f\b\16\bw\13\b\3\t\3\t")
        buf.write(u"\3\t\3\t\3\t\3\t\7\t\177\n\t\f\t\16\t\u0082\13\t\3\n")
        buf.write(u"\3\n\3\n\3\n\3\n\3\n\7\n\u008a\n\n\f\n\16\n\u008d\13")
        buf.write(u"\n\3\13\3\13\3\13\6\13\u0092\n\13\r\13\16\13\u0093\5")
        buf.write(u"\13\u0096\n\13\3\f\3\f\3\f\3\f\7\f\u009c\n\f\f\f\16\f")
        buf.write(u"\u009f\13\f\5\f\u00a1\n\f\3\r\3\r\7\r\u00a5\n\r\f\r\16")
        buf.write(u"\r\u00a8\13\r\3\16\3\16\7\16\u00ac\n\16\f\16\16\16\u00af")
        buf.write(u"\13\16\3\17\3\17\5\17\u00b3\n\17\3\20\3\20\3\20\3\20")
        buf.write(u"\3\20\3\20\5\20\u00bb\n\20\3\21\3\21\3\21\3\21\5\21\u00c1")
        buf.write(u"\n\21\3\21\3\21\3\22\3\22\3\22\3\22\5\22\u00c9\n\22\3")
        buf.write(u"\22\3\22\3\23\3\23\3\23\3\23\3\23\3\23\3\23\3\23\3\23")
        buf.write(u"\3\23\5\23\u00d7\n\23\3\23\5\23\u00da\n\23\7\23\u00dc")
        buf.write(u"\n\23\f\23\16\23\u00df\13\23\3\24\3\24\3\24\3\24\3\24")
        buf.write(u"\3\24\3\24\3\24\3\24\3\24\5\24\u00eb\n\24\3\24\5\24\u00ee")
        buf.write(u"\n\24\7\24\u00f0\n\24\f\24\16\24\u00f3\13\24\3\25\3\25")
        buf.write(u"\3\25\3\25\3\25\3\25\5\25\u00fb\n\25\3\26\3\26\3\26\3")
        buf.write(u"\26\3\26\5\26\u0102\n\26\3\27\3\27\3\27\3\27\3\27\3\27")
        buf.write(u"\3\27\3\27\3\27\3\27\3\27\3\27\5\27\u0110\n\27\3\30\3")
        buf.write(u"\30\3\30\3\30\3\31\3\31\5\31\u0118\n\31\3\31\3\31\3\31")
        buf.write(u"\5\31\u011d\n\31\3\32\3\32\3\32\3\32\3\32\3\33\7\33\u0125")
        buf.write(u"\n\33\f\33\16\33\u0128\13\33\3\34\3\34\3\34\3\34\3\34")
        buf.write(u"\3\34\3\34\3\34\3\35\3\35\3\35\3\35\3\35\3\35\3\35\3")
        buf.write(u"\35\3\36\3\36\3\37\3\37\5\37\u013e\n\37\3\37\5\37\u0141")
        buf.write(u"\n\37\3\37\5\37\u0144\n\37\3\37\5\37\u0147\n\37\5\37")
        buf.write(u"\u0149\n\37\3\37\3\37\3\37\3\37\3\37\5\37\u0150\n\37")
        buf.write(u"\3\37\3\37\5\37\u0154\n\37\3\37\3\37\3\37\3\37\3\37\3")
        buf.write(u"\37\5\37\u015c\n\37\3\37\3\37\3\37\3\37\3\37\3\37\5\37")
        buf.write(u"\u0164\n\37\3\37\5\37\u0167\n\37\3\37\3\37\3\37\5\37")
        buf.write(u"\u016c\n\37\3\37\3\37\3\37\3\37\3\37\5\37\u0173\n\37")
        buf.write(u"\3\37\3\37\3\37\3\37\3\37\3\37\3\37\3\37\3\37\3\37\3")
        buf.write(u"\37\5\37\u0180\n\37\3\37\3\37\3\37\3\37\3\37\3\37\5\37")
        buf.write(u"\u0188\n\37\3 \3 \3 \3 \3 \5 \u018f\n \3!\3!\3!\3!\3")
        buf.write(u"!\3!\3!\3!\3!\5!\u019a\n!\3!\3!\3\"\3\"\3\"\3\"\3\"\5")
        buf.write(u"\"\u01a3\n\"\3#\3#\3$\3$\3$\3$\3$\3$\5$\u01ad\n$\3%\3")
        buf.write(u"%\3%\3%\3%\3%\5%\u01b5\n%\3&\3&\3&\3&\5&\u01bb\n&\3&")
        buf.write(u"\3&\3\'\3\'\3\'\3\'\5\'\u01c3\n\'\3\'\3\'\3\'\2\b\b\16")
        buf.write(u"\20\22$&(\2\4\6\b\n\f\16\20\22\24\26\30\32\34\36 \"$")
        buf.write(u"&(*,.\60\62\64\668:<>@BDFHJL\2\n\3\2\17\20\3\2>Q\3\2")
        buf.write(u"\4\5\5\2\6\7\16\16+-\4\2<<SS\3\2/\61\3\2\26)\3\2\24\25")
        buf.write(u"\2\u01e2\2N\3\2\2\2\4P\3\2\2\2\6R\3\2\2\2\b\\\3\2\2\2")
        buf.write(u"\ng\3\2\2\2\fk\3\2\2\2\16m\3\2\2\2\20x\3\2\2\2\22\u0083")
        buf.write(u"\3\2\2\2\24\u0095\3\2\2\2\26\u00a0\3\2\2\2\30\u00a2\3")
        buf.write(u"\2\2\2\32\u00a9\3\2\2\2\34\u00b2\3\2\2\2\36\u00b4\3\2")
        buf.write(u"\2\2 \u00bc\3\2\2\2\"\u00c4\3\2\2\2$\u00cc\3\2\2\2&\u00e0")
        buf.write(u"\3\2\2\2(\u00fa\3\2\2\2*\u0101\3\2\2\2,\u010f\3\2\2\2")
        buf.write(u".\u0111\3\2\2\2\60\u011c\3\2\2\2\62\u011e\3\2\2\2\64")
        buf.write(u"\u0126\3\2\2\2\66\u0129\3\2\2\28\u0131\3\2\2\2:\u0139")
        buf.write(u"\3\2\2\2<\u0187\3\2\2\2>\u018e\3\2\2\2@\u0190\3\2\2\2")
        buf.write(u"B\u01a2\3\2\2\2D\u01a4\3\2\2\2F\u01a6\3\2\2\2H\u01ae")
        buf.write(u"\3\2\2\2J\u01b6\3\2\2\2L\u01be\3\2\2\2NO\t\2\2\2O\3\3")
        buf.write(u"\2\2\2PQ\t\3\2\2Q\5\3\2\2\2RS\5\b\5\2S\7\3\2\2\2TU\b")
        buf.write(u"\5\1\2U]\5\f\7\2VY\7\67\2\2WZ\79\2\2XZ\5\b\5\2YW\3\2")
        buf.write(u"\2\2YX\3\2\2\2Z[\3\2\2\2[]\78\2\2\\T\3\2\2\2\\V\3\2\2")
        buf.write(u"\2]d\3\2\2\2^_\f\5\2\2_`\5\4\3\2`a\5\b\5\6ac\3\2\2\2")
        buf.write(u"b^\3\2\2\2cf\3\2\2\2db\3\2\2\2de\3\2\2\2e\t\3\2\2\2f")
        buf.write(u"d\3\2\2\2gh\5\f\7\2hi\7>\2\2ij\5\f\7\2j\13\3\2\2\2kl")
        buf.write(u"\5\16\b\2l\r\3\2\2\2mn\b\b\1\2no\5\20\t\2ou\3\2\2\2p")
        buf.write(u"q\f\4\2\2qr\t\4\2\2rt\5\16\b\5sp\3\2\2\2tw\3\2\2\2us")
        buf.write(u"\3\2\2\2uv\3\2\2\2v\17\3\2\2\2wu\3\2\2\2xy\b\t\1\2yz")
        buf.write(u"\5\24\13\2z\u0080\3\2\2\2{|\f\4\2\2|}\t\5\2\2}\177\5")
        buf.write(u"\20\t\5~{\3\2\2\2\177\u0082\3\2\2\2\u0080~\3\2\2\2\u0080")
        buf.write(u"\u0081\3\2\2\2\u0081\21\3\2\2\2\u0082\u0080\3\2\2\2\u0083")
        buf.write(u"\u0084\b\n\1\2\u0084\u0085\5\26\f\2\u0085\u008b\3\2\2")
        buf.write(u"\2\u0086\u0087\f\4\2\2\u0087\u0088\t\5\2\2\u0088\u008a")
        buf.write(u"\5\22\n\5\u0089\u0086\3\2\2\2\u008a\u008d\3\2\2\2\u008b")
        buf.write(u"\u0089\3\2\2\2\u008b\u008c\3\2\2\2\u008c\23\3\2\2\2\u008d")
        buf.write(u"\u008b\3\2\2\2\u008e\u008f\t\4\2\2\u008f\u0096\5\24\13")
        buf.write(u"\2\u0090\u0092\5\30\r\2\u0091\u0090\3\2\2\2\u0092\u0093")
        buf.write(u"\3\2\2\2\u0093\u0091\3\2\2\2\u0093\u0094\3\2\2\2\u0094")
        buf.write(u"\u0096\3\2\2\2\u0095\u008e\3\2\2\2\u0095\u0091\3\2\2")
        buf.write(u"\2\u0096\25\3\2\2\2\u0097\u0098\t\4\2\2\u0098\u00a1\5")
        buf.write(u"\26\f\2\u0099\u009d\5\30\r\2\u009a\u009c\5\32\16\2\u009b")
        buf.write(u"\u009a\3\2\2\2\u009c\u009f\3\2\2\2\u009d\u009b\3\2\2")
        buf.write(u"\2\u009d\u009e\3\2\2\2\u009e\u00a1\3\2\2\2\u009f\u009d")
        buf.write(u"\3\2\2\2\u00a0\u0097\3\2\2\2\u00a0\u0099\3\2\2\2\u00a1")
        buf.write(u"\27\3\2\2\2\u00a2\u00a6\5$\23\2\u00a3\u00a5\5\34\17\2")
        buf.write(u"\u00a4\u00a3\3\2\2\2\u00a5\u00a8\3\2\2\2\u00a6\u00a4")
        buf.write(u"\3\2\2\2\u00a6\u00a7\3\2\2\2\u00a7\31\3\2\2\2\u00a8\u00a6")
        buf.write(u"\3\2\2\2\u00a9\u00ad\5&\24\2\u00aa\u00ac\5\34\17\2\u00ab")
        buf.write(u"\u00aa\3\2\2\2\u00ac\u00af\3\2\2\2\u00ad\u00ab\3\2\2")
        buf.write(u"\2\u00ad\u00ae\3\2\2\2\u00ae\33\3\2\2\2\u00af\u00ad\3")
        buf.write(u"\2\2\2\u00b0\u00b3\7R\2\2\u00b1\u00b3\5\36\20\2\u00b2")
        buf.write(u"\u00b0\3\2\2\2\u00b2\u00b1\3\2\2\2\u00b3\35\3\2\2\2\u00b4")
        buf.write(u"\u00ba\7\21\2\2\u00b5\u00bb\5\"\22\2\u00b6\u00bb\5 \21")
        buf.write(u"\2\u00b7\u00b8\5\"\22\2\u00b8\u00b9\5 \21\2\u00b9\u00bb")
        buf.write(u"\3\2\2\2\u00ba\u00b5\3\2\2\2\u00ba\u00b6\3\2\2\2\u00ba")
        buf.write(u"\u00b7\3\2\2\2\u00bb\37\3\2\2\2\u00bc\u00bd\7\63\2\2")
        buf.write(u"\u00bd\u00c0\7\n\2\2\u00be\u00c1\5\f\7\2\u00bf\u00c1")
        buf.write(u"\5\n\6\2\u00c0\u00be\3\2\2\2\u00c0\u00bf\3\2\2\2\u00c1")
        buf.write(u"\u00c2\3\2\2\2\u00c2\u00c3\7\13\2\2\u00c3!\3\2\2\2\u00c4")
        buf.write(u"\u00c5\7\64\2\2\u00c5\u00c8\7\n\2\2\u00c6\u00c9\5\f\7")
        buf.write(u"\2\u00c7\u00c9\5\n\6\2\u00c8\u00c6\3\2\2\2\u00c8\u00c7")
        buf.write(u"\3\2\2\2\u00c9\u00ca\3\2\2\2\u00ca\u00cb\7\13\2\2\u00cb")
        buf.write(u"#\3\2\2\2\u00cc\u00cd\b\23\1\2\u00cd\u00ce\5(\25\2\u00ce")
        buf.write(u"\u00dd\3\2\2\2\u00cf\u00d0\f\4\2\2\u00d0\u00d6\7\64\2")
        buf.write(u"\2\u00d1\u00d7\5\60\31\2\u00d2\u00d3\7\n\2\2\u00d3\u00d4")
        buf.write(u"\5\f\7\2\u00d4\u00d5\7\13\2\2\u00d5\u00d7\3\2\2\2\u00d6")
        buf.write(u"\u00d1\3\2\2\2\u00d6\u00d2\3\2\2\2\u00d7\u00d9\3\2\2")
        buf.write(u"\2\u00d8\u00da\5F$\2\u00d9\u00d8\3\2\2\2\u00d9\u00da")
        buf.write(u"\3\2\2\2\u00da\u00dc\3\2\2\2\u00db\u00cf\3\2\2\2\u00dc")
        buf.write(u"\u00df\3\2\2\2\u00dd\u00db\3\2\2\2\u00dd\u00de\3\2\2")
        buf.write(u"\2\u00de%\3\2\2\2\u00df\u00dd\3\2\2\2\u00e0\u00e1\b\24")
        buf.write(u"\1\2\u00e1\u00e2\5*\26\2\u00e2\u00f1\3\2\2\2\u00e3\u00e4")
        buf.write(u"\f\4\2\2\u00e4\u00ea\7\64\2\2\u00e5\u00eb\5\60\31\2\u00e6")
        buf.write(u"\u00e7\7\n\2\2\u00e7\u00e8\5\f\7\2\u00e8\u00e9\7\13\2")
        buf.write(u"\2\u00e9\u00eb\3\2\2\2\u00ea\u00e5\3\2\2\2\u00ea\u00e6")
        buf.write(u"\3\2\2\2\u00eb\u00ed\3\2\2\2\u00ec\u00ee\5F$\2\u00ed")
        buf.write(u"\u00ec\3\2\2\2\u00ed\u00ee\3\2\2\2\u00ee\u00f0\3\2\2")
        buf.write(u"\2\u00ef\u00e3\3\2\2\2\u00f0\u00f3\3\2\2\2\u00f1\u00ef")
        buf.write(u"\3\2\2\2\u00f1\u00f2\3\2\2\2\u00f2\'\3\2\2\2\u00f3\u00f1")
        buf.write(u"\3\2\2\2\u00f4\u00fb\5,\27\2\u00f5\u00fb\5.\30\2\u00f6")
        buf.write(u"\u00fb\5<\37\2\u00f7\u00fb\5\60\31\2\u00f8\u00fb\5\66")
        buf.write(u"\34\2\u00f9\u00fb\58\35\2\u00fa\u00f4\3\2\2\2\u00fa\u00f5")
        buf.write(u"\3\2\2\2\u00fa\u00f6\3\2\2\2\u00fa\u00f7\3\2\2\2\u00fa")
        buf.write(u"\u00f8\3\2\2\2\u00fa\u00f9\3\2\2\2\u00fb)\3\2\2\2\u00fc")
        buf.write(u"\u0102\5,\27\2\u00fd\u0102\5.\30\2\u00fe\u0102\5\60\31")
        buf.write(u"\2\u00ff\u0102\5\66\34\2\u0100\u0102\58\35\2\u0101\u00fc")
        buf.write(u"\3\2\2\2\u0101\u00fd\3\2\2\2\u0101\u00fe\3\2\2\2\u0101")
        buf.write(u"\u00ff\3\2\2\2\u0101\u0100\3\2\2\2\u0102+\3\2\2\2\u0103")
        buf.write(u"\u0104\7\b\2\2\u0104\u0105\5\f\7\2\u0105\u0106\7\t\2")
        buf.write(u"\2\u0106\u0110\3\2\2\2\u0107\u0108\7\f\2\2\u0108\u0109")
        buf.write(u"\5\f\7\2\u0109\u010a\7\r\2\2\u010a\u0110\3\2\2\2\u010b")
        buf.write(u"\u010c\7\n\2\2\u010c\u010d\5\f\7\2\u010d\u010e\7\13\2")
        buf.write(u"\2\u010e\u0110\3\2\2\2\u010f\u0103\3\2\2\2\u010f\u0107")
        buf.write(u"\3\2\2\2\u010f\u010b\3\2\2\2\u0110-\3\2\2\2\u0111\u0112")
        buf.write(u"\7\21\2\2\u0112\u0113\5\f\7\2\u0113\u0114\7\21\2\2\u0114")
        buf.write(u"/\3\2\2\2\u0115\u0117\t\6\2\2\u0116\u0118\5F$\2\u0117")
        buf.write(u"\u0116\3\2\2\2\u0117\u0118\3\2\2\2\u0118\u011d\3\2\2")
        buf.write(u"\2\u0119\u011d\7=\2\2\u011a\u011d\7;\2\2\u011b\u011d")
        buf.write(u"\5\62\32\2\u011c\u0115\3\2\2\2\u011c\u0119\3\2\2\2\u011c")
        buf.write(u"\u011a\3\2\2\2\u011c\u011b\3\2\2\2\u011d\61\3\2\2\2\u011e")
        buf.write(u"\u011f\7\62\2\2\u011f\u0120\7\n\2\2\u0120\u0121\5\64")
        buf.write(u"\33\2\u0121\u0122\7\13\2\2\u0122\63\3\2\2\2\u0123\u0125")
        buf.write(u"\7<\2\2\u0124\u0123\3\2\2\2\u0125\u0128\3\2\2\2\u0126")
        buf.write(u"\u0124\3\2\2\2\u0126\u0127\3\2\2\2\u0127\65\3\2\2\2\u0128")
        buf.write(u"\u0126\3\2\2\2\u0129\u012a\7.\2\2\u012a\u012b\7\n\2\2")
        buf.write(u"\u012b\u012c\5\f\7\2\u012c\u012d\7\13\2\2\u012d\u012e")
        buf.write(u"\7\n\2\2\u012e\u012f\5\f\7\2\u012f\u0130\7\13\2\2\u0130")
        buf.write(u"\67\3\2\2\2\u0131\u0132\t\7\2\2\u0132\u0133\7\n\2\2\u0133")
        buf.write(u"\u0134\5\f\7\2\u0134\u0135\7\13\2\2\u0135\u0136\7\n\2")
        buf.write(u"\2\u0136\u0137\5\f\7\2\u0137\u0138\7\13\2\2\u01389\3")
        buf.write(u"\2\2\2\u0139\u013a\t\b\2\2\u013a;\3\2\2\2\u013b\u0148")
        buf.write(u"\5:\36\2\u013c\u013e\5F$\2\u013d\u013c\3\2\2\2\u013d")
        buf.write(u"\u013e\3\2\2\2\u013e\u0140\3\2\2\2\u013f\u0141\5H%\2")
        buf.write(u"\u0140\u013f\3\2\2\2\u0140\u0141\3\2\2\2\u0141\u0149")
        buf.write(u"\3\2\2\2\u0142\u0144\5H%\2\u0143\u0142\3\2\2\2\u0143")
        buf.write(u"\u0144\3\2\2\2\u0144\u0146\3\2\2\2\u0145\u0147\5F$\2")
        buf.write(u"\u0146\u0145\3\2\2\2\u0146\u0147\3\2\2\2\u0147\u0149")
        buf.write(u"\3\2\2\2\u0148\u013d\3\2\2\2\u0148\u0143\3\2\2\2\u0149")
        buf.write(u"\u014f\3\2\2\2\u014a\u014b\7\b\2\2\u014b\u014c\5B\"\2")
        buf.write(u"\u014c\u014d\7\t\2\2\u014d\u0150\3\2\2\2\u014e\u0150")
        buf.write(u"\5D#\2\u014f\u014a\3\2\2\2\u014f\u014e\3\2\2\2\u0150")
        buf.write(u"\u0188\3\2\2\2\u0151\u0153\t\6\2\2\u0152\u0154\5F$\2")
        buf.write(u"\u0153\u0152\3\2\2\2\u0153\u0154\3\2\2\2\u0154\u0155")
        buf.write(u"\3\2\2\2\u0155\u0156\7\b\2\2\u0156\u0157\5> \2\u0157")
        buf.write(u"\u0158\7\t\2\2\u0158\u0188\3\2\2\2\u0159\u015b\7\23\2")
        buf.write(u"\2\u015a\u015c\7\63\2\2\u015b\u015a\3\2\2\2\u015b\u015c")
        buf.write(u"\3\2\2\2\u015c\u0163\3\2\2\2\u015d\u015e\5F$\2\u015e")
        buf.write(u"\u015f\5H%\2\u015f\u0164\3\2\2\2\u0160\u0161\5H%\2\u0161")
        buf.write(u"\u0162\5F$\2\u0162\u0164\3\2\2\2\u0163\u015d\3\2\2\2")
        buf.write(u"\u0163\u0160\3\2\2\2\u0163\u0164\3\2\2\2\u0164\u016b")
        buf.write(u"\3\2\2\2\u0165\u0167\5\16\b\2\u0166\u0165\3\2\2\2\u0166")
        buf.write(u"\u0167\3\2\2\2\u0167\u0168\3\2\2\2\u0168\u016c\7;\2\2")
        buf.write(u"\u0169\u016c\5\66\34\2\u016a\u016c\5\16\b\2\u016b\u0166")
        buf.write(u"\3\2\2\2\u016b\u0169\3\2\2\2\u016b\u016a\3\2\2\2\u016c")
        buf.write(u"\u0188\3\2\2\2\u016d\u0172\7*\2\2\u016e\u016f\7\f\2\2")
        buf.write(u"\u016f\u0170\5\f\7\2\u0170\u0171\7\r\2\2\u0171\u0173")
        buf.write(u"\3\2\2\2\u0172\u016e\3\2\2\2\u0172\u0173\3\2\2\2\u0173")
        buf.write(u"\u0174\3\2\2\2\u0174\u0175\7\n\2\2\u0175\u0176\5\f\7")
        buf.write(u"\2\u0176\u0177\7\13\2\2\u0177\u0188\3\2\2\2\u0178\u017f")
        buf.write(u"\t\t\2\2\u0179\u017a\5J&\2\u017a\u017b\5H%\2\u017b\u0180")
        buf.write(u"\3\2\2\2\u017c\u017d\5H%\2\u017d\u017e\5J&\2\u017e\u0180")
        buf.write(u"\3\2\2\2\u017f\u0179\3\2\2\2\u017f\u017c\3\2\2\2\u0180")
        buf.write(u"\u0181\3\2\2\2\u0181\u0182\5\20\t\2\u0182\u0188\3\2\2")
        buf.write(u"\2\u0183\u0184\7\22\2\2\u0184\u0185\5@!\2\u0185\u0186")
        buf.write(u"\5\20\t\2\u0186\u0188\3\2\2\2\u0187\u013b\3\2\2\2\u0187")
        buf.write(u"\u0151\3\2\2\2\u0187\u0159\3\2\2\2\u0187\u016d\3\2\2")
        buf.write(u"\2\u0187\u0178\3\2\2\2\u0187\u0183\3\2\2\2\u0188=\3\2")
        buf.write(u"\2\2\u0189\u018a\5\f\7\2\u018a\u018b\7\66\2\2\u018b\u018c")
        buf.write(u"\5> \2\u018c\u018f\3\2\2\2\u018d\u018f\5\f\7\2\u018e")
        buf.write(u"\u0189\3\2\2\2\u018e\u018d\3\2\2\2\u018f?\3\2\2\2\u0190")
        buf.write(u"\u0191\7\63\2\2\u0191\u0192\7\n\2\2\u0192\u0193\t\6\2")
        buf.write(u"\2\u0193\u0194\5\2\2\2\u0194\u0199\5\f\7\2\u0195\u0196")
        buf.write(u"\7\64\2\2\u0196\u0197\7\n\2\2\u0197\u0198\t\4\2\2\u0198")
        buf.write(u"\u019a\7\13\2\2\u0199\u0195\3\2\2\2\u0199\u019a\3\2\2")
        buf.write(u"\2\u019a\u019b\3\2\2\2\u019b\u019c\7\13\2\2\u019cA\3")
        buf.write(u"\2\2\2\u019d\u01a3\5\f\7\2\u019e\u019f\5\f\7\2\u019f")
        buf.write(u"\u01a0\7\66\2\2\u01a0\u01a1\5B\"\2\u01a1\u01a3\3\2\2")
        buf.write(u"\2\u01a2\u019d\3\2\2\2\u01a2\u019e\3\2\2\2\u01a3C\3\2")
        buf.write(u"\2\2\u01a4\u01a5\5\22\n\2\u01a5E\3\2\2\2\u01a6\u01ac")
        buf.write(u"\7\63\2\2\u01a7\u01ad\5\60\31\2\u01a8\u01a9\7\n\2\2\u01a9")
        buf.write(u"\u01aa\5\f\7\2\u01aa\u01ab\7\13\2\2\u01ab\u01ad\3\2\2")
        buf.write(u"\2\u01ac\u01a7\3\2\2\2\u01ac\u01a8\3\2\2\2\u01adG\3\2")
        buf.write(u"\2\2\u01ae\u01b4\7\64\2\2\u01af\u01b5\5\60\31\2\u01b0")
        buf.write(u"\u01b1\7\n\2\2\u01b1\u01b2\5\f\7\2\u01b2\u01b3\7\13\2")
        buf.write(u"\2\u01b3\u01b5\3\2\2\2\u01b4\u01af\3\2\2\2\u01b4\u01b0")
        buf.write(u"\3\2\2\2\u01b5I\3\2\2\2\u01b6\u01b7\7\63\2\2\u01b7\u01ba")
        buf.write(u"\7\n\2\2\u01b8\u01bb\5\f\7\2\u01b9\u01bb\5\n\6\2\u01ba")
        buf.write(u"\u01b8\3\2\2\2\u01ba\u01b9\3\2\2\2\u01bb\u01bc\3\2\2")
        buf.write(u"\2\u01bc\u01bd\7\13\2\2\u01bdK\3\2\2\2\u01be\u01bf\7")
        buf.write(u"\63\2\2\u01bf\u01c2\7\n\2\2\u01c0\u01c3\5\f\7\2\u01c1")
        buf.write(u"\u01c3\5\n\6\2\u01c2\u01c0\3\2\2\2\u01c2\u01c1\3\2\2")
        buf.write(u"\2\u01c3\u01c4\3\2\2\2\u01c4\u01c5\7\13\2\2\u01c5M\3")
        buf.write(u"\2\2\2\63Y\\du\u0080\u008b\u0093\u0095\u009d\u00a0\u00a6")
        buf.write(u"\u00ad\u00b2\u00ba\u00c0\u00c8\u00d6\u00d9\u00dd\u00ea")
        buf.write(u"\u00ed\u00f1\u00fa\u0101\u010f\u0117\u011c\u0126\u013d")
        buf.write(u"\u0140\u0143\u0146\u0148\u014f\u0153\u015b\u0163\u0166")
        buf.write(u"\u016b\u0172\u017f\u0187\u018e\u0199\u01a2\u01ac\u01b4")
        buf.write(u"\u01ba\u01c2")
        return buf.getvalue()


class LaTeXParser ( Parser ):

    grammarFileName = "LaTeX.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ u"<INVALID>", u"<INVALID>", u"'+'", u"'-'", u"'*'", 
                     u"'/'", u"'('", u"')'", u"'{'", u"'}'", u"'['", u"']'", 
                     u"':'", u"<INVALID>", u"<INVALID>", u"'|'", u"'\\lim'", 
                     u"'\\int'", u"'\\sum'", u"'\\prod'", u"'\\log'", u"'\\ln'", 
                     u"'\\sin'", u"'\\cos'", u"'\\tan'", u"'\\csc'", u"'\\sec'", 
                     u"'\\cot'", u"'\\arcsin'", u"'\\arccos'", u"'\\arctan'", 
                     u"'\\arccsc'", u"'\\arcsec'", u"'\\arccot'", u"'\\sinh'", 
                     u"'\\cosh'", u"'\\tanh'", u"'\\arsinh'", u"'\\arcosh'", 
                     u"'\\artanh'", u"'\\sqrt'", u"'\\times'", u"'\\cdot'", 
                     u"'\\div'", u"'\\frac'", u"'\\binom'", u"'\\dbinom'", 
                     u"'\\tbinom'", u"'\\mathit'", u"'_'", u"'^'", u"'&'", 
                     u"','", u"<INVALID>", u"<INVALID>", u"'.'", u"'\\rm'", 
                     u"<INVALID>", u"<INVALID>", u"<INVALID>", u"'='", u"'\\doteq'", 
                     u"'\\equiv'", u"'\\approx'", u"'\\cong'", u"'\\simeq'", 
                     u"'\\sim'", u"'\\propto'", u"<INVALID>", u"'<'", u"'\\nless'", 
                     u"<INVALID>", u"<INVALID>", u"<INVALID>", u"<INVALID>", 
                     u"<INVALID>", u"'>'", u"'\\ngtr'", u"<INVALID>", u"<INVALID>", 
                     u"'!'" ]

    symbolicNames = [ u"<INVALID>", u"WS", u"ADD", u"SUB", u"MUL", u"DIV", 
                      u"L_PAREN", u"R_PAREN", u"L_BRACE", u"R_BRACE", u"L_BRACKET", 
                      u"R_BRACKET", u"COLON", u"RIGHTARROW", u"LONGRIGHTARROW", 
                      u"BAR", u"FUNC_LIM", u"FUNC_INT", u"FUNC_SUM", u"FUNC_PROD", 
                      u"FUNC_LOG", u"FUNC_LN", u"FUNC_SIN", u"FUNC_COS", 
                      u"FUNC_TAN", u"FUNC_CSC", u"FUNC_SEC", u"FUNC_COT", 
                      u"FUNC_ARCSIN", u"FUNC_ARCCOS", u"FUNC_ARCTAN", u"FUNC_ARCCSC", 
                      u"FUNC_ARCSEC", u"FUNC_ARCCOT", u"FUNC_SINH", u"FUNC_COSH", 
                      u"FUNC_TANH", u"FUNC_ARSINH", u"FUNC_ARCOSH", u"FUNC_ARTANH", 
                      u"FUNC_SQRT", u"CMD_TIMES", u"CMD_CDOT", u"CMD_DIV", 
                      u"CMD_FRAC", u"CMD_BINOM", u"CMD_DBINOM", u"CMD_TBINOM", 
                      u"CMD_MATHIT", u"UNDERSCORE", u"CARET", u"AMPERSAND", 
                      u"COMMA", u"LEFT", u"RIGHT", u"DOT", u"RM", u"DIFFERENTIAL", 
                      u"LETTER", u"NUMBER", u"EQUAL", u"DOTEQ", u"EQUIV", 
                      u"APPROX", u"CONG", u"SIMEQ", u"SIM", u"PROPTO", u"NEQ", 
                      u"LT", u"NLESS", u"LTE", u"PROPERSUBSET", u"NOTPROPERSUBSET", 
                      u"SUBSET", u"NOTSUBSET", u"GT", u"NGTR", u"GTE", u"NGEQ", 
                      u"BANG", u"SYMBOL" ]

    RULE_lim_approach_sym = 0
    RULE_relation_operators = 1
    RULE_math = 2
    RULE_relation = 3
    RULE_equality = 4
    RULE_expr = 5
    RULE_additive = 6
    RULE_mp = 7
    RULE_mp_nofunc = 8
    RULE_unary = 9
    RULE_unary_nofunc = 10
    RULE_postfix = 11
    RULE_postfix_nofunc = 12
    RULE_postfix_op = 13
    RULE_eval_at = 14
    RULE_eval_at_sub = 15
    RULE_eval_at_sup = 16
    RULE_exp = 17
    RULE_exp_nofunc = 18
    RULE_comp = 19
    RULE_comp_nofunc = 20
    RULE_group = 21
    RULE_abs_group = 22
    RULE_atom = 23
    RULE_mathit = 24
    RULE_mathit_text = 25
    RULE_frac = 26
    RULE_binom = 27
    RULE_func_normal = 28
    RULE_func = 29
    RULE_args = 30
    RULE_limit_sub = 31
    RULE_func_arg = 32
    RULE_func_arg_noparens = 33
    RULE_subexpr = 34
    RULE_supexpr = 35
    RULE_subeq = 36
    RULE_supeq = 37

    ruleNames =  [ u"lim_approach_sym", u"relation_operators", u"math", 
                   u"relation", u"equality", u"expr", u"additive", u"mp", 
                   u"mp_nofunc", u"unary", u"unary_nofunc", u"postfix", 
                   u"postfix_nofunc", u"postfix_op", u"eval_at", u"eval_at_sub", 
                   u"eval_at_sup", u"exp", u"exp_nofunc", u"comp", u"comp_nofunc", 
                   u"group", u"abs_group", u"atom", u"mathit", u"mathit_text", 
                   u"frac", u"binom", u"func_normal", u"func", u"args", 
                   u"limit_sub", u"func_arg", u"func_arg_noparens", u"subexpr", 
                   u"supexpr", u"subeq", u"supeq" ]

    EOF = Token.EOF
    WS=1
    ADD=2
    SUB=3
    MUL=4
    DIV=5
    L_PAREN=6
    R_PAREN=7
    L_BRACE=8
    R_BRACE=9
    L_BRACKET=10
    R_BRACKET=11
    COLON=12
    RIGHTARROW=13
    LONGRIGHTARROW=14
    BAR=15
    FUNC_LIM=16
    FUNC_INT=17
    FUNC_SUM=18
    FUNC_PROD=19
    FUNC_LOG=20
    FUNC_LN=21
    FUNC_SIN=22
    FUNC_COS=23
    FUNC_TAN=24
    FUNC_CSC=25
    FUNC_SEC=26
    FUNC_COT=27
    FUNC_ARCSIN=28
    FUNC_ARCCOS=29
    FUNC_ARCTAN=30
    FUNC_ARCCSC=31
    FUNC_ARCSEC=32
    FUNC_ARCCOT=33
    FUNC_SINH=34
    FUNC_COSH=35
    FUNC_TANH=36
    FUNC_ARSINH=37
    FUNC_ARCOSH=38
    FUNC_ARTANH=39
    FUNC_SQRT=40
    CMD_TIMES=41
    CMD_CDOT=42
    CMD_DIV=43
    CMD_FRAC=44
    CMD_BINOM=45
    CMD_DBINOM=46
    CMD_TBINOM=47
    CMD_MATHIT=48
    UNDERSCORE=49
    CARET=50
    AMPERSAND=51
    COMMA=52
    LEFT=53
    RIGHT=54
    DOT=55
    RM=56
    DIFFERENTIAL=57
    LETTER=58
    NUMBER=59
    EQUAL=60
    DOTEQ=61
    EQUIV=62
    APPROX=63
    CONG=64
    SIMEQ=65
    SIM=66
    PROPTO=67
    NEQ=68
    LT=69
    NLESS=70
    LTE=71
    PROPERSUBSET=72
    NOTPROPERSUBSET=73
    SUBSET=74
    NOTSUBSET=75
    GT=76
    NGTR=77
    GTE=78
    NGEQ=79
    BANG=80
    SYMBOL=81

    def __init__(self, input, output=sys.stdout):
        super(LaTeXParser, self).__init__(input, output=output)
        self.checkVersion("4.7.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None



    class Lim_approach_symContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(LaTeXParser.Lim_approach_symContext, self).__init__(parent, invokingState)
            self.parser = parser

        def RIGHTARROW(self):
            return self.getToken(LaTeXParser.RIGHTARROW, 0)

        def LONGRIGHTARROW(self):
            return self.getToken(LaTeXParser.LONGRIGHTARROW, 0)

        def getRuleIndex(self):
            return LaTeXParser.RULE_lim_approach_sym




    def lim_approach_sym(self):

        localctx = LaTeXParser.Lim_approach_symContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_lim_approach_sym)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 76
            _la = self._input.LA(1)
            if not(_la==LaTeXParser.RIGHTARROW or _la==LaTeXParser.LONGRIGHTARROW):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Relation_operatorsContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(LaTeXParser.Relation_operatorsContext, self).__init__(parent, invokingState)
            self.parser = parser

        def EQUAL(self):
            return self.getToken(LaTeXParser.EQUAL, 0)

        def DOTEQ(self):
            return self.getToken(LaTeXParser.DOTEQ, 0)

        def EQUIV(self):
            return self.getToken(LaTeXParser.EQUIV, 0)

        def APPROX(self):
            return self.getToken(LaTeXParser.APPROX, 0)

        def CONG(self):
            return self.getToken(LaTeXParser.CONG, 0)

        def SIMEQ(self):
            return self.getToken(LaTeXParser.SIMEQ, 0)

        def SIM(self):
            return self.getToken(LaTeXParser.SIM, 0)

        def PROPTO(self):
            return self.getToken(LaTeXParser.PROPTO, 0)

        def NEQ(self):
            return self.getToken(LaTeXParser.NEQ, 0)

        def LT(self):
            return self.getToken(LaTeXParser.LT, 0)

        def NLESS(self):
            return self.getToken(LaTeXParser.NLESS, 0)

        def LTE(self):
            return self.getToken(LaTeXParser.LTE, 0)

        def PROPERSUBSET(self):
            return self.getToken(LaTeXParser.PROPERSUBSET, 0)

        def NOTPROPERSUBSET(self):
            return self.getToken(LaTeXParser.NOTPROPERSUBSET, 0)

        def SUBSET(self):
            return self.getToken(LaTeXParser.SUBSET, 0)

        def NOTSUBSET(self):
            return self.getToken(LaTeXParser.NOTSUBSET, 0)

        def GT(self):
            return self.getToken(LaTeXParser.GT, 0)

        def NGTR(self):
            return self.getToken(LaTeXParser.NGTR, 0)

        def GTE(self):
            return self.getToken(LaTeXParser.GTE, 0)

        def NGEQ(self):
            return self.getToken(LaTeXParser.NGEQ, 0)

        def getRuleIndex(self):
            return LaTeXParser.RULE_relation_operators




    def relation_operators(self):

        localctx = LaTeXParser.Relation_operatorsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_relation_operators)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 78
            _la = self._input.LA(1)
            if not(((((_la - 60)) & ~0x3f) == 0 and ((1 << (_la - 60)) & ((1 << (LaTeXParser.EQUAL - 60)) | (1 << (LaTeXParser.DOTEQ - 60)) | (1 << (LaTeXParser.EQUIV - 60)) | (1 << (LaTeXParser.APPROX - 60)) | (1 << (LaTeXParser.CONG - 60)) | (1 << (LaTeXParser.SIMEQ - 60)) | (1 << (LaTeXParser.SIM - 60)) | (1 << (LaTeXParser.PROPTO - 60)) | (1 << (LaTeXParser.NEQ - 60)) | (1 << (LaTeXParser.LT - 60)) | (1 << (LaTeXParser.NLESS - 60)) | (1 << (LaTeXParser.LTE - 60)) | (1 << (LaTeXParser.PROPERSUBSET - 60)) | (1 << (LaTeXParser.NOTPROPERSUBSET - 60)) | (1 << (LaTeXParser.SUBSET - 60)) | (1 << (LaTeXParser.NOTSUBSET - 60)) | (1 << (LaTeXParser.GT - 60)) | (1 << (LaTeXParser.NGTR - 60)) | (1 << (LaTeXParser.GTE - 60)) | (1 << (LaTeXParser.NGEQ - 60)))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class MathContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(LaTeXParser.MathContext, self).__init__(parent, invokingState)
            self.parser = parser

        def relation(self):
            return self.getTypedRuleContext(LaTeXParser.RelationContext,0)


        def getRuleIndex(self):
            return LaTeXParser.RULE_math




    def math(self):

        localctx = LaTeXParser.MathContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_math)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 80
            self.relation(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class RelationContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(LaTeXParser.RelationContext, self).__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(LaTeXParser.ExprContext,0)


        def LEFT(self):
            return self.getToken(LaTeXParser.LEFT, 0)

        def RIGHT(self):
            return self.getToken(LaTeXParser.RIGHT, 0)

        def DOT(self):
            return self.getToken(LaTeXParser.DOT, 0)

        def relation(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(LaTeXParser.RelationContext)
            else:
                return self.getTypedRuleContext(LaTeXParser.RelationContext,i)


        def relation_operators(self):
            return self.getTypedRuleContext(LaTeXParser.Relation_operatorsContext,0)


        def getRuleIndex(self):
            return LaTeXParser.RULE_relation



    def relation(self, _p=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = LaTeXParser.RelationContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 6
        self.enterRecursionRule(localctx, 6, self.RULE_relation, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 90
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [LaTeXParser.ADD, LaTeXParser.SUB, LaTeXParser.L_PAREN, LaTeXParser.L_BRACE, LaTeXParser.L_BRACKET, LaTeXParser.BAR, LaTeXParser.FUNC_LIM, LaTeXParser.FUNC_INT, LaTeXParser.FUNC_SUM, LaTeXParser.FUNC_PROD, LaTeXParser.FUNC_LOG, LaTeXParser.FUNC_LN, LaTeXParser.FUNC_SIN, LaTeXParser.FUNC_COS, LaTeXParser.FUNC_TAN, LaTeXParser.FUNC_CSC, LaTeXParser.FUNC_SEC, LaTeXParser.FUNC_COT, LaTeXParser.FUNC_ARCSIN, LaTeXParser.FUNC_ARCCOS, LaTeXParser.FUNC_ARCTAN, LaTeXParser.FUNC_ARCCSC, LaTeXParser.FUNC_ARCSEC, LaTeXParser.FUNC_ARCCOT, LaTeXParser.FUNC_SINH, LaTeXParser.FUNC_COSH, LaTeXParser.FUNC_TANH, LaTeXParser.FUNC_ARSINH, LaTeXParser.FUNC_ARCOSH, LaTeXParser.FUNC_ARTANH, LaTeXParser.FUNC_SQRT, LaTeXParser.CMD_FRAC, LaTeXParser.CMD_BINOM, LaTeXParser.CMD_DBINOM, LaTeXParser.CMD_TBINOM, LaTeXParser.CMD_MATHIT, LaTeXParser.DIFFERENTIAL, LaTeXParser.LETTER, LaTeXParser.NUMBER, LaTeXParser.SYMBOL]:
                self.state = 83
                self.expr()
                pass
            elif token in [LaTeXParser.LEFT]:
                self.state = 84
                self.match(LaTeXParser.LEFT)
                self.state = 87
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [LaTeXParser.DOT]:
                    self.state = 85
                    self.match(LaTeXParser.DOT)
                    pass
                elif token in [LaTeXParser.ADD, LaTeXParser.SUB, LaTeXParser.L_PAREN, LaTeXParser.L_BRACE, LaTeXParser.L_BRACKET, LaTeXParser.BAR, LaTeXParser.FUNC_LIM, LaTeXParser.FUNC_INT, LaTeXParser.FUNC_SUM, LaTeXParser.FUNC_PROD, LaTeXParser.FUNC_LOG, LaTeXParser.FUNC_LN, LaTeXParser.FUNC_SIN, LaTeXParser.FUNC_COS, LaTeXParser.FUNC_TAN, LaTeXParser.FUNC_CSC, LaTeXParser.FUNC_SEC, LaTeXParser.FUNC_COT, LaTeXParser.FUNC_ARCSIN, LaTeXParser.FUNC_ARCCOS, LaTeXParser.FUNC_ARCTAN, LaTeXParser.FUNC_ARCCSC, LaTeXParser.FUNC_ARCSEC, LaTeXParser.FUNC_ARCCOT, LaTeXParser.FUNC_SINH, LaTeXParser.FUNC_COSH, LaTeXParser.FUNC_TANH, LaTeXParser.FUNC_ARSINH, LaTeXParser.FUNC_ARCOSH, LaTeXParser.FUNC_ARTANH, LaTeXParser.FUNC_SQRT, LaTeXParser.CMD_FRAC, LaTeXParser.CMD_BINOM, LaTeXParser.CMD_DBINOM, LaTeXParser.CMD_TBINOM, LaTeXParser.CMD_MATHIT, LaTeXParser.LEFT, LaTeXParser.DIFFERENTIAL, LaTeXParser.LETTER, LaTeXParser.NUMBER, LaTeXParser.SYMBOL]:
                    self.state = 86
                    self.relation(0)
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 89
                self.match(LaTeXParser.RIGHT)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 98
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,2,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = LaTeXParser.RelationContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_relation)
                    self.state = 92
                    if not self.precpred(self._ctx, 3):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                    self.state = 93
                    self.relation_operators()
                    self.state = 94
                    self.relation(4) 
                self.state = 100
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,2,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class EqualityContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(LaTeXParser.EqualityContext, self).__init__(parent, invokingState)
            self.parser = parser

        def expr(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(LaTeXParser.ExprContext)
            else:
                return self.getTypedRuleContext(LaTeXParser.ExprContext,i)


        def EQUAL(self):
            return self.getToken(LaTeXParser.EQUAL, 0)

        def getRuleIndex(self):
            return LaTeXParser.RULE_equality




    def equality(self):

        localctx = LaTeXParser.EqualityContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_equality)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 101
            self.expr()
            self.state = 102
            self.match(LaTeXParser.EQUAL)
            self.state = 103
            self.expr()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ExprContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(LaTeXParser.ExprContext, self).__init__(parent, invokingState)
            self.parser = parser

        def additive(self):
            return self.getTypedRuleContext(LaTeXParser.AdditiveContext,0)


        def getRuleIndex(self):
            return LaTeXParser.RULE_expr




    def expr(self):

        localctx = LaTeXParser.ExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_expr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 105
            self.additive(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class AdditiveContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(LaTeXParser.AdditiveContext, self).__init__(parent, invokingState)
            self.parser = parser

        def mp(self):
            return self.getTypedRuleContext(LaTeXParser.MpContext,0)


        def additive(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(LaTeXParser.AdditiveContext)
            else:
                return self.getTypedRuleContext(LaTeXParser.AdditiveContext,i)


        def ADD(self):
            return self.getToken(LaTeXParser.ADD, 0)

        def SUB(self):
            return self.getToken(LaTeXParser.SUB, 0)

        def getRuleIndex(self):
            return LaTeXParser.RULE_additive



    def additive(self, _p=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = LaTeXParser.AdditiveContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 12
        self.enterRecursionRule(localctx, 12, self.RULE_additive, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 108
            self.mp(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 115
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,3,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = LaTeXParser.AdditiveContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_additive)
                    self.state = 110
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 111
                    _la = self._input.LA(1)
                    if not(_la==LaTeXParser.ADD or _la==LaTeXParser.SUB):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 112
                    self.additive(3) 
                self.state = 117
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,3,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class MpContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(LaTeXParser.MpContext, self).__init__(parent, invokingState)
            self.parser = parser

        def unary(self):
            return self.getTypedRuleContext(LaTeXParser.UnaryContext,0)


        def mp(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(LaTeXParser.MpContext)
            else:
                return self.getTypedRuleContext(LaTeXParser.MpContext,i)


        def MUL(self):
            return self.getToken(LaTeXParser.MUL, 0)

        def CMD_TIMES(self):
            return self.getToken(LaTeXParser.CMD_TIMES, 0)

        def CMD_CDOT(self):
            return self.getToken(LaTeXParser.CMD_CDOT, 0)

        def DIV(self):
            return self.getToken(LaTeXParser.DIV, 0)

        def CMD_DIV(self):
            return self.getToken(LaTeXParser.CMD_DIV, 0)

        def COLON(self):
            return self.getToken(LaTeXParser.COLON, 0)

        def getRuleIndex(self):
            return LaTeXParser.RULE_mp



    def mp(self, _p=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = LaTeXParser.MpContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 14
        self.enterRecursionRule(localctx, 14, self.RULE_mp, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 119
            self.unary()
            self._ctx.stop = self._input.LT(-1)
            self.state = 126
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,4,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = LaTeXParser.MpContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_mp)
                    self.state = 121
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 122
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << LaTeXParser.MUL) | (1 << LaTeXParser.DIV) | (1 << LaTeXParser.COLON) | (1 << LaTeXParser.CMD_TIMES) | (1 << LaTeXParser.CMD_CDOT) | (1 << LaTeXParser.CMD_DIV))) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 123
                    self.mp(3) 
                self.state = 128
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,4,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class Mp_nofuncContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(LaTeXParser.Mp_nofuncContext, self).__init__(parent, invokingState)
            self.parser = parser

        def unary_nofunc(self):
            return self.getTypedRuleContext(LaTeXParser.Unary_nofuncContext,0)


        def mp_nofunc(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(LaTeXParser.Mp_nofuncContext)
            else:
                return self.getTypedRuleContext(LaTeXParser.Mp_nofuncContext,i)


        def MUL(self):
            return self.getToken(LaTeXParser.MUL, 0)

        def CMD_TIMES(self):
            return self.getToken(LaTeXParser.CMD_TIMES, 0)

        def CMD_CDOT(self):
            return self.getToken(LaTeXParser.CMD_CDOT, 0)

        def DIV(self):
            return self.getToken(LaTeXParser.DIV, 0)

        def CMD_DIV(self):
            return self.getToken(LaTeXParser.CMD_DIV, 0)

        def COLON(self):
            return self.getToken(LaTeXParser.COLON, 0)

        def getRuleIndex(self):
            return LaTeXParser.RULE_mp_nofunc



    def mp_nofunc(self, _p=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = LaTeXParser.Mp_nofuncContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 16
        self.enterRecursionRule(localctx, 16, self.RULE_mp_nofunc, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 130
            self.unary_nofunc()
            self._ctx.stop = self._input.LT(-1)
            self.state = 137
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,5,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = LaTeXParser.Mp_nofuncContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_mp_nofunc)
                    self.state = 132
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 133
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << LaTeXParser.MUL) | (1 << LaTeXParser.DIV) | (1 << LaTeXParser.COLON) | (1 << LaTeXParser.CMD_TIMES) | (1 << LaTeXParser.CMD_CDOT) | (1 << LaTeXParser.CMD_DIV))) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 134
                    self.mp_nofunc(3) 
                self.state = 139
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,5,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class UnaryContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(LaTeXParser.UnaryContext, self).__init__(parent, invokingState)
            self.parser = parser

        def unary(self):
            return self.getTypedRuleContext(LaTeXParser.UnaryContext,0)


        def ADD(self):
            return self.getToken(LaTeXParser.ADD, 0)

        def SUB(self):
            return self.getToken(LaTeXParser.SUB, 0)

        def postfix(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(LaTeXParser.PostfixContext)
            else:
                return self.getTypedRuleContext(LaTeXParser.PostfixContext,i)


        def getRuleIndex(self):
            return LaTeXParser.RULE_unary




    def unary(self):

        localctx = LaTeXParser.UnaryContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_unary)
        self._la = 0 # Token type
        try:
            self.state = 147
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [LaTeXParser.ADD, LaTeXParser.SUB]:
                self.enterOuterAlt(localctx, 1)
                self.state = 140
                _la = self._input.LA(1)
                if not(_la==LaTeXParser.ADD or _la==LaTeXParser.SUB):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 141
                self.unary()
                pass
            elif token in [LaTeXParser.L_PAREN, LaTeXParser.L_BRACE, LaTeXParser.L_BRACKET, LaTeXParser.BAR, LaTeXParser.FUNC_LIM, LaTeXParser.FUNC_INT, LaTeXParser.FUNC_SUM, LaTeXParser.FUNC_PROD, LaTeXParser.FUNC_LOG, LaTeXParser.FUNC_LN, LaTeXParser.FUNC_SIN, LaTeXParser.FUNC_COS, LaTeXParser.FUNC_TAN, LaTeXParser.FUNC_CSC, LaTeXParser.FUNC_SEC, LaTeXParser.FUNC_COT, LaTeXParser.FUNC_ARCSIN, LaTeXParser.FUNC_ARCCOS, LaTeXParser.FUNC_ARCTAN, LaTeXParser.FUNC_ARCCSC, LaTeXParser.FUNC_ARCSEC, LaTeXParser.FUNC_ARCCOT, LaTeXParser.FUNC_SINH, LaTeXParser.FUNC_COSH, LaTeXParser.FUNC_TANH, LaTeXParser.FUNC_ARSINH, LaTeXParser.FUNC_ARCOSH, LaTeXParser.FUNC_ARTANH, LaTeXParser.FUNC_SQRT, LaTeXParser.CMD_FRAC, LaTeXParser.CMD_BINOM, LaTeXParser.CMD_DBINOM, LaTeXParser.CMD_TBINOM, LaTeXParser.CMD_MATHIT, LaTeXParser.DIFFERENTIAL, LaTeXParser.LETTER, LaTeXParser.NUMBER, LaTeXParser.SYMBOL]:
                self.enterOuterAlt(localctx, 2)
                self.state = 143 
                self._errHandler.sync(self)
                _alt = 1
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt == 1:
                        self.state = 142
                        self.postfix()

                    else:
                        raise NoViableAltException(self)
                    self.state = 145 
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,6,self._ctx)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Unary_nofuncContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(LaTeXParser.Unary_nofuncContext, self).__init__(parent, invokingState)
            self.parser = parser

        def unary_nofunc(self):
            return self.getTypedRuleContext(LaTeXParser.Unary_nofuncContext,0)


        def ADD(self):
            return self.getToken(LaTeXParser.ADD, 0)

        def SUB(self):
            return self.getToken(LaTeXParser.SUB, 0)

        def postfix(self):
            return self.getTypedRuleContext(LaTeXParser.PostfixContext,0)


        def postfix_nofunc(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(LaTeXParser.Postfix_nofuncContext)
            else:
                return self.getTypedRuleContext(LaTeXParser.Postfix_nofuncContext,i)


        def getRuleIndex(self):
            return LaTeXParser.RULE_unary_nofunc




    def unary_nofunc(self):

        localctx = LaTeXParser.Unary_nofuncContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_unary_nofunc)
        self._la = 0 # Token type
        try:
            self.state = 158
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [LaTeXParser.ADD, LaTeXParser.SUB]:
                self.enterOuterAlt(localctx, 1)
                self.state = 149
                _la = self._input.LA(1)
                if not(_la==LaTeXParser.ADD or _la==LaTeXParser.SUB):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 150
                self.unary_nofunc()
                pass
            elif token in [LaTeXParser.L_PAREN, LaTeXParser.L_BRACE, LaTeXParser.L_BRACKET, LaTeXParser.BAR, LaTeXParser.FUNC_LIM, LaTeXParser.FUNC_INT, LaTeXParser.FUNC_SUM, LaTeXParser.FUNC_PROD, LaTeXParser.FUNC_LOG, LaTeXParser.FUNC_LN, LaTeXParser.FUNC_SIN, LaTeXParser.FUNC_COS, LaTeXParser.FUNC_TAN, LaTeXParser.FUNC_CSC, LaTeXParser.FUNC_SEC, LaTeXParser.FUNC_COT, LaTeXParser.FUNC_ARCSIN, LaTeXParser.FUNC_ARCCOS, LaTeXParser.FUNC_ARCTAN, LaTeXParser.FUNC_ARCCSC, LaTeXParser.FUNC_ARCSEC, LaTeXParser.FUNC_ARCCOT, LaTeXParser.FUNC_SINH, LaTeXParser.FUNC_COSH, LaTeXParser.FUNC_TANH, LaTeXParser.FUNC_ARSINH, LaTeXParser.FUNC_ARCOSH, LaTeXParser.FUNC_ARTANH, LaTeXParser.FUNC_SQRT, LaTeXParser.CMD_FRAC, LaTeXParser.CMD_BINOM, LaTeXParser.CMD_DBINOM, LaTeXParser.CMD_TBINOM, LaTeXParser.CMD_MATHIT, LaTeXParser.DIFFERENTIAL, LaTeXParser.LETTER, LaTeXParser.NUMBER, LaTeXParser.SYMBOL]:
                self.enterOuterAlt(localctx, 2)
                self.state = 151
                self.postfix()
                self.state = 155
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,8,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 152
                        self.postfix_nofunc() 
                    self.state = 157
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,8,self._ctx)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class PostfixContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(LaTeXParser.PostfixContext, self).__init__(parent, invokingState)
            self.parser = parser

        def exp(self):
            return self.getTypedRuleContext(LaTeXParser.ExpContext,0)


        def postfix_op(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(LaTeXParser.Postfix_opContext)
            else:
                return self.getTypedRuleContext(LaTeXParser.Postfix_opContext,i)


        def getRuleIndex(self):
            return LaTeXParser.RULE_postfix




    def postfix(self):

        localctx = LaTeXParser.PostfixContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_postfix)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 160
            self.exp(0)
            self.state = 164
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,10,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 161
                    self.postfix_op() 
                self.state = 166
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,10,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Postfix_nofuncContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(LaTeXParser.Postfix_nofuncContext, self).__init__(parent, invokingState)
            self.parser = parser

        def exp_nofunc(self):
            return self.getTypedRuleContext(LaTeXParser.Exp_nofuncContext,0)


        def postfix_op(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(LaTeXParser.Postfix_opContext)
            else:
                return self.getTypedRuleContext(LaTeXParser.Postfix_opContext,i)


        def getRuleIndex(self):
            return LaTeXParser.RULE_postfix_nofunc




    def postfix_nofunc(self):

        localctx = LaTeXParser.Postfix_nofuncContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_postfix_nofunc)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 167
            self.exp_nofunc(0)
            self.state = 171
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,11,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 168
                    self.postfix_op() 
                self.state = 173
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,11,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Postfix_opContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(LaTeXParser.Postfix_opContext, self).__init__(parent, invokingState)
            self.parser = parser

        def BANG(self):
            return self.getToken(LaTeXParser.BANG, 0)

        def eval_at(self):
            return self.getTypedRuleContext(LaTeXParser.Eval_atContext,0)


        def getRuleIndex(self):
            return LaTeXParser.RULE_postfix_op




    def postfix_op(self):

        localctx = LaTeXParser.Postfix_opContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_postfix_op)
        try:
            self.state = 176
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [LaTeXParser.BANG]:
                self.enterOuterAlt(localctx, 1)
                self.state = 174
                self.match(LaTeXParser.BANG)
                pass
            elif token in [LaTeXParser.BAR]:
                self.enterOuterAlt(localctx, 2)
                self.state = 175
                self.eval_at()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Eval_atContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(LaTeXParser.Eval_atContext, self).__init__(parent, invokingState)
            self.parser = parser

        def BAR(self):
            return self.getToken(LaTeXParser.BAR, 0)

        def eval_at_sup(self):
            return self.getTypedRuleContext(LaTeXParser.Eval_at_supContext,0)


        def eval_at_sub(self):
            return self.getTypedRuleContext(LaTeXParser.Eval_at_subContext,0)


        def getRuleIndex(self):
            return LaTeXParser.RULE_eval_at




    def eval_at(self):

        localctx = LaTeXParser.Eval_atContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_eval_at)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 178
            self.match(LaTeXParser.BAR)
            self.state = 184
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,13,self._ctx)
            if la_ == 1:
                self.state = 179
                self.eval_at_sup()
                pass

            elif la_ == 2:
                self.state = 180
                self.eval_at_sub()
                pass

            elif la_ == 3:
                self.state = 181
                self.eval_at_sup()
                self.state = 182
                self.eval_at_sub()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Eval_at_subContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(LaTeXParser.Eval_at_subContext, self).__init__(parent, invokingState)
            self.parser = parser

        def UNDERSCORE(self):
            return self.getToken(LaTeXParser.UNDERSCORE, 0)

        def L_BRACE(self):
            return self.getToken(LaTeXParser.L_BRACE, 0)

        def R_BRACE(self):
            return self.getToken(LaTeXParser.R_BRACE, 0)

        def expr(self):
            return self.getTypedRuleContext(LaTeXParser.ExprContext,0)


        def equality(self):
            return self.getTypedRuleContext(LaTeXParser.EqualityContext,0)


        def getRuleIndex(self):
            return LaTeXParser.RULE_eval_at_sub




    def eval_at_sub(self):

        localctx = LaTeXParser.Eval_at_subContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_eval_at_sub)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 186
            self.match(LaTeXParser.UNDERSCORE)
            self.state = 187
            self.match(LaTeXParser.L_BRACE)
            self.state = 190
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,14,self._ctx)
            if la_ == 1:
                self.state = 188
                self.expr()
                pass

            elif la_ == 2:
                self.state = 189
                self.equality()
                pass


            self.state = 192
            self.match(LaTeXParser.R_BRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Eval_at_supContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(LaTeXParser.Eval_at_supContext, self).__init__(parent, invokingState)
            self.parser = parser

        def CARET(self):
            return self.getToken(LaTeXParser.CARET, 0)

        def L_BRACE(self):
            return self.getToken(LaTeXParser.L_BRACE, 0)

        def R_BRACE(self):
            return self.getToken(LaTeXParser.R_BRACE, 0)

        def expr(self):
            return self.getTypedRuleContext(LaTeXParser.ExprContext,0)


        def equality(self):
            return self.getTypedRuleContext(LaTeXParser.EqualityContext,0)


        def getRuleIndex(self):
            return LaTeXParser.RULE_eval_at_sup




    def eval_at_sup(self):

        localctx = LaTeXParser.Eval_at_supContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_eval_at_sup)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 194
            self.match(LaTeXParser.CARET)
            self.state = 195
            self.match(LaTeXParser.L_BRACE)
            self.state = 198
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,15,self._ctx)
            if la_ == 1:
                self.state = 196
                self.expr()
                pass

            elif la_ == 2:
                self.state = 197
                self.equality()
                pass


            self.state = 200
            self.match(LaTeXParser.R_BRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ExpContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(LaTeXParser.ExpContext, self).__init__(parent, invokingState)
            self.parser = parser

        def comp(self):
            return self.getTypedRuleContext(LaTeXParser.CompContext,0)


        def exp(self):
            return self.getTypedRuleContext(LaTeXParser.ExpContext,0)


        def CARET(self):
            return self.getToken(LaTeXParser.CARET, 0)

        def atom(self):
            return self.getTypedRuleContext(LaTeXParser.AtomContext,0)


        def L_BRACE(self):
            return self.getToken(LaTeXParser.L_BRACE, 0)

        def expr(self):
            return self.getTypedRuleContext(LaTeXParser.ExprContext,0)


        def R_BRACE(self):
            return self.getToken(LaTeXParser.R_BRACE, 0)

        def subexpr(self):
            return self.getTypedRuleContext(LaTeXParser.SubexprContext,0)


        def getRuleIndex(self):
            return LaTeXParser.RULE_exp



    def exp(self, _p=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = LaTeXParser.ExpContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 34
        self.enterRecursionRule(localctx, 34, self.RULE_exp, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 203
            self.comp()
            self._ctx.stop = self._input.LT(-1)
            self.state = 219
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,18,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = LaTeXParser.ExpContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_exp)
                    self.state = 205
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 206
                    self.match(LaTeXParser.CARET)
                    self.state = 212
                    self._errHandler.sync(self)
                    token = self._input.LA(1)
                    if token in [LaTeXParser.CMD_MATHIT, LaTeXParser.DIFFERENTIAL, LaTeXParser.LETTER, LaTeXParser.NUMBER, LaTeXParser.SYMBOL]:
                        self.state = 207
                        self.atom()
                        pass
                    elif token in [LaTeXParser.L_BRACE]:
                        self.state = 208
                        self.match(LaTeXParser.L_BRACE)
                        self.state = 209
                        self.expr()
                        self.state = 210
                        self.match(LaTeXParser.R_BRACE)
                        pass
                    else:
                        raise NoViableAltException(self)

                    self.state = 215
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,17,self._ctx)
                    if la_ == 1:
                        self.state = 214
                        self.subexpr()

             
                self.state = 221
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,18,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class Exp_nofuncContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(LaTeXParser.Exp_nofuncContext, self).__init__(parent, invokingState)
            self.parser = parser

        def comp_nofunc(self):
            return self.getTypedRuleContext(LaTeXParser.Comp_nofuncContext,0)


        def exp_nofunc(self):
            return self.getTypedRuleContext(LaTeXParser.Exp_nofuncContext,0)


        def CARET(self):
            return self.getToken(LaTeXParser.CARET, 0)

        def atom(self):
            return self.getTypedRuleContext(LaTeXParser.AtomContext,0)


        def L_BRACE(self):
            return self.getToken(LaTeXParser.L_BRACE, 0)

        def expr(self):
            return self.getTypedRuleContext(LaTeXParser.ExprContext,0)


        def R_BRACE(self):
            return self.getToken(LaTeXParser.R_BRACE, 0)

        def subexpr(self):
            return self.getTypedRuleContext(LaTeXParser.SubexprContext,0)


        def getRuleIndex(self):
            return LaTeXParser.RULE_exp_nofunc



    def exp_nofunc(self, _p=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = LaTeXParser.Exp_nofuncContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 36
        self.enterRecursionRule(localctx, 36, self.RULE_exp_nofunc, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 223
            self.comp_nofunc()
            self._ctx.stop = self._input.LT(-1)
            self.state = 239
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,21,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = LaTeXParser.Exp_nofuncContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_exp_nofunc)
                    self.state = 225
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 226
                    self.match(LaTeXParser.CARET)
                    self.state = 232
                    self._errHandler.sync(self)
                    token = self._input.LA(1)
                    if token in [LaTeXParser.CMD_MATHIT, LaTeXParser.DIFFERENTIAL, LaTeXParser.LETTER, LaTeXParser.NUMBER, LaTeXParser.SYMBOL]:
                        self.state = 227
                        self.atom()
                        pass
                    elif token in [LaTeXParser.L_BRACE]:
                        self.state = 228
                        self.match(LaTeXParser.L_BRACE)
                        self.state = 229
                        self.expr()
                        self.state = 230
                        self.match(LaTeXParser.R_BRACE)
                        pass
                    else:
                        raise NoViableAltException(self)

                    self.state = 235
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,20,self._ctx)
                    if la_ == 1:
                        self.state = 234
                        self.subexpr()

             
                self.state = 241
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,21,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class CompContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(LaTeXParser.CompContext, self).__init__(parent, invokingState)
            self.parser = parser

        def group(self):
            return self.getTypedRuleContext(LaTeXParser.GroupContext,0)


        def abs_group(self):
            return self.getTypedRuleContext(LaTeXParser.Abs_groupContext,0)


        def func(self):
            return self.getTypedRuleContext(LaTeXParser.FuncContext,0)


        def atom(self):
            return self.getTypedRuleContext(LaTeXParser.AtomContext,0)


        def frac(self):
            return self.getTypedRuleContext(LaTeXParser.FracContext,0)


        def binom(self):
            return self.getTypedRuleContext(LaTeXParser.BinomContext,0)


        def getRuleIndex(self):
            return LaTeXParser.RULE_comp




    def comp(self):

        localctx = LaTeXParser.CompContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_comp)
        try:
            self.state = 248
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,22,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 242
                self.group()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 243
                self.abs_group()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 244
                self.func()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 245
                self.atom()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 246
                self.frac()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 247
                self.binom()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Comp_nofuncContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(LaTeXParser.Comp_nofuncContext, self).__init__(parent, invokingState)
            self.parser = parser

        def group(self):
            return self.getTypedRuleContext(LaTeXParser.GroupContext,0)


        def abs_group(self):
            return self.getTypedRuleContext(LaTeXParser.Abs_groupContext,0)


        def atom(self):
            return self.getTypedRuleContext(LaTeXParser.AtomContext,0)


        def frac(self):
            return self.getTypedRuleContext(LaTeXParser.FracContext,0)


        def binom(self):
            return self.getTypedRuleContext(LaTeXParser.BinomContext,0)


        def getRuleIndex(self):
            return LaTeXParser.RULE_comp_nofunc




    def comp_nofunc(self):

        localctx = LaTeXParser.Comp_nofuncContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_comp_nofunc)
        try:
            self.state = 255
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [LaTeXParser.L_PAREN, LaTeXParser.L_BRACE, LaTeXParser.L_BRACKET]:
                self.enterOuterAlt(localctx, 1)
                self.state = 250
                self.group()
                pass
            elif token in [LaTeXParser.BAR]:
                self.enterOuterAlt(localctx, 2)
                self.state = 251
                self.abs_group()
                pass
            elif token in [LaTeXParser.CMD_MATHIT, LaTeXParser.DIFFERENTIAL, LaTeXParser.LETTER, LaTeXParser.NUMBER, LaTeXParser.SYMBOL]:
                self.enterOuterAlt(localctx, 3)
                self.state = 252
                self.atom()
                pass
            elif token in [LaTeXParser.CMD_FRAC]:
                self.enterOuterAlt(localctx, 4)
                self.state = 253
                self.frac()
                pass
            elif token in [LaTeXParser.CMD_BINOM, LaTeXParser.CMD_DBINOM, LaTeXParser.CMD_TBINOM]:
                self.enterOuterAlt(localctx, 5)
                self.state = 254
                self.binom()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class GroupContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(LaTeXParser.GroupContext, self).__init__(parent, invokingState)
            self.parser = parser

        def L_PAREN(self):
            return self.getToken(LaTeXParser.L_PAREN, 0)

        def expr(self):
            return self.getTypedRuleContext(LaTeXParser.ExprContext,0)


        def R_PAREN(self):
            return self.getToken(LaTeXParser.R_PAREN, 0)

        def L_BRACKET(self):
            return self.getToken(LaTeXParser.L_BRACKET, 0)

        def R_BRACKET(self):
            return self.getToken(LaTeXParser.R_BRACKET, 0)

        def L_BRACE(self):
            return self.getToken(LaTeXParser.L_BRACE, 0)

        def R_BRACE(self):
            return self.getToken(LaTeXParser.R_BRACE, 0)

        def getRuleIndex(self):
            return LaTeXParser.RULE_group




    def group(self):

        localctx = LaTeXParser.GroupContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_group)
        try:
            self.state = 269
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [LaTeXParser.L_PAREN]:
                self.enterOuterAlt(localctx, 1)
                self.state = 257
                self.match(LaTeXParser.L_PAREN)
                self.state = 258
                self.expr()
                self.state = 259
                self.match(LaTeXParser.R_PAREN)
                pass
            elif token in [LaTeXParser.L_BRACKET]:
                self.enterOuterAlt(localctx, 2)
                self.state = 261
                self.match(LaTeXParser.L_BRACKET)
                self.state = 262
                self.expr()
                self.state = 263
                self.match(LaTeXParser.R_BRACKET)
                pass
            elif token in [LaTeXParser.L_BRACE]:
                self.enterOuterAlt(localctx, 3)
                self.state = 265
                self.match(LaTeXParser.L_BRACE)
                self.state = 266
                self.expr()
                self.state = 267
                self.match(LaTeXParser.R_BRACE)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Abs_groupContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(LaTeXParser.Abs_groupContext, self).__init__(parent, invokingState)
            self.parser = parser

        def BAR(self, i=None):
            if i is None:
                return self.getTokens(LaTeXParser.BAR)
            else:
                return self.getToken(LaTeXParser.BAR, i)

        def expr(self):
            return self.getTypedRuleContext(LaTeXParser.ExprContext,0)


        def getRuleIndex(self):
            return LaTeXParser.RULE_abs_group




    def abs_group(self):

        localctx = LaTeXParser.Abs_groupContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_abs_group)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 271
            self.match(LaTeXParser.BAR)
            self.state = 272
            self.expr()
            self.state = 273
            self.match(LaTeXParser.BAR)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class AtomContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(LaTeXParser.AtomContext, self).__init__(parent, invokingState)
            self.parser = parser

        def LETTER(self):
            return self.getToken(LaTeXParser.LETTER, 0)

        def SYMBOL(self):
            return self.getToken(LaTeXParser.SYMBOL, 0)

        def subexpr(self):
            return self.getTypedRuleContext(LaTeXParser.SubexprContext,0)


        def NUMBER(self):
            return self.getToken(LaTeXParser.NUMBER, 0)

        def DIFFERENTIAL(self):
            return self.getToken(LaTeXParser.DIFFERENTIAL, 0)

        def mathit(self):
            return self.getTypedRuleContext(LaTeXParser.MathitContext,0)


        def getRuleIndex(self):
            return LaTeXParser.RULE_atom




    def atom(self):

        localctx = LaTeXParser.AtomContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_atom)
        self._la = 0 # Token type
        try:
            self.state = 282
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [LaTeXParser.LETTER, LaTeXParser.SYMBOL]:
                self.enterOuterAlt(localctx, 1)
                self.state = 275
                _la = self._input.LA(1)
                if not(_la==LaTeXParser.LETTER or _la==LaTeXParser.SYMBOL):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 277
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,25,self._ctx)
                if la_ == 1:
                    self.state = 276
                    self.subexpr()


                pass
            elif token in [LaTeXParser.NUMBER]:
                self.enterOuterAlt(localctx, 2)
                self.state = 279
                self.match(LaTeXParser.NUMBER)
                pass
            elif token in [LaTeXParser.DIFFERENTIAL]:
                self.enterOuterAlt(localctx, 3)
                self.state = 280
                self.match(LaTeXParser.DIFFERENTIAL)
                pass
            elif token in [LaTeXParser.CMD_MATHIT]:
                self.enterOuterAlt(localctx, 4)
                self.state = 281
                self.mathit()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class MathitContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(LaTeXParser.MathitContext, self).__init__(parent, invokingState)
            self.parser = parser

        def CMD_MATHIT(self):
            return self.getToken(LaTeXParser.CMD_MATHIT, 0)

        def L_BRACE(self):
            return self.getToken(LaTeXParser.L_BRACE, 0)

        def mathit_text(self):
            return self.getTypedRuleContext(LaTeXParser.Mathit_textContext,0)


        def R_BRACE(self):
            return self.getToken(LaTeXParser.R_BRACE, 0)

        def getRuleIndex(self):
            return LaTeXParser.RULE_mathit




    def mathit(self):

        localctx = LaTeXParser.MathitContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_mathit)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 284
            self.match(LaTeXParser.CMD_MATHIT)
            self.state = 285
            self.match(LaTeXParser.L_BRACE)
            self.state = 286
            self.mathit_text()
            self.state = 287
            self.match(LaTeXParser.R_BRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Mathit_textContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(LaTeXParser.Mathit_textContext, self).__init__(parent, invokingState)
            self.parser = parser

        def LETTER(self, i=None):
            if i is None:
                return self.getTokens(LaTeXParser.LETTER)
            else:
                return self.getToken(LaTeXParser.LETTER, i)

        def getRuleIndex(self):
            return LaTeXParser.RULE_mathit_text




    def mathit_text(self):

        localctx = LaTeXParser.Mathit_textContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_mathit_text)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 292
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==LaTeXParser.LETTER:
                self.state = 289
                self.match(LaTeXParser.LETTER)
                self.state = 294
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class FracContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(LaTeXParser.FracContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.upper = None # ExprContext
            self.lower = None # ExprContext

        def CMD_FRAC(self):
            return self.getToken(LaTeXParser.CMD_FRAC, 0)

        def L_BRACE(self, i=None):
            if i is None:
                return self.getTokens(LaTeXParser.L_BRACE)
            else:
                return self.getToken(LaTeXParser.L_BRACE, i)

        def R_BRACE(self, i=None):
            if i is None:
                return self.getTokens(LaTeXParser.R_BRACE)
            else:
                return self.getToken(LaTeXParser.R_BRACE, i)

        def expr(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(LaTeXParser.ExprContext)
            else:
                return self.getTypedRuleContext(LaTeXParser.ExprContext,i)


        def getRuleIndex(self):
            return LaTeXParser.RULE_frac




    def frac(self):

        localctx = LaTeXParser.FracContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_frac)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 295
            self.match(LaTeXParser.CMD_FRAC)
            self.state = 296
            self.match(LaTeXParser.L_BRACE)
            self.state = 297
            localctx.upper = self.expr()
            self.state = 298
            self.match(LaTeXParser.R_BRACE)
            self.state = 299
            self.match(LaTeXParser.L_BRACE)
            self.state = 300
            localctx.lower = self.expr()
            self.state = 301
            self.match(LaTeXParser.R_BRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class BinomContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(LaTeXParser.BinomContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.n = None # ExprContext
            self.k = None # ExprContext

        def L_BRACE(self, i=None):
            if i is None:
                return self.getTokens(LaTeXParser.L_BRACE)
            else:
                return self.getToken(LaTeXParser.L_BRACE, i)

        def R_BRACE(self, i=None):
            if i is None:
                return self.getTokens(LaTeXParser.R_BRACE)
            else:
                return self.getToken(LaTeXParser.R_BRACE, i)

        def CMD_BINOM(self):
            return self.getToken(LaTeXParser.CMD_BINOM, 0)

        def CMD_DBINOM(self):
            return self.getToken(LaTeXParser.CMD_DBINOM, 0)

        def CMD_TBINOM(self):
            return self.getToken(LaTeXParser.CMD_TBINOM, 0)

        def expr(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(LaTeXParser.ExprContext)
            else:
                return self.getTypedRuleContext(LaTeXParser.ExprContext,i)


        def getRuleIndex(self):
            return LaTeXParser.RULE_binom




    def binom(self):

        localctx = LaTeXParser.BinomContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_binom)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 303
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << LaTeXParser.CMD_BINOM) | (1 << LaTeXParser.CMD_DBINOM) | (1 << LaTeXParser.CMD_TBINOM))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 304
            self.match(LaTeXParser.L_BRACE)
            self.state = 305
            localctx.n = self.expr()
            self.state = 306
            self.match(LaTeXParser.R_BRACE)
            self.state = 307
            self.match(LaTeXParser.L_BRACE)
            self.state = 308
            localctx.k = self.expr()
            self.state = 309
            self.match(LaTeXParser.R_BRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Func_normalContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(LaTeXParser.Func_normalContext, self).__init__(parent, invokingState)
            self.parser = parser

        def FUNC_LOG(self):
            return self.getToken(LaTeXParser.FUNC_LOG, 0)

        def FUNC_LN(self):
            return self.getToken(LaTeXParser.FUNC_LN, 0)

        def FUNC_SIN(self):
            return self.getToken(LaTeXParser.FUNC_SIN, 0)

        def FUNC_COS(self):
            return self.getToken(LaTeXParser.FUNC_COS, 0)

        def FUNC_TAN(self):
            return self.getToken(LaTeXParser.FUNC_TAN, 0)

        def FUNC_CSC(self):
            return self.getToken(LaTeXParser.FUNC_CSC, 0)

        def FUNC_SEC(self):
            return self.getToken(LaTeXParser.FUNC_SEC, 0)

        def FUNC_COT(self):
            return self.getToken(LaTeXParser.FUNC_COT, 0)

        def FUNC_ARCSIN(self):
            return self.getToken(LaTeXParser.FUNC_ARCSIN, 0)

        def FUNC_ARCCOS(self):
            return self.getToken(LaTeXParser.FUNC_ARCCOS, 0)

        def FUNC_ARCTAN(self):
            return self.getToken(LaTeXParser.FUNC_ARCTAN, 0)

        def FUNC_ARCCSC(self):
            return self.getToken(LaTeXParser.FUNC_ARCCSC, 0)

        def FUNC_ARCSEC(self):
            return self.getToken(LaTeXParser.FUNC_ARCSEC, 0)

        def FUNC_ARCCOT(self):
            return self.getToken(LaTeXParser.FUNC_ARCCOT, 0)

        def FUNC_SINH(self):
            return self.getToken(LaTeXParser.FUNC_SINH, 0)

        def FUNC_COSH(self):
            return self.getToken(LaTeXParser.FUNC_COSH, 0)

        def FUNC_TANH(self):
            return self.getToken(LaTeXParser.FUNC_TANH, 0)

        def FUNC_ARSINH(self):
            return self.getToken(LaTeXParser.FUNC_ARSINH, 0)

        def FUNC_ARCOSH(self):
            return self.getToken(LaTeXParser.FUNC_ARCOSH, 0)

        def FUNC_ARTANH(self):
            return self.getToken(LaTeXParser.FUNC_ARTANH, 0)

        def getRuleIndex(self):
            return LaTeXParser.RULE_func_normal




    def func_normal(self):

        localctx = LaTeXParser.Func_normalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_func_normal)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 311
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << LaTeXParser.FUNC_LOG) | (1 << LaTeXParser.FUNC_LN) | (1 << LaTeXParser.FUNC_SIN) | (1 << LaTeXParser.FUNC_COS) | (1 << LaTeXParser.FUNC_TAN) | (1 << LaTeXParser.FUNC_CSC) | (1 << LaTeXParser.FUNC_SEC) | (1 << LaTeXParser.FUNC_COT) | (1 << LaTeXParser.FUNC_ARCSIN) | (1 << LaTeXParser.FUNC_ARCCOS) | (1 << LaTeXParser.FUNC_ARCTAN) | (1 << LaTeXParser.FUNC_ARCCSC) | (1 << LaTeXParser.FUNC_ARCSEC) | (1 << LaTeXParser.FUNC_ARCCOT) | (1 << LaTeXParser.FUNC_SINH) | (1 << LaTeXParser.FUNC_COSH) | (1 << LaTeXParser.FUNC_TANH) | (1 << LaTeXParser.FUNC_ARSINH) | (1 << LaTeXParser.FUNC_ARCOSH) | (1 << LaTeXParser.FUNC_ARTANH))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class FuncContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(LaTeXParser.FuncContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.root = None # ExprContext
            self.base = None # ExprContext

        def func_normal(self):
            return self.getTypedRuleContext(LaTeXParser.Func_normalContext,0)


        def L_PAREN(self):
            return self.getToken(LaTeXParser.L_PAREN, 0)

        def func_arg(self):
            return self.getTypedRuleContext(LaTeXParser.Func_argContext,0)


        def R_PAREN(self):
            return self.getToken(LaTeXParser.R_PAREN, 0)

        def func_arg_noparens(self):
            return self.getTypedRuleContext(LaTeXParser.Func_arg_noparensContext,0)


        def subexpr(self):
            return self.getTypedRuleContext(LaTeXParser.SubexprContext,0)


        def supexpr(self):
            return self.getTypedRuleContext(LaTeXParser.SupexprContext,0)


        def args(self):
            return self.getTypedRuleContext(LaTeXParser.ArgsContext,0)


        def LETTER(self):
            return self.getToken(LaTeXParser.LETTER, 0)

        def SYMBOL(self):
            return self.getToken(LaTeXParser.SYMBOL, 0)

        def FUNC_INT(self):
            return self.getToken(LaTeXParser.FUNC_INT, 0)

        def DIFFERENTIAL(self):
            return self.getToken(LaTeXParser.DIFFERENTIAL, 0)

        def frac(self):
            return self.getTypedRuleContext(LaTeXParser.FracContext,0)


        def additive(self):
            return self.getTypedRuleContext(LaTeXParser.AdditiveContext,0)


        def UNDERSCORE(self):
            return self.getToken(LaTeXParser.UNDERSCORE, 0)

        def FUNC_SQRT(self):
            return self.getToken(LaTeXParser.FUNC_SQRT, 0)

        def L_BRACE(self):
            return self.getToken(LaTeXParser.L_BRACE, 0)

        def R_BRACE(self):
            return self.getToken(LaTeXParser.R_BRACE, 0)

        def expr(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(LaTeXParser.ExprContext)
            else:
                return self.getTypedRuleContext(LaTeXParser.ExprContext,i)


        def L_BRACKET(self):
            return self.getToken(LaTeXParser.L_BRACKET, 0)

        def R_BRACKET(self):
            return self.getToken(LaTeXParser.R_BRACKET, 0)

        def mp(self):
            return self.getTypedRuleContext(LaTeXParser.MpContext,0)


        def FUNC_SUM(self):
            return self.getToken(LaTeXParser.FUNC_SUM, 0)

        def FUNC_PROD(self):
            return self.getToken(LaTeXParser.FUNC_PROD, 0)

        def subeq(self):
            return self.getTypedRuleContext(LaTeXParser.SubeqContext,0)


        def FUNC_LIM(self):
            return self.getToken(LaTeXParser.FUNC_LIM, 0)

        def limit_sub(self):
            return self.getTypedRuleContext(LaTeXParser.Limit_subContext,0)


        def getRuleIndex(self):
            return LaTeXParser.RULE_func




    def func(self):

        localctx = LaTeXParser.FuncContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_func)
        self._la = 0 # Token type
        try:
            self.state = 389
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [LaTeXParser.FUNC_LOG, LaTeXParser.FUNC_LN, LaTeXParser.FUNC_SIN, LaTeXParser.FUNC_COS, LaTeXParser.FUNC_TAN, LaTeXParser.FUNC_CSC, LaTeXParser.FUNC_SEC, LaTeXParser.FUNC_COT, LaTeXParser.FUNC_ARCSIN, LaTeXParser.FUNC_ARCCOS, LaTeXParser.FUNC_ARCTAN, LaTeXParser.FUNC_ARCCSC, LaTeXParser.FUNC_ARCSEC, LaTeXParser.FUNC_ARCCOT, LaTeXParser.FUNC_SINH, LaTeXParser.FUNC_COSH, LaTeXParser.FUNC_TANH, LaTeXParser.FUNC_ARSINH, LaTeXParser.FUNC_ARCOSH, LaTeXParser.FUNC_ARTANH]:
                self.enterOuterAlt(localctx, 1)
                self.state = 313
                self.func_normal()
                self.state = 326
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,32,self._ctx)
                if la_ == 1:
                    self.state = 315
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if _la==LaTeXParser.UNDERSCORE:
                        self.state = 314
                        self.subexpr()


                    self.state = 318
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if _la==LaTeXParser.CARET:
                        self.state = 317
                        self.supexpr()


                    pass

                elif la_ == 2:
                    self.state = 321
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if _la==LaTeXParser.CARET:
                        self.state = 320
                        self.supexpr()


                    self.state = 324
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if _la==LaTeXParser.UNDERSCORE:
                        self.state = 323
                        self.subexpr()


                    pass


                self.state = 333
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,33,self._ctx)
                if la_ == 1:
                    self.state = 328
                    self.match(LaTeXParser.L_PAREN)
                    self.state = 329
                    self.func_arg()
                    self.state = 330
                    self.match(LaTeXParser.R_PAREN)
                    pass

                elif la_ == 2:
                    self.state = 332
                    self.func_arg_noparens()
                    pass


                pass
            elif token in [LaTeXParser.LETTER, LaTeXParser.SYMBOL]:
                self.enterOuterAlt(localctx, 2)
                self.state = 335
                _la = self._input.LA(1)
                if not(_la==LaTeXParser.LETTER or _la==LaTeXParser.SYMBOL):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 337
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==LaTeXParser.UNDERSCORE:
                    self.state = 336
                    self.subexpr()


                self.state = 339
                self.match(LaTeXParser.L_PAREN)
                self.state = 340
                self.args()
                self.state = 341
                self.match(LaTeXParser.R_PAREN)
                pass
            elif token in [LaTeXParser.FUNC_INT]:
                self.enterOuterAlt(localctx, 3)
                self.state = 343
                self.match(LaTeXParser.FUNC_INT)
                self.state = 345
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,35,self._ctx)
                if la_ == 1:
                    self.state = 344
                    self.match(LaTeXParser.UNDERSCORE)


                self.state = 353
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [LaTeXParser.UNDERSCORE]:
                    self.state = 347
                    self.subexpr()
                    self.state = 348
                    self.supexpr()
                    pass
                elif token in [LaTeXParser.CARET]:
                    self.state = 350
                    self.supexpr()
                    self.state = 351
                    self.subexpr()
                    pass
                elif token in [LaTeXParser.ADD, LaTeXParser.SUB, LaTeXParser.L_PAREN, LaTeXParser.L_BRACE, LaTeXParser.L_BRACKET, LaTeXParser.BAR, LaTeXParser.FUNC_LIM, LaTeXParser.FUNC_INT, LaTeXParser.FUNC_SUM, LaTeXParser.FUNC_PROD, LaTeXParser.FUNC_LOG, LaTeXParser.FUNC_LN, LaTeXParser.FUNC_SIN, LaTeXParser.FUNC_COS, LaTeXParser.FUNC_TAN, LaTeXParser.FUNC_CSC, LaTeXParser.FUNC_SEC, LaTeXParser.FUNC_COT, LaTeXParser.FUNC_ARCSIN, LaTeXParser.FUNC_ARCCOS, LaTeXParser.FUNC_ARCTAN, LaTeXParser.FUNC_ARCCSC, LaTeXParser.FUNC_ARCSEC, LaTeXParser.FUNC_ARCCOT, LaTeXParser.FUNC_SINH, LaTeXParser.FUNC_COSH, LaTeXParser.FUNC_TANH, LaTeXParser.FUNC_ARSINH, LaTeXParser.FUNC_ARCOSH, LaTeXParser.FUNC_ARTANH, LaTeXParser.FUNC_SQRT, LaTeXParser.CMD_FRAC, LaTeXParser.CMD_BINOM, LaTeXParser.CMD_DBINOM, LaTeXParser.CMD_TBINOM, LaTeXParser.CMD_MATHIT, LaTeXParser.DIFFERENTIAL, LaTeXParser.LETTER, LaTeXParser.NUMBER, LaTeXParser.SYMBOL]:
                    pass
                else:
                    pass
                self.state = 361
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,38,self._ctx)
                if la_ == 1:
                    self.state = 356
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,37,self._ctx)
                    if la_ == 1:
                        self.state = 355
                        self.additive(0)


                    self.state = 358
                    self.match(LaTeXParser.DIFFERENTIAL)
                    pass

                elif la_ == 2:
                    self.state = 359
                    self.frac()
                    pass

                elif la_ == 3:
                    self.state = 360
                    self.additive(0)
                    pass


                pass
            elif token in [LaTeXParser.FUNC_SQRT]:
                self.enterOuterAlt(localctx, 4)
                self.state = 363
                self.match(LaTeXParser.FUNC_SQRT)
                self.state = 368
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==LaTeXParser.L_BRACKET:
                    self.state = 364
                    self.match(LaTeXParser.L_BRACKET)
                    self.state = 365
                    localctx.root = self.expr()
                    self.state = 366
                    self.match(LaTeXParser.R_BRACKET)


                self.state = 370
                self.match(LaTeXParser.L_BRACE)
                self.state = 371
                localctx.base = self.expr()
                self.state = 372
                self.match(LaTeXParser.R_BRACE)
                pass
            elif token in [LaTeXParser.FUNC_SUM, LaTeXParser.FUNC_PROD]:
                self.enterOuterAlt(localctx, 5)
                self.state = 374
                _la = self._input.LA(1)
                if not(_la==LaTeXParser.FUNC_SUM or _la==LaTeXParser.FUNC_PROD):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 381
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [LaTeXParser.UNDERSCORE]:
                    self.state = 375
                    self.subeq()
                    self.state = 376
                    self.supexpr()
                    pass
                elif token in [LaTeXParser.CARET]:
                    self.state = 378
                    self.supexpr()
                    self.state = 379
                    self.subeq()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 383
                self.mp(0)
                pass
            elif token in [LaTeXParser.FUNC_LIM]:
                self.enterOuterAlt(localctx, 6)
                self.state = 385
                self.match(LaTeXParser.FUNC_LIM)
                self.state = 386
                self.limit_sub()
                self.state = 387
                self.mp(0)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ArgsContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(LaTeXParser.ArgsContext, self).__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(LaTeXParser.ExprContext,0)


        def args(self):
            return self.getTypedRuleContext(LaTeXParser.ArgsContext,0)


        def getRuleIndex(self):
            return LaTeXParser.RULE_args




    def args(self):

        localctx = LaTeXParser.ArgsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_args)
        try:
            self.state = 396
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,42,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 391
                self.expr()
                self.state = 392
                self.match(LaTeXParser.COMMA)
                self.state = 393
                self.args()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 395
                self.expr()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Limit_subContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(LaTeXParser.Limit_subContext, self).__init__(parent, invokingState)
            self.parser = parser

        def UNDERSCORE(self):
            return self.getToken(LaTeXParser.UNDERSCORE, 0)

        def L_BRACE(self, i=None):
            if i is None:
                return self.getTokens(LaTeXParser.L_BRACE)
            else:
                return self.getToken(LaTeXParser.L_BRACE, i)

        def lim_approach_sym(self):
            return self.getTypedRuleContext(LaTeXParser.Lim_approach_symContext,0)


        def expr(self):
            return self.getTypedRuleContext(LaTeXParser.ExprContext,0)


        def R_BRACE(self, i=None):
            if i is None:
                return self.getTokens(LaTeXParser.R_BRACE)
            else:
                return self.getToken(LaTeXParser.R_BRACE, i)

        def LETTER(self):
            return self.getToken(LaTeXParser.LETTER, 0)

        def SYMBOL(self):
            return self.getToken(LaTeXParser.SYMBOL, 0)

        def CARET(self):
            return self.getToken(LaTeXParser.CARET, 0)

        def ADD(self):
            return self.getToken(LaTeXParser.ADD, 0)

        def SUB(self):
            return self.getToken(LaTeXParser.SUB, 0)

        def getRuleIndex(self):
            return LaTeXParser.RULE_limit_sub




    def limit_sub(self):

        localctx = LaTeXParser.Limit_subContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_limit_sub)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 398
            self.match(LaTeXParser.UNDERSCORE)
            self.state = 399
            self.match(LaTeXParser.L_BRACE)
            self.state = 400
            _la = self._input.LA(1)
            if not(_la==LaTeXParser.LETTER or _la==LaTeXParser.SYMBOL):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 401
            self.lim_approach_sym()
            self.state = 402
            self.expr()
            self.state = 407
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==LaTeXParser.CARET:
                self.state = 403
                self.match(LaTeXParser.CARET)
                self.state = 404
                self.match(LaTeXParser.L_BRACE)
                self.state = 405
                _la = self._input.LA(1)
                if not(_la==LaTeXParser.ADD or _la==LaTeXParser.SUB):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 406
                self.match(LaTeXParser.R_BRACE)


            self.state = 409
            self.match(LaTeXParser.R_BRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Func_argContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(LaTeXParser.Func_argContext, self).__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(LaTeXParser.ExprContext,0)


        def func_arg(self):
            return self.getTypedRuleContext(LaTeXParser.Func_argContext,0)


        def getRuleIndex(self):
            return LaTeXParser.RULE_func_arg




    def func_arg(self):

        localctx = LaTeXParser.Func_argContext(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_func_arg)
        try:
            self.state = 416
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,44,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 411
                self.expr()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 412
                self.expr()
                self.state = 413
                self.match(LaTeXParser.COMMA)
                self.state = 414
                self.func_arg()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Func_arg_noparensContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(LaTeXParser.Func_arg_noparensContext, self).__init__(parent, invokingState)
            self.parser = parser

        def mp_nofunc(self):
            return self.getTypedRuleContext(LaTeXParser.Mp_nofuncContext,0)


        def getRuleIndex(self):
            return LaTeXParser.RULE_func_arg_noparens




    def func_arg_noparens(self):

        localctx = LaTeXParser.Func_arg_noparensContext(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_func_arg_noparens)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 418
            self.mp_nofunc(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class SubexprContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(LaTeXParser.SubexprContext, self).__init__(parent, invokingState)
            self.parser = parser

        def UNDERSCORE(self):
            return self.getToken(LaTeXParser.UNDERSCORE, 0)

        def atom(self):
            return self.getTypedRuleContext(LaTeXParser.AtomContext,0)


        def L_BRACE(self):
            return self.getToken(LaTeXParser.L_BRACE, 0)

        def expr(self):
            return self.getTypedRuleContext(LaTeXParser.ExprContext,0)


        def R_BRACE(self):
            return self.getToken(LaTeXParser.R_BRACE, 0)

        def getRuleIndex(self):
            return LaTeXParser.RULE_subexpr




    def subexpr(self):

        localctx = LaTeXParser.SubexprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 68, self.RULE_subexpr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 420
            self.match(LaTeXParser.UNDERSCORE)
            self.state = 426
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [LaTeXParser.CMD_MATHIT, LaTeXParser.DIFFERENTIAL, LaTeXParser.LETTER, LaTeXParser.NUMBER, LaTeXParser.SYMBOL]:
                self.state = 421
                self.atom()
                pass
            elif token in [LaTeXParser.L_BRACE]:
                self.state = 422
                self.match(LaTeXParser.L_BRACE)
                self.state = 423
                self.expr()
                self.state = 424
                self.match(LaTeXParser.R_BRACE)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class SupexprContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(LaTeXParser.SupexprContext, self).__init__(parent, invokingState)
            self.parser = parser

        def CARET(self):
            return self.getToken(LaTeXParser.CARET, 0)

        def atom(self):
            return self.getTypedRuleContext(LaTeXParser.AtomContext,0)


        def L_BRACE(self):
            return self.getToken(LaTeXParser.L_BRACE, 0)

        def expr(self):
            return self.getTypedRuleContext(LaTeXParser.ExprContext,0)


        def R_BRACE(self):
            return self.getToken(LaTeXParser.R_BRACE, 0)

        def getRuleIndex(self):
            return LaTeXParser.RULE_supexpr




    def supexpr(self):

        localctx = LaTeXParser.SupexprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 70, self.RULE_supexpr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 428
            self.match(LaTeXParser.CARET)
            self.state = 434
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [LaTeXParser.CMD_MATHIT, LaTeXParser.DIFFERENTIAL, LaTeXParser.LETTER, LaTeXParser.NUMBER, LaTeXParser.SYMBOL]:
                self.state = 429
                self.atom()
                pass
            elif token in [LaTeXParser.L_BRACE]:
                self.state = 430
                self.match(LaTeXParser.L_BRACE)
                self.state = 431
                self.expr()
                self.state = 432
                self.match(LaTeXParser.R_BRACE)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class SubeqContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(LaTeXParser.SubeqContext, self).__init__(parent, invokingState)
            self.parser = parser

        def UNDERSCORE(self):
            return self.getToken(LaTeXParser.UNDERSCORE, 0)

        def L_BRACE(self):
            return self.getToken(LaTeXParser.L_BRACE, 0)

        def R_BRACE(self):
            return self.getToken(LaTeXParser.R_BRACE, 0)

        def expr(self):
            return self.getTypedRuleContext(LaTeXParser.ExprContext,0)


        def equality(self):
            return self.getTypedRuleContext(LaTeXParser.EqualityContext,0)


        def getRuleIndex(self):
            return LaTeXParser.RULE_subeq




    def subeq(self):

        localctx = LaTeXParser.SubeqContext(self, self._ctx, self.state)
        self.enterRule(localctx, 72, self.RULE_subeq)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 436
            self.match(LaTeXParser.UNDERSCORE)
            self.state = 437
            self.match(LaTeXParser.L_BRACE)
            self.state = 440
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,47,self._ctx)
            if la_ == 1:
                self.state = 438
                self.expr()
                pass

            elif la_ == 2:
                self.state = 439
                self.equality()
                pass


            self.state = 442
            self.match(LaTeXParser.R_BRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class SupeqContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(LaTeXParser.SupeqContext, self).__init__(parent, invokingState)
            self.parser = parser

        def UNDERSCORE(self):
            return self.getToken(LaTeXParser.UNDERSCORE, 0)

        def L_BRACE(self):
            return self.getToken(LaTeXParser.L_BRACE, 0)

        def R_BRACE(self):
            return self.getToken(LaTeXParser.R_BRACE, 0)

        def expr(self):
            return self.getTypedRuleContext(LaTeXParser.ExprContext,0)


        def equality(self):
            return self.getTypedRuleContext(LaTeXParser.EqualityContext,0)


        def getRuleIndex(self):
            return LaTeXParser.RULE_supeq




    def supeq(self):

        localctx = LaTeXParser.SupeqContext(self, self._ctx, self.state)
        self.enterRule(localctx, 74, self.RULE_supeq)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 444
            self.match(LaTeXParser.UNDERSCORE)
            self.state = 445
            self.match(LaTeXParser.L_BRACE)
            self.state = 448
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,48,self._ctx)
            if la_ == 1:
                self.state = 446
                self.expr()
                pass

            elif la_ == 2:
                self.state = 447
                self.equality()
                pass


            self.state = 450
            self.match(LaTeXParser.R_BRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx, ruleIndex, predIndex):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[3] = self.relation_sempred
        self._predicates[6] = self.additive_sempred
        self._predicates[7] = self.mp_sempred
        self._predicates[8] = self.mp_nofunc_sempred
        self._predicates[17] = self.exp_sempred
        self._predicates[18] = self.exp_nofunc_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def relation_sempred(self, localctx, predIndex):
            if predIndex == 0:
                return self.precpred(self._ctx, 3)
         

    def additive_sempred(self, localctx, predIndex):
            if predIndex == 1:
                return self.precpred(self._ctx, 2)
         

    def mp_sempred(self, localctx, predIndex):
            if predIndex == 2:
                return self.precpred(self._ctx, 2)
         

    def mp_nofunc_sempred(self, localctx, predIndex):
            if predIndex == 3:
                return self.precpred(self._ctx, 2)
         

    def exp_sempred(self, localctx, predIndex):
            if predIndex == 4:
                return self.precpred(self._ctx, 2)
         

    def exp_nofunc_sempred(self, localctx, predIndex):
            if predIndex == 5:
                return self.precpred(self._ctx, 2)
         




