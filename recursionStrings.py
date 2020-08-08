def changeOccurence(inputString,a,b):
    if len(inputString) == 0:
        return inputString

    smallString = changeOccurence(inputString[1:],a,b)
    if inputString[0] == a:
        return b + smallString
    else:
        return inputString[0] + smallString

print(changeOccurence("dacdxcd",'c','x'))