def reverseWord(startIndex,endIndex,string):
    newString = ''
    while startIndex <= endIndex:
        newString = newString + string[endIndex]
        endIndex -= 1
    return newString

string = "Welcome to Coding Ninjas"
startIndex = 0
endIndex = 0
reverseString = ''
while endIndex < len(string):
    if (string[endIndex] == ' ') or (string[endIndex] in '\n' and endIndex <len(string)):
        reverseString = reverseString  + reverseWord(startIndex,endIndex - 1,string) + " "
        endIndex = endIndex + 1
        startIndex = endIndex
    else:
        endIndex += 1
print(reverseString)        