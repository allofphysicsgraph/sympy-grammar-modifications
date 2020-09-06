import re
from collections import defaultdict
from nltk.tokenize import mwe


class Trie(dict):
    from collections import defaultdict

    """A Trie implementation for strings"""
    LEAF = True

    def __init__(self, strings=None):
        super(Trie, self).__init__()
        if strings:
            for string in strings:
                self.insert(string)

    def insert(self, string):
        if len(string):
            self[string[0]].insert(string[1:])
        else:
            # mark the string is complete
            self[Trie.LEAF] = None

    def __missing__(self, key):
        self[key] = Trie()
        return self[key]


def add_new_token(string):
    tokenizer.add_mwe(r"{}".format(string))


def manual_entries(pattern, data):
    resp = re.findall(pattern, data)
    if resp:
        for match in resp:
            add_new_token(match)


def print_symbols_not_used():
    for k, v in symbols_use_count.items():
        if v == 0:
            print(k)


def symbols_not_accounted_for(seen_count):
    for item in sorted(dct.items(), key=lambda x: -x[1]):
        if item[1] > seen_count:
            print(item[0])


dct = defaultdict(int)
tokenizer = mwe.MWETokenizer(separator="")
symbols_use_count = defaultdict(int)

path_to_symbol_list = "symbol_list"
with open(path_to_symbol_list) as f:
    symbols = [x.replace("\n", "") for x in f.readlines()]

symbols = sorted(symbols, key=lambda x: -len(x))

for symbol in symbols:
    add_new_token(symbol)

add_new_token(r"\\ ")

path_to_expressions_list = "expressions"
with open(path_to_expressions_list) as f:
    expressions = [x.replace("\n", "").replace("$", "") for x in f.readlines()]

for expression in expressions[:]:
    # >4 is to show only expressions of len > 4
    if len(expression) > 4:
        if "\\" in tokenizer.tokenize(expression):
            print(expression)
            lst = tokenizer.tokenize(expression)
            print(lst)
            dct["".join(lst[lst.index("\\") :])] += 1

        else:
            # if there is a pattern not matched that should be split on, add the pattern here with manual_entries
            # I am not sure if you can add regex to the mwe tokenizer without changing it.
            manual_entries("\d+\.\d+|\d+", expression)
            lst = tokenizer.tokenize(expression)
            for x in lst:
                if x in symbols:
                    symbols_use_count[x] += 1

#print any word defined in the symbols file that was not seen
print_symbols_not_used()

# print any symbol that showed up 50 or more times and not accounted for
symbols_not_accounted_for(50)

