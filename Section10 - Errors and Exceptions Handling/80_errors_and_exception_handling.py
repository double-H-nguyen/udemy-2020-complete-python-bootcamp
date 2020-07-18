def add():
    try:
        # attempt this code
        # may have error
        result = 10 + 10
        # result = 10 + '10'
    except:
        print("Unable to add correctly")
    else:
        print("Adding was successful")
        print(result)


def read_file():
    try:
        f = open('testfile', 'r')
        f.write("Write a test line")
    except TypeError:
        print("There was a type error!")
    except OSError:
        print("There was an OS error")
    except:
        print("An unknown error")
    finally:
        print("This statement always show up")


def ask_for_int():
    while True:
        try:
            result = int(input("Please provide number: "))
        except:
            print("Whoops! That is not a number")
            continue
        else:
            print("Thank you!")
            break
        finally:
            print("End of try/except/finally")
            print()


# add()
# read_file()
ask_for_int()
