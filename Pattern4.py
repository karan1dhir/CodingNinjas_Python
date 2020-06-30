## Read input as specified in the question.
## Print output as specified in the question.
number = 5
index = 1
while index <= number//2 + 1:
    spaces = 1
    while spaces <= (number//2 - index + 1):
        print(' ',end="")
        spaces += 1
    index1 = 1    
    while index1 <= (2 * index - 1):
        print('*',end="")
        index1 += 1
    print()
    index += 1  
index2 = 1
while index2 <= number//2 :
    spaces = 1
    while spaces <= index2:
        print(' ',end="")
        spaces += 1
    index1 = 1   
    count = number //2 - index2 + 1
    while index1 <= 2 * count - 1:
        print('*',end="")
        index1 += 1
    print()
    index2 += 1