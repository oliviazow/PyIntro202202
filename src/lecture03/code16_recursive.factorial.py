# recursive.factorial.py
def factorial(n):
    if n in (0, 1):  # base case
        return 1
    return n * factorial(n - 1)  # recursive case


print([factorial(n) for n in range(10)])
