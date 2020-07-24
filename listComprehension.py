li = [1,2,3,4]
li_new = [ele**2 for ele in li];
print(li_new);
li_even_new = [ele**2 for ele in li if ele%2 ==0]
print(li_even_new)

li = [1,2,3,4,5,6,7,8,9]
li_new = [ele**2 for ele in li if ele %2 == 0 if ele%3 ==0]
print(li_new);

li_1 = [1,2,3,4,5]
li_2 = [2,4,6,7]
li_inter = [ele for ele in li_1 for ele2 in li_2 if ele == ele2]
print(li_inter)

li = [1,2,3,4,5]
li_new = [ele**2 if ele %2 ==0 else ele for ele in li]
print(li_new)

s = 'Parikh'
li_new = [ele for ele in s]
print(li_new)

li = ['Parikh','Rohan','Ankush']
li_2d = [[ s for s in ele] for ele in li]
print(li_2d)

li = [ele**2 for ele in range(10) if ele%3 ==0]
print(li)
li = [[ i*j for j in range(4)] for i in range(3)]
print(li)