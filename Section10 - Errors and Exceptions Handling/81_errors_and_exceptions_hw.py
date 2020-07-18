# Problem 1
try:
    for i in ['a', 'b', 'c']:
        print(i**2)
except:
    print("Unable to perform action")

# Problem 2
x = 5
y = 0
try:
    z = x/y
except:
    print(f"Unable to divide {x} by {y}")
finally:
    print("All Done.")

# Problem 3
def ask():
    while True:
        try:
            number = int(input("Please enter a number: "))
        except:
            print("That is not a number")
            print()
        else:
            print(f"The square of {number} is {number**2}")
            print()
            break


ask()
