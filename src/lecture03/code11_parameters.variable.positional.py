# parameters.variable.positional.py
def minimum(*n):
    # print(type(n))  # n is a tuple
    if n:  # explained after the code
        min = n[0]
        for value in n[1:]:
            if value < min:
                min = value
        print(min)

minimum(1, 3, -7, 9)  # n = (1, 3, -7, 9) - prints: -7
minimum()             # n = () - prints: nothing
minimum(1, 3, -7, 9, -100)