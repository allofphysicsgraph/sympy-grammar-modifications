grammar LatexFrac;


init: frac;

frac:
	'\\frac' INT  INT
	| '\\frac' LBRACE expression+ RBRACE INT
	| '\\frac' INT LBRACE expression+ RBRACE
	| '\\frac' LBRACE expression+ RBRACE LBRACE expression+ RBRACE
	| MINUS frac
	;


expression:
	frac+
	| INT
	| GREEK+
	| binop GREEK
	| symbol GREEK
	| symbol binop INT
	| GREEK CARET INT
	| symbol CARET INT
	| symbol CARET LBRACE expression+ RBRACE
	| symbol+
	| LPAREN symbol UNDERSCORE (symbol|INT) binop symbol UNDERSCORE (symbol|INT) RPAREN
	| symbol UNDERSCORE symbol
	| symbol UNDERSCORE INT
	| LPAREN expression+ RPAREN
	| LPAREN expression+ RPAREN CARET LBRACE expression+ RBRACE
	| GREEK UNDERSCORE LBRACE expression+ RBRACE
	;



LPAREN: '(';
RPAREN: ')';
LBRACE: 
	'{'
	;

UNDERSCORE: '_';
RBRACE:
	'}'
	;

elementaryfunctions:
	'\\cos'
	|'\\cosh'
	|'\\cot'
	|'\\coth'
	|'\\csc'
	|'\\arccos'
	|'\\arcsin'
	|'\\arctan'
	|'\\ln'
	|'\\log'
	|'\\sin'
	|'\\sinh'
	|'\\tan'
	|'\\tanh'
	|'\\sec'
	;

INT: [1-9][0-9]* ;

WS:	[ \t\r\n]+ -> skip;

ADD: 
	'+'
	;

TIMES: 
	'*'
	|'\\times'
	;

MINUS:
	'-'
	;
binop:
	ADD
	|TIMES
	|MINUS

	;
CARET:
	'^'
	;
GREEK:
	'\\Delta'
	|'\\Gamma'
	|'\\Lambda'
	|'\\Omega'
	|'\\Phi'
	|'\\Pi'
	|'\\Psi'
	|'\\Sigma'
	|'\\Theta'
	|'\\Upsilon'
	|'\\Xi'
	|'\\alpha'
	|'\\beta'
	|'\\chi'
	|'\\delta'
	|'\\digamma'
	|'\\epsilon'
	|'\\eta'
	|'\\gamma'
	|'\\iota'
	|'\\kappa'
	|'\\lambda'
	|'\\mu'
	|'\\nu'
	|'\\omega'
	|'\\phi'
	|'\\pi'
	|'\\psi'
	|'\\rho'
	|'\\sigma'
	|'\\tau'
	|'\\theta'
	|'\\upsilon'
	|'\\varepsilon'
	|'\\varkappa'
	|'\\varphi'
	|'\\varpi'
	|'\\varrho'
	|'\\varsigma'
	|'\\vartheta'
	|'\\xi'
	|'\\zeta'
	;

UPPERCASE: ('A'..'Z');
LOWERCASE: ('a'..'z');

symbol:
	UPPERCASE
	| LOWERCASE;


SETNOTATION:
	'\\N'
	|'\\Z'
	|'\\Q'
	|'\\matgbb{A}'
	|'\\R'
	|'\\C'
	|'\\in'
	|'\\notin'
	|'\\cup'
	|'\\cap'
	|'\\setminus'
	|'\\exists'
	|'\\rightarrow'
	|'\\to'
	|'\\nexists'
	|'\\leftarrow'
	|'\\forall'
	|'\\mapsto'
	|'\\neg'
	|'\\implies'
	|'\\subset'
	|'\\impliedby'
	|'\\supset'
	|'\\Rightarrow'
	|'\\leftrightarrow'
	|'\\iff'
	|'\\ni'
	|'\\Leftrightarrow'
	|'\\land'
	|'\\top'
	|'\\lor'	
	|'\\bot'
	|'\\angle'  
	|'\\varnothing' 
	|'\\emptyset'
	;



/**

BANG: 
	'!'
	;

COMMA:
	','
	;

DOT:
	'.'
	;

DIV:
	'/'
	;
 
COLON:
	':'
	;

SEMICOLON:
	';',

LT:
	'<'
	;
EQ:
	'='
	;
GT:
	'>'
	;

 
LBRAC:
	'['
	;

\acutea
\aleph
\amalg
\angle
\approx
\arg
\ast
\asymp
\backslash
\bara
\BbbB
\bigcap
\bigcirc
\bigcup
\bigodot
\bigoplus
\bigotimes
\bigtriangledown
\bigtriangleup
\bigsqcup
\biguplus
\bigvee
\bigwedge
\bot
\bowtie
\Box
\brevea
\bullet
\calB
\cap
\cdot
\checka
\circ
\clubsuit
\cong
\coprod
\cup
\dagger
\dashv
\ddagger
\ddota
\ddots
\deg
\det
\diamond
\Diamond
\diamondsuit
\dim
\div
\dota
\doteq
\ell


\emptyset
\setminus



\equiv
\exists
\exp
\flat
\forall
\frown
\gcd
\ge
\geq
\gets
\gg
\gravea
\hata
\hbar
\heartsuit
\hom
\hookleftarrow
\hookrightarrow
\iff
\Im
\imath
\in
\inf
\infty
\int
\iota
\jmath
\Join
\ker
\land
\langle
\lbrace
\lbrack
\lceil
\le
\leadsto
\leftharpoondown
\leftharpoonup
\Leftrightarrow
\leq
\lfloor
\lg
\lhd
\lim
\liminf
\limsup
\ll
\lnot
\Longleftarrow
\Longleftrightarrow
\longmapsto
\Longrightarrow
\lor
\mapsto
\max
\mho
\mid
\min
\models
\mp
\mu
\nabla
\natural
\ne
\nearrow
\neg
\neq
\ni
\not=
\notin
\nu
\nwarrow
\odot
\oint
\omega
\Omega
\ominus
\oplus
\oslash
\otimes
\owns
\parallel
\partial
\perp
\Pi
\Pr

relation:
	\prec
	\preceq



\prime
\prod
\propto
\rangle
\rbrace
\rbrack
\rceil
\Re
\rfloor
\rhd
\Rightarrow
\rightharpoondown
\rightharpoonup
\rightleftharpoons
\searrow
\sharp
\sim
\simeq
\smallint
\smile
\spadesuit
\sqcap
\sqcup
\sqsubset
\sqsubseteq
\sqsupset
\sqsupseteq
\star
\subset
\subseteq
\succ
\succeq
\sum
\sup
\supset
\supseteq
\surd
\swarrow
\tildea
\to
\top
\triangle
\triangleleft
\triangleright
\unlhd
\unrhd
\uparrow
\Uparrow
\uplus
\vdash
\vdots
\veca
\vee
\vert
\Vert
\wedge
\wp
\wr
**/
