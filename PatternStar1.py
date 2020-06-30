number = int(input())
index = 1
while index <= number:
    spaces = 1
    while spaces <= number - index:
        print(' ',end="")
        spaces += 1
    index1 = 1 
    index2 = 1
    while index1 <= index:
        print('*',end="")
        index1 += 1
    while index2 < index:
        print('*',end="")
        index2 +=1
    print()
    index+=1