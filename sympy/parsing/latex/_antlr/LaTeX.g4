grammar LaTeX;		
prog:	(expr NEWLINE?)* ;

expr:	
    <assoc=right> expr EXPO expr # exponent
    |   expr op=(MUL|DIV) expr     # mul_div
    |	expr op=(ADD|SUBTRACT) expr    # add_sub
    |   array_1_d # vector
    |	number  #   number_
    |   symbols #   symbols_
    |   frac    #   frac_
    |   common_functions    # common_functions_  
    |   expr UNDERSCORE expr    # underscore_
    |   expr relation_operators expr    #   relation_operators_   
    |   TRIG_FUNCTIONS  # trig_functions_
    |	L_PAREN expr R_PAREN    # l_paren_
    |   L_BRACE expr R_BRACE    # sss   
    |   L_BRACKET expr R_BRACKET    # sssss 
    |   BEGIN_ARRAY expr END_ARRAY  # array
    |   BEGIN_SUBEQUATIONS  expr END_SUBEQUATIONS # aaaa    
    |   BEGIN_SPLIT expr END_SPLIT  # begin_split_
    |   BEGIN_EQUATION expr END_EQUATION    # begin_eq_
    |   BEGIN_EQNARRAY expr END_EQNARRAY    # being_eqnarray
    ;


array_1_d:
    '[' number (',' number)* ']'
    ;



WS: [ \t\r]+ -> skip;

maybe_common:
     '\\tau(\\phi)'
    |	'\\alpha(2)'
    |	'\\alpha(z)'
    |	'\\Delta(k)'
    |	'\\ep(q_0)'
    |	'\\mu(k)'
    |	'\\rho(0)'
    |	'\\sigma(y)'
    |	'\\epsilon(p_0)'
    |	'\\rho(\\lambda)'
    |	'\\rho(r)'
    |	'\\gamma(1)'
    |	'\\mu(\\tau)'
    |	'\\phi(t)'
    |	'\\prime(\\tau)'
    |	'\\psi(r)'
    |	'\\Lambda(x)'
    |	'\\L(H)'
    |	'\\varphi(r)'
    |	'\\lambda(x)'
    |	'\\omega(z)'
    |	'\\chi(x)'
    |	'\\kappa(n)'
    |	'\\dagger(x)'
    |	'\\phi(y)'
    |	'\\rho(\\sigma)'
    |	'\\U(1)'
    |	'\\eta(q)'
    |	'\\Psi(x)'
    |	'\\Phi(0)'
    |	'\\omega(x)'
    |	'\\Spin(7)'
    |	'\\phi(z)'
    |	'\\SU(3)'
    |	'\\delta(x)'
    |	'\\gamma(k)'
    |	'\\alpha(m)'
    |	'\\psi(p)'
    |	'\\iota(\\lie{h})'
    |	'\\phi(f)'
    |	'\\vector(0,1)'
    |	'\\U(N)'
    |	'\\rho(x)'
    |	'\\sigma(x)'
    |	'\\Phi(x)'
    |	'\\psi(z)'
    |  	'\\dagger(x)'
    |  	'\\om(z)'
    |  	'\\chi(z)'
    |  	'\\delta(x-y)'
    |  	'\\varphi(x)'
    |  	'\\alpha(x)'
    |  	'\\eta(\\tau)'
    |  	'\\Phi(\\theta)'
    |  	'\\psi(x)'
    |	'\\delta(y)'
    |	'\\lambda(s)'
    |	'\\Phi(z)'
    |	'\\Gamma(s)'
    |	'\\SU(2)'
    |	'\\alpha(1)'
    |	'\\psi(x)'
    |	'\\mu(x)'
    |	'\\phi(x)'
    |	'\\Gamma(\\theta)'
    |   '\\int'
    |   '\\varGamma'
    |   '\\varind'
    |   '\\varLambda'
    |   '\\varOmega'
    |   '\\varphi'
    |   '\\varPhi'
    |   '\\varpi'
    |   '\\varPi'
    |   '\\varpir'
    |   '\\varPsi'
    |   '\\varrho'
    |   '\\varsigma'
    ;



common_functions:
       '\\sqrt'
    |   '\\log'
    |   '\\ln';


frac: '\\frac' L_BRACE expr R_BRACE L_BRACE expr R_BRACE ;

ADD: '+';
SUBTRACT: '-';
EXPO: '^';
MUL: '*';
DIV: '/';
AMPERSAND: '&';
UNDERSCORE: '_';
COMMA: ',';

