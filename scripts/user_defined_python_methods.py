#!/usr/bin/python3

""" python3 -W ignore user_defined_python_methods.py # ignores future warnings
How to read in a file and use regular expressions in python
mimics grep by taking a regular expession (what) and a filename (where)"""

import re

def cat_file_with_newlines(where):
    with open(where, 'r') as file:
        for line in file:
            print(line)

# python3 only
def cat_file(where):
    with open(where, 'r') as file:
        for line in file:
            print(line, end="")


def count_matches(what, where):
    count = 0
    with open(where, 'r') as file:
        for line in file:
            if re.match(what, line):  # match file lines
                count += 1
    print(count)

def show_match_line(what, where):
    with open(where, 'r') as file:
        for line in file:
            if re.match(what, line):
                print(line)

def show_match_line_number(what, where):
    line_numbers = []
    with open(where, 'r') as file:
        for num, line in enumerate(file, 0):
            if re.match(what, line):
                line_numbers = num
                print(num)
    return line_numbers

def find_all(what, where):
    with open(where, 'r') as file:
        for line in file:
            if re.findall(what, line):                   # findall, not match 1
                print(re.split(r'\s*', line, re.I|re.M)) # split line up into a list,
                                                         # ignore case and multiline
input_file = '../data/SS_DATA.txt'

# method calls

# cat_file(input_file)
# cat_file_with_newlines(input_file)
# count_matches("^#", input_file)
# show_match_line("^#", input_file)
# show_match_line_number("^#", input_file)
# line_numbers=show_match_line_number("^#", input_file) # store #'s
find_all('CY_REVBUD', input_file)
# find_all('[CY_REVBUD]', input_file)

# split a string into a list by space delimination
# print('sdfsd fsdf sdf'.split())
# print(re.split(r'\s*', 'sdfsd fsdf sdf'))
