
>>> # -------------------------------------------------------------------------
>>> 2 + 2  # this line is an expression
4
>>> 50 - 5*6
20
>>> (50 - 5*6) / 4
5.0
>>> 8 / 5  # division always returns a floating point number
1.6

>>> 17 / 3  # classic division returns a float
5.666666666666667
>>>
>>> 17 // 3  # floor division discards the fractional part
5
>>> 17 % 3  # the % operator returns the remainder of the division
2
>>> 5 * 3 + 2  # floored quotient * divisor + remainder
17

>>> 5 ** 2  # 5 squared
25
>>> 2 ** 7  # 2 to the power of 7
128

>>> # -------------------------------------------------------------------------
>>> width = 20  # width is a variable, this line is a statement
>>> height = 5 * 9  # height is another variable
>>> width * height
900

>>> # -------------------------------------------------------------------------
>>> n  # try to access an undefined variable
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'n' is not defined

>>> # -------------------------------------------------------------------------
>>> # float
>>> 4 * 3.75 - 1
14.0

>>> tax = 12.5 / 100
>>> price = 100.50
>>> price * tax
12.5625
>>> price + _ # the last printed expression is assigned to the variable _
113.0625
>>> round(_, 2)  # function call
113.06