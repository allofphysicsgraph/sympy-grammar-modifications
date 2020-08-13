#!/usr/bin/env python3
import json

import sympy
from sympy.parsing.latex import parse_latex    

#import random
from subprocess import PIPE  # https://docs.python.org/3/library/subprocess.html
import subprocess  # https://stackoverflow.com/questions/39187886/what-is-the-difference-between-subprocess-popen-and-subprocess-run/39187984

# all of the following entries are valid latex, 
# as verified by the production of pdf files compiled with latex
# some of these are parsed by Sympy, others are not
list_of_latex = [
          # without an equal sign
          'a',
          # more valid latex without equal sign
          'a + b',
          # inequality
          'a > b',
          # a trivial latex input to verify that Sympy works as expected. No problem here
          'a = b + c',
          # a slightly more complicated latex input; still works. No problem here
          'x^2 + \int f(x) dx = 3',
          # with spacing; see https://github.com/sympy/sympy/issues/19075
          'x\\ y = f',
          'x\\; y = f',
          'x\\, y = f',
          'x\\: y = f',
          # the following cannot be evaluated mathematically but is valid latex. 
          # this fails in Sympy with the message "I expected one of these: '='"          
          '\sum_{x+y}^{a} \int_{3}^6 dy = 3',
          # the following is complicated but valid math and valid latex.
          # fails in the second array          
          '\\left[\\begin{array}{cc}\\cos\\theta & \\sin\\theta\\\\-\\sin\\theta & \\cos\\theta\\end{array}\\right]\\left[\\begin{array}{c}A_x \\\\ A_y \\end{array}\\right]=\\left[\\begin{array}{c}A_{x\'} \\\\ A_{y\'} \\end{array}\\right]',
          # here I isolate the problem array
          '\left[\\begin{array}{c}A_{x\'} \\\\ A_{y\'} \\end{array}\\right]',
          # the following is used in quantum mechanics and is valid latex. Fails in Sympy
          '\\hat{p} = -i \\hbar \\frac{\\partial }{\\partial x}',
          # fails in sympy and is (usually) incomplete mathematically
          'f = \\frac{\\partial }{\\partial x}',
          # this succeeds in Sympy, indicating an argument is expected
          'g = \\frac{\\partial }{\\partial x} k(x)', 
          # the following is used in quantum mechanics and is valid latex. Fails in Sympy
          '[\\hat{x},\\hat{p}] = i \\hbar',
          # valid math and valid latex but fails in Sympy
          '\\frac{1}{a^2}= \\frac{1}{2}W - \\frac{1}{2}\\left. \\frac{W}{2n\\pi}\\sin\\left(\\frac{2n\\pi}{W} x\\right)\\right|_0^W    when{n \\in {\\rm Integer}}',
          # problem for Sympy is the bar
          'a = \\left. f(x)\\right|_a^b'
       ]

proc_timeout = 30

def compile_tex_to_dvi(file_name):
    process = subprocess.run(
        ["latex", "-halt-on-error", file_name + ".tex"],
        stdout=PIPE,
        stderr=PIPE,
        timeout=proc_timeout,
    )
    # latex_stdout, latex_stderr = process.communicate()
    # https://stackoverflow.com/questions/41171791/how-to-suppress-or-capture-the-output-of-subprocess-run
    latex_stdout = process.stdout.decode("utf-8")
    latex_stderr = process.stderr.decode("utf-8")
    return

def dvi_to_pdf(file_name):
    # https://tex.stackexchange.com/questions/73783/dvipdfm-or-dvipdfmx-or-dvipdft
    process = subprocess.run(
        ["dvipdfmx", file_name + ".dvi"],
        stdout=PIPE,
        stderr=PIPE,
        timeout=proc_timeout,
    )

    dvipdf_stdout = process.stdout.decode("utf-8")
    dvipdf_stderr = process.stderr.decode("utf-8")
    return

def create_latex_file(file_name, math_latex):
    """
    >>> runme() 
    """
    with open(file_name + ".tex", "w") as lat_file:
        lat_file.write("\\documentclass[12pt]{article}\n")
        lat_file.write("\\thispagestyle{empty}\n")

        lat_file.write("\\begin{document}\n")
        lat_file.write("\\begin{equation}\n")

        lat_file.write(math_latex + "\n")

        lat_file.write("\\end{equation}\n")
        lat_file.write("\\end{document}\n")
    return

def get_latex_from_json(json_filename='data.json'):
    with open(json_filename) as json_file:
        dat = json.load(json_file)
    failed_latex = {}
    for expr_id, expr_dict in dat['expressions'].items():
        try:
            out_no_print = parse_latex(expr_dict['latex']);
        except Exception as er:
            failed_latex[expr_id] = expr_dict['latex']
            #print('expr ID =', expr_id)
            #print(er)
    return failed_latex

def check_list_of_latex(list_of_latex):
    file_indx = 9
    for this_latex in list_of_latex:
        file_indx += 1
        print('\nfile',str(file_indx),'contains\n', this_latex, '\n')
        file_name = str(file_indx)
        create_latex_file(file_name, this_latex)
        compile_tex_to_dvi(file_name)
        dvi_to_pdf(file_name)

        try:
            out = parse_latex(this_latex)
        except Exception as er:
            list_of_failed_latex.append(this_latex)
            #print(er)

    return list_of_failed_latex

if __name__ == "__main__":

    print('sympy', sympy.__version__)

    #check_list_of_latex(list_of_latex)

    failed_latex_dict = get_latex_from_json('data.json')
    for expr_id, expr_latex in failed_latex_dict.items():
        print('\n' + expr_latex)
        try:
            out = parse_latex(expr_latex)
        except Exception as er:
            print(er) 

