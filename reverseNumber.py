number = 4321
reverseNumber = 0
while number > 0:
    last = number % 10
    reverseNumber = reverseNumber * 10 + last
    number = number // 10
print(reverseNumber)    