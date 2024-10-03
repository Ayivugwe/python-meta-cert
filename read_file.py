# Reading files is the same as writing except that we have to change the mode: write or append to read

# Read the whole content of the file

with open('new_file.txt', "r") as file:
    print(file.read())

# Read one line at a time
with open('new_file.txt', "r") as file:
    print("Single line: ", file.readline())
    
# Read multiple lines
with open('new_file.txt', "r") as file:
    print("Multiple lines: ", file.readlines())
    
# Read just a portion of the content of the file 
with open('new_file.txt', "r") as file:
    print("Read 20 characters of the content's file : ", file.read(20))
    