arr = [2 ,4,7,2,7]
list = []
element_unique = 0 
for index in range(0,256):
      list.append(0)
    
for index in range(len(arr)):
   list[arr[index]] += 1

print(list)    
for index in list:
   if list[index] == 1:
      element_unique = index
      break
print(element_unique)   