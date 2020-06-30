# range(x) - iterate that x times
for num in range(10):
    print(num)  # 0 - 9
print()

for num in range(3, 10):
    print(num)  # 3 - 9
print()

for num in range(0, 11, 2):
    print(num)  # 0 - 11, but skip every other number
print()

index_count = 0
for letter in 'abcde':
    print(f"At index {index_count} the letter is {letter}")
    index_count += 1
print()

# enumerate
word = 'abcde'
for index, letter in enumerate(word):
    print(f"{index} and {letter}")
print()

# zip
mylist1 = [1, 2, 3]
mylist2 = ['a', 'b', 'c', 'd']
mylist3 = [100, 200, 300, 400]
for item in zip(mylist1, mylist2, mylist3):
    print(item)  # ignore 4th tuple since does not have enough values
print(list(zip(mylist1, mylist2, mylist3)))
print()

# check if object is in a list
print('x' in [1, 2, 3])
print('x' in ['x', 'y', 'z'])
print('a' in 'a world')
d = {'mykey': 345}
print('mykey' in d)
print(345 in d)
print(345 in d.values())
print()

# find min and max value
mylist = [10,20,30,40,100]
print(min(mylist))
print(max(mylist))
print()

# importing
from random import shuffle # from 'random' library, import 'shuffle' function
mylist = [1,2,3,4,5,6,7,8,9,10]
print(mylist)
shuffle(mylist)
print(mylist)
print()

# generate random number
from random import randint
print(randint(0, 100)) # generate random number from 0 - 100
print()

# accept user's input
userInput = input('Enter a number here: ')
print(type(userInput))
print(userInput)
print()
userInput = int(input('Enter a number again: '))
print(type(userInput))
print(userInput)
print()

result = input('What is your name?: ')
print(f"Your name is {result}")
print()