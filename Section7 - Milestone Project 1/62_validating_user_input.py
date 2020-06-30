def userChoice():
    correctVal = False

    while not correctVal:
        choice = input("Please enter a number (0-10): ")

        if not choice.isdigit():
            print("Sorry that is not a digit!")
        elif not (0 <= int(choice) <= 10):
            print("This number is not between 0 and 10!")
        else:
            correctVal = True

    return int(choice)

print(userChoice())