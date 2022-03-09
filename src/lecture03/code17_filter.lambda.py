# filter.lambda.py

l = lambda x: x*2
print(l(2))

print([(l(x)) for x in range(10)])

def get_multiples_of_five(n):
    return list(filter(lambda k: not k % 5, range(n)))


print(get_multiples_of_five(50))


