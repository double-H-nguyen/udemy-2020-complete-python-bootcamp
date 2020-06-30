myfile = open('Section3 - Python Object and Data Structure Basics\\27_text_file.txt')
print(myfile.read())
print(myfile.read()) # read nothing because marker is at the end of the file
myfile.seek(0) # restart marker
contents = myfile.read()
print(contents)
myfile.seek(0)
contentList = myfile.readlines()
print(contentList)
myfile.close() # always close file

# preferred way to read contents in file
# exiting this block will auto close
with open('Section3 - Python Object and Data Structure Basics\\27_text_file.txt') as my_new_file:
    contents = my_new_file.read()
    print(contents)

# append
with open('Section3 - Python Object and Data Structure Basics\\27_text_file.txt', mode='a') as f:
    f.write('\nFOUR ON FOURTH')

# write
with open('Section3 - Python Object and Data Structure Basics\\27_write_to_text_file.txt', mode='w') as f:
    f.write('I CREATED THIS FILE!')