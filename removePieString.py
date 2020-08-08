def replacePie(inputString):
    if len(inputString) == 0 or len(inputString) == 1:
        return inputString

    if inputString[0] == 'p' and inputString[1] == 'i':
       smallAns =  replacePie(inputString[2:])
       return '3.14' + smallAns;
    else:
        smallAns =  replacePie(inputString[1:])
        return inputString[0] + smallAns
    
print(replacePie('abcpidefpi'))