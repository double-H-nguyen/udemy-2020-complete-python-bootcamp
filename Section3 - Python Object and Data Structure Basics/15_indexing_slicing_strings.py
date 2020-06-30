mystring = "Hello World"

# Indexing
print(mystring[0])
print(mystring[8])
print(mystring[-1])

# Slicing
mystring = "abcdefghijk"
print(mystring[2])
print(mystring[2:])
print(mystring[:3]) # up to, but not including nth character

# Combine
mystring = "abcdefghijk"
print(mystring[3:6])
print(mystring[1:3])
print(mystring[4:-2])

# Step size
mystring = "abcdefghijk"
print(mystring[::2])
print(mystring[::5])
print(mystring[2:7:2])
print(mystring[::-1]) # reverse string