/*
  ANTLR4 LaTeX Math Grammar

  Ported from latex2sympy by @augustt198
  https://github.com/augustt198/latex2sympy
  See license in LICENSE.txt
*/

/*
  After changing this file, it is necessary to run `python setup.py antlr`
  in the root directory of the repository. This will regenerate the code in
  `sympy/parsing/latex/_antlr/*.py`.
*/


/*
References:
    https://oeis.org/wiki/List_of_LaTeX_mathematical_symbols

 */



grammar LaTeX;

options {
    language=Python3;
}

WS: [ \t\r\n]+ -> skip;


TOBEADDED:  '\\over'
    |   '\\angle'
    |   '\\arg'
    |   '\\ast'
    |   '\\asymp'
    |   '\\because'
    |   '\\ddots'
    |   '\\deg'
    |   '\\det'
    |   '\\dim'
    |   '\\exists'
    |   '\\forall'
    |   '\\gcd'
    |   '\\iff'
    |   '\\Im'
    |   '\\implies'
    |   '\\inf'
    |   '\\infty'
    |   '\\ldots'
    |   '\\lnot'
    |   '\\nabla'
    |   '\\partial'
    |   '\\prec'
    |   '\\preceq'
    |   '\\prime'
    |   '\\sqcap'
    |   '\\sqcup'
    |   '\\sqsubset'
    |   '\\sqsubseteq'
    |   '\\sqsupset'
    |   '\\sqsupseteq'
    |   '\\star'
    |   '\\succ'
    |   '\\succeq'
    |   '\\sup'
    |   '\\therefore'
    |   '\\vdash'
    |   '\\vdots';

common_functions:
    |   '\\delta(x)'
    |   '\\rho(x)'
    |   'T(x)'
    |   'A(x)'
    |   'F(x)'
    |   'U(x)'
    |   '\\lambda(x)'
    |   'P(x)'
    |   '\\phi(x)'
    |   '\\alpha(x)'
    |   '\\Phi(x)'
    |   '\\varphi_i(x)'
    |   'h(x)'
    |   '\\psi(x)'
    |   'S(x)'
    |   'P_N(x)'
    |   'z(x)'
    |   'f(x)'
    |   'V(x)'
    |   '\\delta\\sigma(x)'
    |   'g(x)'
    |   '\\phi(x)'
    |   'm(x)'
    |   'V(x)'
    |   'W(x)'
    |   'T(x)'
    |   '\\psi^\\dagger(x)'
    |   'g(x)'
    |   '\\phi(x)'
    |   'P_N(x)' 
    |   'f(x)'
    |   '\\psi(x)';


GREEK:  '\\Alpha'
    |	 '\\Beta'
    |	 '\\Chi'
    |	 '\\Delta'
    |	 '\\Digamma'
    |	 '\\Epsilon'
    |	 '\\Eta'
    |	 '\\Gamma'
    |	 '\\Iota'
    |	 '\\Kappa'
    |	 '\\Lambda'
    |	 '\\Mu'
    |	 '\\Nu'
    |	 '\\Omega'
    |	 '\\Omicron'
    |	 '\\Phi'
    |	 '\\Pi'
    |	 '\\Psi'
    |	 '\\Rho'
    |	 '\\Sigma'
    |	 '\\Tau'
    |	 '\\Theta'
    |	 '\\Upsilon'
    |	 '\\Xi'
    |	 '\\Zeta'
    |	 '\\alpha'
    |	 '\\beta'
    |	 '\\chi'
    |	 '\\delta'
    |	 '\\digamma'
    |	 '\\epsilon'
    |	 '\\eta'
    |	 '\\gamma'
    |	 '\\iota'
    |	 '\\kappa'
    |	 '\\lambda'
    |	 '\\mu'
    |	 '\\nu'
    |	 '\\omega'
    |	 '\\omicron'
    |	 '\\phi'
    |	 '\\pi'
    |	 '\\psi'
    |	 '\\rho'
    |	 '\\sigma'
    |	 '\\tau'
    |	 '\\theta'
    |	 '\\upsilon'
    |	 '\\varepsilon'
    |	 '\\vargamma'
    |	 '\\varkappa'
    |	 '\\varphi'
    |	 '\\varpi'
    |	 '\\varrho'
    |	 '\\varsigma'
    |	 '\\vartheta'
    |	 '\\xi'
    |	 '\\zeta';


