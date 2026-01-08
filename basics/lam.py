'''
lambda () one liner funcation likhne me hota hai 
or funcation ke andar funcation pass bhi liya jata hai 
'''
from functools import reduce  # for reduce
def fun(fx , data ):
    return 3 + fx(data)

mul = lambda x  : x *2
print (f"{mul(2)} this is average ")
print (fun(mul, 4 ))

# map ,filter , reduce
# map
def tabel(x):
    t = []
    for i in range(1,11):
       
        t.append(i*x)
    return t
    

l =[1,2,5,4]
newl  = list(map(tabel , l))
print(newl , type(newl))

# filter

def funcation_list(a):
    return a > 4

newf= list(filter(funcation_list , l))
print(newf)

# reduce

newr= reduce( lambda x ,y : (x+y)/2 , l)
print(newr)