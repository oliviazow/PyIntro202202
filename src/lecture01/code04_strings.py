
>>> # -------------------------------------------------------------------------
>>> # by single, double, triple quotes
>>> 'This is a string'  # single quotes
'This is a string'
>>> "This is a string"  # double quotes
'This is a string'
>>> '''This is a string'''  # triple quotes
'This is a string'
>>> """This is a string"""  # triple quotes
'This is a string'

>>> # -------------------------------------------------------------------------
>>> # escape
>>> 'doesn\'t'  # use \' to escape the single quote
"doesn't"
>>> "doesn't"  # or use double quotes instead
"doesn't"
>>> '"Yes," they said.'
'"Yes," they said.'
>>> "\"Yes,\" they said."  # use \" to escape the double quote
'"Yes," they said.'
>>> s = 'First line.\nSecond line.'  # \n means newline
>>> s  # without print(), \n is included in the output
'First line.\nSecond line.'
>>> print(s)  # with print(), \n produces a new line
First line.
Second line.

>>> # -------------------------------------------------------------------------
>>> # repeat
>>> '--#--' * 10
'--#----#----#----#----#----#----#----#----#----#--'
>>> 10 * '--#--'
'--#----#----#----#----#----#----#----#----#----#--'

>>> # -------------------------------------------------------------------------
>>> # concat
>>> 'Py' 'thon'  # Two or more string literals next to each other are automatically concatenated
Python
# This feature is particularly useful when you want to break long strings:
>>> text = ('Put several strings within parentheses '
            'to have them joined together.')
>>> text
'Put several strings within parentheses to have them joined together.'
>>> 'Py' + 'thon'  # use +
Python

>>> # -------------------------------------------------------------------------
>>> # multiple lines
>>> # triple quotes
>>> print("""
Usage: thingy [OPTIONS]
     -h                        Display this usage message
     -H hostname               Hostname to connect to
""")
Usage: thingy [OPTIONS]
     -h                        Display this usage message
     -H hostname               Hostname to connect to
print('''\
Usage: thingy [OPTIONS]
     -h                        Display this usage message
     -H hostname               Hostname to connect to
''')
Usage: thingy [OPTIONS]
     -h                        Display this usage message
     -H hostname               Hostname to connect to


>>> # -------------------------------------------------------------------------
>>> # indexing
>>> word = 'Python'
>>> word[0]  # character in position 0
'P'
>>> word[-2]  # second-last character
'o'

>>> # -------------------------------------------------------------------------
>>> # slicing
>>> word[0:2]  # characters from position 0 (included) to 2 (excluded)
'Py'
>>> word[2:5]  # characters from position 2 (included) to 5 (excluded)
'tho'
>>> word[:2]   # character from the beginning to position 2 (excluded)
'Py'
>>> word[4:]   # characters from position 4 (included) to the end
'on'
>>> word[-2:]  # characters from the second-last (included) to the end
'on'
>>> word[:2] + word[2:]
'Python'
>>> word[:4] + word[4:]
'Python'

 +---+---+---+---+---+---+
 | P | y | t | h | o | n |
 +---+---+---+---+---+---+
 0   1   2   3   4   5   6
-6  -5  -4  -3  -2  -1

>>> word[42]  # the word only has 6 characters
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
IndexError: string index out of range

>>> word[4:42]
'on'
>>> word[42:]
''

>>> # -------------------------------------------------------------------------
>>> # strings are immutable
>>> word[0] = 'J'
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'str' object does not support item assignment
>>> 'J' + word[1:]
'Jython'
>>> word[:2] + 'py'
'Pypy'