RIGHTARROW:	 '\\rightarrow'|'\\to'|'\\Rightarrow';
LONGRIGHTARROW:	 '\\longrightarrow' |'\\Longrightarrow';
MAPSTO:	 '\\mapsto';
LONGMAPSTO:	 '\\longmapsto';
LEFTARROW:	 '\\leftarrow'|'\\gets'|'\\Leftarrow';
LONGLEFTARROW:	 '\\longleftarrow'|'\\Longleftarrow';
UPARROW:	 '\\uparrow'|'\\Uparrow';
DOWNARROW:	 '\\downarrow'|'\\Downarrow';
UPDOWNARROW:	 '\\updownarrow'|'\\Updownarrow';



ADD: '+';
SUB: '-';
MUL: '*';
DIV: '/';

L_PAREN: '(';
R_PAREN: ')';
L_BRACE: '{';
R_BRACE: '}';
L_BRACKET: '[';
R_BRACKET: ']';
COLON: ':';
BACKSLASH:	 '\\backslash';
L_ANGLE:	 '\\langle';
R_ANGLE:	 '\\rangle';
L_CEIL:	 '\\lceil';
R_CEIL:	 '\\rceil';
L_FLOOR:	 '\\lfloor';
R_FLOOR:	 '\\rfloor';
UL_CORNER:	 '\\ulcorner';
UR_CORNER:	 '\\urcorner';
LL_CORNER:	 '\\llcorner';
LR_CORNER:	 '\\lrcorner';


DELIMITERS: L_PAREN
    |   R_PAREN
    |   L_BRACE
    |   R_BRACE
    |   L_BRACKET
    |   R_BRACKET
    |   COLON
    |   BACKSLASH
    |   L_ANGLE
    |   R_ANGLE
    |   L_CEIL
    |   R_CEIL
    |   L_FLOOR
    |   R_FLOOR
    |   UL_CORNER
    |   UR_CORNER
    |   LL_CORNER
    |   LR_CORNER;


BAR: '|';

FUNC_LIM:  '\\lim';
//LIM_APPROACH_SYM: '\\to' | '\\rightarrow' | '\\Rightarrow' | '\\longrightarrow' | '\\Longrightarrow';
LIM_APPROACH_SYM:   RIGHTARROW    |   LONGRIGHTARROW;
FUNC_INT:  '\\int';
FUNC_SUM:  '\\sum';
FUNC_PROD: '\\prod';

FUNC_LOG:  '\\log';
FUNC_LN:   '\\ln';
FUNC_SIN:  '\\sin';
FUNC_COS:  '\\cos';
FUNC_TAN:  '\\tan';
FUNC_CSC:  '\\csc';
FUNC_SEC:  '\\sec';
FUNC_COT:  '\\cot';


FUNC_ARCSIN: '\\arcsin';
FUNC_ARCCOS: '\\arccos';
FUNC_ARCTAN: '\\arctan';
FUNC_ARCCSC: '\\arccsc';
FUNC_ARCSEC: '\\arcsec';
FUNC_ARCCOT: '\\arccot';

FUNC_SINH: '\\sinh';
FUNC_COSH: '\\cosh';
FUNC_TANH: '\\tanh';
FUNC_ARSINH: '\\arsinh';
FUNC_ARCOSH: '\\arcosh';
FUNC_ARTANH: '\\artanh';

FUNC_SQRT: '\\sqrt';

CMD_TIMES: '\\times';
CMD_CDOT:  '\\cdot';
CMD_DIV:   '\\div';
CMD_FRAC:  '\\frac';
CMD_BINOM: '\\binom';
CMD_DBINOM: '\\dbinom';
CMD_TBINOM: '\\tbinom';

CMD_MATHIT: '\\mathit';

