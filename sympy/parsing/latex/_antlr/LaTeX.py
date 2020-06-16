from antlr4 import *
from LaTeXLexer import LaTeXLexer
from LaTeXParser import LaTeXParser
from LaTeXVisitor import LaTeXVisitor
from sys import argv

#https://github.com/AkiraHakuta/antlr4_tex2sym.git
# from https://github.com/antlr/antlr4/blob/master/runtime/Python3/bin/pygrun
# this is a python version of TestRig
def beautify_lisp_string(in_string):
    indent_size = 3
    add_indent = ' '*indent_size
    out_string = in_string[0]  # no indent for 1st (
    indent = ''
    for i in range(1, len(in_string)):
        if in_string[i] == '(' and in_string[i+1] != ' ':
            indent += add_indent
            out_string += "\n" + indent + '('
        elif in_string[i] == ')':
            out_string += ')'
            if len(indent) > 0:
                indent = indent.replace(add_indent, '', 1)
        else:
            out_string += in_string[i]
    return out_string
    
class Calc(LaTeXVisitor):
    def __init__(self):
        super().__init__()    
        self.result = ''
        self.id_memory = {}

    def visitInteger(self, ctx):
        return int(ctx.INT().getText()) 
 
    def visitVector(self,ctx):
        import numpy as np
        lst = []
        for ix in ctx.array_1_d().children:
            lst.append(self.visit(ix))
        resp = [ x for x in lst if x]
        print(resp)
        return np.array(resp)

    def visitMul_div(self, ctx):        
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))
        print(type(left))
        if ctx.op.text == '*':
            print(left * right)

  
file_name = argv[1] 
input_stream = FileStream(file_name)
print('input_stream:')
print(input_stream)
print()
lexer = LaTeXLexer(input_stream)
token_stream = CommonTokenStream(lexer)
token_stream.fill()
print('tokens:')
for tk in token_stream.tokens:
    print(tk)
    if '\\n' in str(tk):
        print('\n\n')

print()
parser = LaTeXParser(token_stream)
tree = parser.prog()

print('tree:')
lisp_tree_str = tree.toStringTree(recog=parser)
print(beautify_lisp_string(lisp_tree_str))
print()

print('calc:')
calc = Calc()
result = calc.visit(tree)

print()
print('result:')
print(result)
