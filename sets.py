a = {"apple","abc",23}
a.remove('apple')
a.discard(23)
print(a)
## a.pop() - remove on , we dont know

# functions of sets
a = {1,2,3,4}
b = {3,4,5,6}
print(a.intersection(b))
print(a.union(b))
print(a.difference(b))
print(a.symmetric_difference(b)) # union minus intersection
print(a.intersection_update(b))
a.difference_update(b)
a.symmetric_difference_update(b)
print(a)

a.issubset(b)
a.isdisjoint(b)
a.issuperset(b)
