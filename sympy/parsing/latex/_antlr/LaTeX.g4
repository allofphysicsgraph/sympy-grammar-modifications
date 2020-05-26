grammar LaTeX;		
prog:	(expr NEWLINE)* ;
expr:	expr (MUL|DIV) expr
    |	expr (ADD|SUBTRACT) expr
    |	number
    |	L_PAREN expr R_PAREN
    |   L_BRACE expr R_BRACE
    |   L_BRACKET expr R_BRACKET
    ;

ADD: '+';
SUBTRACT: '-';
CARET: '^';
MUL: '*';
DIV: '/';
AMPERSAND: '&';

NEWLINE : [\r\n]+ ;
INT     : [0-9]+ ;
//Real number as defined in CFITSIO Lexical Parser
FLOAT:   ([0-9]*[.][0-9]+)
        |([0-9]*[.]*[0-9]+[eEdD][+-]?[0-9]+)
        |([0-9]*[.])
        ;

number:
    INT
    | FLOAT;

L_PAREN: '(';
R_PAREN:  ')';
L_BRACE:  '{';
R_BRACE: '}';
L_BRACKET: '[';
R_BRACKET: ']';

