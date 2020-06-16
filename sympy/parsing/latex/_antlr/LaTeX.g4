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
    |   letter_like_symbols  # letter_like_symbols_
    |   common_functions    # common_functions_ 
    |   maybe_common    # maybe_common_
    |   expr UNDERSCORE expr    # underscore_
    |   expr relation_operators expr    #   relation_operators_   
    |   TRIG_FUNCTIONS L_PAREN expr R_PAREN # trig_functions_
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
    |  '\\prod'
    |   '\\vec'  
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


number:
    INT     #   integer
    | FLOAT #   float
    ;

prime: EXPO'\\prime'
    |    '\'';

EQUAL: '=';
DOTEQ: '\\doteq';
EQUIV: '\\equiv';
APPROX: '\\approx';
CONG: '\\cong';
SIMEQ: '\\simeq';
SIM: '\\sim';
PROPTO: '\\propto';
NEQ: '\\neq'|    '\\ne';
LT: '<';
NLESS: '\\nless';
LTE: '\\leq'|    '\\leqslant';
PROPERSUBSET: '\\subset'|    '\\supset' ;
NOTPROPERSUBSET: '\\not\\subset'|    '\\not\\supset';
SUBSET: '\\subseteq'|    '\\supseteq';
NOTSUBSET: '\\nsubseteq'|    '\\nsupseteq';
GT: '>';
NGTR: '\\ngtr';
GTE: '\\geq'|    '\\geqslant';
NGEQ: '\\ngeq'|    '\\ngeqslant';

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

DOTS:
    '\\dots'
    |    '\\ldots'
    |    '\\cdots';

BAR:
    '\\Bar'
    |    '\\bar';

  
symbols:
  '\\bigodot'
    |   '\\bigoplus'
    |   '\\bigotimes'
    |   '\\la'
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
    |   'j'
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
    |   '\\angle'
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
    |   '\\cosh'
    |   '\\tan'
    |   '\\tanh'
    |   '\\cot'
    |   '\\coth'
    |   '\\sinh'
    |   '\\arccos'
    |   '\\arcsin'
    |   '\\arctan'
    ;



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
RIGHTARROW:      '\\rightarrow'|    '\\to'|    '\\Rightarrow';
LONGRIGHTARROW:  '\\longrightarrow' |    '\\Longrightarrow';
MAPSTO:  '\\mapsto';
LONGMAPSTO:      '\\longmapsto';
LEFTARROW:       '\\leftarrow'|    '\\gets'|    '\\Leftarrow';
LONGLEFTARROW:   '\\longleftarrow'|    '\\Longleftarrow';
UPARROW:         '\\uparrow'|    '\\Uparrow';
DOWNARROW:       '\\downarrow'|    '\\Downarrow';
UPDOWNARROW:     '\\updownarrow'|    '\\Updownarrow';

HOOKLEFTARROW: '\\hookleftarrow';
HOOKRIGHTARROW: '\\hookrightarrow';
LONGLRARROW:    '\\longleftrightarrow';

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

GREEK:  
    '\\alpha'
    |    '\\Alpha'
    |    '\\beta'
    |    '\\Beta'
    |    '\\chi'
    |    '\\Chi'
    |    '\\delta'
    |    '\\Delta'
    |    '\\digamma'
    |    '\\Digamma'
    |    '\\epsilon'
    |    '\\Epsilon'
    |    '\\eta'
    |    '\\Eta'
    |    '\\gamma'
    |    '\\Gamma'
    |    '\\iota'
    |    '\\Iota'
    |    '\\kappa'
    |    '\\Kappa'
    |    '\\lambda'
    |    '\\Lambda'
    |    '\\mu'
    |    '\\Mu'
    |    '\\nu'
    |    '\\Nu'
    |    '\\omega'
    |    '\\Omega'
    |    '\\omicron'
    |    '\\Omicron'
    |    '\\phi'
    |    '\\Phi'
    |    '\\pi'
    |    '\\Pi'
    |    '\\psi'
    |    '\\Psi'
    |    '\\rho'
    |    '\\Rho'
    |    '\\sigma'
    |    '\\Sigma'
    |    '\\tau'
    |    '\\Tau'
    |    '\\theta'
    |    '\\Theta'
    |    '\\upsilon'
    |    '\\Upsilon'
    |    '\\varDelta'
    |    '\\varepsilon'
    |    '\\vargamma'
    |    '\\varGamma'
    |    '\\varkappa'
    |    '\\varLambda'
    |    '\\varliminf'
    |    '\\varlimsup'
    |    '\\varOmega'
    |    '\\varphi'
    |    '\\varPhi'
    |    '\\varpi'
    |    '\\varPi'
    |    '\\varPsi'
    |    '\\varrho'
    |    '\\varsigma'
    |    '\\varSigma'
    |    '\\vartheta'
    |    '\\varTheta'
    |    '\\vartriangle'
    |    '\\varUpsilon'
    |    '\\varXi'
    |    '\\xi'
    |    '\\Xi'
    |    '\\zeta'
    |    '\\Zeta';


IGNORE:
    ('\\vrule'|    '\\quad'|    '\\hfil'|    '\\quad'|    '\\vcenter'|    '\\vbox'|    '\\vskip'|    '\\vspace'
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


variable_sized_math_operators:
	'\\iint'          
|	'\\iiint'
|	'\\iiiint'
|	'\\idotsint'
;

binary_relations:
| '\\approxeq'
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



greek_letters:
     '\\digamma'
|    '\\varkappa'
|    '\\z'
;


hebrew_letters:
     '\\beth'
|    '\\daleth'
|    '\\gimel'
|    '\\i'
|    '\\k'
;


letter_like_symbols:
     '\\Bbbk'
|    '\\Finv'
|    '\\Game'
|    '\\circledR'
|    '\\circledS'
|    '\\complement'
|    '\\hbar'
|    '\\hslash'
|    '\\nexists'
|    '\\a'
|    '\\k'
|    '\\r'
|    '\\s'
;



delimiters:
     '\\llcorner'
|    '\\lrcorner'
|    '\\ulcorner'
|    '\\urcorner'
;


variable_sized_delimiters:
     '\\lVert'
|    '\\lvert'
|    '\\rVert'
|    '\\rvert'
;                                  
                                                                             
math_mode_accents:
     '\\ddddot{a}'
|    '\\dddot{a}'
;

extensible_accents:
     '\\overleftrightarrow{abc}'
|    '\\underleftarrow{abc}'
|    '\\underleftrightarrow{abc}'
|    '\\underrightarrow{abc}'
;


extensible_arrows:
     '\\xleftarrow{abc}'
|    '\\xrightarrow{abc}'
;


dots:
     '\\because*'
|    '\\dotsb'
|    '\\dotsc'
|    '\\dotsi'
|    '\\dotsm'
|    '\\dotso'
|    '\\therefore*'
;


angles:
     '\\angle'
|    '\\measuredangle'
|    '\\sphericalangle'
;




math_symbols:
     '\\backprime'
|    '\\bigstar'
|    '\\blacklozenge'
|    '\\blacksquare'
|    '\\blacktriangle'
|    '\\blacktriangledown'
|    '\\diagdown'
|    '\\diagup'
|    '\\eth'
|    '\\lozenge'
|    '\\mho'
|    '\\square'
|    '\\triangledown'
|    '\\varnothing'
|    '\\vartriangle'
;