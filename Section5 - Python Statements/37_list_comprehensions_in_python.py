# list comprehensions to quickly create a list
# used when using "for loop" with ".append()" to create a list

mystring = 'hello'
mylist = []
for letter in mystring:
    mylist.append(letter)
print(mylist)
print()

# list comprehension
mylist = [letter for letter in mystring]
print(mylist)
print()

mylist = [x for x in 'word']
print(mylist)
print()

mylist = [(num ** 2) for num in range(0, 11)]
print(mylist)
print()

mylist = [x for x in range(0, 11) if ((x % 2) == 0)]
print(mylist)
print()

celcius = [0, 10, 20, 34.5]
fahrenheit = [(((9 / 5) * temp) + 32) for temp in celcius]
print(fahrenheit)
print()

# for loop equivalent
fahrenheit = []
for temp in celcius:
    fahrenheit.append((((9 / 5) * temp) + 32))
print(fahrenheit)
print()

# add if-else statements
results = [x if (x % 2 == 0) else 'ODD' for x in range(0, 11)]
print(results)
print()
