grammar LaTeX_v1;		



SYMBOLS:
	'}'
	|    '#'
	|    '>'
	|    '\\'
	|    '+'
	|    '='
	|    '^'
	|    '|'
	|    ';'
	|    '~'
	|    '('
	|    '/'
	|    '*'
	|    '-'
	|    ']'
	|    ' '
	|    '!'
	|    '_'
	|    '.'
	|    ')'
	|    '['
	|    '{'
	|    '<'
	;


ELEMENTARY_FUNCTIONS:
		'\\arccos'
	|	'\\arccosh'
	|	'\\arccot'
	|	'\\arccoth'
	|	'\\arccsc'
	|	'\\arccsch'
	|	'\\arcsec'
	|	'\\arcsech'
	|	'\\arcsin'
	|	'\\arcsinh'
	|	'\\arctan'
	|	'\\arctanh'
	|	'\\cos'
	|	'\\cosh'
	|	'\\cot'
	|	'\\coth'
	|	'\\csc'
	|	'\\csch'
	|	'\\exp'
	|	'\\lg'
	|	'\\ln'
	|	'\\log'
	|	'\\sec'
	|	'\\sech'
	|	'\\sin'
	|	'\\sinh'
	|	'\\tan'
	|	'\\tanh'
	;

GREEK:  
	  	 '\\varepsilon'
	 | 	 '\\varUpsilon'
	 | 	 '\\alpha'
	 | 	 '\\varLambda'
	 | 	 '\\varDelta'
	 | 	 '\\vargamma'
	 | 	 '\\varGamma'
	 | 	 '\\varkappa'
	 | 	 '\\varOmega'
	 | 	 '\\varsigma'
	 | 	 '\\varSigma'
	 | 	 '\\vartheta'
	 | 	 '\\varTheta'
	 | 	 '\\digamma'
	 | 	 '\\Digamma'
	 | 	 '\\epsilon'
	 | 	 '\\Epsilon'
	 | 	 '\\omicron'
	 | 	 '\\Omicron'
	 | 	 '\\upsilon'
	 | 	 '\\Upsilon'
	 | 	 '\\lambda'
	 | 	 '\\Lambda'
	 | 	 '\\varphi'
	 | 	 '\\varPhi'
	 | 	 '\\varPsi'
	 | 	 '\\varrho'
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
	 | 	 '\\Zeta'
	 | 	 '\\beta'
	 | 	 '\\Beta'
	 | 	 '\\iota'
	 | 	 '\\Iota'
	 | 	 '\\zeta'
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
	 | 	 '\\mu'
	 | 	 '\\Mu'
	 | 	 '\\nu'
	 | 	 '\\Nu'
	 | 	 '\\pi'
	 | 	 '\\Pi'
	 | 	 '\\xi'
	 | 	 '\\Xi';

IGNORE:
	('\\vrule'
	|   '\\quad'
	|   '\\hfil'
	|   '\\quad'
	|   '\\vcenter'
	|   '\\vbox'
	|   '\\vskip'
	|   '\\vspace'
	|   '\\left'
	|   '\\right'
	|   '\\*'
	|   '\\,'
	|   '\\-'
	|   '\\.'
	|   '\\/'
	|   '\\;'
	|   '\\!'
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
	 '\\approxeq'
	|    '\\backepsilon'
	|    '\\backsim'
	|    '\\backsimeq'
	|    '\\because'
	|    '\\between'
	|    '\\bumpeq'
	|    '\\Bumpeq'
	|    '\\circeq'
	|    '\\curlyeqprec'
	|    '\\curlyeqsucc'
	|    '\\doteqdot'
	|    '\\eqcirc'
	|    '\\fallingdotseq'
	|    '\\multimap'
	|    '\\pitchfork'
	|    '\\precapprox'
	|    '\\preccurlyeq'
	|    '\\precsim'
	|    '\\risingdotseq'
	|    '\\shortmid'
	|    '\\shortparallel'
	|    '\\smallfrown'
	|    '\\smallsmile'
	|    '\\succapprox'
	|    '\\succcurlyeq'
	|    '\\succsim'
	|    '\\therefore'
	|    '\\thickapprox'
	|    '\\thicksim'
	|    '\\varpropto'
	|    '\\vDash'
	|    '\\Vdash'
	|    '\\Vvdash'
	;

negated_binary_relations:
		'\\ncong'
	| 	'\\nmid'
	| 	'\\nparallel'
	| 	'\\nprec'
	| 	'\\npreceq'
	| 	'\\nshortmid'
	| 	'\\nshortparallel'
	| 	'\\nsim'
	| 	'\\nsucc'
	|	 '\\nsucceq'
	| 	'\\nvdash'
	| 	'\\nvDash'
	| 	'\\nVDash'
	| 	'\\precnapprox'
	| 	'\\precnsim'
	| 	'\\succnapprox'
	| 	'\\succnsim'
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


hebrew_letters:
	     '\\beth'
	|    '\\daleth'
	|    '\\gimel'
	|    '\\i'
	|    '\\k'
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
