grammar PDG;


prog: expression+;

LBRACE: '{'	;
RBRACE: '}'	;
LPAREN: '('	;
RPAREN: ')'	;
UNDERSCORE: '_' ;
INT: [0-9]+	;
SMALLINT: '0'|'1'|'2';
POSSMALLINT: '1'|'2';


expression:
	symbol_phrases
	|	SYMBOLS
	;


symbol_phrases:
	'a' UNDERSCORE LBRACE ('\\alpha'|'\\beta') RBRACE
	 | 	 '\\langle \\psi_{\\alpha} |*Ket'
	 | 	 'r_{\\rm geostationary\\ orbit}'
	 | 	 'T_{\\rm geostationary\\ orbit}'
	 | 	 '\\theta' UNDERSCORE POSSMALLINT
	 | 	 ('v'|'V') UNDERSCORE SMALLINT
	 | 	 'PE_{\\rm Earth\\ surface}'
	 | 	 '\\vec{p}_{\\rm electron}'
	 | 	 'm' UNDERSCORE POSSMALLINT
	 | 	 'I' UNDERSCORE POSSMALLINT
	 | 	 '\\psi_{\\beta} \\rangle'
	 | 	 '\theta_{\\rm refracted}'
	 | 	 ('v'|'C'|'r') UNDERSCORE LBRACE '\\rm Earth\\ orbit' RBRACE
	 | 	 'r_{\\rm Schwarzschild}'
	 | 	 '\theta_{\\rm Brewster}'
	 | 	 't_{\\rm Earth\\ orbit}'
	 | 	 'E' UNDERSCORE SMALLINT
	 | 	 'F_{\\rm centripetal}'
	 | 	 'v_{\\rm satellite}'
	 | 	 'm_{\\rm satellite}'
	 | 	 'KE_{\\rm initial}'
	 | 	 'v_{\\rm initial}'
	 | 	 'F_{\\rm gravity}'
	 | 	 'KE_{\\rm escape}'
	 | 	 'a_{\\alpha}*Bra'
	 | 	 'v_{\\rm escape}'
	 | 	 'KE_{\\rm final}'
	 | 	 '\\langle \\psi|'
	 | 	 'v_{\\rm final}'
	 | 	 'm_{\\rm Earth}'
	 | 	 'r_{\\rm Earth}'
	 | 	 'R_{\\rm total}'
	 | 	 'T_{\\rm orbit}'
	 | 	 'g_{\\rm Earth}'
	 | 	 'I_{\\rm total}'
	 | 	 '\\vec{p}_2'
	 | 	 '\\hbar'
	 | 	 'KE_1'
	 | 	 'PE_1'
	 | 	 'y_0'
	 | 	 'x_f'
	 | 	 'y_f'
	 | 	 'x_0'
	 | 	 'x_1'
	 | 	 'n_1'
	 | 	 'R_1'
	 | 	 'R_2'
	 | 	 't_f'
	  	 ;


SYMBOLS:
	'\\gamma'
	 | 	 '\\theta'
	 | 	 '\\phi'
	 | 	 '\\psi'
	 | 	 '\\exp'
	 | 	 '\\pi'
	 | 	 'PE'
	 | 	 'dt'
	 | 	 'dx'
	 | 	 'KE'
	 | 	 'm'
	 | 	 'I'
	 | 	 'P'
	 | 	 'r'
	 | 	 'R'
	 | 	 'a'
	 | 	 'A'
	 | 	 't'
	 | 	 'T'
	 | 	 'B'
	 | 	 'c'
	 | 	 'C'
	 | 	 'd'
	 | 	 'E'
	 | 	 'f'
	 | 	 'F'
	 | 	 'g'
	 | 	 'G'
	 | 	 'h'
	 | 	 'i'
	 | 	 'u'
	 | 	 'v'
	 | 	 'V'
	 | 	 'W'
	 | 	 'x'
	 | 	 'y'
	 | 	 'Z'
	  	 ;

