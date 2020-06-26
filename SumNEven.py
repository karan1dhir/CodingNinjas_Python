## Read input as specified in the question.
## Print output as specified in the question.
n = int(input())
count = 1
sum = 0
while count <= n:
    if count % 2 == 0:
        sum += count
    count += 1
print(sum)