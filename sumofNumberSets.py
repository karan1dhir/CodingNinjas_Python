
def sumUnique(list):
    s = set()
    sum = 0
    for element in list:
        s.add(element)
    for element in s:
        sum += element
    return sum

sum_unique = sumUnique([1,2,3,4,5,1,2,3,4,5])
print(sum_unique)   