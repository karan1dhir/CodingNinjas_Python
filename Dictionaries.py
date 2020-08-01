# a = {'the':3, 'a' : 4}
# b = a.copy()
# c = dict([('the',3),('a',5),('an',10)])
# print(c)
# print(b)

# d = dict.fromkeys(["abc",32,4],10)
# print(d)



a = {1:2,3:4,'list':[1,2,4],'dict':{1,2}}
c = a.get(100,0)
print(a.keys())
print(a.values())
print(c)

for i in a:
    print(i,a[i])

for i in a.values():
    print(i);    

print("list" in a)    


# to update a.update(b)
# to remove a.pop() , del a[1]
# to clear a.clear()
# to delete (del a)


