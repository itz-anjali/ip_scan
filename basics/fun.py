# MAKE A FUNCATION

def force( m ,a):
    F = m * a
    print("The force is: ", F)
    

m= int(input("Enter mass: "))
a= int(input("Enter acceleration: "))
force(m ,a)

# greet your name
def greet (fname,lname = " kumari "):
    print("Hello", fname, lname)

fname= input("Enter girl first name: ")
greet(fname )