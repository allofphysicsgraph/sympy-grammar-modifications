/*
BSD License

Copyright (c) 2013, Tom Everett
All rights reserved.

Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions
are met:

1. Redistributions of source code must retain the above copyright
   notice, this list of conditions and the following disclaimer.
2. Redistributions in binary form must reproduce the above copyright
   notice, this list of conditions and the following disclaimer in the
   documentation and/or other materials provided with the distribution.
3. Neither the name of Tom Everett nor the names of its contributors
   may be used to endorse or promote products derived from this software
   without specific prior written permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
"AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT
HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
(INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
*/

grammar arithmetic;

file : equation* EOF
     | expression* EOF
;

equation
   : expression relop expression
   ;

expression
   :  expression  POW expression
   |  expression  (TIMES | DIV)  expression
   |  expression  (PLUS | MINUS) expression
   |  LPAREN expression RPAREN
   |  DOLLARSIGN expression*  DOLLARSIGN
   |  (PLUS | MINUS)* atom
   |  VARIABLE+   
;

atom
   : scientific
   | variable
   ;

scientific
   : SCIENTIFIC_NUMBER
   ;

variable
   : VARIABLE
   ;

relop:         
        
        EQ
    |    GTE
       |     GT
       |     LT

   ;


VARIABLE: 
    VALID_ID_START VALID_ID_CHAR*
    |    GREEK
   
;

TO_BE_LABELED:	
        '\\ell'
    |    '\\to'
    |    '\\infty'
    |     '\\approx'
    |     '\\arcmin'
    |     '\\arcsec'
    |     '\\ast'
    |     '\\cdot'
    |     '\\cdots'
    |     '\\circ'
    |     '\\dagger'
    |     '\\degr'
    |     '\\gev'
    |     '\\hbar'
    |     '\\ldots'
    |     '\\lok{B}'
    |     '\\mathcal{A}'
    |     '\\mathcal{C}'
    |     '\\mathcal{L}'
    |     '\\mathcal{S}'
    |     '\\mu'
    |     '\\nu'
    |     '\\pi'
    |     '\\pm'
    |     '\\prime'
    |     '\\rangle'
    |     '\\sim'
    |     '\\simeq'
    |     '\\sqrt'
    |     '\\square'
    |     '\\star'
    |     '\\times'
;

fragment VALID_ID_START:
     ('a' .. 'z') | ('A' .. 'Z') | '_'
   ;


fragment VALID_ID_CHAR
   : VALID_ID_START | ('0' .. '9')
   ;

//The NUMBER part gets its potential sign from "(PLUS | MINUS)* atom" in the expression rule
SCIENTIFIC_NUMBER
   : NUMBER (E SIGN? UNSIGNED_INTEGER)?
   ;

fragment NUMBER
   : ('0' .. '9') + ('.' ('0' .. '9') +)?
   ;

fragment UNSIGNED_INTEGER
   : ('0' .. '9')+
   ;


fragment E
   : 'E' | 'e'
   ;


fragment SIGN
   : ('+' | '-')
   ;


LPAREN
   : '('
   ;


RPAREN
   : ')'
   ;


PLUS
   : '+'
   ;


MINUS
   : '-'
   ;


TIMES
   : '*'
   ;


DIV
   : '/'
   ;


GT
   : '>'
   ;

GTE
    :    '\\geq'
    |    '\\ge'
    ;

LT
   : '<'
   |    '\\leq'
   ;

LTE:
	:	'<='
	|	'\\leq'
	|	'\\le'
	;

EQ
   : '='
   ;


POINT
   : '.'
   ;


POW
   : '^'
   ;

DOLLARSIGN:
    '$'
    ;

GREEK:  
           '\\varepsilon'
     |      '\\varUpsilon'
     |      '\\alpha'
     |      '\\varLambda'
     |      '\\varDelta'
     |      '\\vargamma'
     |      '\\varGamma'
     |      '\\varkappa'
     |      '\\varOmega'
     |      '\\varsigma'
     |      '\\varSigma'
     |      '\\vartheta'
     |      '\\varTheta'
     |      '\\digamma'
     |      '\\Digamma'
     |      '\\epsilon'
     |      '\\Epsilon'
     |      '\\omicron'
     |      '\\Omicron'
     |      '\\upsilon'
     |      '\\Upsilon'
     |      '\\lambda'
     |      '\\Lambda'
     |      '\\varphi'
     |      '\\varPhi'
     |      '\\varPsi'
     |      '\\varrho'
     |      '\\Alpha'
     |      '\\delta'
     |      '\\Delta'
     |      '\\gamma'
     |      '\\Gamma'
     |      '\\kappa'
     |      '\\Kappa'
     |      '\\omega'
     |      '\\Omega'
     |      '\\sigma'
     |      '\\Sigma'
     |      '\\theta'
     |      '\\Theta'
     |      '\\varpi'
     |      '\\varPi'
     |      '\\varXi'
     |      '\\Zeta'
     |      '\\beta'
     |      '\\Beta'
     |      '\\iota'
     |      '\\zeta'
     |      '\\chi'
     |      '\\eta'
     |      '\\phi'
     |      '\\Phi'
    |     '\\rho'
    ;

WS
   : [ \r\n\t] + -> skip
   ;
