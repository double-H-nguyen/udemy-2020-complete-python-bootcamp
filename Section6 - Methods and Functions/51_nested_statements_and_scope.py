# SCOPE: Local, Enclosing function locals, Global, Built-in functions

x = 50

def func():
    global x # tell func to use the global variable of x
    print(f"x is {x}")

    x = 200
    print(f"I just locally changed x to {x}")

print(x)
func()
print(x)