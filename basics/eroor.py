# handling error
'''
try:
   code that may cause error
except:
    code to handle the error

finally:
    code that will run no matter what
    ye tb useful jb try except or finally ek def funcation me ho

'''
'''
 raise valueError("This is an error message")
 ye use coder custom error message dena chahte hai 
'''
a = input("Enter a number: ")
if a =="quit":
    raise SystemExit("You chose to exit the program.")
a = int(a)
if a < 5 or a>9 :
    raise ValueError("The number is not in the range 5-9.")
    
else:
    print("Program completed successfully.")