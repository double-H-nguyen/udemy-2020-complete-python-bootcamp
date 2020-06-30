myset = set()
print(myset)
myset.add(1)
print(myset)
myset.add(2)
print(myset)
myset.add(2)  # will not be added to set
print(myset)

mylist = [1, 1, 1, 1, 2, 2, 2, 2, 2]
myset = set(mylist)
print(mylist)
print(myset)
