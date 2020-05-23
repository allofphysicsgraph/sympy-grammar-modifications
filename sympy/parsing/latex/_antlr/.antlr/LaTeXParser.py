# Generated from /home/user/sympy-grammar-modifications/sympy/parsing/latex/_antlr/LaTeX.g4 by ANTLR 4.7.1
# encoding: utf-8
from __future__ import print_function
from antlr4 import *
from io import StringIO
import sys

def serializedATN():
    with StringIO() as buf:
        buf.write(u"\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3")
        buf.write(u"I\u01b4\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t")
        buf.write(u"\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write(u"\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4")
        buf.write(u"\23\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30")
        buf.write(u"\t\30\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t")
        buf.write(u"\35\4\36\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$")
        buf.write(u"\t$\3\2\3\2\3\3\3\3\3\3\3\3\3\3\3\3\5\3Q\n\3\3\3\3\3")
        buf.write(u"\3\3\7\3V\n\3\f\3\16\3Y\13\3\3\4\3\4\3\4\3\4\3\5\3\5")
        buf.write(u"\3\6\3\6\3\6\3\6\3\6\3\6\7\6g\n\6\f\6\16\6j\13\6\3\7")
        buf.write(u"\3\7\3\7\3\7\3\7\3\7\7\7r\n\7\f\7\16\7u\13\7\3\b\3\b")
        buf.write(u"\3\b\3\b\3\b\3\b\7\b}\n\b\f\b\16\b\u0080\13\b\3\t\3\t")
        buf.write(u"\3\t\6\t\u0085\n\t\r\t\16\t\u0086\5\t\u0089\n\t\3\n\3")
        buf.write(u"\n\3\n\3\n\7\n\u008f\n\n\f\n\16\n\u0092\13\n\5\n\u0094")
        buf.write(u"\n\n\3\13\3\13\7\13\u0098\n\13\f\13\16\13\u009b\13\13")
        buf.write(u"\3\f\3\f\7\f\u009f\n\f\f\f\16\f\u00a2\13\f\3\r\3\r\5")
        buf.write(u"\r\u00a6\n\r\3\16\3\16\3\16\3\16\3\16\3\16\5\16\u00ae")
        buf.write(u"\n\16\3\17\3\17\3\17\3\17\5\17\u00b4\n\17\3\17\3\17\3")
        buf.write(u"\20\3\20\3\20\3\20\5\20\u00bc\n\20\3\20\3\20\3\21\3\21")
        buf.write(u"\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21\5\21\u00ca\n")
        buf.write(u"\21\3\21\5\21\u00cd\n\21\7\21\u00cf\n\21\f\21\16\21\u00d2")
        buf.write(u"\13\21\3\22\3\22\3\22\3\22\3\22\3\22\3\22\3\22\3\22\3")
        buf.write(u"\22\5\22\u00de\n\22\3\22\5\22\u00e1\n\22\7\22\u00e3\n")
        buf.write(u"\22\f\22\16\22\u00e6\13\22\3\23\3\23\3\23\3\23\3\23\5")
        buf.write(u"\23\u00ed\n\23\3\24\3\24\3\24\3\24\5\24\u00f3\n\24\3")
        buf.write(u"\25\3\25\3\25\3\25\3\25\3\25\3\25\3\25\5\25\u00fd\n\25")
        buf.write(u"\3\25\3\25\3\25\3\25\3\25\3\25\5\25\u0105\n\25\3\26\3")
        buf.write(u"\26\3\26\3\26\3\27\3\27\5\27\u010d\n\27\3\27\3\27\3\27")
        buf.write(u"\5\27\u0112\n\27\3\30\3\30\3\30\3\30\3\30\3\31\7\31\u011a")
        buf.write(u"\n\31\f\31\16\31\u011d\13\31\3\32\3\32\3\32\3\32\3\32")
        buf.write(u"\3\32\3\32\3\32\3\33\3\33\3\34\3\34\5\34\u012b\n\34\3")
        buf.write(u"\34\5\34\u012e\n\34\3\34\5\34\u0131\n\34\3\34\5\34\u0134")
        buf.write(u"\n\34\5\34\u0136\n\34\3\34\3\34\3\34\3\34\3\34\5\34\u013d")
        buf.write(u"\n\34\3\34\3\34\5\34\u0141\n\34\3\34\3\34\3\34\3\34\3")
        buf.write(u"\34\3\34\5\34\u0149\n\34\3\34\3\34\3\34\3\34\3\34\3\34")
        buf.write(u"\5\34\u0151\n\34\3\34\5\34\u0154\n\34\3\34\3\34\3\34")
        buf.write(u"\5\34\u0159\n\34\3\34\3\34\3\34\3\34\3\34\5\34\u0160")
        buf.write(u"\n\34\3\34\3\34\3\34\3\34\3\34\3\34\3\34\3\34\3\34\3")
        buf.write(u"\34\3\34\5\34\u016d\n\34\3\34\3\34\3\34\3\34\3\34\3\34")
        buf.write(u"\5\34\u0175\n\34\3\35\3\35\3\35\3\35\3\35\5\35\u017c")
        buf.write(u"\n\35\3\36\3\36\3\36\3\36\3\36\3\36\3\36\3\36\3\36\5")
        buf.write(u"\36\u0187\n\36\3\36\3\36\3\37\3\37\3\37\3\37\3\37\5\37")
        buf.write(u"\u0190\n\37\3 \3 \3!\3!\3!\3!\3!\3!\5!\u019a\n!\3\"\3")
        buf.write(u"\"\3\"\3\"\3\"\3\"\5\"\u01a2\n\"\3#\3#\3#\3#\5#\u01a8")
        buf.write(u"\n#\3#\3#\3$\3$\3$\3$\5$\u01b0\n$\3$\3$\3$\2\b\4\n\f")
        buf.write(u"\16 \"%\2\4\6\b\n\f\16\20\22\24\26\30\32\34\36 \"$&(")
        buf.write(u"*,.\60\62\64\668:<>@BDF\2\b\3\2CG\3\2\5\6\5\2\7\b*,\61")
        buf.write(u"\61\4\2AAII\3\2\25(\3\2\23\24\2\u01d0\2H\3\2\2\2\4P\3")
        buf.write(u"\2\2\2\6Z\3\2\2\2\b^\3\2\2\2\n`\3\2\2\2\fk\3\2\2\2\16")
        buf.write(u"v\3\2\2\2\20\u0088\3\2\2\2\22\u0093\3\2\2\2\24\u0095")
        buf.write(u"\3\2\2\2\26\u009c\3\2\2\2\30\u00a5\3\2\2\2\32\u00a7\3")
        buf.write(u"\2\2\2\34\u00af\3\2\2\2\36\u00b7\3\2\2\2 \u00bf\3\2\2")
        buf.write(u"\2\"\u00d3\3\2\2\2$\u00ec\3\2\2\2&\u00f2\3\2\2\2(\u0104")
        buf.write(u"\3\2\2\2*\u0106\3\2\2\2,\u0111\3\2\2\2.\u0113\3\2\2\2")
        buf.write(u"\60\u011b\3\2\2\2\62\u011e\3\2\2\2\64\u0126\3\2\2\2\66")
        buf.write(u"\u0174\3\2\2\28\u017b\3\2\2\2:\u017d\3\2\2\2<\u018f\3")
        buf.write(u"\2\2\2>\u0191\3\2\2\2@\u0193\3\2\2\2B\u019b\3\2\2\2D")
        buf.write(u"\u01a3\3\2\2\2F\u01ab\3\2\2\2HI\5\4\3\2I\3\3\2\2\2JK")
        buf.write(u"\b\3\1\2KQ\5\b\5\2LM\79\2\2MN\5\4\3\2NO\7:\2\2OQ\3\2")
        buf.write(u"\2\2PJ\3\2\2\2PL\3\2\2\2QW\3\2\2\2RS\f\5\2\2ST\t\2\2")
        buf.write(u"\2TV\5\4\3\6UR\3\2\2\2VY\3\2\2\2WU\3\2\2\2WX\3\2\2\2")
        buf.write(u"X\5\3\2\2\2YW\3\2\2\2Z[\5\b\5\2[\\\7C\2\2\\]\5\b\5\2")
        buf.write(u"]\7\3\2\2\2^_\5\n\6\2_\t\3\2\2\2`a\b\6\1\2ab\5\f\7\2")
        buf.write(u"bh\3\2\2\2cd\f\4\2\2de\t\3\2\2eg\5\n\6\5fc\3\2\2\2gj")
        buf.write(u"\3\2\2\2hf\3\2\2\2hi\3\2\2\2i\13\3\2\2\2jh\3\2\2\2kl")
        buf.write(u"\b\7\1\2lm\5\20\t\2ms\3\2\2\2no\f\4\2\2op\t\4\2\2pr\5")
        buf.write(u"\f\7\5qn\3\2\2\2ru\3\2\2\2sq\3\2\2\2st\3\2\2\2t\r\3\2")
        buf.write(u"\2\2us\3\2\2\2vw\b\b\1\2wx\5\22\n\2x~\3\2\2\2yz\f\4\2")
        buf.write(u"\2z{\t\4\2\2{}\5\16\b\5|y\3\2\2\2}\u0080\3\2\2\2~|\3")
        buf.write(u"\2\2\2~\177\3\2\2\2\177\17\3\2\2\2\u0080~\3\2\2\2\u0081")
        buf.write(u"\u0082\t\3\2\2\u0082\u0089\5\20\t\2\u0083\u0085\5\24")
        buf.write(u"\13\2\u0084\u0083\3\2\2\2\u0085\u0086\3\2\2\2\u0086\u0084")
        buf.write(u"\3\2\2\2\u0086\u0087\3\2\2\2\u0087\u0089\3\2\2\2\u0088")
        buf.write(u"\u0081\3\2\2\2\u0088\u0084\3\2\2\2\u0089\21\3\2\2\2\u008a")
        buf.write(u"\u008b\t\3\2\2\u008b\u0094\5\22\n\2\u008c\u0090\5\24")
        buf.write(u"\13\2\u008d\u008f\5\26\f\2\u008e\u008d\3\2\2\2\u008f")
        buf.write(u"\u0092\3\2\2\2\u0090\u008e\3\2\2\2\u0090\u0091\3\2\2")
        buf.write(u"\2\u0091\u0094\3\2\2\2\u0092\u0090\3\2\2\2\u0093\u008a")
        buf.write(u"\3\2\2\2\u0093\u008c\3\2\2\2\u0094\23\3\2\2\2\u0095\u0099")
        buf.write(u"\5 \21\2\u0096\u0098\5\30\r\2\u0097\u0096\3\2\2\2\u0098")
        buf.write(u"\u009b\3\2\2\2\u0099\u0097\3\2\2\2\u0099\u009a\3\2\2")
        buf.write(u"\2\u009a\25\3\2\2\2\u009b\u0099\3\2\2\2\u009c\u00a0\5")
        buf.write(u"\"\22\2\u009d\u009f\5\30\r\2\u009e\u009d\3\2\2\2\u009f")
        buf.write(u"\u00a2\3\2\2\2\u00a0\u009e\3\2\2\2\u00a0\u00a1\3\2\2")
        buf.write(u"\2\u00a1\27\3\2\2\2\u00a2\u00a0\3\2\2\2\u00a3\u00a6\7")
        buf.write(u"H\2\2\u00a4\u00a6\5\32\16\2\u00a5\u00a3\3\2\2\2\u00a5")
        buf.write(u"\u00a4\3\2\2\2\u00a6\31\3\2\2\2\u00a7\u00ad\7\17\2\2")
        buf.write(u"\u00a8\u00ae\5\36\20\2\u00a9\u00ae\5\34\17\2\u00aa\u00ab")
        buf.write(u"\5\36\20\2\u00ab\u00ac\5\34\17\2\u00ac\u00ae\3\2\2\2")
        buf.write(u"\u00ad\u00a8\3\2\2\2\u00ad\u00a9\3\2\2\2\u00ad\u00aa")
        buf.write(u"\3\2\2\2\u00ae\33\3\2\2\2\u00af\u00b0\7/\2\2\u00b0\u00b3")
        buf.write(u"\7\13\2\2\u00b1\u00b4\5\b\5\2\u00b2\u00b4\5\6\4\2\u00b3")
        buf.write(u"\u00b1\3\2\2\2\u00b3\u00b2\3\2\2\2\u00b4\u00b5\3\2\2")
        buf.write(u"\2\u00b5\u00b6\7\f\2\2\u00b6\35\3\2\2\2\u00b7\u00b8\7")
        buf.write(u"\60\2\2\u00b8\u00bb\7\13\2\2\u00b9\u00bc\5\b\5\2\u00ba")
        buf.write(u"\u00bc\5\6\4\2\u00bb\u00b9\3\2\2\2\u00bb\u00ba\3\2\2")
        buf.write(u"\2\u00bc\u00bd\3\2\2\2\u00bd\u00be\7\f\2\2\u00be\37\3")
        buf.write(u"\2\2\2\u00bf\u00c0\b\21\1\2\u00c0\u00c1\5$\23\2\u00c1")
        buf.write(u"\u00d0\3\2\2\2\u00c2\u00c3\f\4\2\2\u00c3\u00c9\7\60\2")
        buf.write(u"\2\u00c4\u00ca\5,\27\2\u00c5\u00c6\7\13\2\2\u00c6\u00c7")
        buf.write(u"\5\b\5\2\u00c7\u00c8\7\f\2\2\u00c8\u00ca\3\2\2\2\u00c9")
        buf.write(u"\u00c4\3\2\2\2\u00c9\u00c5\3\2\2\2\u00ca\u00cc\3\2\2")
        buf.write(u"\2\u00cb\u00cd\5@!\2\u00cc\u00cb\3\2\2\2\u00cc\u00cd")
        buf.write(u"\3\2\2\2\u00cd\u00cf\3\2\2\2\u00ce\u00c2\3\2\2\2\u00cf")
        buf.write(u"\u00d2\3\2\2\2\u00d0\u00ce\3\2\2\2\u00d0\u00d1\3\2\2")
        buf.write(u"\2\u00d1!\3\2\2\2\u00d2\u00d0\3\2\2\2\u00d3\u00d4\b\22")
        buf.write(u"\1\2\u00d4\u00d5\5&\24\2\u00d5\u00e4\3\2\2\2\u00d6\u00d7")
        buf.write(u"\f\4\2\2\u00d7\u00dd\7\60\2\2\u00d8\u00de\5,\27\2\u00d9")
        buf.write(u"\u00da\7\13\2\2\u00da\u00db\5\b\5\2\u00db\u00dc\7\f\2")
        buf.write(u"\2\u00dc\u00de\3\2\2\2\u00dd\u00d8\3\2\2\2\u00dd\u00d9")
        buf.write(u"\3\2\2\2\u00de\u00e0\3\2\2\2\u00df\u00e1\5@!\2\u00e0")
        buf.write(u"\u00df\3\2\2\2\u00e0\u00e1\3\2\2\2\u00e1\u00e3\3\2\2")
        buf.write(u"\2\u00e2\u00d6\3\2\2\2\u00e3\u00e6\3\2\2\2\u00e4\u00e2")
        buf.write(u"\3\2\2\2\u00e4\u00e5\3\2\2\2\u00e5#\3\2\2\2\u00e6\u00e4")
        buf.write(u"\3\2\2\2\u00e7\u00ed\5(\25\2\u00e8\u00ed\5*\26\2\u00e9")
        buf.write(u"\u00ed\5\66\34\2\u00ea\u00ed\5,\27\2\u00eb\u00ed\5\62")
        buf.write(u"\32\2\u00ec\u00e7\3\2\2\2\u00ec\u00e8\3\2\2\2\u00ec\u00e9")
        buf.write(u"\3\2\2\2\u00ec\u00ea\3\2\2\2\u00ec\u00eb\3\2\2\2\u00ed")
        buf.write(u"%\3\2\2\2\u00ee\u00f3\5(\25\2\u00ef\u00f3\5*\26\2\u00f0")
        buf.write(u"\u00f3\5,\27\2\u00f1\u00f3\5\62\32\2\u00f2\u00ee\3\2")
        buf.write(u"\2\2\u00f2\u00ef\3\2\2\2\u00f2\u00f0\3\2\2\2\u00f2\u00f1")
        buf.write(u"\3\2\2\2\u00f3\'\3\2\2\2\u00f4\u00f5\7\t\2\2\u00f5\u00f6")
        buf.write(u"\5\b\5\2\u00f6\u00f7\7\n\2\2\u00f7\u0105\3\2\2\2\u00f8")
        buf.write(u"\u00f9\7\r\2\2\u00f9\u00fc\5\b\5\2\u00fa\u00fb\7\63\2")
        buf.write(u"\2\u00fb\u00fd\5\b\5\2\u00fc\u00fa\3\2\2\2\u00fc\u00fd")
        buf.write(u"\3\2\2\2\u00fd\u00fe\3\2\2\2\u00fe\u00ff\7\16\2\2\u00ff")
        buf.write(u"\u0105\3\2\2\2\u0100\u0101\7\13\2\2\u0101\u0102\5\b\5")
        buf.write(u"\2\u0102\u0103\7\f\2\2\u0103\u0105\3\2\2\2\u0104\u00f4")
        buf.write(u"\3\2\2\2\u0104\u00f8\3\2\2\2\u0104\u0100\3\2\2\2\u0105")
        buf.write(u")\3\2\2\2\u0106\u0107\7\17\2\2\u0107\u0108\5\b\5\2\u0108")
        buf.write(u"\u0109\7\17\2\2\u0109+\3\2\2\2\u010a\u010c\t\5\2\2\u010b")
        buf.write(u"\u010d\5@!\2\u010c\u010b\3\2\2\2\u010c\u010d\3\2\2\2")
        buf.write(u"\u010d\u0112\3\2\2\2\u010e\u0112\7B\2\2\u010f\u0112\7")
        buf.write(u"@\2\2\u0110\u0112\5.\30\2\u0111\u010a\3\2\2\2\u0111\u010e")
        buf.write(u"\3\2\2\2\u0111\u010f\3\2\2\2\u0111\u0110\3\2\2\2\u0112")
        buf.write(u"-\3\2\2\2\u0113\u0114\7.\2\2\u0114\u0115\7\13\2\2\u0115")
        buf.write(u"\u0116\5\60\31\2\u0116\u0117\7\f\2\2\u0117/\3\2\2\2\u0118")
        buf.write(u"\u011a\7A\2\2\u0119\u0118\3\2\2\2\u011a\u011d\3\2\2\2")
        buf.write(u"\u011b\u0119\3\2\2\2\u011b\u011c\3\2\2\2\u011c\61\3\2")
        buf.write(u"\2\2\u011d\u011b\3\2\2\2\u011e\u011f\7-\2\2\u011f\u0120")
        buf.write(u"\7\13\2\2\u0120\u0121\5\b\5\2\u0121\u0122\7\f\2\2\u0122")
        buf.write(u"\u0123\7\13\2\2\u0123\u0124\5\b\5\2\u0124\u0125\7\f\2")
        buf.write(u"\2\u0125\63\3\2\2\2\u0126\u0127\t\6\2\2\u0127\65\3\2")
        buf.write(u"\2\2\u0128\u0135\5\64\33\2\u0129\u012b\5@!\2\u012a\u0129")
        buf.write(u"\3\2\2\2\u012a\u012b\3\2\2\2\u012b\u012d\3\2\2\2\u012c")
        buf.write(u"\u012e\5B\"\2\u012d\u012c\3\2\2\2\u012d\u012e\3\2\2\2")
        buf.write(u"\u012e\u0136\3\2\2\2\u012f\u0131\5B\"\2\u0130\u012f\3")
        buf.write(u"\2\2\2\u0130\u0131\3\2\2\2\u0131\u0133\3\2\2\2\u0132")
        buf.write(u"\u0134\5@!\2\u0133\u0132\3\2\2\2\u0133\u0134\3\2\2\2")
        buf.write(u"\u0134\u0136\3\2\2\2\u0135\u012a\3\2\2\2\u0135\u0130")
        buf.write(u"\3\2\2\2\u0136\u013c\3\2\2\2\u0137\u0138\7\t\2\2\u0138")
        buf.write(u"\u0139\5<\37\2\u0139\u013a\7\n\2\2\u013a\u013d\3\2\2")
        buf.write(u"\2\u013b\u013d\5> \2\u013c\u0137\3\2\2\2\u013c\u013b")
        buf.write(u"\3\2\2\2\u013d\u0175\3\2\2\2\u013e\u0140\t\5\2\2\u013f")
        buf.write(u"\u0141\5@!\2\u0140\u013f\3\2\2\2\u0140\u0141\3\2\2\2")
        buf.write(u"\u0141\u0142\3\2\2\2\u0142\u0143\7\t\2\2\u0143\u0144")
        buf.write(u"\58\35\2\u0144\u0145\7\n\2\2\u0145\u0175\3\2\2\2\u0146")
        buf.write(u"\u0148\7\22\2\2\u0147\u0149\7/\2\2\u0148\u0147\3\2\2")
        buf.write(u"\2\u0148\u0149\3\2\2\2\u0149\u0150\3\2\2\2\u014a\u014b")
        buf.write(u"\5@!\2\u014b\u014c\5B\"\2\u014c\u0151\3\2\2\2\u014d\u014e")
        buf.write(u"\5B\"\2\u014e\u014f\5@!\2\u014f\u0151\3\2\2\2\u0150\u014a")
        buf.write(u"\3\2\2\2\u0150\u014d\3\2\2\2\u0150\u0151\3\2\2\2\u0151")
        buf.write(u"\u0158\3\2\2\2\u0152\u0154\5\n\6\2\u0153\u0152\3\2\2")
        buf.write(u"\2\u0153\u0154\3\2\2\2\u0154\u0155\3\2\2\2\u0155\u0159")
        buf.write(u"\7@\2\2\u0156\u0159\5\62\32\2\u0157\u0159\5\n\6\2\u0158")
        buf.write(u"\u0153\3\2\2\2\u0158\u0156\3\2\2\2\u0158\u0157\3\2\2")
        buf.write(u"\2\u0159\u0175\3\2\2\2\u015a\u015f\7)\2\2\u015b\u015c")
        buf.write(u"\7\r\2\2\u015c\u015d\5\b\5\2\u015d\u015e\7\16\2\2\u015e")
        buf.write(u"\u0160\3\2\2\2\u015f\u015b\3\2\2\2\u015f\u0160\3\2\2")
        buf.write(u"\2\u0160\u0161\3\2\2\2\u0161\u0162\7\13\2\2\u0162\u0163")
        buf.write(u"\5\b\5\2\u0163\u0164\7\f\2\2\u0164\u0175\3\2\2\2\u0165")
        buf.write(u"\u016c\t\7\2\2\u0166\u0167\5D#\2\u0167\u0168\5B\"\2\u0168")
        buf.write(u"\u016d\3\2\2\2\u0169\u016a\5B\"\2\u016a\u016b\5D#\2\u016b")
        buf.write(u"\u016d\3\2\2\2\u016c\u0166\3\2\2\2\u016c\u0169\3\2\2")
        buf.write(u"\2\u016d\u016e\3\2\2\2\u016e\u016f\5\f\7\2\u016f\u0175")
        buf.write(u"\3\2\2\2\u0170\u0171\7\20\2\2\u0171\u0172\5:\36\2\u0172")
        buf.write(u"\u0173\5\f\7\2\u0173\u0175\3\2\2\2\u0174\u0128\3\2\2")
        buf.write(u"\2\u0174\u013e\3\2\2\2\u0174\u0146\3\2\2\2\u0174\u015a")
        buf.write(u"\3\2\2\2\u0174\u0165\3\2\2\2\u0174\u0170\3\2\2\2\u0175")
        buf.write(u"\67\3\2\2\2\u0176\u0177\5\b\5\2\u0177\u0178\7\63\2\2")
        buf.write(u"\u0178\u0179\58\35\2\u0179\u017c\3\2\2\2\u017a\u017c")
        buf.write(u"\5\b\5\2\u017b\u0176\3\2\2\2\u017b\u017a\3\2\2\2\u017c")
        buf.write(u"9\3\2\2\2\u017d\u017e\7/\2\2\u017e\u017f\7\13\2\2\u017f")
        buf.write(u"\u0180\t\5\2\2\u0180\u0181\7\21\2\2\u0181\u0186\5\b\5")
        buf.write(u"\2\u0182\u0183\7\60\2\2\u0183\u0184\7\13\2\2\u0184\u0185")
        buf.write(u"\t\3\2\2\u0185\u0187\7\f\2\2\u0186\u0182\3\2\2\2\u0186")
        buf.write(u"\u0187\3\2\2\2\u0187\u0188\3\2\2\2\u0188\u0189\7\f\2")
        buf.write(u"\2\u0189;\3\2\2\2\u018a\u0190\5\b\5\2\u018b\u018c\5\b")
        buf.write(u"\5\2\u018c\u018d\7\63\2\2\u018d\u018e\5<\37\2\u018e\u0190")
        buf.write(u"\3\2\2\2\u018f\u018a\3\2\2\2\u018f\u018b\3\2\2\2\u0190")
        buf.write(u"=\3\2\2\2\u0191\u0192\5\16\b\2\u0192?\3\2\2\2\u0193\u0199")
        buf.write(u"\7/\2\2\u0194\u019a\5,\27\2\u0195\u0196\7\13\2\2\u0196")
        buf.write(u"\u0197\5\b\5\2\u0197\u0198\7\f\2\2\u0198\u019a\3\2\2")
        buf.write(u"\2\u0199\u0194\3\2\2\2\u0199\u0195\3\2\2\2\u019aA\3\2")
        buf.write(u"\2\2\u019b\u01a1\7\60\2\2\u019c\u01a2\5,\27\2\u019d\u019e")
        buf.write(u"\7\13\2\2\u019e\u019f\5\b\5\2\u019f\u01a0\7\f\2\2\u01a0")
        buf.write(u"\u01a2\3\2\2\2\u01a1\u019c\3\2\2\2\u01a1\u019d\3\2\2")
        buf.write(u"\2\u01a2C\3\2\2\2\u01a3\u01a4\7/\2\2\u01a4\u01a7\7\13")
        buf.write(u"\2\2\u01a5\u01a8\5\b\5\2\u01a6\u01a8\5\6\4\2\u01a7\u01a5")
        buf.write(u"\3\2\2\2\u01a7\u01a6\3\2\2\2\u01a8\u01a9\3\2\2\2\u01a9")
        buf.write(u"\u01aa\7\f\2\2\u01aaE\3\2\2\2\u01ab\u01ac\7/\2\2\u01ac")
        buf.write(u"\u01af\7\13\2\2\u01ad\u01b0\5\b\5\2\u01ae\u01b0\5\6\4")
        buf.write(u"\2\u01af\u01ad\3\2\2\2\u01af\u01ae\3\2\2\2\u01b0\u01b1")
        buf.write(u"\3\2\2\2\u01b1\u01b2\7\f\2\2\u01b2G\3\2\2\2\63PWhs~\u0086")
        buf.write(u"\u0088\u0090\u0093\u0099\u00a0\u00a5\u00ad\u00b3\u00bb")
        buf.write(u"\u00c9\u00cc\u00d0\u00dd\u00e0\u00e4\u00ec\u00f2\u00fc")
        buf.write(u"\u0104\u010c\u0111\u011b\u012a\u012d\u0130\u0133\u0135")
        buf.write(u"\u013c\u0140\u0148\u0150\u0153\u0158\u015f\u016c\u0174")
        buf.write(u"\u017b\u0186\u018f\u0199\u01a1\u01a7\u01af")
        return buf.getvalue()


class LaTeXParser ( Parser ):

    grammarFileName = "LaTeX.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ u"<INVALID>", u"<INVALID>", u"<INVALID>", u"'+'", u"'-'", 
                     u"'*'", u"'/'", u"'('", u"')'", u"'{'", u"'}'", u"'['", 
                     u"']'", u"'|'", u"'\\lim'", u"<INVALID>", u"'\\int'", 
                     u"'\\sum'", u"'\\prod'", u"'\\log'", u"'\\ln'", u"'\\sin'", 
                     u"'\\cos'", u"'\\tan'", u"'\\csc'", u"'\\sec'", u"'\\cot'", 
                     u"'\\arcsin'", u"'\\arccos'", u"'\\arctan'", u"'\\arccsc'", 
                     u"'\\arcsec'", u"'\\arccot'", u"'\\sinh'", u"'\\cosh'", 
                     u"'\\tanh'", u"'\\arsinh'", u"'\\arcosh'", u"'\\artanh'", 
                     u"'\\sqrt'", u"'\\times'", u"'\\cdot'", u"'\\div'", 
                     u"'\\frac'", u"'\\mathit'", u"'_'", u"'^'", u"':'", 
                     u"'&'", u"','", u"<INVALID>", u"<INVALID>", u"<INVALID>", 
                     u"<INVALID>", u"<INVALID>", u"<INVALID>", u"<INVALID>", 
                     u"'\\left['", u"'\\left'", u"'\\right'", u"'.'", u"'\\rm'", 
                     u"<INVALID>", u"<INVALID>", u"<INVALID>", u"'='", u"'<'", 
                     u"'\\leq'", u"'>'", u"'\\geq'", u"'!'" ]

    symbolicNames = [ u"<INVALID>", u"WS", u"GREEK", u"ADD", u"SUB", u"MUL", 
                      u"DIV", u"L_PAREN", u"R_PAREN", u"L_BRACE", u"R_BRACE", 
                      u"L_BRACKET", u"R_BRACKET", u"BAR", u"FUNC_LIM", u"LIM_APPROACH_SYM", 
                      u"FUNC_INT", u"FUNC_SUM", u"FUNC_PROD", u"FUNC_LOG", 
                      u"FUNC_LN", u"FUNC_SIN", u"FUNC_COS", u"FUNC_TAN", 
                      u"FUNC_CSC", u"FUNC_SEC", u"FUNC_COT", u"FUNC_ARCSIN", 
                      u"FUNC_ARCCOS", u"FUNC_ARCTAN", u"FUNC_ARCCSC", u"FUNC_ARCSEC", 
                      u"FUNC_ARCCOT", u"FUNC_SINH", u"FUNC_COSH", u"FUNC_TANH", 
                      u"FUNC_ARSINH", u"FUNC_ARCOSH", u"FUNC_ARTANH", u"FUNC_SQRT", 
                      u"CMD_TIMES", u"CMD_CDOT", u"CMD_DIV", u"CMD_FRAC", 
                      u"CMD_MATHIT", u"UNDERSCORE", u"CARET", u"COLON", 
                      u"AMPERSAND", u"COMMA", u"ARRAY", u"SUBEQUATIONS", 
                      u"SPLIT", u"EQUATION", u"EQNARRAY", u"BEGIN", u"END", 
                      u"LEFT_BRACKET", u"LEFT", u"RIGHT", u"DOT", u"RM", 
                      u"DIFFERENTIAL", u"LETTER", u"NUMBER", u"EQUAL", u"LT", 
                      u"LTE", u"GT", u"GTE", u"BANG", u"SYMBOL" ]

    RULE_math = 0
    RULE_relation = 1
    RULE_equality = 2
    RULE_expr = 3
    RULE_additive = 4
    RULE_mp = 5
    RULE_mp_nofunc = 6
    RULE_unary = 7
    RULE_unary_nofunc = 8
    RULE_postfix = 9
    RULE_postfix_nofunc = 10
    RULE_postfix_op = 11
    RULE_eval_at = 12
    RULE_eval_at_sub = 13
    RULE_eval_at_sup = 14
    RULE_exp = 15
    RULE_exp_nofunc = 16
    RULE_comp = 17
    RULE_comp_nofunc = 18
    RULE_group = 19
    RULE_abs_group = 20
    RULE_atom = 21
    RULE_mathit = 22
    RULE_mathit_text = 23
    RULE_frac = 24
    RULE_func_normal = 25
    RULE_func = 26
    RULE_args = 27
    RULE_limit_sub = 28
    RULE_func_arg = 29
    RULE_func_arg_noparens = 30
    RULE_subexpr = 31
    RULE_supexpr = 32
    RULE_subeq = 33
    RULE_supeq = 34

    ruleNames =  [ u"math", u"relation", u"equality", u"expr", u"additive", 
                   u"mp", u"mp_nofunc", u"unary", u"unary_nofunc", u"postfix", 
                   u"postfix_nofunc", u"postfix_op", u"eval_at", u"eval_at_sub", 
                   u"eval_at_sup", u"exp", u"exp_nofunc", u"comp", u"comp_nofunc", 
                   u"group", u"abs_group", u"atom", u"mathit", u"mathit_text", 
                   u"frac", u"func_normal", u"func", u"args", u"limit_sub", 
                   u"func_arg", u"func_arg_noparens", u"subexpr", u"supexpr", 
                   u"subeq", u"supeq" ]

    EOF = Token.EOF
    WS=1
    GREEK=2
    ADD=3
    SUB=4
    MUL=5
    DIV=6
    L_PAREN=7
    R_PAREN=8
    L_BRACE=9
    R_BRACE=10
    L_BRACKET=11
    R_BRACKET=12
    BAR=13
    FUNC_LIM=14
    LIM_APPROACH_SYM=15
    FUNC_INT=16
    FUNC_SUM=17
    FUNC_PROD=18
    FUNC_LOG=19
    FUNC_LN=20
    FUNC_SIN=21
    FUNC_COS=22
    FUNC_TAN=23
    FUNC_CSC=24
    FUNC_SEC=25
    FUNC_COT=26
    FUNC_ARCSIN=27
    FUNC_ARCCOS=28
    FUNC_ARCTAN=29
    FUNC_ARCCSC=30
    FUNC_ARCSEC=31
    FUNC_ARCCOT=32
    FUNC_SINH=33
    FUNC_COSH=34
    FUNC_TANH=35
    FUNC_ARSINH=36
    FUNC_ARCOSH=37
    FUNC_ARTANH=38
    FUNC_SQRT=39
    CMD_TIMES=40
    CMD_CDOT=41
    CMD_DIV=42
    CMD_FRAC=43
    CMD_MATHIT=44
    UNDERSCORE=45
    CARET=46
    COLON=47
    AMPERSAND=48
    COMMA=49
    ARRAY=50
    SUBEQUATIONS=51
    SPLIT=52
    EQUATION=53
    EQNARRAY=54
    BEGIN=55
    END=56
    LEFT_BRACKET=57
    LEFT=58
    RIGHT=59
    DOT=60
    RM=61
    DIFFERENTIAL=62
    LETTER=63
    NUMBER=64
    EQUAL=65
    LT=66
    LTE=67
    GT=68
    GTE=69
    BANG=70
    SYMBOL=71

    def __init__(self, input, output=sys.stdout):
        super(LaTeXParser, self).__init__(input, output=output)
        self.checkVersion("4.7.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None



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
        self.enterRule(localctx, 0, self.RULE_math)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 70
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


        def BEGIN(self):
            return self.getToken(LaTeXParser.BEGIN, 0)

        def relation(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(LaTeXParser.RelationContext)
            else:
                return self.getTypedRuleContext(LaTeXParser.RelationContext,i)


        def END(self):
            return self.getToken(LaTeXParser.END, 0)

        def EQUAL(self):
            return self.getToken(LaTeXParser.EQUAL, 0)

        def LT(self):
            return self.getToken(LaTeXParser.LT, 0)

        def LTE(self):
            return self.getToken(LaTeXParser.LTE, 0)

        def GT(self):
            return self.getToken(LaTeXParser.GT, 0)

        def GTE(self):
            return self.getToken(LaTeXParser.GTE, 0)

        def getRuleIndex(self):
            return LaTeXParser.RULE_relation



    def relation(self, _p=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = LaTeXParser.RelationContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 2
        self.enterRecursionRule(localctx, 2, self.RULE_relation, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 78
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [LaTeXParser.ADD, LaTeXParser.SUB, LaTeXParser.L_PAREN, LaTeXParser.L_BRACE, LaTeXParser.L_BRACKET, LaTeXParser.BAR, LaTeXParser.FUNC_LIM, LaTeXParser.FUNC_INT, LaTeXParser.FUNC_SUM, LaTeXParser.FUNC_PROD, LaTeXParser.FUNC_LOG, LaTeXParser.FUNC_LN, LaTeXParser.FUNC_SIN, LaTeXParser.FUNC_COS, LaTeXParser.FUNC_TAN, LaTeXParser.FUNC_CSC, LaTeXParser.FUNC_SEC, LaTeXParser.FUNC_COT, LaTeXParser.FUNC_ARCSIN, LaTeXParser.FUNC_ARCCOS, LaTeXParser.FUNC_ARCTAN, LaTeXParser.FUNC_ARCCSC, LaTeXParser.FUNC_ARCSEC, LaTeXParser.FUNC_ARCCOT, LaTeXParser.FUNC_SINH, LaTeXParser.FUNC_COSH, LaTeXParser.FUNC_TANH, LaTeXParser.FUNC_ARSINH, LaTeXParser.FUNC_ARCOSH, LaTeXParser.FUNC_ARTANH, LaTeXParser.FUNC_SQRT, LaTeXParser.CMD_FRAC, LaTeXParser.CMD_MATHIT, LaTeXParser.DIFFERENTIAL, LaTeXParser.LETTER, LaTeXParser.NUMBER, LaTeXParser.SYMBOL]:
                self.state = 73
                self.expr()
                pass
            elif token in [LaTeXParser.BEGIN]:
                self.state = 74
                self.match(LaTeXParser.BEGIN)
                self.state = 75
                self.relation(0)
                self.state = 76
                self.match(LaTeXParser.END)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 85
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,1,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = LaTeXParser.RelationContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_relation)
                    self.state = 80
                    if not self.precpred(self._ctx, 3):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                    self.state = 81
                    _la = self._input.LA(1)
                    if not(((((_la - 65)) & ~0x3f) == 0 and ((1 << (_la - 65)) & ((1 << (LaTeXParser.EQUAL - 65)) | (1 << (LaTeXParser.LT - 65)) | (1 << (LaTeXParser.LTE - 65)) | (1 << (LaTeXParser.GT - 65)) | (1 << (LaTeXParser.GTE - 65)))) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 82
                    self.relation(4) 
                self.state = 87
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,1,self._ctx)

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
        self.enterRule(localctx, 4, self.RULE_equality)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 88
            self.expr()
            self.state = 89
            self.match(LaTeXParser.EQUAL)
            self.state = 90
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
        self.enterRule(localctx, 6, self.RULE_expr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 92
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
        _startState = 8
        self.enterRecursionRule(localctx, 8, self.RULE_additive, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 95
            self.mp(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 102
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,2,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = LaTeXParser.AdditiveContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_additive)
                    self.state = 97
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 98
                    _la = self._input.LA(1)
                    if not(_la==LaTeXParser.ADD or _la==LaTeXParser.SUB):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 99
                    self.additive(3) 
                self.state = 104
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,2,self._ctx)

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
        _startState = 10
        self.enterRecursionRule(localctx, 10, self.RULE_mp, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 106
            self.unary()
            self._ctx.stop = self._input.LT(-1)
            self.state = 113
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,3,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = LaTeXParser.MpContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_mp)
                    self.state = 108
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 109
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << LaTeXParser.MUL) | (1 << LaTeXParser.DIV) | (1 << LaTeXParser.CMD_TIMES) | (1 << LaTeXParser.CMD_CDOT) | (1 << LaTeXParser.CMD_DIV) | (1 << LaTeXParser.COLON))) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 110
                    self.mp(3) 
                self.state = 115
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,3,self._ctx)

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
        _startState = 12
        self.enterRecursionRule(localctx, 12, self.RULE_mp_nofunc, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 117
            self.unary_nofunc()
            self._ctx.stop = self._input.LT(-1)
            self.state = 124
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,4,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = LaTeXParser.Mp_nofuncContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_mp_nofunc)
                    self.state = 119
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 120
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << LaTeXParser.MUL) | (1 << LaTeXParser.DIV) | (1 << LaTeXParser.CMD_TIMES) | (1 << LaTeXParser.CMD_CDOT) | (1 << LaTeXParser.CMD_DIV) | (1 << LaTeXParser.COLON))) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 121
                    self.mp_nofunc(3) 
                self.state = 126
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,4,self._ctx)

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
        self.enterRule(localctx, 14, self.RULE_unary)
        self._la = 0 # Token type
        try:
            self.state = 134
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [LaTeXParser.ADD, LaTeXParser.SUB]:
                self.enterOuterAlt(localctx, 1)
                self.state = 127
                _la = self._input.LA(1)
                if not(_la==LaTeXParser.ADD or _la==LaTeXParser.SUB):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 128
                self.unary()
                pass
            elif token in [LaTeXParser.L_PAREN, LaTeXParser.L_BRACE, LaTeXParser.L_BRACKET, LaTeXParser.BAR, LaTeXParser.FUNC_LIM, LaTeXParser.FUNC_INT, LaTeXParser.FUNC_SUM, LaTeXParser.FUNC_PROD, LaTeXParser.FUNC_LOG, LaTeXParser.FUNC_LN, LaTeXParser.FUNC_SIN, LaTeXParser.FUNC_COS, LaTeXParser.FUNC_TAN, LaTeXParser.FUNC_CSC, LaTeXParser.FUNC_SEC, LaTeXParser.FUNC_COT, LaTeXParser.FUNC_ARCSIN, LaTeXParser.FUNC_ARCCOS, LaTeXParser.FUNC_ARCTAN, LaTeXParser.FUNC_ARCCSC, LaTeXParser.FUNC_ARCSEC, LaTeXParser.FUNC_ARCCOT, LaTeXParser.FUNC_SINH, LaTeXParser.FUNC_COSH, LaTeXParser.FUNC_TANH, LaTeXParser.FUNC_ARSINH, LaTeXParser.FUNC_ARCOSH, LaTeXParser.FUNC_ARTANH, LaTeXParser.FUNC_SQRT, LaTeXParser.CMD_FRAC, LaTeXParser.CMD_MATHIT, LaTeXParser.DIFFERENTIAL, LaTeXParser.LETTER, LaTeXParser.NUMBER, LaTeXParser.SYMBOL]:
                self.enterOuterAlt(localctx, 2)
                self.state = 130 
                self._errHandler.sync(self)
                _alt = 1
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt == 1:
                        self.state = 129
                        self.postfix()

                    else:
                        raise NoViableAltException(self)
                    self.state = 132 
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,5,self._ctx)

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
        self.enterRule(localctx, 16, self.RULE_unary_nofunc)
        self._la = 0 # Token type
        try:
            self.state = 145
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [LaTeXParser.ADD, LaTeXParser.SUB]:
                self.enterOuterAlt(localctx, 1)
                self.state = 136
                _la = self._input.LA(1)
                if not(_la==LaTeXParser.ADD or _la==LaTeXParser.SUB):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 137
                self.unary_nofunc()
                pass
            elif token in [LaTeXParser.L_PAREN, LaTeXParser.L_BRACE, LaTeXParser.L_BRACKET, LaTeXParser.BAR, LaTeXParser.FUNC_LIM, LaTeXParser.FUNC_INT, LaTeXParser.FUNC_SUM, LaTeXParser.FUNC_PROD, LaTeXParser.FUNC_LOG, LaTeXParser.FUNC_LN, LaTeXParser.FUNC_SIN, LaTeXParser.FUNC_COS, LaTeXParser.FUNC_TAN, LaTeXParser.FUNC_CSC, LaTeXParser.FUNC_SEC, LaTeXParser.FUNC_COT, LaTeXParser.FUNC_ARCSIN, LaTeXParser.FUNC_ARCCOS, LaTeXParser.FUNC_ARCTAN, LaTeXParser.FUNC_ARCCSC, LaTeXParser.FUNC_ARCSEC, LaTeXParser.FUNC_ARCCOT, LaTeXParser.FUNC_SINH, LaTeXParser.FUNC_COSH, LaTeXParser.FUNC_TANH, LaTeXParser.FUNC_ARSINH, LaTeXParser.FUNC_ARCOSH, LaTeXParser.FUNC_ARTANH, LaTeXParser.FUNC_SQRT, LaTeXParser.CMD_FRAC, LaTeXParser.CMD_MATHIT, LaTeXParser.DIFFERENTIAL, LaTeXParser.LETTER, LaTeXParser.NUMBER, LaTeXParser.SYMBOL]:
                self.enterOuterAlt(localctx, 2)
                self.state = 138
                self.postfix()
                self.state = 142
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,7,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 139
                        self.postfix_nofunc() 
                    self.state = 144
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,7,self._ctx)

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
        self.enterRule(localctx, 18, self.RULE_postfix)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 147
            self.exp(0)
            self.state = 151
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,9,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 148
                    self.postfix_op() 
                self.state = 153
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,9,self._ctx)

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
        self.enterRule(localctx, 20, self.RULE_postfix_nofunc)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 154
            self.exp_nofunc(0)
            self.state = 158
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,10,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 155
                    self.postfix_op() 
                self.state = 160
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,10,self._ctx)

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
        self.enterRule(localctx, 22, self.RULE_postfix_op)
        try:
            self.state = 163
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [LaTeXParser.BANG]:
                self.enterOuterAlt(localctx, 1)
                self.state = 161
                self.match(LaTeXParser.BANG)
                pass
            elif token in [LaTeXParser.BAR]:
                self.enterOuterAlt(localctx, 2)
                self.state = 162
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
        self.enterRule(localctx, 24, self.RULE_eval_at)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 165
            self.match(LaTeXParser.BAR)
            self.state = 171
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,12,self._ctx)
            if la_ == 1:
                self.state = 166
                self.eval_at_sup()
                pass

            elif la_ == 2:
                self.state = 167
                self.eval_at_sub()
                pass

            elif la_ == 3:
                self.state = 168
                self.eval_at_sup()
                self.state = 169
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
        self.enterRule(localctx, 26, self.RULE_eval_at_sub)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 173
            self.match(LaTeXParser.UNDERSCORE)
            self.state = 174
            self.match(LaTeXParser.L_BRACE)
            self.state = 177
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,13,self._ctx)
            if la_ == 1:
                self.state = 175
                self.expr()
                pass

            elif la_ == 2:
                self.state = 176
                self.equality()
                pass


            self.state = 179
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
        self.enterRule(localctx, 28, self.RULE_eval_at_sup)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 181
            self.match(LaTeXParser.CARET)
            self.state = 182
            self.match(LaTeXParser.L_BRACE)
            self.state = 185
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,14,self._ctx)
            if la_ == 1:
                self.state = 183
                self.expr()
                pass

            elif la_ == 2:
                self.state = 184
                self.equality()
                pass


            self.state = 187
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
        _startState = 30
        self.enterRecursionRule(localctx, 30, self.RULE_exp, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 190
            self.comp()
            self._ctx.stop = self._input.LT(-1)
            self.state = 206
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,17,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = LaTeXParser.ExpContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_exp)
                    self.state = 192
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 193
                    self.match(LaTeXParser.CARET)
                    self.state = 199
                    self._errHandler.sync(self)
                    token = self._input.LA(1)
                    if token in [LaTeXParser.CMD_MATHIT, LaTeXParser.DIFFERENTIAL, LaTeXParser.LETTER, LaTeXParser.NUMBER, LaTeXParser.SYMBOL]:
                        self.state = 194
                        self.atom()
                        pass
                    elif token in [LaTeXParser.L_BRACE]:
                        self.state = 195
                        self.match(LaTeXParser.L_BRACE)
                        self.state = 196
                        self.expr()
                        self.state = 197
                        self.match(LaTeXParser.R_BRACE)
                        pass
                    else:
                        raise NoViableAltException(self)

                    self.state = 202
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,16,self._ctx)
                    if la_ == 1:
                        self.state = 201
                        self.subexpr()

             
                self.state = 208
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,17,self._ctx)

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
        _startState = 32
        self.enterRecursionRule(localctx, 32, self.RULE_exp_nofunc, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 210
            self.comp_nofunc()
            self._ctx.stop = self._input.LT(-1)
            self.state = 226
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,20,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = LaTeXParser.Exp_nofuncContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_exp_nofunc)
                    self.state = 212
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 213
                    self.match(LaTeXParser.CARET)
                    self.state = 219
                    self._errHandler.sync(self)
                    token = self._input.LA(1)
                    if token in [LaTeXParser.CMD_MATHIT, LaTeXParser.DIFFERENTIAL, LaTeXParser.LETTER, LaTeXParser.NUMBER, LaTeXParser.SYMBOL]:
                        self.state = 214
                        self.atom()
                        pass
                    elif token in [LaTeXParser.L_BRACE]:
                        self.state = 215
                        self.match(LaTeXParser.L_BRACE)
                        self.state = 216
                        self.expr()
                        self.state = 217
                        self.match(LaTeXParser.R_BRACE)
                        pass
                    else:
                        raise NoViableAltException(self)

                    self.state = 222
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,19,self._ctx)
                    if la_ == 1:
                        self.state = 221
                        self.subexpr()

             
                self.state = 228
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,20,self._ctx)

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


        def getRuleIndex(self):
            return LaTeXParser.RULE_comp




    def comp(self):

        localctx = LaTeXParser.CompContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_comp)
        try:
            self.state = 234
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,21,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 229
                self.group()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 230
                self.abs_group()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 231
                self.func()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 232
                self.atom()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 233
                self.frac()
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


        def getRuleIndex(self):
            return LaTeXParser.RULE_comp_nofunc




    def comp_nofunc(self):

        localctx = LaTeXParser.Comp_nofuncContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_comp_nofunc)
        try:
            self.state = 240
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [LaTeXParser.L_PAREN, LaTeXParser.L_BRACE, LaTeXParser.L_BRACKET]:
                self.enterOuterAlt(localctx, 1)
                self.state = 236
                self.group()
                pass
            elif token in [LaTeXParser.BAR]:
                self.enterOuterAlt(localctx, 2)
                self.state = 237
                self.abs_group()
                pass
            elif token in [LaTeXParser.CMD_MATHIT, LaTeXParser.DIFFERENTIAL, LaTeXParser.LETTER, LaTeXParser.NUMBER, LaTeXParser.SYMBOL]:
                self.enterOuterAlt(localctx, 3)
                self.state = 238
                self.atom()
                pass
            elif token in [LaTeXParser.CMD_FRAC]:
                self.enterOuterAlt(localctx, 4)
                self.state = 239
                self.frac()
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

        def expr(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(LaTeXParser.ExprContext)
            else:
                return self.getTypedRuleContext(LaTeXParser.ExprContext,i)


        def R_PAREN(self):
            return self.getToken(LaTeXParser.R_PAREN, 0)

        def L_BRACKET(self):
            return self.getToken(LaTeXParser.L_BRACKET, 0)

        def R_BRACKET(self):
            return self.getToken(LaTeXParser.R_BRACKET, 0)

        def COMMA(self):
            return self.getToken(LaTeXParser.COMMA, 0)

        def L_BRACE(self):
            return self.getToken(LaTeXParser.L_BRACE, 0)

        def R_BRACE(self):
            return self.getToken(LaTeXParser.R_BRACE, 0)

        def getRuleIndex(self):
            return LaTeXParser.RULE_group




    def group(self):

        localctx = LaTeXParser.GroupContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_group)
        self._la = 0 # Token type
        try:
            self.state = 258
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [LaTeXParser.L_PAREN]:
                self.enterOuterAlt(localctx, 1)
                self.state = 242
                self.match(LaTeXParser.L_PAREN)
                self.state = 243
                self.expr()
                self.state = 244
                self.match(LaTeXParser.R_PAREN)
                pass
            elif token in [LaTeXParser.L_BRACKET]:
                self.enterOuterAlt(localctx, 2)
                self.state = 246
                self.match(LaTeXParser.L_BRACKET)
                self.state = 247
                self.expr()
                self.state = 250
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==LaTeXParser.COMMA:
                    self.state = 248
                    self.match(LaTeXParser.COMMA)
                    self.state = 249
                    self.expr()


                self.state = 252
                self.match(LaTeXParser.R_BRACKET)
                pass
            elif token in [LaTeXParser.L_BRACE]:
                self.enterOuterAlt(localctx, 3)
                self.state = 254
                self.match(LaTeXParser.L_BRACE)
                self.state = 255
                self.expr()
                self.state = 256
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
        self.enterRule(localctx, 40, self.RULE_abs_group)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 260
            self.match(LaTeXParser.BAR)
            self.state = 261
            self.expr()
            self.state = 262
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
        self.enterRule(localctx, 42, self.RULE_atom)
        self._la = 0 # Token type
        try:
            self.state = 271
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [LaTeXParser.LETTER, LaTeXParser.SYMBOL]:
                self.enterOuterAlt(localctx, 1)
                self.state = 264
                _la = self._input.LA(1)
                if not(_la==LaTeXParser.LETTER or _la==LaTeXParser.SYMBOL):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 266
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,25,self._ctx)
                if la_ == 1:
                    self.state = 265
                    self.subexpr()


                pass
            elif token in [LaTeXParser.NUMBER]:
                self.enterOuterAlt(localctx, 2)
                self.state = 268
                self.match(LaTeXParser.NUMBER)
                pass
            elif token in [LaTeXParser.DIFFERENTIAL]:
                self.enterOuterAlt(localctx, 3)
                self.state = 269
                self.match(LaTeXParser.DIFFERENTIAL)
                pass
            elif token in [LaTeXParser.CMD_MATHIT]:
                self.enterOuterAlt(localctx, 4)
                self.state = 270
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
        self.enterRule(localctx, 44, self.RULE_mathit)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 273
            self.match(LaTeXParser.CMD_MATHIT)
            self.state = 274
            self.match(LaTeXParser.L_BRACE)
            self.state = 275
            self.mathit_text()
            self.state = 276
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
        self.enterRule(localctx, 46, self.RULE_mathit_text)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 281
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==LaTeXParser.LETTER:
                self.state = 278
                self.match(LaTeXParser.LETTER)
                self.state = 283
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
        self.enterRule(localctx, 48, self.RULE_frac)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 284
            self.match(LaTeXParser.CMD_FRAC)
            self.state = 285
            self.match(LaTeXParser.L_BRACE)
            self.state = 286
            localctx.upper = self.expr()
            self.state = 287
            self.match(LaTeXParser.R_BRACE)
            self.state = 288
            self.match(LaTeXParser.L_BRACE)
            self.state = 289
            localctx.lower = self.expr()
            self.state = 290
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
        self.enterRule(localctx, 50, self.RULE_func_normal)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 292
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
        self.enterRule(localctx, 52, self.RULE_func)
        self._la = 0 # Token type
        try:
            self.state = 370
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [LaTeXParser.FUNC_LOG, LaTeXParser.FUNC_LN, LaTeXParser.FUNC_SIN, LaTeXParser.FUNC_COS, LaTeXParser.FUNC_TAN, LaTeXParser.FUNC_CSC, LaTeXParser.FUNC_SEC, LaTeXParser.FUNC_COT, LaTeXParser.FUNC_ARCSIN, LaTeXParser.FUNC_ARCCOS, LaTeXParser.FUNC_ARCTAN, LaTeXParser.FUNC_ARCCSC, LaTeXParser.FUNC_ARCSEC, LaTeXParser.FUNC_ARCCOT, LaTeXParser.FUNC_SINH, LaTeXParser.FUNC_COSH, LaTeXParser.FUNC_TANH, LaTeXParser.FUNC_ARSINH, LaTeXParser.FUNC_ARCOSH, LaTeXParser.FUNC_ARTANH]:
                self.enterOuterAlt(localctx, 1)
                self.state = 294
                self.func_normal()
                self.state = 307
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,32,self._ctx)
                if la_ == 1:
                    self.state = 296
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if _la==LaTeXParser.UNDERSCORE:
                        self.state = 295
                        self.subexpr()


                    self.state = 299
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if _la==LaTeXParser.CARET:
                        self.state = 298
                        self.supexpr()


                    pass

                elif la_ == 2:
                    self.state = 302
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if _la==LaTeXParser.CARET:
                        self.state = 301
                        self.supexpr()


                    self.state = 305
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if _la==LaTeXParser.UNDERSCORE:
                        self.state = 304
                        self.subexpr()


                    pass


                self.state = 314
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,33,self._ctx)
                if la_ == 1:
                    self.state = 309
                    self.match(LaTeXParser.L_PAREN)
                    self.state = 310
                    self.func_arg()
                    self.state = 311
                    self.match(LaTeXParser.R_PAREN)
                    pass

                elif la_ == 2:
                    self.state = 313
                    self.func_arg_noparens()
                    pass


                pass
            elif token in [LaTeXParser.LETTER, LaTeXParser.SYMBOL]:
                self.enterOuterAlt(localctx, 2)
                self.state = 316
                _la = self._input.LA(1)
                if not(_la==LaTeXParser.LETTER or _la==LaTeXParser.SYMBOL):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 318
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==LaTeXParser.UNDERSCORE:
                    self.state = 317
                    self.subexpr()


                self.state = 320
                self.match(LaTeXParser.L_PAREN)
                self.state = 321
                self.args()
                self.state = 322
                self.match(LaTeXParser.R_PAREN)
                pass
            elif token in [LaTeXParser.FUNC_INT]:
                self.enterOuterAlt(localctx, 3)
                self.state = 324
                self.match(LaTeXParser.FUNC_INT)
                self.state = 326
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,35,self._ctx)
                if la_ == 1:
                    self.state = 325
                    self.match(LaTeXParser.UNDERSCORE)


                self.state = 334
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [LaTeXParser.UNDERSCORE]:
                    self.state = 328
                    self.subexpr()
                    self.state = 329
                    self.supexpr()
                    pass
                elif token in [LaTeXParser.CARET]:
                    self.state = 331
                    self.supexpr()
                    self.state = 332
                    self.subexpr()
                    pass
                elif token in [LaTeXParser.ADD, LaTeXParser.SUB, LaTeXParser.L_PAREN, LaTeXParser.L_BRACE, LaTeXParser.L_BRACKET, LaTeXParser.BAR, LaTeXParser.FUNC_LIM, LaTeXParser.FUNC_INT, LaTeXParser.FUNC_SUM, LaTeXParser.FUNC_PROD, LaTeXParser.FUNC_LOG, LaTeXParser.FUNC_LN, LaTeXParser.FUNC_SIN, LaTeXParser.FUNC_COS, LaTeXParser.FUNC_TAN, LaTeXParser.FUNC_CSC, LaTeXParser.FUNC_SEC, LaTeXParser.FUNC_COT, LaTeXParser.FUNC_ARCSIN, LaTeXParser.FUNC_ARCCOS, LaTeXParser.FUNC_ARCTAN, LaTeXParser.FUNC_ARCCSC, LaTeXParser.FUNC_ARCSEC, LaTeXParser.FUNC_ARCCOT, LaTeXParser.FUNC_SINH, LaTeXParser.FUNC_COSH, LaTeXParser.FUNC_TANH, LaTeXParser.FUNC_ARSINH, LaTeXParser.FUNC_ARCOSH, LaTeXParser.FUNC_ARTANH, LaTeXParser.FUNC_SQRT, LaTeXParser.CMD_FRAC, LaTeXParser.CMD_MATHIT, LaTeXParser.DIFFERENTIAL, LaTeXParser.LETTER, LaTeXParser.NUMBER, LaTeXParser.SYMBOL]:
                    pass
                else:
                    pass
                self.state = 342
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,38,self._ctx)
                if la_ == 1:
                    self.state = 337
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,37,self._ctx)
                    if la_ == 1:
                        self.state = 336
                        self.additive(0)


                    self.state = 339
                    self.match(LaTeXParser.DIFFERENTIAL)
                    pass

                elif la_ == 2:
                    self.state = 340
                    self.frac()
                    pass

                elif la_ == 3:
                    self.state = 341
                    self.additive(0)
                    pass


                pass
            elif token in [LaTeXParser.FUNC_SQRT]:
                self.enterOuterAlt(localctx, 4)
                self.state = 344
                self.match(LaTeXParser.FUNC_SQRT)
                self.state = 349
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==LaTeXParser.L_BRACKET:
                    self.state = 345
                    self.match(LaTeXParser.L_BRACKET)
                    self.state = 346
                    localctx.root = self.expr()
                    self.state = 347
                    self.match(LaTeXParser.R_BRACKET)


                self.state = 351
                self.match(LaTeXParser.L_BRACE)
                self.state = 352
                localctx.base = self.expr()
                self.state = 353
                self.match(LaTeXParser.R_BRACE)
                pass
            elif token in [LaTeXParser.FUNC_SUM, LaTeXParser.FUNC_PROD]:
                self.enterOuterAlt(localctx, 5)
                self.state = 355
                _la = self._input.LA(1)
                if not(_la==LaTeXParser.FUNC_SUM or _la==LaTeXParser.FUNC_PROD):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 362
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [LaTeXParser.UNDERSCORE]:
                    self.state = 356
                    self.subeq()
                    self.state = 357
                    self.supexpr()
                    pass
                elif token in [LaTeXParser.CARET]:
                    self.state = 359
                    self.supexpr()
                    self.state = 360
                    self.subeq()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 364
                self.mp(0)
                pass
            elif token in [LaTeXParser.FUNC_LIM]:
                self.enterOuterAlt(localctx, 6)
                self.state = 366
                self.match(LaTeXParser.FUNC_LIM)
                self.state = 367
                self.limit_sub()
                self.state = 368
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
        self.enterRule(localctx, 54, self.RULE_args)
        try:
            self.state = 377
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,42,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 372
                self.expr()
                self.state = 373
                self.match(LaTeXParser.COMMA)
                self.state = 374
                self.args()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 376
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

        def LIM_APPROACH_SYM(self):
            return self.getToken(LaTeXParser.LIM_APPROACH_SYM, 0)

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
        self.enterRule(localctx, 56, self.RULE_limit_sub)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 379
            self.match(LaTeXParser.UNDERSCORE)
            self.state = 380
            self.match(LaTeXParser.L_BRACE)
            self.state = 381
            _la = self._input.LA(1)
            if not(_la==LaTeXParser.LETTER or _la==LaTeXParser.SYMBOL):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 382
            self.match(LaTeXParser.LIM_APPROACH_SYM)
            self.state = 383
            self.expr()
            self.state = 388
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==LaTeXParser.CARET:
                self.state = 384
                self.match(LaTeXParser.CARET)
                self.state = 385
                self.match(LaTeXParser.L_BRACE)
                self.state = 386
                _la = self._input.LA(1)
                if not(_la==LaTeXParser.ADD or _la==LaTeXParser.SUB):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 387
                self.match(LaTeXParser.R_BRACE)


            self.state = 390
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
        self.enterRule(localctx, 58, self.RULE_func_arg)
        try:
            self.state = 397
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,44,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 392
                self.expr()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 393
                self.expr()
                self.state = 394
                self.match(LaTeXParser.COMMA)
                self.state = 395
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
        self.enterRule(localctx, 60, self.RULE_func_arg_noparens)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 399
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
        self.enterRule(localctx, 62, self.RULE_subexpr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 401
            self.match(LaTeXParser.UNDERSCORE)
            self.state = 407
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [LaTeXParser.CMD_MATHIT, LaTeXParser.DIFFERENTIAL, LaTeXParser.LETTER, LaTeXParser.NUMBER, LaTeXParser.SYMBOL]:
                self.state = 402
                self.atom()
                pass
            elif token in [LaTeXParser.L_BRACE]:
                self.state = 403
                self.match(LaTeXParser.L_BRACE)
                self.state = 404
                self.expr()
                self.state = 405
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
        self.enterRule(localctx, 64, self.RULE_supexpr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 409
            self.match(LaTeXParser.CARET)
            self.state = 415
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [LaTeXParser.CMD_MATHIT, LaTeXParser.DIFFERENTIAL, LaTeXParser.LETTER, LaTeXParser.NUMBER, LaTeXParser.SYMBOL]:
                self.state = 410
                self.atom()
                pass
            elif token in [LaTeXParser.L_BRACE]:
                self.state = 411
                self.match(LaTeXParser.L_BRACE)
                self.state = 412
                self.expr()
                self.state = 413
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
        self.enterRule(localctx, 66, self.RULE_subeq)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 417
            self.match(LaTeXParser.UNDERSCORE)
            self.state = 418
            self.match(LaTeXParser.L_BRACE)
            self.state = 421
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,47,self._ctx)
            if la_ == 1:
                self.state = 419
                self.expr()
                pass

            elif la_ == 2:
                self.state = 420
                self.equality()
                pass


            self.state = 423
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
        self.enterRule(localctx, 68, self.RULE_supeq)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 425
            self.match(LaTeXParser.UNDERSCORE)
            self.state = 426
            self.match(LaTeXParser.L_BRACE)
            self.state = 429
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,48,self._ctx)
            if la_ == 1:
                self.state = 427
                self.expr()
                pass

            elif la_ == 2:
                self.state = 428
                self.equality()
                pass


            self.state = 431
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
        self._predicates[1] = self.relation_sempred
        self._predicates[4] = self.additive_sempred
        self._predicates[5] = self.mp_sempred
        self._predicates[6] = self.mp_nofunc_sempred
        self._predicates[15] = self.exp_sempred
        self._predicates[16] = self.exp_nofunc_sempred
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
         




