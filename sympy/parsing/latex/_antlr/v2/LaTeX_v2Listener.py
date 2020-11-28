# Generated from LaTeX_v2.g4 by ANTLR 4.7.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .LaTeX_v2Parser import LaTeX_v2Parser
else:
    from LaTeX_v2Parser import LaTeX_v2Parser

# This class defines a complete listener for a parse tree produced by LaTeX_v2Parser.
class LaTeX_v2Listener(ParseTreeListener):

    # Enter a parse tree produced by LaTeX_v2Parser#expression.
    def enterExpression(self, ctx:LaTeX_v2Parser.ExpressionContext):
        from pudb import set_trace
        set_trace()
        pass

    # Exit a parse tree produced by LaTeX_v2Parser#expression.
    def exitExpression(self, ctx:LaTeX_v2Parser.ExpressionContext):
        pass

x = LaTeX_v2Parser('1')

