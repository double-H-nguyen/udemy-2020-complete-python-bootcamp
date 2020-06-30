import math
import string


def vol(rad):
    return (4/3) * (math.pi) * (rad ** 3)
# Write a function that computes the volume of a sphere given its radius


def ran_bool(num, low, high):
    # return num in range(low, high + 1)
    return (num >= low) and (num <= high)
# Write a function that checks whether a number is in a given range (inclusive of high and low)


def ran_check(num, low, high):
    if ran_bool(num, low, high):
        return f"{num} is in the range of {low} and {high}"
    else:
        return f"{num} is NOT in the range of {low} and {high}"
# Write a function that checks whether a number is in a given range (inclusive of high and low)


def up_low(s):
    numOfUppers = 0
    numOfLowers = 0
    for letter in s:
        if letter.isupper():
            numOfUppers += 1
        elif letter.islower():
            numOfLowers += 1
        else:
            pass
    print(f"Original string: {s}")
    print(f"No. of Upper case characters: {numOfUppers}")
    print(f"No. of Lower case characters: {numOfLowers}")
# Write a function that accepts a string and calculates the number of upper case letters and lower case letters


def unique_list(lst):
    return list(set(lst))
# write a python function that takes a list and returns a new list with unique elements of the first list


def multiply(numbers):
    total = 1
    for num in numbers:
        total *= num
    return total
# Write a python function to multiply all the numbers in a list


def palindrome(s):
    original = s.replace(' ', '')
    reversedWord = original[::-1]
    return original == reversedWord
# Write a Python function that checks whether a word or phrase is palindrome or not


def ispangram(str1, alphabet=string.ascii_lowercase):
    # alphabet = set(alphabet)
    # str1 = str1.replace(' ','')
    # str1 = str1.lower()
    # str1 = set(str1)
    # return str1 == alphabet

    stringSet = set()
    for letter in str1:
        letterLower = letter.lower()
        if letterLower in alphabet:
            stringSet.add(letterLower)

    return len(stringSet) == len(alphabet)
# write a function to check whether a string is pangram or not


print(vol(2))  # 33.4933333
print(ran_check(5, 2, 7))  # true
print(ran_check(10, 2, 7))  # false
print(ran_bool(3, 1, 10))  # true
up_low("Hello Mr. Rogers, how are you this fine Tuesday?")
print(unique_list([1, 1, 1, 1, 2, 2, 3, 3, 3, 3, 4, 5]))
print(multiply([1, 2, 3, -4]))
print(palindrome("helleh"))
print(palindrome("helleh mom wow"))
print(palindrome("wow mom wow"))
print(palindrome("nurse run"))
print(ispangram("The quick brown fox jumps over the lazy dog"))
