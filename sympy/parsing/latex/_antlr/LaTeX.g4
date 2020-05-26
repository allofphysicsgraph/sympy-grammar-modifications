grammar LaTeX;		
prog:	(expr NEWLINE)* ;
expr:	expr (MUL|DIV) expr
    |	expr (ADD|SUBTRACT) expr
    |	number
    |	L_PAREN expr R_PAREN
    |   L_BRACE expr R_BRACE
    |   L_BRACKET expr R_BRACKET
    |   BEGIN_ARRAY expr END_ARRAY
    |   BEGIN_SUBEQUATIONS  expr END_SUBEQUATIONS
    |   BEGIN_SPLIT expr END_SPLIT
    |   BEGIN_EQUATION expr END_EQUATION
    |   BEGIN_EQNARRAY expr END_EQNARRAY
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



//Handle simple begin end expressions
ARRAY: L_BRACE 'array' R_BRACE ;
SUBEQUATIONS: L_BRACE 'subequations' R_BRACE;
SPLIT: L_BRACE 'split' R_BRACE;
EQUATION: L_BRACE 'equation' R_BRACE ;
EQNARRAY: L_BRACE 'eqnarray' R_BRACE;

BEGIN_ARRAY: '\\begin' ARRAY;
END_ARRAY: '\\end' ARRAY;

BEGIN_SUBEQUATIONS: '\\begin' SUBEQUATIONS;
END_SUBEQUATIONS: '\\end' SUBEQUATIONS;

BEGIN_SPLIT: '\\begin' SPLIT;
END_SPLIT: '\\end' SPLIT;

BEGIN_EQUATION: '\\begin' EQUATION;
END_EQUATION: '\\end' EQUATION;

BEGIN_EQNARRAY: '\\begin' EQNARRAY;
END_EQNARRAY: '\\end' EQNARRAY;

