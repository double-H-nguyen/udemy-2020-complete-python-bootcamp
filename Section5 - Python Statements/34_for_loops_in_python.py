my_iterable = [1, 2, 3]
for item_name in my_iterable:
    print(item_name)
print()

myList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for num in myList:
    # check for even
    if ((num % 2) == 0):
        print(num)
    else:
        print(f"Odd number: {num}")
print()

list_sum = 0
for num in myList:
    list_sum = list_sum + num
    print(list_sum)
print()

for letter in 'Hello World':
    print(letter)
print()

myList = [(1, 2), (3, 4), (5, 6), (7, 8)]
for a, b in myList:
    print(f"{a} and {b}")
print()

d = {'k1': 1, 'k2': 2, 'k3': 3}
for key,value in d.items():
    print(f"{key} and {value}")
