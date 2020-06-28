number = int(input())
index = 1
while index <= number:
    index1 = 1
    char = chr(ord('A') + index -1)
    while index1 <= index:   
        print(char,end='')
        index1 += 1
        char = chr(ord(char) + 1)
    print()
    index += 1
    