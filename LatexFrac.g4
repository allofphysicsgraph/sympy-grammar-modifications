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


INT: [1-9][0-9]* ;

WS:	[ \t\r\n]+ -> skip;

ADD: 
	'+'
	;

TIMES: 
	'*'
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
	|'\\Delta'
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
\alpha
\amalg
\angle
\approx
\arccos
\arcsin
\arctan
\arg
\ast
\asymp
\backslash
\bara
\BbbB
\beta
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
\chi
\circ
\clubsuit
\cong
\coprod
\cos
\cosh
\cot
\coth
\csc
\cup
\dagger
\dashv
\ddagger
\ddota
\ddots
\deg
\delta
\Delta
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
\epsilon
\equiv
\eta
\exists
\exp
\flat
\forall
\frown
\gamma
\Gamma
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
\kappa
\ker
\lambda
\Lambda
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
\ln
\lnot
\log
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
\phi
\Phi
\pi
\Pi
\pm
\Pr
\prec
\preceq
\prime
\prod
\propto
\psi
\Psi
\rangle
\rbrace
\rbrack
\rceil
\Re
\rfloor
\rhd
\rho
\Rightarrow
\rightharpoondown
\rightharpoonup
\rightleftharpoons
\searrow
\sec
\setminus
\sharp
\sigma
\Sigma
\sim
\simeq
\sin
\sinh
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
\tan
\tanh
\tau
\theta
\Theta
\tildea
\times
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
\upsilon
\Upsilon
\varepsilon
\varphi
\varpi
\varrho
\varsigma
\vartheta
\vdash
\vdots
\veca
\vee
\vert
\Vert
\wedge
\wp
\wr
\xi
\Xi
\zeta

**/
