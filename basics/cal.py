# calculater

print("Welcome to the calculator!")
print("enter 1st number:")
num1= float(input())
print("enter 2nd number:")
num2= float(input())
print("Select operation -\n" 
      "1. Add\n" 
      "2. Subtract\n" 
      "3. Multiply\n" 
      "4. Divide\n")
operation =input("Enter operation number:")
if operation == '1':
    #  agar input ko show krna hai tho f me {} use krna hai
    print(f"{num1} + {num2} = {num1 + num2}")
elif operation == '2':
    print(num1 - num2)
elif operation == '3':
    print(num1 * num2)
elif operation == '4':
    if num2 != 0:
        print(num1 / num2)
    else:
        print("Error! Division by zero.")
else:
    print("Invalid operation selected.")
