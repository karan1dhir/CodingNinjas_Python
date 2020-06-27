def checkPalindrome(num):
    reverseNumber = 0
    initialNumber = num
    while num > 0:
        last = num % 10
        reverseNumber = reverseNumber * 10 + last
        num = num // 10
    if  reverseNumber == initialNumber:
        return True
    else:
        return False
		
num = int(input())
isPalindrome = checkPalindrome(num)
if(isPalindrome):
	print('true')
else:
	print('false')
