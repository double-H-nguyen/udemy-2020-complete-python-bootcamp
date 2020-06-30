def myfunc(*args):
    print(f"{type(args)} {args}")  # treat as tuple
    # return 5% of the sum
    return sum(args) * 0.05
print(myfunc(40, 60))
print(myfunc(40, 60, 100))
print(myfunc(40, 60, 100, 1, 34))
print()


def myfunc2(**kwargs):
    print(f"{type(kwargs)} {kwargs}")  # treat as dictionary
    if 'fruit' in kwargs:
        print('My fruit of choise is {kwargs}')
    else:
        print('I did not find any fruit here')
print(myfunc2(fruit='apple', veggie='lettuce'))
print()


def myfunc3(*args, **kwargs):
    print(args)
    print(kwargs)
    print(f"I would like {args[0]} {kwargs['food']}")
myfunc3(10, 20, 30, fruit='orange', food='eggs', animal='dog')
