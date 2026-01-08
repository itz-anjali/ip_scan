# make a list
list =[ i for i in range(100) if i % 2 == 0]
print(list)
list.append(101)
print(list.count(0))

# set is well defined object which is not repeated
s ={1,2,3,4,5,6,7,8,9,1,2,3,4}
print(s)
s2 ={}
print(type(s2))

s2 = set()
print(type(s2))