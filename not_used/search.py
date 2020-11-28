#!/usr/bin/env python3

from sys import argv
def regex_and_or(pattern,file_name=False,list_of_strings_to_search=False, delimiter='\s+'):
    import re
    from sys import argv
    if file_name:
        f = open(file_name)
        data = f.readlines()
        f.close()
        list_of_strings_to_search = data
    """
    # when multiple terms are present in the pattern, 
    # then search "term1 AND term2 AND term3" in the list of strings

    # default is to split each string in the corpus on spaces

    >>> list_of_strings_to_search = ["Normally matches any character except a newline.", "Within square brackets the dot is literal."]
    >>> regex_and_or('(Normally|With) (anyf|char)? square', list_of_strings_to_search)
    ['Within square brackets the dot is literal. ']

    # match one of the two
    >>> regex_and_or('Normally|With', list_of_strings_to_search)
    ['Normally matches any character except a newline.', 'Within square brackets the dot is literal. ']

    # The question mark makes the preceding token in the regular expression optional. 
    # https://www.regular-expressions.info/optional.html
    >>> regex_and_or('(anyf|char)?', list_of_strings_to_search)
    ['Normally matches any character except a newline.', 'Within square brackets the dot is literal. ']
 
    # exact match
    >>> regex_and_or('square', list_of_strings_to_search)
    ['Within square brackets the dot is literal. ']

    # look for a math expression that has both "cos" and "2" present
    >>> list_of_strings_to_search = ['sin(x) + cos(2x) = f(x)', 'ax^2 + bx + c = 0']
    >>> regex_and_or('cos 2', list_of_strings_to_search)
    ['sin(x) + cos(2x) = f(x)']
    """
    ands = re.split(delimiter,pattern)

    match_list = []
    for line in list_of_strings_to_search:
        ignore_line = False
        for word in ands:
            if not re.findall(word,line):
                ignore_line = True
        if not ignore_line:
            match_list.append(line)
    return match_list


for  match in regex_and_or(argv[1],file_name=argv[2]):
    print(match)
# EOF
