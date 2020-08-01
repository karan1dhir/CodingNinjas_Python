# s = 'this is a word string having many many word'
# k = 2
# words = s.split()
# d = {}
# for w in words:
#     d[w] = d.get(w,0) + 1
# print(d)    
# for w in d:
#     if d[w] == k:
#         print(w)

input_string = 'aaabbccdsa'
output_string = ''
count = 1
index = 0
i = 1
while i < len(input_string):
    if input_string[index] == input_string[i]:
        count += 1
        i += 1 
    else:
        output_string = output_string + input_string[index] + str(count)
        index = i
        count = 0
output_string =   output_string + input_string[index] + str(count)      
print(output_string)        






    