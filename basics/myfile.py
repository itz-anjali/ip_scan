'''
file handelimg

<name>  = open("filename.txt" , <mode{r, w, a}>)
r = reading 
w = writeing
a = appending
<virable name> = <name>.read()
print(<variablename>)

'''
# reading mode
f = open("file.txt", "r")
data  = f.read()
print(data)
f.close

'''
writing 
if we use only w then it earse pervious data from are 
'''
f = open("file2.txt" , "w" )
data2 = f.write ("earse  msg ")
print ("suecessfully")
f.close

'''
append
when the run this code whenever it append always 
'''
f = open("file.txt" , "a")
f.write("\n append the next line")
f = open("file.txt" , "r")
data3 = f.read()
print(data3)
f.close