t = (1, 2, 3)
mylist = [1, 2, 3]
print(type(t))
print(len(t))

t = ('one', 2)
print(t[-1])
print(t[0:])

t = ('a', 'a', 'b')
print(t.count('a'))
print(t.index('a'))
print(t.index('b'))
# t[0] = 'new' <-- not allowed in tuples