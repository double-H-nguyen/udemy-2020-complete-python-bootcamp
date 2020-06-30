# 1 print Hello World
def myfunc():
    print('Hello World')

# 2 print Hello Name
def myfunc(name):
    print('Hello {}'.format(name))

# 3 simple boolean
def myfunc(a):
    if a:
        return 'Hello'
    else:
        return 'Goodbye'

# 4 using booleans
def myfunc(x, y, z):
    if z:
        return x
    else:
        return y

# 5 simple math
def myfunc(n1, n2):
    return n1 + n2

#6 is even
def is_even(num):
    return (num % 2) == 0

#7 is greater
def is_greater(n1, n2):
    return n1 > n2

#8 *args
def myfunc(*args):
    return sum(args)

#9 pick evens
def myfunc(*args):
    evens = []
    for num in args:
        if (num % 2) == 0:
            evens.append(num)
    return evens

#10 skyline
def myfunc(word):
    newWord = ""
    for i, letter in enumerate(word, 1):
        if (i % 2) == 0:
            newWord += letter.upper()
        else:
            newWord += letter.lower()
    return newWord