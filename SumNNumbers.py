def sum_n(n):
    if n == 0:
        return 0
    smallAns = sum_n(n-1)
    return n + smallAns

sum_numbers = sum_n(5);
print(sum_numbers) 
