x = 0

while x < 5:
    print(f"The current value of x is {x}")
    x += 1
else:
    print('X is not less than 5\n')

# break - break out of the current closest enclosing loop
# continue - goes to the top of the closest enclosing loop
# pass - does nothing at all

mystring = 'Sammy'

# continue
for letter in mystring:
    if letter == 'a':
        continue
    print(letter)
print()

# break
for letter in mystring:
    if letter == 'a':
        break
    print(letter)
print()