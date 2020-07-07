number = int(input())
list = []
for i in range(0,number):
    element = int(input()) 
    list.append(element)
sum = 0
for i in list:
    sum = sum + i
print(sum)