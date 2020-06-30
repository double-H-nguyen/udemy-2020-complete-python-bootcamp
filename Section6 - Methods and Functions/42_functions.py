def add_function(num1, num2):
    return num1 + num2

def name_function(name='default name'):
    '''
    DOCSTRING: Information about the function
    INPUT: name
    OUTPUT: Hello..
    '''
    print(f"hello {name}")

# Find out if the word "dog" is in a string?
def dog_check(mystring):
    return 'dog' in mystring.lower()

# PIG LATIN
def pig_latin(word):
    first_letter = word[0]
    if (first_letter.lower() in 'aeiou'):
        return word + 'ay'
    else:
        return word[1:] + first_letter + 'ay'

print(add_function(2, 1))
help(name_function)
name_function('Henry')
name_function()
print(dog_check('Dog in the house'))
print(dog_check('dog in the house'))
print(dog_check('cat in the house'))
print(pig_latin('word'))
print(pig_latin('apple'))