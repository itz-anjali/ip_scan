# creat atm show credit ,debit and print balance

class atm:
    def __init__(self , name ,amt):
        self.name = name
        self.amt = amt
    def credit (self):
        f= open("amt.txt" , "w")
        f.write(str(self.amt)) # file me bs str save hota hai
        f = open("amt.txt" , "r")
        data = f.read()
        return (f"{data} is added in your acc. {self.name} ")

    def debit (self , deb):
        final = self.amt - deb
        '''
        self.variable ka matlab hai wo cheez jo Class
         ke paas humesha rehti hai (Jaise self.name, self.amt).

        deb wo variable hai jo bahar se aaya hai
         (bracket ke andar). Wo ek "Mehmaan" hai.

        Mehmaan ke aage self nahi lagate.
        '''
        return (f"{self.name} your current money is {final}")
        
while True:
    print("welcome to our ATM \n")
    user = input("enter your name :")
    amount = int(input("enter your credited amt : "))
    a = atm(user,amount)
    print("what do you want \n 1) credit \n 2) debit:")
    user1 = int(input("enter your choice 1 or 2 : "))
    try :
        if user1 == 1 :
            print(a.credit())
        elif user1 == 2 :
            print(f"how much do you want to debit from {(amount)}")
            deb = int(input("enter your money : "))
            if deb > amount :
                print(f"aukaat ke anusar u have only {amount}")
            else:
                print(a.debit(deb))
        else:
            print("wrong option plx choose 1 or 2 ")
    except:
        print("something wrong try again!")


