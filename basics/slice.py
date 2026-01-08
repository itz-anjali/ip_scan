# string slicing examples
nm= "harry"
print(nm[6:1:-1])  # prints yrra

# [start:end:step] slicing syntax
'''
[-4:-2]
-4 means start from 4th last character
length of string is 5 -2 = 3rd last character
'''
a="bca"
print(a[100:])  # prints full string
'''
agar slicing range se bahar ho to bhi program crash nhi hota
bs empty string print kr deta hai
'''
name = input("Enter your name: ")
print(name[: : -1])  # prints the name in reverse order
print(name[::-2])
'''
-2 means print characters from last with a step of 2
so if name is "harry"
it will print "yrh"

'''
print(name[:-1])
'''
prints the string except the last character
start 0 se or last me 1 chhod ke ruk jayega
example soni
prints "son"
'''