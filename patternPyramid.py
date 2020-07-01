## Read input as specified in the question.
## Print output as specified in the question.
number = 4
index = 1
while index <= number:
    spaces = 1
    while spaces <= index - 1:
        print(' ',end="")
        spaces += 1
    index2 = 1
    while index2 <= number - index + 1:
        print(index2 + index -1,end='')
        index2 += 1
    print()
    index += 1
index2 = 1  
while index2 <= number - 1:
    spaces = 1
    while spaces <= number - index2 -1:
        print(' ',end="")
        spaces += 1
    index3 = 1
    while index3 <= index2 + 1:
        print(number - index3 +1,end="")
        index3 += 1
    print()
    index2 += 1