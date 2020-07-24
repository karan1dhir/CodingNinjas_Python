string = 'aabccbaa'
index = 1
while index < len(string):
    if string[index] == string[index - 1]:
        nextIndex = index + 1
        string = string[:index] + string[nextIndex:]
    else:
        index += 1
print(string);        