NEWLINE : [\r\n]+ ;
INT     : [0-9]+ ;
//Real number as defined in CFITSIO Lexical Parser
FLOAT:   ([0-9]*[.][0-9]+)
        |([0-9]*[.]*[0-9]+[eEdD][+-]?[0-9]+)
        |([0-9]*[.])
        ;
BAR: '|';

number:
    INT     #   integer
    | FLOAT #   float
    ;

prime: EXPO'\\prime'
    |'\'';

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

relation_operators:
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

TILDE: '~'
    |   '\\tilde';
    
maybe_remove:
    '\\textrm';

 
symbols:

    '\\la'
    |   '\\ell'
    |   'T'
    |   'CKG'
    |   '\\perp'
    |   'dp'
    |   'det'
    |   'ik'
    |   '\\tV'
    |   '\\tX'
    |   'dE'
    |   'M'
    |   'p'
    |   '\\tj'
    |   'x'
    |   'y'
    |   'z'
    |   'v'
    |   'y'
    |   't'
    |   'T'
    |   'r'
    |   'b'
    |   'm'
    |   's'
    |   'n'
    |   'g'
    |   'p'
    |   'q'
    |   'e'
    |   'p'
    |   'q'
    |   'g'
    |   'a'
    |   'R'
    |   'vn'
    |   'W'
    |   'd'
    |   'k'
    |   'R'
    |   'z'
    |   'r'
    |   'C'
    |   'c'
    |   'V'
    |   'L'
    |   'S'
    |   'J'
    |   'i'
    |   'n'
    |   'N'
    |   'k'
    |   'K'
    |   '\\partial'
    |   '\\a'
    |   '\\r'
    |   'A'
    |   'dp'
    |   '\\cal'
    |   '\\exp'
    |   '\\rm'
    |   '\\Bar'
    |   '\\p'
    |   '\\del'
    |   '\\wt'
    |   'G'
    |   'dx'
    |   'dr'
    |   'dt'
    |   'dy'
    |   '\\cdot'
    |   '\\dot'
    |   '\\langle'
    |   '\\rangle'
    |   '\\adot'
    |   '\\xdot'
    |   TILDE
    |   ADD
    |   SUBTRACT
    |   GREEK
    |   BANG
    |   symbols prime;
    

BANG: '!';

TRIG_FUNCTIONS:
    '\\sin'
    |   '\\cos'
    |   '\\tan'
    |   '\\tanh'
    |   '\\coth'
    |   '\\sinh';



L_PAREN: '(';
R_PAREN:  ')';
L_BRACE:  '{';
R_BRACE: '}';
L_BRACKET: '[';
R_BRACKET: ']';


PLUS_OR_MINUS: '\\pm';

//Set Notation
MULTISET_ADDITION: '\\uplus';
EMPTY_SET:      '\\varnothing';
SET_OF_NATURAL_NUMBERS: '\\N';
SET_OF_INTEGERS:        '\\Z';
SET_OF_RATIONAL_NUMBERS:        '\\Q';
SET_OF_ALGEBRAIC_NUMBERS:       '\\mathbb';
SET_OF_REAL_NUMBERS:    '\\R';
SET_OF_COMPLEX_NUMBERS: '\\C';
IS_MEMBER_OF:   '\\in';
IS_NOT_MEMBER_OF:       '\\notin';
SET_UNION:      '\\cup';
SET_INTERSECTION:       '\\cap';
SET_DIFFERENCE: '\\setminus';


//Arrows
RIGHTARROW:      '\\rightarrow'|'\\to'|'\\Rightarrow';
LONGRIGHTARROW:  '\\longrightarrow' |'\\Longrightarrow';
MAPSTO:  '\\mapsto';
LONGMAPSTO:      '\\longmapsto';
LEFTARROW:       '\\leftarrow'|'\\gets'|'\\Leftarrow';
LONGLEFTARROW:   '\\longleftarrow'|'\\Longleftarrow';
UPARROW:         '\\uparrow'|'\\Uparrow';
DOWNARROW:       '\\downarrow'|'\\Downarrow';
UPDOWNARROW:     '\\updownarrow'|'\\Updownarrow';


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


IGNORE:
    ('\\vrule'|'\\quad'|'\\hfil'|'\\quad'|'\\vcenter'|'\\vbox'|'\\vskip'|'\\vspace') -> skip;