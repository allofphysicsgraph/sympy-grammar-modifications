# Generated from /home/user/sympy-grammar-modifications/sympy/parsing/latex/LaTeX.g4 by ANTLR 4.7.1
# encoding: utf-8
from __future__ import print_function
from antlr4 import *
from io import StringIO
import sys


def serializedATN():
    with StringIO() as buf:
        buf.write(u"\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2")
        buf.write(u"S\u031d\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4")
        buf.write(u"\7\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r")
        buf.write(u"\t\r\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22")
        buf.write(u"\4\23\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4")
        buf.write(u"\30\t\30\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35")
        buf.write(u"\t\35\4\36\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4")
        buf.write(u"$\t$\4%\t%\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t")
        buf.write(u",\4-\t-\4.\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63")
        buf.write(u"\t\63\4\64\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\4")
        buf.write(u"9\t9\4:\t:\4;\t;\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA")
        buf.write(u"\4B\tB\4C\tC\4D\tD\4E\tE\4F\tF\4G\tG\4H\tH\4I\tI\4J\t")
        buf.write(u"J\4K\tK\4L\tL\4M\tM\4N\tN\4O\tO\4P\tP\4Q\tQ\4R\tR\4S")
        buf.write(u"\tS\4T\tT\3\2\6\2\u00ab\n\2\r\2\16\2\u00ac\3\2\3\2\3")
        buf.write(u"\3\3\3\3\4\3\4\3\5\3\5\3\6\3\6\3\7\3\7\3\b\3\b\3\t\3")
        buf.write(u"\t\3\n\3\n\3\13\3\13\3\f\3\f\3\r\3\r\3\16\3\16\3\16\3")
        buf.write(u"\16\3\16\3\16\3\16\3\16\3\16\3\16\3\16\3\16\3\16\3\16")
        buf.write(u"\3\16\3\16\3\16\3\16\3\16\3\16\3\16\3\16\3\16\3\16\3")
        buf.write(u"\16\5\16\u00e0\n\16\3\17\3\17\3\17\3\17\3\17\3\17\3\17")
        buf.write(u"\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3")
        buf.write(u"\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17")
        buf.write(u"\3\17\3\17\5\17\u0100\n\17\3\20\3\20\3\21\3\21\3\21\3")
        buf.write(u"\21\3\21\3\22\3\22\3\22\3\22\3\22\3\23\3\23\3\23\3\23")
        buf.write(u"\3\23\3\24\3\24\3\24\3\24\3\24\3\24\3\25\3\25\3\25\3")
        buf.write(u"\25\3\25\3\26\3\26\3\26\3\26\3\27\3\27\3\27\3\27\3\27")
        buf.write(u"\3\30\3\30\3\30\3\30\3\30\3\31\3\31\3\31\3\31\3\31\3")
        buf.write(u"\32\3\32\3\32\3\32\3\32\3\33\3\33\3\33\3\33\3\33\3\34")
        buf.write(u"\3\34\3\34\3\34\3\34\3\35\3\35\3\35\3\35\3\35\3\35\3")
        buf.write(u"\35\3\35\3\36\3\36\3\36\3\36\3\36\3\36\3\36\3\36\3\37")
        buf.write(u"\3\37\3\37\3\37\3\37\3\37\3\37\3\37\3 \3 \3 \3 \3 \3")
        buf.write(u" \3 \3 \3!\3!\3!\3!\3!\3!\3!\3!\3\"\3\"\3\"\3\"\3\"\3")
        buf.write(u"\"\3\"\3\"\3#\3#\3#\3#\3#\3#\3$\3$\3$\3$\3$\3$\3%\3%")
        buf.write(u"\3%\3%\3%\3%\3&\3&\3&\3&\3&\3&\3&\3&\3\'\3\'\3\'\3\'")
        buf.write(u"\3\'\3\'\3\'\3\'\3(\3(\3(\3(\3(\3(\3(\3(\3)\3)\3)\3)")
        buf.write(u"\3)\3)\3*\3*\3*\3*\3*\3*\3*\3+\3+\3+\3+\3+\3+\3,\3,\3")
        buf.write(u",\3,\3,\3-\3-\3-\3-\3-\3-\3.\3.\3.\3.\3.\3.\3.\3/\3/")
        buf.write(u"\3/\3/\3/\3/\3/\3/\3\60\3\60\3\60\3\60\3\60\3\60\3\60")
        buf.write(u"\3\60\3\61\3\61\3\61\3\61\3\61\3\61\3\61\3\61\3\62\3")
        buf.write(u"\62\3\63\3\63\3\64\3\64\3\65\3\65\3\66\3\66\3\66\3\66")
        buf.write(u"\3\66\3\66\3\66\3\66\5\66\u01e7\n\66\3\67\3\67\3\67\3")
        buf.write(u"\67\3\67\3\67\3\67\3\67\3\67\5\67\u01f2\n\67\38\38\3")
        buf.write(u"9\39\39\39\3:\3:\3;\3;\7;\u01fe\n;\f;\16;\u0201\13;\3")
        buf.write(u";\3;\3;\6;\u0206\n;\r;\16;\u0207\5;\u020a\n;\3<\3<\3")
        buf.write(u"=\3=\3>\6>\u0211\n>\r>\16>\u0212\3>\3>\3>\3>\3>\7>\u021a")
        buf.write(u"\n>\f>\16>\u021d\13>\3>\7>\u0220\n>\f>\16>\u0223\13>")
        buf.write(u"\3>\3>\3>\3>\3>\7>\u022a\n>\f>\16>\u022d\13>\3>\3>\6")
        buf.write(u">\u0231\n>\r>\16>\u0232\5>\u0235\n>\3?\3?\3@\3@\3@\3")
        buf.write(u"@\3@\3@\3@\3A\3A\3A\3A\3A\3A\3A\3B\3B\3B\3B\3B\3B\3B")
        buf.write(u"\3B\3C\3C\3C\3C\3C\3C\3D\3D\3D\3D\3D\3D\3D\3E\3E\3E\3")
        buf.write(u"E\3E\3F\3F\3F\3F\3F\3F\3F\3F\3G\3G\3G\3G\3G\3G\3G\5G")
        buf.write(u"\u0270\nG\3H\3H\3I\3I\3I\3I\3I\3I\3I\3J\3J\3J\3J\3J\3")
        buf.write(u"J\3J\3J\3J\3J\3J\3J\3J\5J\u0288\nJ\3K\3K\3K\3K\3K\3K")
        buf.write(u"\3K\3K\3K\3K\3K\3K\3K\3K\5K\u0298\nK\3L\3L\3L\3L\3L\3")
        buf.write(u"L\3L\3L\3L\3L\3L\3L\3L\3L\3L\3L\3L\3L\3L\3L\3L\3L\5L")
        buf.write(u"\u02b0\nL\3M\3M\3M\3M\3M\3M\3M\3M\3M\3M\3M\3M\3M\3M\3")
        buf.write(u"M\3M\3M\3M\5M\u02c4\nM\3N\3N\3N\3N\3N\3N\3N\3N\3N\3N")
        buf.write(u"\3N\3N\3N\3N\3N\3N\3N\3N\3N\3N\5N\u02da\nN\3O\3O\3P\3")
        buf.write(u"P\3P\3P\3P\3P\3Q\3Q\3Q\3Q\3Q\3Q\3Q\3Q\3Q\3Q\3Q\3Q\3Q")
        buf.write(u"\5Q\u02f1\nQ\3R\3R\3R\3R\3R\3R\3R\3R\3R\3R\3R\3R\3R\3")
        buf.write(u"R\3R\5R\u0302\nR\3S\3S\3T\3T\6T\u0308\nT\rT\16T\u0309")
        buf.write(u"\3T\3T\6T\u030e\nT\rT\16T\u030f\3T\5T\u0313\nT\3T\6T")
        buf.write(u"\u0316\nT\rT\16T\u0317\3T\3T\5T\u031c\nT\3\u01ff\2U\3")
        buf.write(u"\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25\f\27\r\31")
        buf.write(u"\16\33\17\35\20\37\21!\22#\23%\24\'\25)\26+\27-\30/\31")
        buf.write(u"\61\32\63\33\65\34\67\359\36;\37= ?!A\"C#E$G%I&K\'M(")
        buf.write(u"O)Q*S+U,W-Y.[/]\60_\61a\62c\63e\64g\65i\66k\67m8o9q:")
        buf.write(u"s\2u;w<y\2{=}>\177?\u0081@\u0083A\u0085B\u0087C\u0089")
        buf.write(u"D\u008bE\u008dF\u008fG\u0091H\u0093I\u0095J\u0097K\u0099")
        buf.write(u"L\u009bM\u009dN\u009fO\u00a1P\u00a3Q\u00a5R\u00a7S\3")
        buf.write(u"\2\7\5\2\13\f\17\17\"\"\4\2C\\c|\3\2\62;\4\2\"\"<=\4")
        buf.write(u"\2..<=\2\u0339\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2")
        buf.write(u"\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21")
        buf.write(u"\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31")
        buf.write(u"\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2!\3")
        buf.write(u"\2\2\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2\2")
        buf.write(u"+\3\2\2\2\2-\3\2\2\2\2/\3\2\2\2\2\61\3\2\2\2\2\63\3\2")
        buf.write(u"\2\2\2\65\3\2\2\2\2\67\3\2\2\2\29\3\2\2\2\2;\3\2\2\2")
        buf.write(u"\2=\3\2\2\2\2?\3\2\2\2\2A\3\2\2\2\2C\3\2\2\2\2E\3\2\2")
        buf.write(u"\2\2G\3\2\2\2\2I\3\2\2\2\2K\3\2\2\2\2M\3\2\2\2\2O\3\2")
        buf.write(u"\2\2\2Q\3\2\2\2\2S\3\2\2\2\2U\3\2\2\2\2W\3\2\2\2\2Y\3")
        buf.write(u"\2\2\2\2[\3\2\2\2\2]\3\2\2\2\2_\3\2\2\2\2a\3\2\2\2\2")
        buf.write(u"c\3\2\2\2\2e\3\2\2\2\2g\3\2\2\2\2i\3\2\2\2\2k\3\2\2\2")
        buf.write(u"\2m\3\2\2\2\2o\3\2\2\2\2q\3\2\2\2\2u\3\2\2\2\2w\3\2\2")
        buf.write(u"\2\2{\3\2\2\2\2}\3\2\2\2\2\177\3\2\2\2\2\u0081\3\2\2")
        buf.write(u"\2\2\u0083\3\2\2\2\2\u0085\3\2\2\2\2\u0087\3\2\2\2\2")
        buf.write(u"\u0089\3\2\2\2\2\u008b\3\2\2\2\2\u008d\3\2\2\2\2\u008f")
        buf.write(u"\3\2\2\2\2\u0091\3\2\2\2\2\u0093\3\2\2\2\2\u0095\3\2")
        buf.write(u"\2\2\2\u0097\3\2\2\2\2\u0099\3\2\2\2\2\u009b\3\2\2\2")
        buf.write(u"\2\u009d\3\2\2\2\2\u009f\3\2\2\2\2\u00a1\3\2\2\2\2\u00a3")
        buf.write(u"\3\2\2\2\2\u00a5\3\2\2\2\2\u00a7\3\2\2\2\3\u00aa\3\2")
        buf.write(u"\2\2\5\u00b0\3\2\2\2\7\u00b2\3\2\2\2\t\u00b4\3\2\2\2")
        buf.write(u"\13\u00b6\3\2\2\2\r\u00b8\3\2\2\2\17\u00ba\3\2\2\2\21")
        buf.write(u"\u00bc\3\2\2\2\23\u00be\3\2\2\2\25\u00c0\3\2\2\2\27\u00c2")
        buf.write(u"\3\2\2\2\31\u00c4\3\2\2\2\33\u00df\3\2\2\2\35\u00ff\3")
        buf.write(u"\2\2\2\37\u0101\3\2\2\2!\u0103\3\2\2\2#\u0108\3\2\2\2")
        buf.write(u"%\u010d\3\2\2\2\'\u0112\3\2\2\2)\u0118\3\2\2\2+\u011d")
        buf.write(u"\3\2\2\2-\u0121\3\2\2\2/\u0126\3\2\2\2\61\u012b\3\2\2")
        buf.write(u"\2\63\u0130\3\2\2\2\65\u0135\3\2\2\2\67\u013a\3\2\2\2")
        buf.write(u"9\u013f\3\2\2\2;\u0147\3\2\2\2=\u014f\3\2\2\2?\u0157")
        buf.write(u"\3\2\2\2A\u015f\3\2\2\2C\u0167\3\2\2\2E\u016f\3\2\2\2")
        buf.write(u"G\u0175\3\2\2\2I\u017b\3\2\2\2K\u0181\3\2\2\2M\u0189")
        buf.write(u"\3\2\2\2O\u0191\3\2\2\2Q\u0199\3\2\2\2S\u019f\3\2\2\2")
        buf.write(u"U\u01a6\3\2\2\2W\u01ac\3\2\2\2Y\u01b1\3\2\2\2[\u01b7")
        buf.write(u"\3\2\2\2]\u01be\3\2\2\2_\u01c6\3\2\2\2a\u01ce\3\2\2\2")
        buf.write(u"c\u01d6\3\2\2\2e\u01d8\3\2\2\2g\u01da\3\2\2\2i\u01dc")
        buf.write(u"\3\2\2\2k\u01de\3\2\2\2m\u01e8\3\2\2\2o\u01f3\3\2\2\2")
        buf.write(u"q\u01f5\3\2\2\2s\u01f9\3\2\2\2u\u01fb\3\2\2\2w\u020b")
        buf.write(u"\3\2\2\2y\u020d\3\2\2\2{\u0234\3\2\2\2}\u0236\3\2\2\2")
        buf.write(u"\177\u0238\3\2\2\2\u0081\u023f\3\2\2\2\u0083\u0246\3")
        buf.write(u"\2\2\2\u0085\u024e\3\2\2\2\u0087\u0254\3\2\2\2\u0089")
        buf.write(u"\u025b\3\2\2\2\u008b\u0260\3\2\2\2\u008d\u026f\3\2\2")
        buf.write(u"\2\u008f\u0271\3\2\2\2\u0091\u0273\3\2\2\2\u0093\u0287")
        buf.write(u"\3\2\2\2\u0095\u0297\3\2\2\2\u0097\u02af\3\2\2\2\u0099")
        buf.write(u"\u02c3\3\2\2\2\u009b\u02d9\3\2\2\2\u009d\u02db\3\2\2")
        buf.write(u"\2\u009f\u02dd\3\2\2\2\u00a1\u02f0\3\2\2\2\u00a3\u0301")
        buf.write(u"\3\2\2\2\u00a5\u0303\3\2\2\2\u00a7\u031b\3\2\2\2\u00a9")
        buf.write(u"\u00ab\t\2\2\2\u00aa\u00a9\3\2\2\2\u00ab\u00ac\3\2\2")
        buf.write(u"\2\u00ac\u00aa\3\2\2\2\u00ac\u00ad\3\2\2\2\u00ad\u00ae")
        buf.write(u"\3\2\2\2\u00ae\u00af\b\2\2\2\u00af\4\3\2\2\2\u00b0\u00b1")
        buf.write(u"\7-\2\2\u00b1\6\3\2\2\2\u00b2\u00b3\7/\2\2\u00b3\b\3")
        buf.write(u"\2\2\2\u00b4\u00b5\7,\2\2\u00b5\n\3\2\2\2\u00b6\u00b7")
        buf.write(u"\7\61\2\2\u00b7\f\3\2\2\2\u00b8\u00b9\7*\2\2\u00b9\16")
        buf.write(u"\3\2\2\2\u00ba\u00bb\7+\2\2\u00bb\20\3\2\2\2\u00bc\u00bd")
        buf.write(u"\7}\2\2\u00bd\22\3\2\2\2\u00be\u00bf\7\177\2\2\u00bf")
        buf.write(u"\24\3\2\2\2\u00c0\u00c1\7]\2\2\u00c1\26\3\2\2\2\u00c2")
        buf.write(u"\u00c3\7_\2\2\u00c3\30\3\2\2\2\u00c4\u00c5\7<\2\2\u00c5")
        buf.write(u"\32\3\2\2\2\u00c6\u00c7\7^\2\2\u00c7\u00c8\7t\2\2\u00c8")
        buf.write(u"\u00c9\7k\2\2\u00c9\u00ca\7i\2\2\u00ca\u00cb\7j\2\2\u00cb")
        buf.write(u"\u00cc\7v\2\2\u00cc\u00cd\7c\2\2\u00cd\u00ce\7t\2\2\u00ce")
        buf.write(u"\u00cf\7t\2\2\u00cf\u00d0\7q\2\2\u00d0\u00e0\7y\2\2\u00d1")
        buf.write(u"\u00d2\7^\2\2\u00d2\u00d3\7v\2\2\u00d3\u00e0\7q\2\2\u00d4")
        buf.write(u"\u00d5\7^\2\2\u00d5\u00d6\7T\2\2\u00d6\u00d7\7k\2\2\u00d7")
        buf.write(u"\u00d8\7i\2\2\u00d8\u00d9\7j\2\2\u00d9\u00da\7v\2\2\u00da")
        buf.write(u"\u00db\7c\2\2\u00db\u00dc\7t\2\2\u00dc\u00dd\7t\2\2\u00dd")
        buf.write(u"\u00de\7q\2\2\u00de\u00e0\7y\2\2\u00df\u00c6\3\2\2\2")
        buf.write(u"\u00df\u00d1\3\2\2\2\u00df\u00d4\3\2\2\2\u00e0\34\3\2")
        buf.write(u"\2\2\u00e1\u00e2\7^\2\2\u00e2\u00e3\7n\2\2\u00e3\u00e4")
        buf.write(u"\7q\2\2\u00e4\u00e5\7p\2\2\u00e5\u00e6\7i\2\2\u00e6\u00e7")
        buf.write(u"\7t\2\2\u00e7\u00e8\7k\2\2\u00e8\u00e9\7i\2\2\u00e9\u00ea")
        buf.write(u"\7j\2\2\u00ea\u00eb\7v\2\2\u00eb\u00ec\7c\2\2\u00ec\u00ed")
        buf.write(u"\7t\2\2\u00ed\u00ee\7t\2\2\u00ee\u00ef\7q\2\2\u00ef\u0100")
        buf.write(u"\7y\2\2\u00f0\u00f1\7^\2\2\u00f1\u00f2\7N\2\2\u00f2\u00f3")
        buf.write(u"\7q\2\2\u00f3\u00f4\7p\2\2\u00f4\u00f5\7i\2\2\u00f5\u00f6")
        buf.write(u"\7t\2\2\u00f6\u00f7\7k\2\2\u00f7\u00f8\7i\2\2\u00f8\u00f9")
        buf.write(u"\7j\2\2\u00f9\u00fa\7v\2\2\u00fa\u00fb\7c\2\2\u00fb\u00fc")
        buf.write(u"\7t\2\2\u00fc\u00fd\7t\2\2\u00fd\u00fe\7q\2\2\u00fe\u0100")
        buf.write(u"\7y\2\2\u00ff\u00e1\3\2\2\2\u00ff\u00f0\3\2\2\2\u0100")
        buf.write(u"\36\3\2\2\2\u0101\u0102\7~\2\2\u0102 \3\2\2\2\u0103\u0104")
        buf.write(u"\7^\2\2\u0104\u0105\7n\2\2\u0105\u0106\7k\2\2\u0106\u0107")
        buf.write(u"\7o\2\2\u0107\"\3\2\2\2\u0108\u0109\7^\2\2\u0109\u010a")
        buf.write(u"\7k\2\2\u010a\u010b\7p\2\2\u010b\u010c\7v\2\2\u010c$")
        buf.write(u"\3\2\2\2\u010d\u010e\7^\2\2\u010e\u010f\7u\2\2\u010f")
        buf.write(u"\u0110\7w\2\2\u0110\u0111\7o\2\2\u0111&\3\2\2\2\u0112")
        buf.write(u"\u0113\7^\2\2\u0113\u0114\7r\2\2\u0114\u0115\7t\2\2\u0115")
        buf.write(u"\u0116\7q\2\2\u0116\u0117\7f\2\2\u0117(\3\2\2\2\u0118")
        buf.write(u"\u0119\7^\2\2\u0119\u011a\7n\2\2\u011a\u011b\7q\2\2\u011b")
        buf.write(u"\u011c\7i\2\2\u011c*\3\2\2\2\u011d\u011e\7^\2\2\u011e")
        buf.write(u"\u011f\7n\2\2\u011f\u0120\7p\2\2\u0120,\3\2\2\2\u0121")
        buf.write(u"\u0122\7^\2\2\u0122\u0123\7u\2\2\u0123\u0124\7k\2\2\u0124")
        buf.write(u"\u0125\7p\2\2\u0125.\3\2\2\2\u0126\u0127\7^\2\2\u0127")
        buf.write(u"\u0128\7e\2\2\u0128\u0129\7q\2\2\u0129\u012a\7u\2\2\u012a")
        buf.write(u"\60\3\2\2\2\u012b\u012c\7^\2\2\u012c\u012d\7v\2\2\u012d")
        buf.write(u"\u012e\7c\2\2\u012e\u012f\7p\2\2\u012f\62\3\2\2\2\u0130")
        buf.write(u"\u0131\7^\2\2\u0131\u0132\7e\2\2\u0132\u0133\7u\2\2\u0133")
        buf.write(u"\u0134\7e\2\2\u0134\64\3\2\2\2\u0135\u0136\7^\2\2\u0136")
        buf.write(u"\u0137\7u\2\2\u0137\u0138\7g\2\2\u0138\u0139\7e\2\2\u0139")
        buf.write(u"\66\3\2\2\2\u013a\u013b\7^\2\2\u013b\u013c\7e\2\2\u013c")
        buf.write(u"\u013d\7q\2\2\u013d\u013e\7v\2\2\u013e8\3\2\2\2\u013f")
        buf.write(u"\u0140\7^\2\2\u0140\u0141\7c\2\2\u0141\u0142\7t\2\2\u0142")
        buf.write(u"\u0143\7e\2\2\u0143\u0144\7u\2\2\u0144\u0145\7k\2\2\u0145")
        buf.write(u"\u0146\7p\2\2\u0146:\3\2\2\2\u0147\u0148\7^\2\2\u0148")
        buf.write(u"\u0149\7c\2\2\u0149\u014a\7t\2\2\u014a\u014b\7e\2\2\u014b")
        buf.write(u"\u014c\7e\2\2\u014c\u014d\7q\2\2\u014d\u014e\7u\2\2\u014e")
        buf.write(u"<\3\2\2\2\u014f\u0150\7^\2\2\u0150\u0151\7c\2\2\u0151")
        buf.write(u"\u0152\7t\2\2\u0152\u0153\7e\2\2\u0153\u0154\7v\2\2\u0154")
        buf.write(u"\u0155\7c\2\2\u0155\u0156\7p\2\2\u0156>\3\2\2\2\u0157")
        buf.write(u"\u0158\7^\2\2\u0158\u0159\7c\2\2\u0159\u015a\7t\2\2\u015a")
        buf.write(u"\u015b\7e\2\2\u015b\u015c\7e\2\2\u015c\u015d\7u\2\2\u015d")
        buf.write(u"\u015e\7e\2\2\u015e@\3\2\2\2\u015f\u0160\7^\2\2\u0160")
        buf.write(u"\u0161\7c\2\2\u0161\u0162\7t\2\2\u0162\u0163\7e\2\2\u0163")
        buf.write(u"\u0164\7u\2\2\u0164\u0165\7g\2\2\u0165\u0166\7e\2\2\u0166")
        buf.write(u"B\3\2\2\2\u0167\u0168\7^\2\2\u0168\u0169\7c\2\2\u0169")
        buf.write(u"\u016a\7t\2\2\u016a\u016b\7e\2\2\u016b\u016c\7e\2\2\u016c")
        buf.write(u"\u016d\7q\2\2\u016d\u016e\7v\2\2\u016eD\3\2\2\2\u016f")
        buf.write(u"\u0170\7^\2\2\u0170\u0171\7u\2\2\u0171\u0172\7k\2\2\u0172")
        buf.write(u"\u0173\7p\2\2\u0173\u0174\7j\2\2\u0174F\3\2\2\2\u0175")
        buf.write(u"\u0176\7^\2\2\u0176\u0177\7e\2\2\u0177\u0178\7q\2\2\u0178")
        buf.write(u"\u0179\7u\2\2\u0179\u017a\7j\2\2\u017aH\3\2\2\2\u017b")
        buf.write(u"\u017c\7^\2\2\u017c\u017d\7v\2\2\u017d\u017e\7c\2\2\u017e")
        buf.write(u"\u017f\7p\2\2\u017f\u0180\7j\2\2\u0180J\3\2\2\2\u0181")
        buf.write(u"\u0182\7^\2\2\u0182\u0183\7c\2\2\u0183\u0184\7t\2\2\u0184")
        buf.write(u"\u0185\7u\2\2\u0185\u0186\7k\2\2\u0186\u0187\7p\2\2\u0187")
        buf.write(u"\u0188\7j\2\2\u0188L\3\2\2\2\u0189\u018a\7^\2\2\u018a")
        buf.write(u"\u018b\7c\2\2\u018b\u018c\7t\2\2\u018c\u018d\7e\2\2\u018d")
        buf.write(u"\u018e\7q\2\2\u018e\u018f\7u\2\2\u018f\u0190\7j\2\2\u0190")
        buf.write(u"N\3\2\2\2\u0191\u0192\7^\2\2\u0192\u0193\7c\2\2\u0193")
        buf.write(u"\u0194\7t\2\2\u0194\u0195\7v\2\2\u0195\u0196\7c\2\2\u0196")
        buf.write(u"\u0197\7p\2\2\u0197\u0198\7j\2\2\u0198P\3\2\2\2\u0199")
        buf.write(u"\u019a\7^\2\2\u019a\u019b\7u\2\2\u019b\u019c\7s\2\2\u019c")
        buf.write(u"\u019d\7t\2\2\u019d\u019e\7v\2\2\u019eR\3\2\2\2\u019f")
        buf.write(u"\u01a0\7^\2\2\u01a0\u01a1\7v\2\2\u01a1\u01a2\7k\2\2\u01a2")
        buf.write(u"\u01a3\7o\2\2\u01a3\u01a4\7g\2\2\u01a4\u01a5\7u\2\2\u01a5")
        buf.write(u"T\3\2\2\2\u01a6\u01a7\7^\2\2\u01a7\u01a8\7e\2\2\u01a8")
        buf.write(u"\u01a9\7f\2\2\u01a9\u01aa\7q\2\2\u01aa\u01ab\7v\2\2\u01ab")
        buf.write(u"V\3\2\2\2\u01ac\u01ad\7^\2\2\u01ad\u01ae\7f\2\2\u01ae")
        buf.write(u"\u01af\7k\2\2\u01af\u01b0\7x\2\2\u01b0X\3\2\2\2\u01b1")
        buf.write(u"\u01b2\7^\2\2\u01b2\u01b3\7h\2\2\u01b3\u01b4\7t\2\2\u01b4")
        buf.write(u"\u01b5\7c\2\2\u01b5\u01b6\7e\2\2\u01b6Z\3\2\2\2\u01b7")
        buf.write(u"\u01b8\7^\2\2\u01b8\u01b9\7d\2\2\u01b9\u01ba\7k\2\2\u01ba")
        buf.write(u"\u01bb\7p\2\2\u01bb\u01bc\7q\2\2\u01bc\u01bd\7o\2\2\u01bd")
        buf.write(u"\\\3\2\2\2\u01be\u01bf\7^\2\2\u01bf\u01c0\7f\2\2\u01c0")
        buf.write(u"\u01c1\7d\2\2\u01c1\u01c2\7k\2\2\u01c2\u01c3\7p\2\2\u01c3")
        buf.write(u"\u01c4\7q\2\2\u01c4\u01c5\7o\2\2\u01c5^\3\2\2\2\u01c6")
        buf.write(u"\u01c7\7^\2\2\u01c7\u01c8\7v\2\2\u01c8\u01c9\7d\2\2\u01c9")
        buf.write(u"\u01ca\7k\2\2\u01ca\u01cb\7p\2\2\u01cb\u01cc\7q\2\2\u01cc")
        buf.write(u"\u01cd\7o\2\2\u01cd`\3\2\2\2\u01ce\u01cf\7^\2\2\u01cf")
        buf.write(u"\u01d0\7o\2\2\u01d0\u01d1\7c\2\2\u01d1\u01d2\7v\2\2\u01d2")
        buf.write(u"\u01d3\7j\2\2\u01d3\u01d4\7k\2\2\u01d4\u01d5\7v\2\2\u01d5")
        buf.write(u"b\3\2\2\2\u01d6\u01d7\7a\2\2\u01d7d\3\2\2\2\u01d8\u01d9")
        buf.write(u"\7`\2\2\u01d9f\3\2\2\2\u01da\u01db\7(\2\2\u01dbh\3\2")
        buf.write(u"\2\2\u01dc\u01dd\7.\2\2\u01ddj\3\2\2\2\u01de\u01df\7")
        buf.write(u"^\2\2\u01df\u01e0\7n\2\2\u01e0\u01e1\7g\2\2\u01e1\u01e2")
        buf.write(u"\7h\2\2\u01e2\u01e3\7v\2\2\u01e3\u01e6\3\2\2\2\u01e4")
        buf.write(u"\u01e7\5\21\t\2\u01e5\u01e7\5\25\13\2\u01e6\u01e4\3\2")
        buf.write(u"\2\2\u01e6\u01e5\3\2\2\2\u01e6\u01e7\3\2\2\2\u01e7l\3")
        buf.write(u"\2\2\2\u01e8\u01e9\7^\2\2\u01e9\u01ea\7t\2\2\u01ea\u01eb")
        buf.write(u"\7k\2\2\u01eb\u01ec\7i\2\2\u01ec\u01ed\7j\2\2\u01ed\u01ee")
        buf.write(u"\7v\2\2\u01ee\u01f1\3\2\2\2\u01ef\u01f2\5\23\n\2\u01f0")
        buf.write(u"\u01f2\5\27\f\2\u01f1\u01ef\3\2\2\2\u01f1\u01f0\3\2\2")
        buf.write(u"\2\u01f1\u01f2\3\2\2\2\u01f2n\3\2\2\2\u01f3\u01f4\7\60")
        buf.write(u"\2\2\u01f4p\3\2\2\2\u01f5\u01f6\7^\2\2\u01f6\u01f7\7")
        buf.write(u"t\2\2\u01f7\u01f8\7o\2\2\u01f8r\3\2\2\2\u01f9\u01fa\t")
        buf.write(u"\2\2\2\u01fat\3\2\2\2\u01fb\u01ff\7f\2\2\u01fc\u01fe")
        buf.write(u"\5s:\2\u01fd\u01fc\3\2\2\2\u01fe\u0201\3\2\2\2\u01ff")
        buf.write(u"\u0200\3\2\2\2\u01ff\u01fd\3\2\2\2\u0200\u0209\3\2\2")
        buf.write(u"\2\u0201\u01ff\3\2\2\2\u0202\u020a\t\3\2\2\u0203\u0205")
        buf.write(u"\7^\2\2\u0204\u0206\t\3\2\2\u0205\u0204\3\2\2\2\u0206")
        buf.write(u"\u0207\3\2\2\2\u0207\u0205\3\2\2\2\u0207\u0208\3\2\2")
        buf.write(u"\2\u0208\u020a\3\2\2\2\u0209\u0202\3\2\2\2\u0209\u0203")
        buf.write(u"\3\2\2\2\u020av\3\2\2\2\u020b\u020c\t\3\2\2\u020cx\3")
        buf.write(u"\2\2\2\u020d\u020e\t\4\2\2\u020ez\3\2\2\2\u020f\u0211")
        buf.write(u"\5y=\2\u0210\u020f\3\2\2\2\u0211\u0212\3\2\2\2\u0212")
        buf.write(u"\u0210\3\2\2\2\u0212\u0213\3\2\2\2\u0213\u021b\3\2\2")
        buf.write(u"\2\u0214\u0215\7.\2\2\u0215\u0216\5y=\2\u0216\u0217\5")
        buf.write(u"y=\2\u0217\u0218\5y=\2\u0218\u021a\3\2\2\2\u0219\u0214")
        buf.write(u"\3\2\2\2\u021a\u021d\3\2\2\2\u021b\u0219\3\2\2\2\u021b")
        buf.write(u"\u021c\3\2\2\2\u021c\u0235\3\2\2\2\u021d\u021b\3\2\2")
        buf.write(u"\2\u021e\u0220\5y=\2\u021f\u021e\3\2\2\2\u0220\u0223")
        buf.write(u"\3\2\2\2\u0221\u021f\3\2\2\2\u0221\u0222\3\2\2\2\u0222")
        buf.write(u"\u022b\3\2\2\2\u0223\u0221\3\2\2\2\u0224\u0225\7.\2\2")
        buf.write(u"\u0225\u0226\5y=\2\u0226\u0227\5y=\2\u0227\u0228\5y=")
        buf.write(u"\2\u0228\u022a\3\2\2\2\u0229\u0224\3\2\2\2\u022a\u022d")
        buf.write(u"\3\2\2\2\u022b\u0229\3\2\2\2\u022b\u022c\3\2\2\2\u022c")
        buf.write(u"\u022e\3\2\2\2\u022d\u022b\3\2\2\2\u022e\u0230\7\60\2")
        buf.write(u"\2\u022f\u0231\5y=\2\u0230\u022f\3\2\2\2\u0231\u0232")
        buf.write(u"\3\2\2\2\u0232\u0230\3\2\2\2\u0232\u0233\3\2\2\2\u0233")
        buf.write(u"\u0235\3\2\2\2\u0234\u0210\3\2\2\2\u0234\u0221\3\2\2")
        buf.write(u"\2\u0235|\3\2\2\2\u0236\u0237\7?\2\2\u0237~\3\2\2\2\u0238")
        buf.write(u"\u0239\7^\2\2\u0239\u023a\7f\2\2\u023a\u023b\7q\2\2\u023b")
        buf.write(u"\u023c\7v\2\2\u023c\u023d\7g\2\2\u023d\u023e\7s\2\2\u023e")
        buf.write(u"\u0080\3\2\2\2\u023f\u0240\7^\2\2\u0240\u0241\7g\2\2")
        buf.write(u"\u0241\u0242\7s\2\2\u0242\u0243\7w\2\2\u0243\u0244\7")
        buf.write(u"k\2\2\u0244\u0245\7x\2\2\u0245\u0082\3\2\2\2\u0246\u0247")
        buf.write(u"\7^\2\2\u0247\u0248\7c\2\2\u0248\u0249\7r\2\2\u0249\u024a")
        buf.write(u"\7r\2\2\u024a\u024b\7t\2\2\u024b\u024c\7q\2\2\u024c\u024d")
        buf.write(u"\7z\2\2\u024d\u0084\3\2\2\2\u024e\u024f\7^\2\2\u024f")
        buf.write(u"\u0250\7e\2\2\u0250\u0251\7q\2\2\u0251\u0252\7p\2\2\u0252")
        buf.write(u"\u0253\7i\2\2\u0253\u0086\3\2\2\2\u0254\u0255\7^\2\2")
        buf.write(u"\u0255\u0256\7u\2\2\u0256\u0257\7k\2\2\u0257\u0258\7")
        buf.write(u"o\2\2\u0258\u0259\7g\2\2\u0259\u025a\7s\2\2\u025a\u0088")
        buf.write(u"\3\2\2\2\u025b\u025c\7^\2\2\u025c\u025d\7u\2\2\u025d")
        buf.write(u"\u025e\7k\2\2\u025e\u025f\7o\2\2\u025f\u008a\3\2\2\2")
        buf.write(u"\u0260\u0261\7^\2\2\u0261\u0262\7r\2\2\u0262\u0263\7")
        buf.write(u"t\2\2\u0263\u0264\7q\2\2\u0264\u0265\7r\2\2\u0265\u0266")
        buf.write(u"\7v\2\2\u0266\u0267\7q\2\2\u0267\u008c\3\2\2\2\u0268")
        buf.write(u"\u0269\7^\2\2\u0269\u026a\7p\2\2\u026a\u026b\7g\2\2\u026b")
        buf.write(u"\u0270\7s\2\2\u026c\u026d\7^\2\2\u026d\u026e\7p\2\2\u026e")
        buf.write(u"\u0270\7g\2\2\u026f\u0268\3\2\2\2\u026f\u026c\3\2\2\2")
        buf.write(u"\u0270\u008e\3\2\2\2\u0271\u0272\7>\2\2\u0272\u0090\3")
        buf.write(u"\2\2\2\u0273\u0274\7^\2\2\u0274\u0275\7p\2\2\u0275\u0276")
        buf.write(u"\7n\2\2\u0276\u0277\7g\2\2\u0277\u0278\7u\2\2\u0278\u0279")
        buf.write(u"\7u\2\2\u0279\u0092\3\2\2\2\u027a\u027b\7^\2\2\u027b")
        buf.write(u"\u027c\7n\2\2\u027c\u027d\7g\2\2\u027d\u0288\7s\2\2\u027e")
        buf.write(u"\u027f\7^\2\2\u027f\u0280\7n\2\2\u0280\u0281\7g\2\2\u0281")
        buf.write(u"\u0282\7s\2\2\u0282\u0283\7u\2\2\u0283\u0284\7n\2\2\u0284")
        buf.write(u"\u0285\7c\2\2\u0285\u0286\7p\2\2\u0286\u0288\7v\2\2\u0287")
        buf.write(u"\u027a\3\2\2\2\u0287\u027e\3\2\2\2\u0288\u0094\3\2\2")
        buf.write(u"\2\u0289\u028a\7^\2\2\u028a\u028b\7u\2\2\u028b\u028c")
        buf.write(u"\7w\2\2\u028c\u028d\7d\2\2\u028d\u028e\7u\2\2\u028e\u028f")
        buf.write(u"\7g\2\2\u028f\u0298\7v\2\2\u0290\u0291\7^\2\2\u0291\u0292")
        buf.write(u"\7u\2\2\u0292\u0293\7w\2\2\u0293\u0294\7r\2\2\u0294\u0295")
        buf.write(u"\7u\2\2\u0295\u0296\7g\2\2\u0296\u0298\7v\2\2\u0297\u0289")
        buf.write(u"\3\2\2\2\u0297\u0290\3\2\2\2\u0298\u0096\3\2\2\2\u0299")
        buf.write(u"\u029a\7^\2\2\u029a\u029b\7p\2\2\u029b\u029c\7q\2\2\u029c")
        buf.write(u"\u029d\7v\2\2\u029d\u029e\7^\2\2\u029e\u029f\7u\2\2\u029f")
        buf.write(u"\u02a0\7w\2\2\u02a0\u02a1\7d\2\2\u02a1\u02a2\7u\2\2\u02a2")
        buf.write(u"\u02a3\7g\2\2\u02a3\u02b0\7v\2\2\u02a4\u02a5\7^\2\2\u02a5")
        buf.write(u"\u02a6\7p\2\2\u02a6\u02a7\7q\2\2\u02a7\u02a8\7v\2\2\u02a8")
        buf.write(u"\u02a9\7^\2\2\u02a9\u02aa\7u\2\2\u02aa\u02ab\7w\2\2\u02ab")
        buf.write(u"\u02ac\7r\2\2\u02ac\u02ad\7u\2\2\u02ad\u02ae\7g\2\2\u02ae")
        buf.write(u"\u02b0\7v\2\2\u02af\u0299\3\2\2\2\u02af\u02a4\3\2\2\2")
        buf.write(u"\u02b0\u0098\3\2\2\2\u02b1\u02b2\7^\2\2\u02b2\u02b3\7")
        buf.write(u"u\2\2\u02b3\u02b4\7w\2\2\u02b4\u02b5\7d\2\2\u02b5\u02b6")
        buf.write(u"\7u\2\2\u02b6\u02b7\7g\2\2\u02b7\u02b8\7v\2\2\u02b8\u02b9")
        buf.write(u"\7g\2\2\u02b9\u02c4\7s\2\2\u02ba\u02bb\7^\2\2\u02bb\u02bc")
        buf.write(u"\7u\2\2\u02bc\u02bd\7w\2\2\u02bd\u02be\7r\2\2\u02be\u02bf")
        buf.write(u"\7u\2\2\u02bf\u02c0\7g\2\2\u02c0\u02c1\7v\2\2\u02c1\u02c2")
        buf.write(u"\7g\2\2\u02c2\u02c4\7s\2\2\u02c3\u02b1\3\2\2\2\u02c3")
        buf.write(u"\u02ba\3\2\2\2\u02c4\u009a\3\2\2\2\u02c5\u02c6\7^\2\2")
        buf.write(u"\u02c6\u02c7\7p\2\2\u02c7\u02c8\7u\2\2\u02c8\u02c9\7")
        buf.write(u"w\2\2\u02c9\u02ca\7d\2\2\u02ca\u02cb\7u\2\2\u02cb\u02cc")
        buf.write(u"\7g\2\2\u02cc\u02cd\7v\2\2\u02cd\u02ce\7g\2\2\u02ce\u02da")
        buf.write(u"\7s\2\2\u02cf\u02d0\7^\2\2\u02d0\u02d1\7p\2\2\u02d1\u02d2")
        buf.write(u"\7u\2\2\u02d2\u02d3\7w\2\2\u02d3\u02d4\7r\2\2\u02d4\u02d5")
        buf.write(u"\7u\2\2\u02d5\u02d6\7g\2\2\u02d6\u02d7\7v\2\2\u02d7\u02d8")
        buf.write(u"\7g\2\2\u02d8\u02da\7s\2\2\u02d9\u02c5\3\2\2\2\u02d9")
        buf.write(u"\u02cf\3\2\2\2\u02da\u009c\3\2\2\2\u02db\u02dc\7@\2\2")
        buf.write(u"\u02dc\u009e\3\2\2\2\u02dd\u02de\7^\2\2\u02de\u02df\7")
        buf.write(u"p\2\2\u02df\u02e0\7i\2\2\u02e0\u02e1\7v\2\2\u02e1\u02e2")
        buf.write(u"\7t\2\2\u02e2\u00a0\3\2\2\2\u02e3\u02e4\7^\2\2\u02e4")
        buf.write(u"\u02e5\7i\2\2\u02e5\u02e6\7g\2\2\u02e6\u02f1\7s\2\2\u02e7")
        buf.write(u"\u02e8\7^\2\2\u02e8\u02e9\7i\2\2\u02e9\u02ea\7g\2\2\u02ea")
        buf.write(u"\u02eb\7s\2\2\u02eb\u02ec\7u\2\2\u02ec\u02ed\7n\2\2\u02ed")
        buf.write(u"\u02ee\7c\2\2\u02ee\u02ef\7p\2\2\u02ef\u02f1\7v\2\2\u02f0")
        buf.write(u"\u02e3\3\2\2\2\u02f0\u02e7\3\2\2\2\u02f1\u00a2\3\2\2")
        buf.write(u"\2\u02f2\u02f3\7^\2\2\u02f3\u02f4\7p\2\2\u02f4\u02f5")
        buf.write(u"\7i\2\2\u02f5\u02f6\7g\2\2\u02f6\u0302\7s\2\2\u02f7\u02f8")
        buf.write(u"\7^\2\2\u02f8\u02f9\7p\2\2\u02f9\u02fa\7i\2\2\u02fa\u02fb")
        buf.write(u"\7g\2\2\u02fb\u02fc\7s\2\2\u02fc\u02fd\7u\2\2\u02fd\u02fe")
        buf.write(u"\7n\2\2\u02fe\u02ff\7c\2\2\u02ff\u0300\7p\2\2\u0300\u0302")
        buf.write(u"\7v\2\2\u0301\u02f2\3\2\2\2\u0301\u02f7\3\2\2\2\u0302")
        buf.write(u"\u00a4\3\2\2\2\u0303\u0304\7#\2\2\u0304\u00a6\3\2\2\2")
        buf.write(u"\u0305\u0307\7^\2\2\u0306\u0308\t\3\2\2\u0307\u0306\3")
        buf.write(u"\2\2\2\u0308\u0309\3\2\2\2\u0309\u0307\3\2\2\2\u0309")
        buf.write(u"\u030a\3\2\2\2\u030a\u031c\3\2\2\2\u030b\u0312\7^\2\2")
        buf.write(u"\u030c\u030e\t\3\2\2\u030d\u030c\3\2\2\2\u030e\u030f")
        buf.write(u"\3\2\2\2\u030f\u030d\3\2\2\2\u030f\u0310\3\2\2\2\u0310")
        buf.write(u"\u0313\3\2\2\2\u0311\u0313\t\5\2\2\u0312\u030d\3\2\2")
        buf.write(u"\2\u0312\u0311\3\2\2\2\u0313\u031c\3\2\2\2\u0314\u0316")
        buf.write(u"\t\3\2\2\u0315\u0314\3\2\2\2\u0316\u0317\3\2\2\2\u0317")
        buf.write(u"\u0315\3\2\2\2\u0317\u0318\3\2\2\2\u0318\u0319\3\2\2")
        buf.write(u"\2\u0319\u031a\7^\2\2\u031a\u031c\t\6\2\2\u031b\u0305")
        buf.write(u"\3\2\2\2\u031b\u030b\3\2\2\2\u031b\u0315\3\2\2\2\u031c")
        buf.write(u"\u00a8\3\2\2\2\36\2\u00ac\u00df\u00ff\u01e6\u01f1\u01ff")
        buf.write(u"\u0207\u0209\u0212\u021b\u0221\u022b\u0232\u0234\u026f")
        buf.write(u"\u0287\u0297\u02af\u02c3\u02d9\u02f0\u0301\u0309\u030f")
        buf.write(u"\u0312\u0317\u031b\3\b\2\2")
        return buf.getvalue()


class LaTeXLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    WS = 1
    ADD = 2
    SUB = 3
    MUL = 4
    DIV = 5
    L_PAREN = 6
    R_PAREN = 7
    L_BRACE = 8
    R_BRACE = 9
    L_BRACKET = 10
    R_BRACKET = 11
    COLON = 12
    RIGHTARROW = 13
    LONGRIGHTARROW = 14
    BAR = 15
    FUNC_LIM = 16
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
    CMD_BINOM = 45
    CMD_DBINOM = 46
    CMD_TBINOM = 47
    CMD_MATHIT = 48
    UNDERSCORE = 49
    CARET = 50
    AMPERSAND = 51
    COMMA = 52
    LEFT = 53
    RIGHT = 54
    DOT = 55
    RM = 56
    DIFFERENTIAL = 57
    LETTER = 58
    NUMBER = 59
    EQUAL = 60
    DOTEQ = 61
    EQUIV = 62
    APPROX = 63
    CONG = 64
    SIMEQ = 65
    SIM = 66
    PROPTO = 67
    NEQ = 68
    LT = 69
    NLESS = 70
    LTE = 71
    PROPERSUBSET = 72
    NOTPROPERSUBSET = 73
    SUBSET = 74
    NOTSUBSET = 75
    GT = 76
    NGTR = 77
    GTE = 78
    NGEQ = 79
    BANG = 80
    SYMBOL = 81

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ u"DEFAULT_MODE" ]

    literalNames = [ u"<INVALID>",
            u"'+'", u"'-'", u"'*'", u"'/'", u"'('", u"')'", u"'{'", u"'}'", 
            u"'['", u"']'", u"':'", u"'|'", u"'\\lim'", u"'\\int'", u"'\\sum'", 
            u"'\\prod'", u"'\\log'", u"'\\ln'", u"'\\sin'", u"'\\cos'", 
            u"'\\tan'", u"'\\csc'", u"'\\sec'", u"'\\cot'", u"'\\arcsin'", 
            u"'\\arccos'", u"'\\arctan'", u"'\\arccsc'", u"'\\arcsec'", 
            u"'\\arccot'", u"'\\sinh'", u"'\\cosh'", u"'\\tanh'", u"'\\arsinh'", 
            u"'\\arcosh'", u"'\\artanh'", u"'\\sqrt'", u"'\\times'", u"'\\cdot'", 
            u"'\\div'", u"'\\frac'", u"'\\binom'", u"'\\dbinom'", u"'\\tbinom'", 
            u"'\\mathit'", u"'_'", u"'^'", u"'&'", u"','", u"'.'", u"'\\rm'", 
            u"'='", u"'\\doteq'", u"'\\equiv'", u"'\\approx'", u"'\\cong'", 
            u"'\\simeq'", u"'\\sim'", u"'\\propto'", u"'<'", u"'\\nless'", 
            u"'>'", u"'\\ngtr'", u"'!'" ]

    symbolicNames = [ u"<INVALID>",
            u"WS", u"ADD", u"SUB", u"MUL", u"DIV", u"L_PAREN", u"R_PAREN", 
            u"L_BRACE", u"R_BRACE", u"L_BRACKET", u"R_BRACKET", u"COLON", 
            u"RIGHTARROW", u"LONGRIGHTARROW", u"BAR", u"FUNC_LIM", u"FUNC_INT", 
            u"FUNC_SUM", u"FUNC_PROD", u"FUNC_LOG", u"FUNC_LN", u"FUNC_SIN", 
            u"FUNC_COS", u"FUNC_TAN", u"FUNC_CSC", u"FUNC_SEC", u"FUNC_COT", 
            u"FUNC_ARCSIN", u"FUNC_ARCCOS", u"FUNC_ARCTAN", u"FUNC_ARCCSC", 
            u"FUNC_ARCSEC", u"FUNC_ARCCOT", u"FUNC_SINH", u"FUNC_COSH", 
            u"FUNC_TANH", u"FUNC_ARSINH", u"FUNC_ARCOSH", u"FUNC_ARTANH", 
            u"FUNC_SQRT", u"CMD_TIMES", u"CMD_CDOT", u"CMD_DIV", u"CMD_FRAC", 
            u"CMD_BINOM", u"CMD_DBINOM", u"CMD_TBINOM", u"CMD_MATHIT", u"UNDERSCORE", 
            u"CARET", u"AMPERSAND", u"COMMA", u"LEFT", u"RIGHT", u"DOT", 
            u"RM", u"DIFFERENTIAL", u"LETTER", u"NUMBER", u"EQUAL", u"DOTEQ", 
            u"EQUIV", u"APPROX", u"CONG", u"SIMEQ", u"SIM", u"PROPTO", u"NEQ", 
            u"LT", u"NLESS", u"LTE", u"PROPERSUBSET", u"NOTPROPERSUBSET", 
            u"SUBSET", u"NOTSUBSET", u"GT", u"NGTR", u"GTE", u"NGEQ", u"BANG", 
            u"SYMBOL" ]

    ruleNames = [ u"WS", u"ADD", u"SUB", u"MUL", u"DIV", u"L_PAREN", u"R_PAREN", 
                  u"L_BRACE", u"R_BRACE", u"L_BRACKET", u"R_BRACKET", u"COLON", 
                  u"RIGHTARROW", u"LONGRIGHTARROW", u"BAR", u"FUNC_LIM", 
                  u"FUNC_INT", u"FUNC_SUM", u"FUNC_PROD", u"FUNC_LOG", u"FUNC_LN", 
                  u"FUNC_SIN", u"FUNC_COS", u"FUNC_TAN", u"FUNC_CSC", u"FUNC_SEC", 
                  u"FUNC_COT", u"FUNC_ARCSIN", u"FUNC_ARCCOS", u"FUNC_ARCTAN", 
                  u"FUNC_ARCCSC", u"FUNC_ARCSEC", u"FUNC_ARCCOT", u"FUNC_SINH", 
                  u"FUNC_COSH", u"FUNC_TANH", u"FUNC_ARSINH", u"FUNC_ARCOSH", 
                  u"FUNC_ARTANH", u"FUNC_SQRT", u"CMD_TIMES", u"CMD_CDOT", 
                  u"CMD_DIV", u"CMD_FRAC", u"CMD_BINOM", u"CMD_DBINOM", 
                  u"CMD_TBINOM", u"CMD_MATHIT", u"UNDERSCORE", u"CARET", 
                  u"AMPERSAND", u"COMMA", u"LEFT", u"RIGHT", u"DOT", u"RM", 
                  u"WS_CHAR", u"DIFFERENTIAL", u"LETTER", u"DIGIT", u"NUMBER", 
                  u"EQUAL", u"DOTEQ", u"EQUIV", u"APPROX", u"CONG", u"SIMEQ", 
                  u"SIM", u"PROPTO", u"NEQ", u"LT", u"NLESS", u"LTE", u"PROPERSUBSET", 
                  u"NOTPROPERSUBSET", u"SUBSET", u"NOTSUBSET", u"GT", u"NGTR", 
                  u"GTE", u"NGEQ", u"BANG", u"SYMBOL" ]

    grammarFileName = u"LaTeX.g4"

    def __init__(self, input=None, output=sys.stdout):
        super(LaTeXLexer, self).__init__(input, output=output)
        self.checkVersion("4.7.1")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


