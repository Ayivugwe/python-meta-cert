# This is a comment 
# Here I start by creating a simple file
# For this first line, if it happens that I make any changes, they going to update the first content.

with open('new_file.txt', "w") as file:
    file.write("Hello there!. This is my first file")
    print(file.name)
    
# Here I create a second file with multiple lines. Same as for the first file, changing the content updates the second file

with open('new_multiline_file.txt', "w") as file2:
    file2.writelines(["\nThis is my first line.", "\nThis is my second line"])
    print(file2.name)

    
# Here I use the second file with multiple lines for appending text which will add the new content update to the existing instead of overwriding it.
# I only change the mode: w to a  with: w = write and a = append

with open('new_multiline_file.txt', 'a') as file3:
    file3.write("\nThis is a new line added to the second file")