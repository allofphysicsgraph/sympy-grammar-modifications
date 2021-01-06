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


/**LPAREN:
 	'(',

BANG: 
	'!'
	;
RPAREN:
	')',


COMMA:
	','
	;

MINUS:
	'-'
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

'\\',
 '\\!',
 '\\(',
 '\\)',
 '\\:',
 '\\;',

'\\Box',

 '\\approx',
 '\\ast',
 '\\bar',
 '\\cal',
 '\\cdot',
 '\\cdots',
 '\\chi',
 '\\cos',
 '\\cosh',
 '\\coth',
 '\\dag',
 '\\dagger',
 '\\ddot',
 '\\det',
 '\\dot',
 '\\ell',
 '\\equiv',
 '\\eta',
 '\\exp',
 '\\flat',
 '\\frac',
 '\\ge',
 '\\geq',
 '\\hat',
 '\\hbar',
 '\\in',
 '\\infty',
 '\\int',
 '\\land',
 '\\langle',
 '\\ldots',
 '\\le',
 '\\leftrightarrow',
 '\\leq',
 '\\ll',
 '\\ln',
 '\\log',
 '\\mbox',
 '\\mid',
 '\\mp',
 '\\nabla',
 '\\neq',
 '\\notin',
 '\\nu',
 '\\oint',
 '\\omega',
 '\\oplus',
 '\\otimes',
 '\\parallel',
 '\\partial',
 '\\perp',
 '\\phi',
 '\\pi',
 '\\pm',
 '\\pounds',
 '\\prime',
 '\\psi',
 '\\rangle',
 '\\rho',
 '\\rightarrow',
 '\\rm',
 '\\sec',
 '\\sigma',
 '\\sim',
 '\\sin',
 '\\sinh',
 '\\sqrt',
 '\\star',
 '\\sum',
 '\\tan',
 '\\tanh',
 '\\tau',
 '\\theta',
 '\\tilde',
 '\\times',
 '\\to',
 '\\top',
 '\\upsilon',
 '\\varepsilon',
 '\\varphi',
 '\\varsigma',
 '\\vartheta',
 '\\vec',
 '\\vert',
 '\\wedge',
 '\\xi',
 '\\zeta',
 '\\{',
 '\\}',
 ']',
 '^',
 '_',
 


 '{',
 '|',
 '}',
 '~'}

 '\\H',
 '\\L',
 '\\O',
 '\\Omega',
**/
