from antlr4 import *
from LaTeXLexer import LaTeXLexer
from LaTeXListener import LaTeXListener
from LaTeXParser import LaTeXParser
import sys
from pudb import set_trace
from antlr4.tree.Trees import Trees
class LaTeXPrintListener(LaTeXListener):
    def enterProg(self, ctx):
        pass
        #print("LaTeX: %s" % ctx)

def main():
    inp = StdinStream()
    lexer = LaTeXLexer(inp)
    stream = CommonTokenStream(lexer)
    parser = LaTeXParser(stream)
    tree = parser.prog()
    printer = LaTeXPrintListener()
    walker = ParseTreeWalker()
    walker.walk(printer, tree)
    tree_out = Trees.toStringTree(tree, None, parser)
    print(tree_out)
if __name__ == '__main__':
    main()
