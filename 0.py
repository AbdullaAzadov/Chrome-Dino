import os
#to get the current working directory
directory = str(os.getcwd())
str_dir = ''
for let in directory:
    if ord(let) == 92: let = "/"
    str_dir+= let
str_dir+='/'
print(str_dir)