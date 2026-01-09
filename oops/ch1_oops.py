# creat a students class and take 3 subject of marks and avg
class students:
    cllg = " cocs"
    def __init__(self , name ,maths , dsa ,c):
            self.name = name 
            self.maths = maths
            self.dsa = dsa
            self.c = c
    def avg (self):
          return (self.maths + self.dsa + self.c)/3
    def info (self):
          print (f"welcome {self.name} from {self.cllg} your 3 subject of marks average is {self.avg()}")

user = input("enter your name : ")
sub1 = int(input("enter your maths mark : "))
sub2 = int(input("enter your dsa mark : "))
sub3 = int(input("enter yourc mark : "))
a = students(user , sub1 ,sub2 ,sub3)
print(a.info())