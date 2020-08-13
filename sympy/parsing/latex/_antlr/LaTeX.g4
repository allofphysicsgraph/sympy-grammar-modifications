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

grammar LaTeX;

options {
    language=Python2;
}

WS: [ \t\r\n]+ -> skip;

IGNORE:
    ('\\vrule'
    |    '\\quad'
    |    '\\hfil'
    |    '\\quad'
    |    '\\vcenter'
    |    '\\vbox'
    |    '\\vskip'
    |    '\\vspace'
    |	'\\left'
	|	'\\right'
    |	'\\thinspace'
	|	'\\medspace'
	|	'\\thickspace'
	|	'\\negmedspace'
	|	'\\negthickspace'
	|	'\\negthinspace'
	|   '\\*'
    |   '\\,'
    |   '\\-'
    |   '\\.'
    |   '\\/'
    |   '\\;'
    |   '\\!'
    |   '\\"'
    |   '\\('
    |   '\\,'
    |   '\\-'
    |   '\\.'
    |   '\\:'
    |   '\\='
    ) -> skip;



ADD: '+';
SUB: '-';
MUL: '*'|'\\ ';
DIV: '/';

L_PAREN: '(';
R_PAREN: ')';
L_BRACE: '{';
R_BRACE: '}';
L_BRACE_LITERAL: '\\{';
R_BRACE_LITERAL: '\\}';
L_BRACKET: '[';
R_BRACKET: ']';

BAR: '|';

FUNC_LIM:  '\\lim';
LIM_APPROACH_SYM: '\\to' | '\\rightarrow' | '\\Rightarrow' | '\\longrightarrow' | '\\Longrightarrow';
FUNC_INT:  '\\int';
FUNC_SUM:  '\\sum';
FUNC_PROD: '\\prod';




FUNC_EXP:  '\\exp';
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
COLON: ':';

fragment WS_CHAR: [ \t\r\n];
DIFFERENTIAL: 'd' ('x'|'y'|'t');

//LETTER: [a-zA-Z];
//fragment DIGIT: [0-9];

INT     : [0-9]+ ;
//Real number as defined in CFITSIO Lexical Parser
FLOAT:   ([0-9]*[.][0-9]+)
        |([0-9]*[.]*[0-9]+[eEdD][+-]?[0-9]+)
        |([0-9]*[.])
        ;

number:
    INT     #   integer
    | FLOAT #   float
    ;


EQUAL: '=';
LT: '<';
LTE: '\\leq';
GT: '>';
GTE: '\\geq';

BANG: '!';



binary_operators:
     '\\Cap'
|    '\\Cup'
|    '\\barwedge'
|    '\\boxdot'
|    '\\boxminus'
|    '\\boxplus'
|    '\\boxtimes'
|    '\\centerdot'
|    '\\circledast'
|    '\\circledcirc'
|    '\\circleddash'
|    '\\curlyvee'
|    '\\curlywedge'
|    '\\divideontimes'
|    '\\dotplus'
|    '\\doublebarwedge'
|    '\\intercal*'
|    '\\leftthreetimes'
|    '\\ltimes'
|    '\\rightthreetimes'
|    '\\rtimes'
|    '\\smallsetminus'
|    '\\veebar'
;

negated_binary_relations:
'\\ncong'
| '\\nmid'
| '\\nparallel'
| '\\nprec'
| '\\npreceq'
| '\\nshortmid'
| '\\nshortparallel'
| '\\nsim'
| '\\nsucc'
| '\\nsucceq'
| '\\nvdash'
| '\\nvDash'
| '\\nVDash'
| '\\precnapprox'
| '\\precnsim'
| '\\succnapprox'
| '\\succnsim'
;

subset_superset:
     '\\Subset'
|    '\\Supset'
|    '\\nsubseteq'
|    '\\nsupseteq'
|    '\\nsupseteqq'
|    '\\sqsubset'
|    '\\sqsupset'
|    '\\subseteqq'
|    '\\subsetneq'
|    '\\subsetneqq'
|    '\\supseteqq'
|    '\\supsetneq'
|    '\\supsetneqq'
|    '\\varsubsetneq'
|    '\\varsubsetneqq'
|    '\\varsupsetneq'
|    '\\varsupsetneqq'
;

triangle_relations:
     '\\blacktriangleleft'
|    '\\blacktriangleright'
|    '\\ntriangleleft'
|    '\\ntrianglelefteq'
|    '\\ntriangleright'
|    '\\ntrianglerighteq'
|    '\\trianglelefteq'
|    '\\triangleq'
|    '\\trianglerighteq'
|    '\\vartriangleleft'
|    '\\vartriangleright'
;


