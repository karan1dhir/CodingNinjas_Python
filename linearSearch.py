number = int(input())
list = [int(x) for x in input().split()]
element = int(input())
isFound = False
for index in range(0,len(list)):
    if list[index] == element:
        print(index)
        isFound = True
        break;
if isFound is False:
    print(-1)