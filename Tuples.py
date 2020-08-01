# a = 1,2
# print(a)


# def sum(a,b,*more):
#     print(a)
#     print(b)
#     ans = a + b
#     for i in more:
#         ans = ans + i
#     return ans    
# ans = sum(1,2,3,4)  
# print(ans)  


def sum_diff(a,b):
    return a + b, a - b


c = sum_diff(4,1)
print(c)