arrows:
     '\\Lleftarrow'
|    '\\Lsh'
|    '\\Rsh'
|    '\\circlearrowleft'
|    '\\circlearrowright'
|    '\\curvearrowleft'
|    '\\curvearrowright'
|    '\\dashleftarrow'
|    '\\dashrightarrow'
|    '\\downdownarrows'
|    '\\leftarrowtail'
|    '\\leftleftarrows'
|    '\\leftrightarrows'
|    '\\leftrightsquigarrow'
|    '\\looparrowleft'
|    '\\looparrowright'
|    '\\rightarrowtail'
|    '\\rightleftarrows'
|    '\\rightrightarrows'
|    '\\rightsquigarrow'
|    '\\twoheadleftarrow'
|    '\\twoheadrightarrow'
|    '\\upuparrows'
;
negated_arrows:
     '\\nLeftarrow'
|    '\\nLeftrightarrow'
|    '\\nRightarrow'
|    '\\nleftarrow'
|    '\\nleftrightarrow'
|    '\\nrightarrow'
;


harpoons:
     '\\downharpoonleft'
|    '\\downharpoonright'
|    '\\leftrightharpoons'
|    '\\rightleftharpoons'
|    '\\upharpoonleft'
|    '\\upharpoonright'
;


SYMBOL:
	 	 '\\varepsilon'
	 | 	 'geostationary'
	 | 	 'Schwarzschild'
	 | 	 '\\varUpsilon'
	 | 	 '\\varLambda'
	 | 	 'centripetal'
	 | 	 '\\varDelta'
	 | 	 '\\vargamma'
	 | 	 '\\varGamma'
	 | 	 '\\varkappa'
	 | 	 '\\varOmega'
	 | 	 '\\varsigma'
	 | 	 '\\varSigma'
	 | 	 '\\vartheta'
	 | 	 '\\varTheta'
	 | 	 'atmosphere'
	 | 	 'incoherent'
	 | 	 'Boltzmann'
	 | 	 '\\digamma'
	 | 	 '\\Digamma'
	 | 	 '\\epsilon'
	 | 	 '\\Epsilon'
	 | 	 '\\omicron'
	 | 	 '\\Omicron'
	 | 	 '\\upsilon'
	 | 	 '\\Upsilon'
	 | 	 'refracted'
	 | 	 '\\partial'
	 | 	 'satellite'
	 | 	 'kilogram'
	 | 	 '\\langle'
	 | 	 '\\rangle'
	 | 	 '\\lambda'
	 | 	 '\\Lambda'
	 | 	 '\\varphi'
	 | 	 '\\varPhi'
	 | 	 '\\varPsi'
	 | 	 '\\varrho'
	 | 	 'electron'
	 | 	 'Brewster'
	 | 	 '\\approx'
	 | 	 'coherent'
	 | 	 'Coulomb'
	 | 	 '\\nabla'
	 | 	 '\\alpha'
	 | 	 '\\Alpha'
	 | 	 '\\delta'
	 | 	 '\\Delta'
	 | 	 '\\gamma'
	 | 	 '\\Gamma'
	 | 	 '\\kappa'
	 | 	 '\\Kappa'
	 | 	 '\\omega'
	 | 	 '\\Omega'
	 | 	 '\\sigma'
	 | 	 '\\Sigma'
	 | 	 '\\theta'
	 | 	 '\\Theta'
	 | 	 '\\varpi'
	 | 	 '\\varPi'
	 | 	 '\\varXi'
	 | 	 'Coulumb'
	 | 	 'minutes'
	 | 	 'seconds'
	 | 	 'Rydberg'
	 | 	 'surface'
	 | 	 'gravity'
	 | 	 '\\infty'
	 | 	 '\\rvert'
	 | 	 'Pascal'
	 | 	 '\\hbar'
	 | 	 '\\Zeta'
	 | 	 '\\beta'
	 | 	 '\\Beta'
	 | 	 '\\iota'
	 | 	 '\\Iota'
	 | 	 '\\zeta'
	 | 	 'escape'
	 | 	 'second'
	 | 	 'pounds'
	 | 	 'before'
	 | 	 'Newton'
	 | 	 'Ampere'
	 | 	 '\\circ'
	 | 	 '\\bigg'
	 | 	 'Tesla'
	 | 	 '\\chi'
	 | 	 '\\Chi'
	 | 	 '\\eta'
	 | 	 '\\Eta'
	 | 	 '\\phi'
	 | 	 '\\Phi'
	 | 	 '\\psi'
	 | 	 '\\Psi'
	 | 	 '\\rho'
	 | 	 '\\Rho'
	 | 	 '\\tau'
	 | 	 '\\Tau'
	 | 	 'Earth'
	 | 	 'Joule'
	 | 	 'orbit'
	 | 	 'after'
	 | 	 'hours'
	 | 	 'Gauss'
	 | 	 'meter'
	 | 	 'total'
	 | 	 '\\vec'
	 | 	 '\\hat'
	 | 	 '\\mu'
	 | 	 '\\Mu'
	 | 	 '\\nu'
	 | 	 '\\Nu'
	 | 	 '\\pi'
	 | 	 '\\Pi'
	 | 	 '\\xi'
	 | 	 '\\Xi'
	 | 	 'inch'
	 | 	 'days'
	 | 	 'year'
	 | 	 'hour'
	 | 	 'Volt'
	 | 	 'Watt'
	 | 	 '\\rm'
	 | 	 'ave'
	 | 	 'sec'
	 | 	 'day'
	 | 	 'CKG'
	 | 	 'det'
	 | 	 '\\a'
	 | 	 '\\r'
	 | 	 '\\p'
	 | 	 'km'
	 | 	 '\''
	 | 	 'kg'
	 | 	 'KE'
	 | 	 'PE'
	 | 	 'PV'
	 | 	 'VP'
	 | 	 '>>'
	 | 	 'dp'
	 | 	 'ik'
	 | 	 'dE'
	 | 	 'vn'
	 | 	 'dx'
	 | 	 'dr'
	 | 	 'dt'
	 | 	 'dy'
	 | 	 'Z'
	 | 	 'F'
	 | 	 'n'
	 | 	 'R'
	 | 	 'U'
	 | 	 'C'
	 | 	 'V'
	 | 	 's'
	 | 	 'P'
	 | 	 'T'
	 | 	 't'
	 | 	 'v'
	 | 	 'y'
	 | 	 'x'
	 | 	 'm'
	 | 	 'A'
	 | 	 'c'
	 | 	 'g'
	 | 	 'Q'
	 | 	 'k'
	 | 	 'B'
	 | 	 'I'
	 | 	 'W'
	 | 	 'd'
	 | 	 'u'
	 | 	 'e'
	 | 	 'p'
	 | 	 'a'
	 | 	 'f'
	 | 	 'K'
	 | 	 'E'
	 | 	 'G'
	 | 	 'i'
	 | 	 'z'
	 | 	 'r'
	 | 	 'S'
	 | 	 'h'
	 | 	 'b'
	 | 	 'l'
	 | 	 'M'
	; 

