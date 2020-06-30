def lesser_of_two_evens(a, b):
    if (a % 2 == 0) and (b % 2 == 0):
        return min(a, b)
    else:
        return max(a, b)
# Write a function that returns the lesser of two given numbers if both numbers are even,
# but returns the greater if one or both numbers are odd


def animal_crackers(text):
    words = text.split()
    return words[0][0] == words[1][0]
# Write a function takes a two-word string
# and returns True if both words begin with same letter


def makes_twenty(n1, n2):
    return (n1 + n2 == 20) or (n1 == 20) or (n2 == 20)
# Given two integers, return True if the sum of the integers is 20 or if one of the integers is 20.
# If not, return False¶


def old_macdonald(name):
    newName = ""
    for i, letter in enumerate(name):
        if (i == 0):
            newName += letter.upper()
        elif (i == 3):
            newName += letter.upper()
        else:
            newName += letter
    return newName
# Write a function that capitalizes the first and fourth letters of a name


def master_yoda(text):
    words = text.split()
    words.reverse()
    return " ".join(words)
# Given a sentence, return a sentence with the words reversed


def almost_there(n):
    # between 90 - 110
    if abs(100 - n) <= 10:
        return True
    elif abs(200 - n) <= 10:
        return True
    else:
        return False
# Given an integer n, return True if n is within 10 of either 100 or 200


def has_33(nums):
    for i in range(0, len(nums) - 1):
        if (nums[i] == 3) and (nums[i + 1] == 3):
            return True
    return False
# Given a list of ints, return True if the array contains a 3 next to a 3 somewhere


def paper_doll(text):
    newText = ""
    for letter in text:
        newText += (letter * 3)
    return newText
# Given a string, return a string where for every character in the original there are three character


def blackjack(a, b, c):  # review video
    nums = [a, b, c]
    total = sum(nums)
    if total <= 21:
        return total
    # if there is an 11, 31 is the highest total value that can be <=21 after subtracting 10
    elif (total <= 31) and (11 in nums):
        return total - 10
    else:
        return 'BUST'
# Given three integers between 1 and 11, if their sum is less than or equal to 21, return their sum.
# If their sum exceeds 21 and there's an eleven, reduce the total sum by 10.
# Finally, if the sum (even after adjustment) exceeds 21, return 'BUST


def summer_69(arr):
    ignoreNum = False
    total = 0
    for num in arr:
        if num == 6:
            ignoreNum = True
        elif num == 9:
            ignoreNum = False
        else:
            if not ignoreNum:
                total += num
    return total
# Return the sum of the numbers in the array,
# except ignore sections of numbers starting with a 6 and extending to the next 9 (every 6 will be followed by at least one 9).
# Return 0 for no numbers


def spy_game(nums):
    goal = [0, 0, 7]
    match = []
    for num in nums:
        if (num == 0) or (num == 7):
            match.append(num)
    return match == goal
# Write a function that takes in a list of integers and returns True if it contains 007 in order


def count_primes(num):
    # number must be greater than 1
    if (num <= 1):
        return 0

    counter = 1  # we will initially count 2 as a prime number

    for i in range(3, num + 1):  # 3 through "num"
        numIsPrime = True

        # If a number can be divided evenly by any other number
        # not counting itself and 1, it is not prime
        for j in range(2, i):  # does not include 1 or itself
            if i % j == 0:
                numIsPrime = False
                break  # don't need to test other combinations

        if numIsPrime:
            counter += 1

    return counter
# Write a function that returns the number of prime numbers that exist up to and including a given number
# A prime number is a numeral that is greater than 1 and cannot be divided evenly by any other number except 1 and itself


def print_big(letter):
    alphabet = {'a': "  *  \n * * \n*****\n*   *\n*   *\n",
                'b': "***  \n*  * \n***  \n*  * \n*****\n",
                'c': "*****\n*    \n*    \n*    \n*****\n",
                'd': "**** \n*   *\n*   *\n*   *\n**** \n",
                'e': "*****\n*    \n*****\n*    \n*****\n",
                }
    return alphabet[f'{letter.lower()}']
# Write a function that takes in a single letter, and returns a 5x5 representation of that letter


############ CHALLENGING PROBLEMS ##############
# print(spy_game([1,2,4,0,0,7,5]))
# print(spy_game([1,0,2,4,0,5,7]))
# print(spy_game([1,7,2,0,4,5,0]))
# print(count_primes(1))
# print(count_primes(5))
# print(count_primes(100))
# print(print_big('a'))
# print(print_big('b'))
# print(print_big('c'))
# print(print_big('d'))
# print(print_big('e'))

############ WARMUP SECTION ##############
# print(lesser_of_two_evens(2, 4))
# print(lesser_of_two_evens(2, 5))
# print(animal_crackers('Levelheaded Llama'))
# print(animal_crackers('Crazy Kangaroo'))
# print(makes_twenty(20,10))
# print(makes_twenty(12,8))
# print(makes_twenty(2,3))

############ LEVEL 1 PROBLEMS ##############
# print(old_macdonald('macdonald'))
# print(master_yoda('I am home'))
# print(master_yoda('We are ready'))
# print(almost_there(90))
# print(almost_there(104))
# print(almost_there(150))
# print(almost_there(209))

############ LEVEL 2 PROBLEMS ##############
# print(has_33([1, 3, 3]))
# print(has_33([1, 3, 1, 3]))
# print(has_33([3, 1, 3]))
# print(has_33([1, 1, 1]))
# print(paper_doll('Hello'))
# print(paper_doll('Mississippi'))
# print(blackjack(5, 6, 7))
# print(blackjack(9, 9, 9))
# print(blackjack(9, 9, 11))
# print(blackjack(11, 11, 11))
# print(blackjack(11, 11, 9))
# print(summer_69([1, 3, 5]))
# print(summer_69([4, 5, 6, 7, 8, 9]))
# print(summer_69([2, 1, 6, 9, 11]))
