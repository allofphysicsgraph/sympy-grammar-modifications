# Generated from /media/user/eee8fa5e-70d6-41f9-80cf-10f909993ce6/mike/DEVELOPMENT/sympy-grammar-modifications/sympy/parsing/latex/_antlr/LaTeX.g4 by ANTLR 4.7.1
# encoding: utf-8
from __future__ import print_function
from antlr4 import *
from io import StringIO
import sys


def serializedATN():
    with StringIO() as buf:
        buf.write(u"\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2")
        buf.write(u"H\u02ed\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4")
        buf.write(u"\7\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r")
        buf.write(u"\t\r\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22")
        buf.write(u"\4\23\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4")
        buf.write(u"\30\t\30\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35")
        buf.write(u"\t\35\4\36\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4")
        buf.write(u"$\t$\4%\t%\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t")
        buf.write(u",\4-\t-\4.\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63")
        buf.write(u"\t\63\4\64\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\4")
        buf.write(u"9\t9\4:\t:\4;\t;\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA")
        buf.write(u"\4B\tB\4C\tC\4D\tD\4E\tE\4F\tF\4G\tG\4H\tH\4I\tI\3\2")
        buf.write(u"\3\2\3\3\6\3\u0097\n\3\r\3\16\3\u0098\3\3\3\3\3\4\3\4")
        buf.write(u"\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4")
        buf.write(u"\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4")
        buf.write(u"\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4")
        buf.write(u"\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4")
        buf.write(u"\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4")
        buf.write(u"\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4")
        buf.write(u"\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4")
        buf.write(u"\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4")
        buf.write(u"\3\4\3\4\3\4\5\4\u010a\n\4\3\5\3\5\3\6\3\6\3\7\3\7\3")
        buf.write(u"\b\3\b\3\t\3\t\3\n\3\n\3\13\3\13\3\f\3\f\3\r\3\r\3\16")
        buf.write(u"\3\16\3\17\3\17\3\20\3\20\3\20\3\20\3\20\3\21\3\21\3")
        buf.write(u"\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21")
        buf.write(u"\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3")
        buf.write(u"\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21")
        buf.write(u"\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3")
        buf.write(u"\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21")
        buf.write(u"\5\21\u015e\n\21\3\22\3\22\3\22\3\22\3\22\3\23\3\23\3")
        buf.write(u"\23\3\23\3\23\3\24\3\24\3\24\3\24\3\24\3\24\3\25\3\25")
        buf.write(u"\3\25\3\25\3\25\3\26\3\26\3\26\3\26\3\27\3\27\3\27\3")
        buf.write(u"\27\3\27\3\30\3\30\3\30\3\30\3\30\3\31\3\31\3\31\3\31")
        buf.write(u"\3\31\3\32\3\32\3\32\3\32\3\32\3\33\3\33\3\33\3\33\3")
        buf.write(u"\33\3\34\3\34\3\34\3\34\3\34\3\35\3\35\3\35\3\35\3\35")
        buf.write(u"\3\35\3\35\3\35\3\36\3\36\3\36\3\36\3\36\3\36\3\36\3")
        buf.write(u"\36\3\37\3\37\3\37\3\37\3\37\3\37\3\37\3\37\3 \3 \3 ")
        buf.write(u"\3 \3 \3 \3 \3 \3!\3!\3!\3!\3!\3!\3!\3!\3\"\3\"\3\"\3")
        buf.write(u"\"\3\"\3\"\3\"\3\"\3#\3#\3#\3#\3#\3#\3$\3$\3$\3$\3$\3")
        buf.write(u"$\3%\3%\3%\3%\3%\3%\3&\3&\3&\3&\3&\3&\3&\3&\3\'\3\'\3")
        buf.write(u"\'\3\'\3\'\3\'\3\'\3\'\3(\3(\3(\3(\3(\3(\3(\3(\3)\3)")
        buf.write(u"\3)\3)\3)\3)\3*\3*\3*\3*\3*\3*\3*\3+\3+\3+\3+\3+\3+\3")
        buf.write(u",\3,\3,\3,\3,\3-\3-\3-\3-\3-\3-\3.\3.\3.\3.\3.\3.\3.")
        buf.write(u"\3.\3/\3/\3\60\3\60\3\61\3\61\3\62\3\62\3\63\3\63\3\63")
        buf.write(u"\3\63\3\63\3\63\3\63\3\63\3\63\3\64\3\64\3\64\3\64\3")
        buf.write(u"\64\3\64\3\64\3\64\3\64\3\64\3\64\3\64\3\64\3\64\3\64")
        buf.write(u"\3\64\3\65\3\65\3\65\3\65\3\65\3\65\3\65\3\65\3\65\3")
        buf.write(u"\66\3\66\3\66\3\66\3\66\3\66\3\66\3\66\3\66\3\66\3\66")
        buf.write(u"\3\66\3\67\3\67\3\67\3\67\3\67\3\67\3\67\3\67\3\67\3")
        buf.write(u"\67\3\67\3\67\38\38\38\38\38\38\38\38\38\38\38\38\58")
        buf.write(u"\u0265\n8\39\39\39\39\39\39\39\3:\3:\3:\3:\3:\3:\3;\3")
        buf.write(u";\3;\3;\3;\3;\3;\3<\3<\3=\3=\3=\3=\3>\3>\3?\3?\7?\u0285")
        buf.write(u"\n?\f?\16?\u0288\13?\3?\3?\3?\6?\u028d\n?\r?\16?\u028e")
        buf.write(u"\5?\u0291\n?\3@\3@\3A\3A\3B\6B\u0298\nB\rB\16B\u0299")
        buf.write(u"\3B\3B\3B\3B\3B\7B\u02a1\nB\fB\16B\u02a4\13B\3B\7B\u02a7")
        buf.write(u"\nB\fB\16B\u02aa\13B\3B\3B\3B\3B\3B\7B\u02b1\nB\fB\16")
        buf.write(u"B\u02b4\13B\3B\3B\6B\u02b8\nB\rB\16B\u02b9\5B\u02bc\n")
        buf.write(u"B\3C\3C\3D\3D\3E\3E\3E\3E\3E\3F\3F\3G\3G\3G\3G\3G\3H")
        buf.write(u"\3H\3I\3I\6I\u02d2\nI\rI\16I\u02d3\3I\5I\u02d7\nI\3I")
        buf.write(u"\6I\u02da\nI\rI\16I\u02db\3I\3I\3I\3I\7I\u02e2\nI\fI")
        buf.write(u"\16I\u02e5\13I\3I\6I\u02e8\nI\rI\16I\u02e9\5I\u02ec\n")
        buf.write(u"I\3\u0286\2J\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13")
        buf.write(u"\25\f\27\r\31\16\33\17\35\20\37\21!\22#\23%\24\'\25)")
        buf.write(u"\26+\27-\30/\31\61\32\63\33\65\34\67\359\36;\37= ?!A")
        buf.write(u"\"C#E$G%I&K\'M(O)Q*S+U,W-Y.[/]\60_\61a\62c\63e\64g\65")
        buf.write(u"i\66k\67m8o9q:s;u<w=y>{\2}?\177@\u0081\2\u0083A\u0085")
        buf.write(u"B\u0087C\u0089D\u008bE\u008dF\u008fG\u0091H\3\2\t\5\2")
        buf.write(u"\13\f\17\17\"\"\4\2C\\c|\3\2\62;\4\2\"\"<=\4\2..<=\3")
        buf.write(u"\2\"\"\3\2c|\2\u0318\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2")
        buf.write(u"\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2")
        buf.write(u"\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2")
        buf.write(u"\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2")
        buf.write(u"\2\2!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3\2\2\2\2)\3")
        buf.write(u"\2\2\2\2+\3\2\2\2\2-\3\2\2\2\2/\3\2\2\2\2\61\3\2\2\2")
        buf.write(u"\2\63\3\2\2\2\2\65\3\2\2\2\2\67\3\2\2\2\29\3\2\2\2\2")
        buf.write(u";\3\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2A\3\2\2\2\2C\3\2\2\2")
        buf.write(u"\2E\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2\2K\3\2\2\2\2M\3\2\2")
        buf.write(u"\2\2O\3\2\2\2\2Q\3\2\2\2\2S\3\2\2\2\2U\3\2\2\2\2W\3\2")
        buf.write(u"\2\2\2Y\3\2\2\2\2[\3\2\2\2\2]\3\2\2\2\2_\3\2\2\2\2a\3")
        buf.write(u"\2\2\2\2c\3\2\2\2\2e\3\2\2\2\2g\3\2\2\2\2i\3\2\2\2\2")
        buf.write(u"k\3\2\2\2\2m\3\2\2\2\2o\3\2\2\2\2q\3\2\2\2\2s\3\2\2\2")
        buf.write(u"\2u\3\2\2\2\2w\3\2\2\2\2y\3\2\2\2\2}\3\2\2\2\2\177\3")
        buf.write(u"\2\2\2\2\u0083\3\2\2\2\2\u0085\3\2\2\2\2\u0087\3\2\2")
        buf.write(u"\2\2\u0089\3\2\2\2\2\u008b\3\2\2\2\2\u008d\3\2\2\2\2")
        buf.write(u"\u008f\3\2\2\2\2\u0091\3\2\2\2\3\u0093\3\2\2\2\5\u0096")
        buf.write(u"\3\2\2\2\7\u0109\3\2\2\2\t\u010b\3\2\2\2\13\u010d\3\2")
        buf.write(u"\2\2\r\u010f\3\2\2\2\17\u0111\3\2\2\2\21\u0113\3\2\2")
        buf.write(u"\2\23\u0115\3\2\2\2\25\u0117\3\2\2\2\27\u0119\3\2\2\2")
        buf.write(u"\31\u011b\3\2\2\2\33\u011d\3\2\2\2\35\u011f\3\2\2\2\37")
        buf.write(u"\u0121\3\2\2\2!\u015d\3\2\2\2#\u015f\3\2\2\2%\u0164\3")
        buf.write(u"\2\2\2\'\u0169\3\2\2\2)\u016f\3\2\2\2+\u0174\3\2\2\2")
        buf.write(u"-\u0178\3\2\2\2/\u017d\3\2\2\2\61\u0182\3\2\2\2\63\u0187")
        buf.write(u"\3\2\2\2\65\u018c\3\2\2\2\67\u0191\3\2\2\29\u0196\3\2")
        buf.write(u"\2\2;\u019e\3\2\2\2=\u01a6\3\2\2\2?\u01ae\3\2\2\2A\u01b6")
        buf.write(u"\3\2\2\2C\u01be\3\2\2\2E\u01c6\3\2\2\2G\u01cc\3\2\2\2")
        buf.write(u"I\u01d2\3\2\2\2K\u01d8\3\2\2\2M\u01e0\3\2\2\2O\u01e8")
        buf.write(u"\3\2\2\2Q\u01f0\3\2\2\2S\u01f6\3\2\2\2U\u01fd\3\2\2\2")
        buf.write(u"W\u0203\3\2\2\2Y\u0208\3\2\2\2[\u020e\3\2\2\2]\u0216")
        buf.write(u"\3\2\2\2_\u0218\3\2\2\2a\u021a\3\2\2\2c\u021c\3\2\2\2")
        buf.write(u"e\u021e\3\2\2\2g\u0227\3\2\2\2i\u0237\3\2\2\2k\u0240")
        buf.write(u"\3\2\2\2m\u024c\3\2\2\2o\u0258\3\2\2\2q\u0266\3\2\2\2")
        buf.write(u"s\u026d\3\2\2\2u\u0273\3\2\2\2w\u027a\3\2\2\2y\u027c")
        buf.write(u"\3\2\2\2{\u0280\3\2\2\2}\u0282\3\2\2\2\177\u0292\3\2")
        buf.write(u"\2\2\u0081\u0294\3\2\2\2\u0083\u02bb\3\2\2\2\u0085\u02bd")
        buf.write(u"\3\2\2\2\u0087\u02bf\3\2\2\2\u0089\u02c1\3\2\2\2\u008b")
        buf.write(u"\u02c6\3\2\2\2\u008d\u02c8\3\2\2\2\u008f\u02cd\3\2\2")
        buf.write(u"\2\u0091\u02eb\3\2\2\2\u0093\u0094\7.\2\2\u0094\4\3\2")
        buf.write(u"\2\2\u0095\u0097\t\2\2\2\u0096\u0095\3\2\2\2\u0097\u0098")
        buf.write(u"\3\2\2\2\u0098\u0096\3\2\2\2\u0098\u0099\3\2\2\2\u0099")
        buf.write(u"\u009a\3\2\2\2\u009a\u009b\b\3\2\2\u009b\6\3\2\2\2\u009c")
        buf.write(u"\u009d\7^\2\2\u009d\u009e\7p\2\2\u009e\u010a\7w\2\2\u009f")
        buf.write(u"\u00a0\7^\2\2\u00a0\u00a1\7z\2\2\u00a1\u010a\7k\2\2\u00a2")
        buf.write(u"\u00a3\7^\2\2\u00a3\u00a4\7Z\2\2\u00a4\u010a\7k\2\2\u00a5")
        buf.write(u"\u00a6\7^\2\2\u00a6\u00a7\7r\2\2\u00a7\u010a\7k\2\2\u00a8")
        buf.write(u"\u00a9\7^\2\2\u00a9\u00aa\7R\2\2\u00aa\u010a\7k\2\2\u00ab")
        buf.write(u"\u00ac\7^\2\2\u00ac\u00ad\7t\2\2\u00ad\u00ae\7j\2\2\u00ae")
        buf.write(u"\u010a\7q\2\2\u00af\u00b0\7^\2\2\u00b0\u00b1\7x\2\2\u00b1")
        buf.write(u"\u00b2\7c\2\2\u00b2\u00b3\7t\2\2\u00b3\u00b4\7t\2\2\u00b4")
        buf.write(u"\u00b5\7j\2\2\u00b5\u010a\7q\2\2\u00b6\u00b7\7^\2\2\u00b7")
        buf.write(u"\u00b8\7u\2\2\u00b8\u00b9\7k\2\2\u00b9\u00ba\7i\2\2\u00ba")
        buf.write(u"\u00bb\7o\2\2\u00bb\u010a\7c\2\2\u00bc\u00bd\7^\2\2\u00bd")
        buf.write(u"\u00be\7U\2\2\u00be\u00bf\7k\2\2\u00bf\u00c0\7i\2\2\u00c0")
        buf.write(u"\u00c1\7o\2\2\u00c1\u010a\7c\2\2\u00c2\u00c3\7^\2\2\u00c3")
        buf.write(u"\u00c4\7v\2\2\u00c4\u00c5\7j\2\2\u00c5\u00c6\7g\2\2\u00c6")
        buf.write(u"\u00c7\7v\2\2\u00c7\u010a\7c\2\2\u00c8\u00c9\7^\2\2\u00c9")
        buf.write(u"\u00ca\7V\2\2\u00ca\u00cb\7j\2\2\u00cb\u00cc\7g\2\2\u00cc")
        buf.write(u"\u00cd\7v\2\2\u00cd\u010a\7c\2\2\u00ce\u00cf\7^\2\2\u00cf")
        buf.write(u"\u00d0\7v\2\2\u00d0\u00d1\7c\2\2\u00d1\u010a\7w\2\2\u00d2")
        buf.write(u"\u00d3\7^\2\2\u00d3\u00d4\7w\2\2\u00d4\u00d5\7r\2\2\u00d5")
        buf.write(u"\u00d6\7u\2\2\u00d6\u00d7\7k\2\2\u00d7\u00d8\7n\2\2\u00d8")
        buf.write(u"\u00d9\7q\2\2\u00d9\u010a\7p\2\2\u00da\u00db\7^\2\2\u00db")
        buf.write(u"\u00dc\7W\2\2\u00dc\u00dd\7r\2\2\u00dd\u00de\7u\2\2\u00de")
        buf.write(u"\u00df\7k\2\2\u00df\u00e0\7n\2\2\u00e0\u00e1\7q\2\2\u00e1")
        buf.write(u"\u010a\7p\2\2\u00e2\u00e3\7^\2\2\u00e3\u00e4\7r\2\2\u00e4")
        buf.write(u"\u00e5\7j\2\2\u00e5\u010a\7k\2\2\u00e6\u00e7\7^\2\2\u00e7")
        buf.write(u"\u00e8\7x\2\2\u00e8\u00e9\7c\2\2\u00e9\u00ea\7t\2\2\u00ea")
        buf.write(u"\u00eb\7r\2\2\u00eb\u00ec\7j\2\2\u00ec\u010a\7k\2\2\u00ed")
        buf.write(u"\u00ee\7^\2\2\u00ee\u00ef\7R\2\2\u00ef\u00f0\7j\2\2\u00f0")
        buf.write(u"\u010a\7k\2\2\u00f1\u00f2\7^\2\2\u00f2\u00f3\7e\2\2\u00f3")
        buf.write(u"\u00f4\7j\2\2\u00f4\u010a\7k\2\2\u00f5\u00f6\7^\2\2\u00f6")
        buf.write(u"\u00f7\7r\2\2\u00f7\u00f8\7u\2\2\u00f8\u010a\7k\2\2\u00f9")
        buf.write(u"\u00fa\7^\2\2\u00fa\u00fb\7R\2\2\u00fb\u00fc\7u\2\2\u00fc")
        buf.write(u"\u010a\7k\2\2\u00fd\u00fe\7^\2\2\u00fe\u00ff\7q\2\2\u00ff")
        buf.write(u"\u0100\7o\2\2\u0100\u0101\7g\2\2\u0101\u0102\7i\2\2\u0102")
        buf.write(u"\u010a\7c\2\2\u0103\u0104\7^\2\2\u0104\u0105\7Q\2\2\u0105")
        buf.write(u"\u0106\7o\2\2\u0106\u0107\7g\2\2\u0107\u0108\7i\2\2\u0108")
        buf.write(u"\u010a\7c\2\2\u0109\u009c\3\2\2\2\u0109\u009f\3\2\2\2")
        buf.write(u"\u0109\u00a2\3\2\2\2\u0109\u00a5\3\2\2\2\u0109\u00a8")
        buf.write(u"\3\2\2\2\u0109\u00ab\3\2\2\2\u0109\u00af\3\2\2\2\u0109")
        buf.write(u"\u00b6\3\2\2\2\u0109\u00bc\3\2\2\2\u0109\u00c2\3\2\2")
        buf.write(u"\2\u0109\u00c8\3\2\2\2\u0109\u00ce\3\2\2\2\u0109\u00d2")
        buf.write(u"\3\2\2\2\u0109\u00da\3\2\2\2\u0109\u00e2\3\2\2\2\u0109")
        buf.write(u"\u00e6\3\2\2\2\u0109\u00ed\3\2\2\2\u0109\u00f1\3\2\2")
        buf.write(u"\2\u0109\u00f5\3\2\2\2\u0109\u00f9\3\2\2\2\u0109\u00fd")
        buf.write(u"\3\2\2\2\u0109\u0103\3\2\2\2\u010a\b\3\2\2\2\u010b\u010c")
        buf.write(u"\7-\2\2\u010c\n\3\2\2\2\u010d\u010e\7/\2\2\u010e\f\3")
        buf.write(u"\2\2\2\u010f\u0110\7,\2\2\u0110\16\3\2\2\2\u0111\u0112")
        buf.write(u"\7\61\2\2\u0112\20\3\2\2\2\u0113\u0114\7*\2\2\u0114\22")
        buf.write(u"\3\2\2\2\u0115\u0116\7+\2\2\u0116\24\3\2\2\2\u0117\u0118")
        buf.write(u"\7}\2\2\u0118\26\3\2\2\2\u0119\u011a\7\177\2\2\u011a")
        buf.write(u"\30\3\2\2\2\u011b\u011c\7]\2\2\u011c\32\3\2\2\2\u011d")
        buf.write(u"\u011e\7_\2\2\u011e\34\3\2\2\2\u011f\u0120\7~\2\2\u0120")
        buf.write(u"\36\3\2\2\2\u0121\u0122\7^\2\2\u0122\u0123\7n\2\2\u0123")
        buf.write(u"\u0124\7k\2\2\u0124\u0125\7o\2\2\u0125 \3\2\2\2\u0126")
        buf.write(u"\u0127\7^\2\2\u0127\u0128\7v\2\2\u0128\u015e\7q\2\2\u0129")
        buf.write(u"\u012a\7^\2\2\u012a\u012b\7t\2\2\u012b\u012c\7k\2\2\u012c")
        buf.write(u"\u012d\7i\2\2\u012d\u012e\7j\2\2\u012e\u012f\7v\2\2\u012f")
        buf.write(u"\u0130\7c\2\2\u0130\u0131\7t\2\2\u0131\u0132\7t\2\2\u0132")
        buf.write(u"\u0133\7q\2\2\u0133\u015e\7y\2\2\u0134\u0135\7^\2\2\u0135")
        buf.write(u"\u0136\7T\2\2\u0136\u0137\7k\2\2\u0137\u0138\7i\2\2\u0138")
        buf.write(u"\u0139\7j\2\2\u0139\u013a\7v\2\2\u013a\u013b\7c\2\2\u013b")
        buf.write(u"\u013c\7t\2\2\u013c\u013d\7t\2\2\u013d\u013e\7q\2\2\u013e")
        buf.write(u"\u015e\7y\2\2\u013f\u0140\7^\2\2\u0140\u0141\7n\2\2\u0141")
        buf.write(u"\u0142\7q\2\2\u0142\u0143\7p\2\2\u0143\u0144\7i\2\2\u0144")
        buf.write(u"\u0145\7t\2\2\u0145\u0146\7k\2\2\u0146\u0147\7i\2\2\u0147")
        buf.write(u"\u0148\7j\2\2\u0148\u0149\7v\2\2\u0149\u014a\7c\2\2\u014a")
        buf.write(u"\u014b\7t\2\2\u014b\u014c\7t\2\2\u014c\u014d\7q\2\2\u014d")
        buf.write(u"\u015e\7y\2\2\u014e\u014f\7^\2\2\u014f\u0150\7N\2\2\u0150")
        buf.write(u"\u0151\7q\2\2\u0151\u0152\7p\2\2\u0152\u0153\7i\2\2\u0153")
        buf.write(u"\u0154\7t\2\2\u0154\u0155\7k\2\2\u0155\u0156\7i\2\2\u0156")
        buf.write(u"\u0157\7j\2\2\u0157\u0158\7v\2\2\u0158\u0159\7c\2\2\u0159")
        buf.write(u"\u015a\7t\2\2\u015a\u015b\7t\2\2\u015b\u015c\7q\2\2\u015c")
        buf.write(u"\u015e\7y\2\2\u015d\u0126\3\2\2\2\u015d\u0129\3\2\2\2")
        buf.write(u"\u015d\u0134\3\2\2\2\u015d\u013f\3\2\2\2\u015d\u014e")
        buf.write(u"\3\2\2\2\u015e\"\3\2\2\2\u015f\u0160\7^\2\2\u0160\u0161")
        buf.write(u"\7k\2\2\u0161\u0162\7p\2\2\u0162\u0163\7v\2\2\u0163$")
        buf.write(u"\3\2\2\2\u0164\u0165\7^\2\2\u0165\u0166\7u\2\2\u0166")
        buf.write(u"\u0167\7w\2\2\u0167\u0168\7o\2\2\u0168&\3\2\2\2\u0169")
        buf.write(u"\u016a\7^\2\2\u016a\u016b\7r\2\2\u016b\u016c\7t\2\2\u016c")
        buf.write(u"\u016d\7q\2\2\u016d\u016e\7f\2\2\u016e(\3\2\2\2\u016f")
        buf.write(u"\u0170\7^\2\2\u0170\u0171\7n\2\2\u0171\u0172\7q\2\2\u0172")
        buf.write(u"\u0173\7i\2\2\u0173*\3\2\2\2\u0174\u0175\7^\2\2\u0175")
        buf.write(u"\u0176\7n\2\2\u0176\u0177\7p\2\2\u0177,\3\2\2\2\u0178")
        buf.write(u"\u0179\7^\2\2\u0179\u017a\7u\2\2\u017a\u017b\7k\2\2\u017b")
        buf.write(u"\u017c\7p\2\2\u017c.\3\2\2\2\u017d\u017e\7^\2\2\u017e")
        buf.write(u"\u017f\7e\2\2\u017f\u0180\7q\2\2\u0180\u0181\7u\2\2\u0181")
        buf.write(u"\60\3\2\2\2\u0182\u0183\7^\2\2\u0183\u0184\7v\2\2\u0184")
        buf.write(u"\u0185\7c\2\2\u0185\u0186\7p\2\2\u0186\62\3\2\2\2\u0187")
        buf.write(u"\u0188\7^\2\2\u0188\u0189\7e\2\2\u0189\u018a\7u\2\2\u018a")
        buf.write(u"\u018b\7e\2\2\u018b\64\3\2\2\2\u018c\u018d\7^\2\2\u018d")
        buf.write(u"\u018e\7u\2\2\u018e\u018f\7g\2\2\u018f\u0190\7e\2\2\u0190")
        buf.write(u"\66\3\2\2\2\u0191\u0192\7^\2\2\u0192\u0193\7e\2\2\u0193")
        buf.write(u"\u0194\7q\2\2\u0194\u0195\7v\2\2\u01958\3\2\2\2\u0196")
        buf.write(u"\u0197\7^\2\2\u0197\u0198\7c\2\2\u0198\u0199\7t\2\2\u0199")
        buf.write(u"\u019a\7e\2\2\u019a\u019b\7u\2\2\u019b\u019c\7k\2\2\u019c")
        buf.write(u"\u019d\7p\2\2\u019d:\3\2\2\2\u019e\u019f\7^\2\2\u019f")
        buf.write(u"\u01a0\7c\2\2\u01a0\u01a1\7t\2\2\u01a1\u01a2\7e\2\2\u01a2")
        buf.write(u"\u01a3\7e\2\2\u01a3\u01a4\7q\2\2\u01a4\u01a5\7u\2\2\u01a5")
        buf.write(u"<\3\2\2\2\u01a6\u01a7\7^\2\2\u01a7\u01a8\7c\2\2\u01a8")
        buf.write(u"\u01a9\7t\2\2\u01a9\u01aa\7e\2\2\u01aa\u01ab\7v\2\2\u01ab")
        buf.write(u"\u01ac\7c\2\2\u01ac\u01ad\7p\2\2\u01ad>\3\2\2\2\u01ae")
        buf.write(u"\u01af\7^\2\2\u01af\u01b0\7c\2\2\u01b0\u01b1\7t\2\2\u01b1")
        buf.write(u"\u01b2\7e\2\2\u01b2\u01b3\7e\2\2\u01b3\u01b4\7u\2\2\u01b4")
        buf.write(u"\u01b5\7e\2\2\u01b5@\3\2\2\2\u01b6\u01b7\7^\2\2\u01b7")
        buf.write(u"\u01b8\7c\2\2\u01b8\u01b9\7t\2\2\u01b9\u01ba\7e\2\2\u01ba")
        buf.write(u"\u01bb\7u\2\2\u01bb\u01bc\7g\2\2\u01bc\u01bd\7e\2\2\u01bd")
        buf.write(u"B\3\2\2\2\u01be\u01bf\7^\2\2\u01bf\u01c0\7c\2\2\u01c0")
        buf.write(u"\u01c1\7t\2\2\u01c1\u01c2\7e\2\2\u01c2\u01c3\7e\2\2\u01c3")
        buf.write(u"\u01c4\7q\2\2\u01c4\u01c5\7v\2\2\u01c5D\3\2\2\2\u01c6")
        buf.write(u"\u01c7\7^\2\2\u01c7\u01c8\7u\2\2\u01c8\u01c9\7k\2\2\u01c9")
        buf.write(u"\u01ca\7p\2\2\u01ca\u01cb\7j\2\2\u01cbF\3\2\2\2\u01cc")
        buf.write(u"\u01cd\7^\2\2\u01cd\u01ce\7e\2\2\u01ce\u01cf\7q\2\2\u01cf")
        buf.write(u"\u01d0\7u\2\2\u01d0\u01d1\7j\2\2\u01d1H\3\2\2\2\u01d2")
        buf.write(u"\u01d3\7^\2\2\u01d3\u01d4\7v\2\2\u01d4\u01d5\7c\2\2\u01d5")
        buf.write(u"\u01d6\7p\2\2\u01d6\u01d7\7j\2\2\u01d7J\3\2\2\2\u01d8")
        buf.write(u"\u01d9\7^\2\2\u01d9\u01da\7c\2\2\u01da\u01db\7t\2\2\u01db")
        buf.write(u"\u01dc\7u\2\2\u01dc\u01dd\7k\2\2\u01dd\u01de\7p\2\2\u01de")
        buf.write(u"\u01df\7j\2\2\u01dfL\3\2\2\2\u01e0\u01e1\7^\2\2\u01e1")
        buf.write(u"\u01e2\7c\2\2\u01e2\u01e3\7t\2\2\u01e3\u01e4\7e\2\2\u01e4")
        buf.write(u"\u01e5\7q\2\2\u01e5\u01e6\7u\2\2\u01e6\u01e7\7j\2\2\u01e7")
        buf.write(u"N\3\2\2\2\u01e8\u01e9\7^\2\2\u01e9\u01ea\7c\2\2\u01ea")
        buf.write(u"\u01eb\7t\2\2\u01eb\u01ec\7v\2\2\u01ec\u01ed\7c\2\2\u01ed")
        buf.write(u"\u01ee\7p\2\2\u01ee\u01ef\7j\2\2\u01efP\3\2\2\2\u01f0")
        buf.write(u"\u01f1\7^\2\2\u01f1\u01f2\7u\2\2\u01f2\u01f3\7s\2\2\u01f3")
        buf.write(u"\u01f4\7t\2\2\u01f4\u01f5\7v\2\2\u01f5R\3\2\2\2\u01f6")
        buf.write(u"\u01f7\7^\2\2\u01f7\u01f8\7v\2\2\u01f8\u01f9\7k\2\2\u01f9")
        buf.write(u"\u01fa\7o\2\2\u01fa\u01fb\7g\2\2\u01fb\u01fc\7u\2\2\u01fc")
        buf.write(u"T\3\2\2\2\u01fd\u01fe\7^\2\2\u01fe\u01ff\7e\2\2\u01ff")
        buf.write(u"\u0200\7f\2\2\u0200\u0201\7q\2\2\u0201\u0202\7v\2\2\u0202")
        buf.write(u"V\3\2\2\2\u0203\u0204\7^\2\2\u0204\u0205\7f\2\2\u0205")
        buf.write(u"\u0206\7k\2\2\u0206\u0207\7x\2\2\u0207X\3\2\2\2\u0208")
        buf.write(u"\u0209\7^\2\2\u0209\u020a\7h\2\2\u020a\u020b\7t\2\2\u020b")
        buf.write(u"\u020c\7c\2\2\u020c\u020d\7e\2\2\u020dZ\3\2\2\2\u020e")
        buf.write(u"\u020f\7^\2\2\u020f\u0210\7o\2\2\u0210\u0211\7c\2\2\u0211")
        buf.write(u"\u0212\7v\2\2\u0212\u0213\7j\2\2\u0213\u0214\7k\2\2\u0214")
        buf.write(u"\u0215\7v\2\2\u0215\\\3\2\2\2\u0216\u0217\7a\2\2\u0217")
        buf.write(u"^\3\2\2\2\u0218\u0219\7`\2\2\u0219`\3\2\2\2\u021a\u021b")
        buf.write(u"\7<\2\2\u021bb\3\2\2\2\u021c\u021d\7(\2\2\u021dd\3\2")
        buf.write(u"\2\2\u021e\u021f\5\25\13\2\u021f\u0220\7c\2\2\u0220\u0221")
        buf.write(u"\7t\2\2\u0221\u0222\7t\2\2\u0222\u0223\7c\2\2\u0223\u0224")
        buf.write(u"\7{\2\2\u0224\u0225\3\2\2\2\u0225\u0226\5\27\f\2\u0226")
        buf.write(u"f\3\2\2\2\u0227\u0228\5\25\13\2\u0228\u0229\7u\2\2\u0229")
        buf.write(u"\u022a\7w\2\2\u022a\u022b\7d\2\2\u022b\u022c\7g\2\2\u022c")
        buf.write(u"\u022d\7s\2\2\u022d\u022e\7w\2\2\u022e\u022f\7c\2\2\u022f")
        buf.write(u"\u0230\7v\2\2\u0230\u0231\7k\2\2\u0231\u0232\7q\2\2\u0232")
        buf.write(u"\u0233\7p\2\2\u0233\u0234\7u\2\2\u0234\u0235\3\2\2\2")
        buf.write(u"\u0235\u0236\5\27\f\2\u0236h\3\2\2\2\u0237\u0238\5\25")
        buf.write(u"\13\2\u0238\u0239\7u\2\2\u0239\u023a\7r\2\2\u023a\u023b")
        buf.write(u"\7n\2\2\u023b\u023c\7k\2\2\u023c\u023d\7v\2\2\u023d\u023e")
        buf.write(u"\3\2\2\2\u023e\u023f\5\27\f\2\u023fj\3\2\2\2\u0240\u0241")
        buf.write(u"\5\25\13\2\u0241\u0242\7g\2\2\u0242\u0243\7s\2\2\u0243")
        buf.write(u"\u0244\7w\2\2\u0244\u0245\7c\2\2\u0245\u0246\7v\2\2\u0246")
        buf.write(u"\u0247\7k\2\2\u0247\u0248\7q\2\2\u0248\u0249\7p\2\2\u0249")
        buf.write(u"\u024a\3\2\2\2\u024a\u024b\5\27\f\2\u024bl\3\2\2\2\u024c")
        buf.write(u"\u024d\5\25\13\2\u024d\u024e\7g\2\2\u024e\u024f\7s\2")
        buf.write(u"\2\u024f\u0250\7p\2\2\u0250\u0251\7c\2\2\u0251\u0252")
        buf.write(u"\7t\2\2\u0252\u0253\7t\2\2\u0253\u0254\7c\2\2\u0254\u0255")
        buf.write(u"\7{\2\2\u0255\u0256\3\2\2\2\u0256\u0257\5\27\f\2\u0257")
        buf.write(u"n\3\2\2\2\u0258\u0259\7^\2\2\u0259\u025a\7d\2\2\u025a")
        buf.write(u"\u025b\7g\2\2\u025b\u025c\7i\2\2\u025c\u025d\7k\2\2\u025d")
        buf.write(u"\u025e\7p\2\2\u025e\u0264\3\2\2\2\u025f\u0265\5e\63\2")
        buf.write(u"\u0260\u0265\5g\64\2\u0261\u0265\5i\65\2\u0262\u0265")
        buf.write(u"\5k\66\2\u0263\u0265\5m\67\2\u0264\u025f\3\2\2\2\u0264")
        buf.write(u"\u0260\3\2\2\2\u0264\u0261\3\2\2\2\u0264\u0262\3\2\2")
        buf.write(u"\2\u0264\u0263\3\2\2\2\u0265p\3\2\2\2\u0266\u0267\7^")
        buf.write(u"\2\2\u0267\u0268\7n\2\2\u0268\u0269\7g\2\2\u0269\u026a")
        buf.write(u"\7h\2\2\u026a\u026b\7v\2\2\u026b\u026c\7]\2\2\u026cr")
        buf.write(u"\3\2\2\2\u026d\u026e\7^\2\2\u026e\u026f\7n\2\2\u026f")
        buf.write(u"\u0270\7g\2\2\u0270\u0271\7h\2\2\u0271\u0272\7v\2\2\u0272")
        buf.write(u"t\3\2\2\2\u0273\u0274\7^\2\2\u0274\u0275\7t\2\2\u0275")
        buf.write(u"\u0276\7k\2\2\u0276\u0277\7i\2\2\u0277\u0278\7j\2\2\u0278")
        buf.write(u"\u0279\7v\2\2\u0279v\3\2\2\2\u027a\u027b\7\60\2\2\u027b")
        buf.write(u"x\3\2\2\2\u027c\u027d\7^\2\2\u027d\u027e\7t\2\2\u027e")
        buf.write(u"\u027f\7o\2\2\u027fz\3\2\2\2\u0280\u0281\t\2\2\2\u0281")
        buf.write(u"|\3\2\2\2\u0282\u0286\7f\2\2\u0283\u0285\5{>\2\u0284")
        buf.write(u"\u0283\3\2\2\2\u0285\u0288\3\2\2\2\u0286\u0287\3\2\2")
        buf.write(u"\2\u0286\u0284\3\2\2\2\u0287\u0290\3\2\2\2\u0288\u0286")
        buf.write(u"\3\2\2\2\u0289\u0291\t\3\2\2\u028a\u028c\7^\2\2\u028b")
        buf.write(u"\u028d\t\3\2\2\u028c\u028b\3\2\2\2\u028d\u028e\3\2\2")
        buf.write(u"\2\u028e\u028c\3\2\2\2\u028e\u028f\3\2\2\2\u028f\u0291")
        buf.write(u"\3\2\2\2\u0290\u0289\3\2\2\2\u0290\u028a\3\2\2\2\u0291")
        buf.write(u"~\3\2\2\2\u0292\u0293\t\3\2\2\u0293\u0080\3\2\2\2\u0294")
        buf.write(u"\u0295\t\4\2\2\u0295\u0082\3\2\2\2\u0296\u0298\5\u0081")
        buf.write(u"A\2\u0297\u0296\3\2\2\2\u0298\u0299\3\2\2\2\u0299\u0297")
        buf.write(u"\3\2\2\2\u0299\u029a\3\2\2\2\u029a\u02a2\3\2\2\2\u029b")
        buf.write(u"\u029c\7.\2\2\u029c\u029d\5\u0081A\2\u029d\u029e\5\u0081")
        buf.write(u"A\2\u029e\u029f\5\u0081A\2\u029f\u02a1\3\2\2\2\u02a0")
        buf.write(u"\u029b\3\2\2\2\u02a1\u02a4\3\2\2\2\u02a2\u02a0\3\2\2")
        buf.write(u"\2\u02a2\u02a3\3\2\2\2\u02a3\u02bc\3\2\2\2\u02a4\u02a2")
        buf.write(u"\3\2\2\2\u02a5\u02a7\5\u0081A\2\u02a6\u02a5\3\2\2\2\u02a7")
        buf.write(u"\u02aa\3\2\2\2\u02a8\u02a6\3\2\2\2\u02a8\u02a9\3\2\2")
        buf.write(u"\2\u02a9\u02b2\3\2\2\2\u02aa\u02a8\3\2\2\2\u02ab\u02ac")
        buf.write(u"\7.\2\2\u02ac\u02ad\5\u0081A\2\u02ad\u02ae\5\u0081A\2")
        buf.write(u"\u02ae\u02af\5\u0081A\2\u02af\u02b1\3\2\2\2\u02b0\u02ab")
        buf.write(u"\3\2\2\2\u02b1\u02b4\3\2\2\2\u02b2\u02b0\3\2\2\2\u02b2")
        buf.write(u"\u02b3\3\2\2\2\u02b3\u02b5\3\2\2\2\u02b4\u02b2\3\2\2")
        buf.write(u"\2\u02b5\u02b7\7\60\2\2\u02b6\u02b8\5\u0081A\2\u02b7")
        buf.write(u"\u02b6\3\2\2\2\u02b8\u02b9\3\2\2\2\u02b9\u02b7\3\2\2")
        buf.write(u"\2\u02b9\u02ba\3\2\2\2\u02ba\u02bc\3\2\2\2\u02bb\u0297")
        buf.write(u"\3\2\2\2\u02bb\u02a8\3\2\2\2\u02bc\u0084\3\2\2\2\u02bd")
        buf.write(u"\u02be\7?\2\2\u02be\u0086\3\2\2\2\u02bf\u02c0\7>\2\2")
        buf.write(u"\u02c0\u0088\3\2\2\2\u02c1\u02c2\7^\2\2\u02c2\u02c3\7")
        buf.write(u"n\2\2\u02c3\u02c4\7g\2\2\u02c4\u02c5\7s\2\2\u02c5\u008a")
        buf.write(u"\3\2\2\2\u02c6\u02c7\7@\2\2\u02c7\u008c\3\2\2\2\u02c8")
        buf.write(u"\u02c9\7^\2\2\u02c9\u02ca\7i\2\2\u02ca\u02cb\7g\2\2\u02cb")
        buf.write(u"\u02cc\7s\2\2\u02cc\u008e\3\2\2\2\u02cd\u02ce\7#\2\2")
        buf.write(u"\u02ce\u0090\3\2\2\2\u02cf\u02d6\7^\2\2\u02d0\u02d2\t")
        buf.write(u"\3\2\2\u02d1\u02d0\3\2\2\2\u02d2\u02d3\3\2\2\2\u02d3")
        buf.write(u"\u02d1\3\2\2\2\u02d3\u02d4\3\2\2\2\u02d4\u02d7\3\2\2")
        buf.write(u"\2\u02d5\u02d7\t\5\2\2\u02d6\u02d1\3\2\2\2\u02d6\u02d5")
        buf.write(u"\3\2\2\2\u02d7\u02ec\3\2\2\2\u02d8\u02da\t\3\2\2\u02d9")
        buf.write(u"\u02d8\3\2\2\2\u02da\u02db\3\2\2\2\u02db\u02d9\3\2\2")
        buf.write(u"\2\u02db\u02dc\3\2\2\2\u02dc\u02dd\3\2\2\2\u02dd\u02de")
        buf.write(u"\7^\2\2\u02de\u02ec\t\6\2\2\u02df\u02e3\5y=\2\u02e0\u02e2")
        buf.write(u"\t\7\2\2\u02e1\u02e0\3\2\2\2\u02e2\u02e5\3\2\2\2\u02e3")
        buf.write(u"\u02e1\3\2\2\2\u02e3\u02e4\3\2\2\2\u02e4\u02e7\3\2\2")
        buf.write(u"\2\u02e5\u02e3\3\2\2\2\u02e6\u02e8\t\b\2\2\u02e7\u02e6")
        buf.write(u"\3\2\2\2\u02e8\u02e9\3\2\2\2\u02e9\u02e7\3\2\2\2\u02e9")
        buf.write(u"\u02ea\3\2\2\2\u02ea\u02ec\3\2\2\2\u02eb\u02cf\3\2\2")
        buf.write(u"\2\u02eb\u02d9\3\2\2\2\u02eb\u02df\3\2\2\2\u02ec\u0092")
        buf.write(u"\3\2\2\2\26\2\u0098\u0109\u015d\u0264\u0286\u028e\u0290")
        buf.write(u"\u0299\u02a2\u02a8\u02b2\u02b9\u02bb\u02d3\u02d6\u02db")
        buf.write(u"\u02e3\u02e9\u02eb\3\b\2\2")
        return buf.getvalue()


class LaTeXLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    WS = 2
    GREEK = 3
    ADD = 4
    SUB = 5
    MUL = 6
    DIV = 7
    L_PAREN = 8
    R_PAREN = 9
    L_BRACE = 10
    R_BRACE = 11
    L_BRACKET = 12
    R_BRACKET = 13
    BAR = 14
    FUNC_LIM = 15
    LIM_APPROACH_SYM = 16
    FUNC_INT = 17
    FUNC_SUM = 18
    FUNC_PROD = 19
    FUNC_LOG = 20
    FUNC_LN = 21
    FUNC_SIN = 22
    FUNC_COS = 23
    FUNC_TAN = 24
    FUNC_CSC = 25
    FUNC_SEC = 26
    FUNC_COT = 27
    FUNC_ARCSIN = 28
    FUNC_ARCCOS = 29
    FUNC_ARCTAN = 30
    FUNC_ARCCSC = 31
    FUNC_ARCSEC = 32
    FUNC_ARCCOT = 33
    FUNC_SINH = 34
    FUNC_COSH = 35
    FUNC_TANH = 36
    FUNC_ARSINH = 37
    FUNC_ARCOSH = 38
    FUNC_ARTANH = 39
    FUNC_SQRT = 40
    CMD_TIMES = 41
    CMD_CDOT = 42
    CMD_DIV = 43
    CMD_FRAC = 44
    CMD_MATHIT = 45
    UNDERSCORE = 46
    CARET = 47
    COLON = 48
    AMPERSAND = 49
    ARRAY = 50
    SUBEQUATIONS = 51
    SPLIT = 52
    EQUATION = 53
    EQNARRAY = 54
    BEGIN = 55
    LEFT_BRACKET = 56
    LEFT = 57
    RIGHT = 58
    DOT = 59
    RM = 60
    DIFFERENTIAL = 61
    LETTER = 62
    NUMBER = 63
    EQUAL = 64
    LT = 65
    LTE = 66
    GT = 67
    GTE = 68
    BANG = 69
    SYMBOL = 70

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ u"DEFAULT_MODE" ]

    literalNames = [ u"<INVALID>",
            u"','", u"'+'", u"'-'", u"'*'", u"'/'", u"'('", u"')'", u"'{'", 
            u"'}'", u"'['", u"']'", u"'|'", u"'\\lim'", u"'\\int'", u"'\\sum'", 
            u"'\\prod'", u"'\\log'", u"'\\ln'", u"'\\sin'", u"'\\cos'", 
            u"'\\tan'", u"'\\csc'", u"'\\sec'", u"'\\cot'", u"'\\arcsin'", 
            u"'\\arccos'", u"'\\arctan'", u"'\\arccsc'", u"'\\arcsec'", 
            u"'\\arccot'", u"'\\sinh'", u"'\\cosh'", u"'\\tanh'", u"'\\arsinh'", 
            u"'\\arcosh'", u"'\\artanh'", u"'\\sqrt'", u"'\\times'", u"'\\cdot'", 
            u"'\\div'", u"'\\frac'", u"'\\mathit'", u"'_'", u"'^'", u"':'", 
            u"'&'", u"'\\left['", u"'\\left'", u"'\\right'", u"'.'", u"'\\rm'", 
            u"'='", u"'<'", u"'\\leq'", u"'>'", u"'\\geq'", u"'!'" ]

    symbolicNames = [ u"<INVALID>",
            u"WS", u"GREEK", u"ADD", u"SUB", u"MUL", u"DIV", u"L_PAREN", 
            u"R_PAREN", u"L_BRACE", u"R_BRACE", u"L_BRACKET", u"R_BRACKET", 
            u"BAR", u"FUNC_LIM", u"LIM_APPROACH_SYM", u"FUNC_INT", u"FUNC_SUM", 
            u"FUNC_PROD", u"FUNC_LOG", u"FUNC_LN", u"FUNC_SIN", u"FUNC_COS", 
            u"FUNC_TAN", u"FUNC_CSC", u"FUNC_SEC", u"FUNC_COT", u"FUNC_ARCSIN", 
            u"FUNC_ARCCOS", u"FUNC_ARCTAN", u"FUNC_ARCCSC", u"FUNC_ARCSEC", 
            u"FUNC_ARCCOT", u"FUNC_SINH", u"FUNC_COSH", u"FUNC_TANH", u"FUNC_ARSINH", 
            u"FUNC_ARCOSH", u"FUNC_ARTANH", u"FUNC_SQRT", u"CMD_TIMES", 
            u"CMD_CDOT", u"CMD_DIV", u"CMD_FRAC", u"CMD_MATHIT", u"UNDERSCORE", 
            u"CARET", u"COLON", u"AMPERSAND", u"ARRAY", u"SUBEQUATIONS", 
            u"SPLIT", u"EQUATION", u"EQNARRAY", u"BEGIN", u"LEFT_BRACKET", 
            u"LEFT", u"RIGHT", u"DOT", u"RM", u"DIFFERENTIAL", u"LETTER", 
            u"NUMBER", u"EQUAL", u"LT", u"LTE", u"GT", u"GTE", u"BANG", 
            u"SYMBOL" ]

    ruleNames = [ u"T__0", u"WS", u"GREEK", u"ADD", u"SUB", u"MUL", u"DIV", 
                  u"L_PAREN", u"R_PAREN", u"L_BRACE", u"R_BRACE", u"L_BRACKET", 
                  u"R_BRACKET", u"BAR", u"FUNC_LIM", u"LIM_APPROACH_SYM", 
                  u"FUNC_INT", u"FUNC_SUM", u"FUNC_PROD", u"FUNC_LOG", u"FUNC_LN", 
                  u"FUNC_SIN", u"FUNC_COS", u"FUNC_TAN", u"FUNC_CSC", u"FUNC_SEC", 
                  u"FUNC_COT", u"FUNC_ARCSIN", u"FUNC_ARCCOS", u"FUNC_ARCTAN", 
                  u"FUNC_ARCCSC", u"FUNC_ARCSEC", u"FUNC_ARCCOT", u"FUNC_SINH", 
                  u"FUNC_COSH", u"FUNC_TANH", u"FUNC_ARSINH", u"FUNC_ARCOSH", 
                  u"FUNC_ARTANH", u"FUNC_SQRT", u"CMD_TIMES", u"CMD_CDOT", 
                  u"CMD_DIV", u"CMD_FRAC", u"CMD_MATHIT", u"UNDERSCORE", 
                  u"CARET", u"COLON", u"AMPERSAND", u"ARRAY", u"SUBEQUATIONS", 
                  u"SPLIT", u"EQUATION", u"EQNARRAY", u"BEGIN", u"LEFT_BRACKET", 
                  u"LEFT", u"RIGHT", u"DOT", u"RM", u"WS_CHAR", u"DIFFERENTIAL", 
                  u"LETTER", u"DIGIT", u"NUMBER", u"EQUAL", u"LT", u"LTE", 
                  u"GT", u"GTE", u"BANG", u"SYMBOL" ]

    grammarFileName = u"LaTeX.g4"

    def __init__(self, input=None, output=sys.stdout):
        super(LaTeXLexer, self).__init__(input, output=output)
        self.checkVersion("4.7.1")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


