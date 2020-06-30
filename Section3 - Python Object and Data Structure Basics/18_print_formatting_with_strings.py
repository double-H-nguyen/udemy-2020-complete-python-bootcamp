# Format Method
print('This is a string {}'.format('INSERTED'))
print('The {} {} {}'.format('fox', 'brown', 'quick'))
print('The {2} {1} {0}'.format('fox', 'brown', 'quick'))
print('The {q} {b} {f}'.format(f='fox', b='brown', q='quick')) 

# Float formatting {value:width.precision f}
result = 100/777
print("The result was {r}".format(r=result))
print("The result was {r:1.3}".format(r=result))
result = 104.12345
print("The result was {r:1.2}".format(r=result))
print("The result was {r:1.2f}".format(r=result))

# f-strings / string literal
name = "Jose"
print(f'Hello, his name is {name}')

name = "Sam"
age = 3
print(f"{name} is {age} years old")