binary_relations:
 '\\approxeq'
| '\\backepsilon'
| '\\backsim'
| '\\backsimeq'
| '\\because'
| '\\between'
| '\\bumpeq'
| '\\Bumpeq'
| '\\circeq'
| '\\curlyeqprec'
| '\\curlyeqsucc'
| '\\doteqdot'
| '\\eqcirc'
| '\\fallingdotseq'
| '\\multimap'
| '\\pitchfork'
| '\\precapprox'
| '\\preccurlyeq'
| '\\precsim'
| '\\risingdotseq'
| '\\shortmid'
| '\\shortparallel'
| '\\smallfrown'
| '\\smallsmile'
| '\\succapprox'
| '\\succcurlyeq'
| '\\succsim'
| '\\therefore'
| '\\thickapprox'
| '\\thicksim'
| '\\varpropto'
| '\\vDash'
| '\\Vdash'
| '\\Vvdash'
;



math: relation;

relation:
    relation (EQUAL | LT | LTE | GT | GTE) relation
    | expr;

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
    | L_BRACE expr R_BRACE
    | L_BRACE_LITERAL expr R_BRACE_LITERAL;

abs_group: BAR expr BAR;

atom: SYMBOL subexpr? | number| DIFFERENTIAL ;

//mathit: CMD_MATHIT L_BRACE mathit_text R_BRACE;
//mathit_text: LETTER*;

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
    FUNC_EXP | FUNC_LOG | FUNC_LN
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

    | SYMBOL subexpr? // e.g. f(x)
    L_PAREN args R_PAREN

    | FUNC_INT
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
    SYMBOL
    LIM_APPROACH_SYM
    expr (CARET L_BRACE (ADD | SUB) R_BRACE)?
    R_BRACE;

func_arg: expr | (expr ',' func_arg);
func_arg_noparens: mp_nofunc;

subexpr: UNDERSCORE (atom | L_BRACE expr R_BRACE);
supexpr: CARET (atom | L_BRACE expr R_BRACE);

subeq: UNDERSCORE L_BRACE (expr|equality) R_BRACE;
supeq: UNDERSCORE L_BRACE (expr|equality) R_BRACE;