UNDERSCORE: '_';
CARET: '^';

AMPERSAND: '&';
COMMA: ',';


ARRAY: L_BRACE 'array' R_BRACE ;
SUBEQUATIONS: L_BRACE 'subequations' R_BRACE;
SPLIT: L_BRACE 'split' R_BRACE;
EQUATION: L_BRACE 'equation' R_BRACE ;
EQNARRAY: L_BRACE 'eqnarray' R_BRACE;

BEGIN: '\\begin' (ARRAY|SUBEQUATIONS|SPLIT|EQUATION|EQNARRAY);
END: '\\end' (ARRAY|SUBEQUATIONS|SPLIT|EQUATION|EQNARRAY);

LEFT: '\\left' (L_BRACE|L_BRACKET)?;
RIGHT: '\\right' (R_BRACE|R_BRACKET)?;
DOT: '.';
RM: '\\rm';


fragment WS_CHAR: [ \t\r\n];
DIFFERENTIAL: 'd' WS_CHAR*? ([a-zA-Z] | '\\' [a-zA-Z]+);

LETTER: [a-zA-Z];
fragment DIGIT: [0-9];
NUMBER:
    DIGIT+ (',' DIGIT DIGIT DIGIT)*
    | DIGIT* (',' DIGIT DIGIT DIGIT)* '.' DIGIT+;

EQUAL: '=';
DOTEQ: '\\doteq';
EQUIV: '\\equiv';
APPROX: '\\approx';
CONG: '\\cong';
SIMEQ: '\\simeq';
SIM: '\\sim';
PROPTO: '\\propto';
NEQ: '\\neq'|'\\ne';
LT: '<';
NLESS: '\\nless';
LTE: '\\leq'|'\\leqslant';
PROPERSUBSET: '\\subset'|'\\supset' ;
NOTPROPERSUBSET: '\\not\\subset'|'\\not\\supset';
SUBSET: '\\subseteq'|'\\supseteq';
NOTSUBSET: '\\nsubseteq'|'\\nsupseteq';
GT: '>';
NGTR: '\\ngtr';
GTE: '\\geq'|'\\geqslant';
NGEQ: '\\ngeq'|'\\ngeqslant';

RELATION_OPERATORS:
    EQUAL 
    |   DOTEQ
    |   EQUIV
    |   APPROX
    |   CONG
    |   SIMEQ
    |   SIM
    |   PROPTO
    |   NEQ
    |   LT
    |   NLESS
    |   LTE
    |   PROPERSUBSET
    |   NOTPROPERSUBSET
    |   SUBSET
    |   NOTSUBSET
    |   GT
    |   NGTR
    |   GTE
    |   NGEQ;



PLUS_OR_MINUS: '\\pm';
MULTISET_ADDITION: '\\uplus';


EMPTY_SET:	'\\varnothing';
SET_OF_NATURAL_NUMBERS:	'\\N';
SET_OF_INTEGERS:	'\\Z';
SET_OF_RATIONAL_NUMBERS:	'\\Q';
SET_OF_ALGEBRAIC_NUMBERS:	'\\mathbb';
SET_OF_REAL_NUMBERS:	'\\R';
SET_OF_COMPLEX_NUMBERS:	'\\C';
IS_MEMBER_OF:	'\\in';
IS_NOT_MEMBER_OF:	'\\notin';
SET_UNION:	'\\cup';
SET_INTERSECTION:	'\\cap';
SET_DIFFERENCE:	'\\setminus';


BANG: '!';

SYMBOL: '\\' [a-zA-Z]+
	|'\\' ([a-zA-Z]+ | [ :;])
	|  [a-zA-Z]+'\\'[,:;]
	|  RM [ ]* [a-z]+
    | GREEK;
 
math: relation;

relation:
    relation RELATION_OPERATORS relation
    | expr
    | BEGIN relation END
    | LEFT (DOT|relation) RIGHT;

equality:
    expr EQUAL expr;

expr: additive;

additive:
    additive (ADD | SUB) additive
    | mp;

