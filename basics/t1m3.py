# time
import time 

timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
print("Current Timestamp:", timestamp)
timestamp = time.strftime("%H")
print(timestamp)
timestamp = time.strftime("%M")
print(timestamp)    
timestamp = time.strftime("%S")
print(timestamp)
name = input("Enter your name: ")
if timestamp>"20":
    print(name, "Good Night")
elif timestamp>"16":
    print(name, "Good Evening")
elif timestamp>"12":
    print(name, "Good Afternoon")
elif timestamp>"4":
    print(name, "Good Morning")
else:
    print(name, "Good Night")