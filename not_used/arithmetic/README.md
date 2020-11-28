# objective

Starting with zero domain knowledge, programmatically introduce new information into the grammar while trying to keep human interaction to a minimum and maintain a readable grammar.

# How

Build a minimum dfa for the grammar. the tokens are grouped by categories, those categories can be use to construct a minimum dfa by using the data we feed to it. The result is a rule set for how the non terminals can be grouped together for the lexer and parser

# outline

To generate the dataset  

run make arithmetic_dataset  
this will print a bunch of expressions to stdout  
generate_rules.py  looks for a file called arithmetic_dataset.txt


The script  
generate_rules.py  
reads the arithmetic_dataset.txt

TRIE_OUTPUT is a DFA via a trie data structure on the grammar

Somehow (?) a grammar file  
Arithmetic.g4  
is produced
