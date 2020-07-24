string1 = 'p'
string2 = 'q'
answer = 'true'
newlist = []

for index in range(0,256):
    newlist.append(0)
for str in string1:
    newlist[ord(str)] += 1
for str in string2:
    newlist[ord(str)] -= 1

for index in range(0,256):
    if newlist[index] is not 0:
        answer = 'false'
        break
if answer:
    print('true')
else:
    print('false')