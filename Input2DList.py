# str = input().split()
# n,m = int(str[0]), int(str[1])
# li = [[int(j) for j in input().split()] for i in range(n)]
# print(li)


# n = int(input())
# li = [[int(j) for j in input().split()] for i in range(n)]
# print(li)


# str = input().split()
# n,m = int(str[0]), int(str[1])
# b = input().split()
# arr = [ [int(b[m*i + j]) for j in range(m)] for i in range(n)]
# print(arr)


# str = input().split()
# n,m = int(str[0]), int(str[1])
# b = str[2:]
# arr = [ [int(b[m*i + j]) for j in range(m)] for i in range(n)]
# print(arr)


li=[[1,2,3,4],[5,6,7,8],[9,10,11,12]]
for j in range(4):
    for ele in li:
        print(ele[j],end = ' ')


        