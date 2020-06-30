# Map function
def square(num):
    return num ** 2


nums = [1, 2, 3, 4, 5]
for item in map(square, nums):
    print(item)
print(list(map(square, nums)))
print()


def splicer(mystring):
    if len(mystring) % 2 == 0:
        return 'EVEN'
    else:
        return mystring[0]


names = ["Andy", "Eve", "Sam"]
print(list(map(splicer, names)))
print()


# Filter Function
def check_even(num):
    return num % 2 == 0


mynums = [1, 2, 3, 4, 5, 6]
for n in filter(check_even, mynums):
    print(n)
print()

# lamda expression / anonymous function
# used when you only intend to use a function once
# lambda num: num **2

print(list(map(lambda num:num**2, mynums)))
print()

print(list(filter(lambda num: num%2 == 0, mynums)))
print()