// mult part
mp:
    mp (MUL | CMD_TIMES | CMD_CDOT | DIV | CMD_DIV | COLON) mp
    | unary;

mp_nofunc:
    mp_nofunc (MUL | CMD_TIMES | CMD_CDOT | DIV | CMD_DIV | COLON) mp_nofunc
    | unary_nofunc;

unary:
    (ADD | SUB) unary
    | postfix+;

unary_nofunc:
    (ADD | SUB) unary_nofunc
    | postfix postfix_nofunc*;

postfix: exp postfix_op*;
postfix_nofunc: exp_nofunc postfix_op*;
postfix_op: BANG | eval_at;

eval_at:
    BAR (eval_at_sup | eval_at_sub | eval_at_sup eval_at_sub);

eval_at_sub:
    UNDERSCORE L_BRACE
    (expr | equality)
    R_BRACE;

eval_at_sup:
    CARET L_BRACE
    (expr | equality) 
    R_BRACE;

exp:
    exp CARET (atom | L_BRACE expr R_BRACE) subexpr?
    | comp;

exp_nofunc:
    exp_nofunc CARET (atom | L_BRACE expr R_BRACE) subexpr?
    | comp_nofunc;

comp:
    group
    | abs_group
    | func
    | atom
    | frac
    | binom;

comp_nofunc:
    group
    | abs_group
    | atom
    | frac
    | binom;

group:
    L_PAREN expr R_PAREN
    | L_BRACKET expr R_BRACKET
    | L_BRACE expr R_BRACE;

abs_group: BAR expr BAR;

atom: (LETTER | SYMBOL) subexpr? | NUMBER | DIFFERENTIAL | mathit;

mathit: CMD_MATHIT L_BRACE mathit_text R_BRACE;
mathit_text: LETTER*;

frac:
    CMD_FRAC L_BRACE
    upper=expr
    R_BRACE L_BRACE
    lower=expr
    R_BRACE;

binom:
    (CMD_BINOM | CMD_DBINOM | CMD_TBINOM) L_BRACE
    n=expr
    R_BRACE L_BRACE
    k=expr
    R_BRACE;

func_normal:
    FUNC_LOG | FUNC_LN
    | FUNC_SIN | FUNC_COS | FUNC_TAN
    | FUNC_CSC | FUNC_SEC | FUNC_COT
    | FUNC_ARCSIN | FUNC_ARCCOS | FUNC_ARCTAN
    | FUNC_ARCCSC | FUNC_ARCSEC | FUNC_ARCCOT
    | FUNC_SINH | FUNC_COSH | FUNC_TANH
    | FUNC_ARSINH | FUNC_ARCOSH | FUNC_ARTANH;

func:
    func_normal
    (subexpr? supexpr? | supexpr? subexpr?)
    (L_PAREN func_arg R_PAREN | func_arg_noparens)

    | (LETTER | SYMBOL| GREEK) subexpr? // e.g. f(x)
    L_PAREN args R_PAREN

    | FUNC_INT UNDERSCORE?
    (subexpr supexpr | supexpr subexpr)?
    (additive? DIFFERENTIAL | frac | additive)

    | FUNC_SQRT
    (L_BRACKET root=expr R_BRACKET)?
    L_BRACE base=expr R_BRACE

    | (FUNC_SUM | FUNC_PROD)
    (subeq supexpr | supexpr subeq)
    mp
    | FUNC_LIM limit_sub mp;

args: (expr ',' args) | expr;

limit_sub:
    UNDERSCORE L_BRACE
    (LETTER | SYMBOL)

    LIM_APPROACH_SYM
    expr (CARET L_BRACE (ADD | SUB) R_BRACE)?
    R_BRACE;

func_arg: expr | (expr ',' func_arg);
func_arg_noparens: mp_nofunc;

subexpr: UNDERSCORE (atom | L_BRACE expr R_BRACE);
supexpr: CARET (atom | L_BRACE expr R_BRACE);

subeq: UNDERSCORE L_BRACE (expr|equality) R_BRACE;
supeq: UNDERSCORE L_BRACE (expr|equality) R_BRACE;
