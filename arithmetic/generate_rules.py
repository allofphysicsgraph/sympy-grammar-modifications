from sys import argv
import re
from sage.coding.source_coding.huffman import Huffman
from trie import Trie
trie_ = Trie()
#Huffman is used for efficient search and to resolve issues with splitting on special characters.

with open('arithmetic_dataset.txt') as f:
    arithmetic_dataset = f.read()
h = Huffman(arithmetic_dataset)
'''
print(h.__dict__)
{'_character_to_code': {'*': '110100', '+': '110101', '\n': '10000', '9': '10001', '7': '10100', '8': '10101', '5': '11011', '6': '11100', '3': '11101', '0': '0000', '4': '0001', '2': '1001', '/': '1011', '1': '1100', ' ': '1111', '-': '001', '(': '010', ')': '011'}, '_tree': ((((9, 10), 15), (16, 17)), ((((2, 3), 11), ((4, 5), 12)), ((13, ((0, 1), 6)), ((7, 8), 14)))), '_index': {0: '*', 1: '+', 2: '\n', 3: '9', 4: '7', 5: '8', 6: '5', 7: '6', 8: '3', 9: '0', 10: '4', 11: '2', 12: '/', 13: '1', 14: ' ', 15: '-', 16: '(', 17: ')'}}
'''

with open(argv[1]) as f:
    data = f.read()
categories = re.findall('[a-zA-Z_]+:.*?;',data,re.DOTALL)

words_in_grammar =set()
LATEX = {}

for ix in range(len(categories)):
    resp = re.findall('([a-zA-Z_]+:.*?);\n',data,re.DOTALL)[ix]
    resp_v1 = [x for x in re.split('(:?[a-zA-Z_]+):|\n|\t|\|',resp) if x]
    x,*y = resp_v1
    for word in y:
        LATEX[x] = [h.encode(word.replace('"','')) for word in y if word]
"""
print(LATEX)
{'SPACE': ['1111'], 'L_PAREN': ['010'], 'R_PAREN': ['011'], 'TIMES': ['110100'], 'ADD': ['110101'], 'SUBTRACT': ['001'], 'DIVIDE': ['1011'], 'DIGIT': ['0000', '1100', '1001', '11101', '0001', '11011', '11100', '10100', '10101', '10001']}
"""

encoded_expressions = []
for line in arithmetic_dataset.splitlines():
    print(line,h.encode(line))
    encoded_expressions.append(h.encode(line))


"""
2 + -20 + (-19632994)/(-1598366) + (-8080)/(-1414)     ->     10011111110101111100110010000111111010111110100011100100011110011101100110001100010001011101101000111001101110001101011110111100111000111111110101111101000110101000010101000001110110100011100000111000001011"""


map_binary_to_category = {}
for k,v in LATEX.items():
    for word in v:
        map_binary_to_category[word] = k

"""
print(map_binary_to_category)
{'1111': 'SPACE', '010': 'L_PAREN', '011': 'R_PAREN', '110100': 'TIMES', '110101': 'ADD', '001': 'SUBTRACT', '1011': 'DIVIDE', '0000': 'DIGIT', '1100': 'DIGIT', '1001': 'DIGIT', '11101': 'DIGIT', '0001': 'DIGIT', '11011': 'DIGIT', '11100': 'DIGIT', '10100': 'DIGIT', '10101': 'DIGIT', '10001': 'DIGIT'}
"""

words_to_split_on = '|'.join(sorted(map_binary_to_category.keys(),key=lambda x: -len(x)))


"""
print(words_to_split_on)
110100|110101|11101|11011|11100|10100|10101|10001|1111|1011|0000|1100|1001|0001|010|011|001
"""


for line in arithmetic_dataset.splitlines():
    resp = re.findall(words_to_split_on,h.encode(line))
    resp_to_category =[map_binary_to_category[x] for x in resp]
    """
    print(resp_to_category)
    ['L_PAREN', 'SUBTRACT', 'DIGIT', 'DIGIT', 'DIGIT', 'DIGIT', 'DIGIT', 'DIGIT', 'DIGIT', 'DIGIT', 'DIGIT', 'DIGIT', 'DIGIT', 'R_PAREN', 'DIVIDE', 'L_PAREN', 'SUBTRACT', 'DIGIT', 'DIGIT', 'DIGIT', 'DIGIT', 'DIGIT', 'DIGIT', 'DIGIT', 'R_PAREN', 'SPACE', 'ADD', 'SPACE', 'SUBTRACT', 'DIGIT', 'DIGIT', 'DIGIT', 'DIGIT']
    """

    trie_.insert(resp_to_category)    


"""
print(trie_)
output is in TRIE_OUTPUT
"""




