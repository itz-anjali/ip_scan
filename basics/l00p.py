# for loop 
colors = ["red", "green", "blue"]
for color in colors:
    print(color)
    for x in color:
        print(x)

# range use hota hai kaha se kaha tk print karna hai
# for i in range(1,5000):
#     print(i)

# range(start, stop, step) 
for i in range(1, 11, 3):
    print(i)

'''
while loop
 condition true hai tab tk chalega
i = 1
 while i<=10:
        print(i)
        i += 1 yha increment karna jaruri hai nahi to infinite loop me chala jayega
        or yaha condition lgta hai fir upar jaa kr fir check hoga

'''
# creat a game using while loop
num = int(input("Enter a number between 1 to 10: "))
while num<=8:
    print("You entered:", num)
    num = int(input("Enter a number between 1 to 10: ")) 
print("You win the game!")
print("You entered:", num)

# jb tk true hai tb tk chalega

# table 
num1 = int(input("Enter a number to print its table: "))
for i in range(0,12):
    print(f"{num1} x {i} = {num1*i}")
    if i==10:
        print("Table printed successfully.")
        break

# break loop se nikl jayega or continue loop ko skip kr dega ek particular condition pr

for i in range (6):
    print(i)
    if i==3:
        print("loop is broken")
        break
else:
    print("sorry loop is ended")