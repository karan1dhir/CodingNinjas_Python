def reverse_list(li):
    length = len(li)
    for start in range(0,length//2):
        li[start] , li[length - start -1] = li[length - start -1] ,li[start]
li = [1,2,3,4,5]
reverse_list(li)
print(li)