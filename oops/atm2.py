# example of basic Encapsulation and  Abstraction 

class ATM:
    def __init__(self):
        self.__pin = "1234"  # ENCAPSULATION: Pin ko '__' lagakar chhupa diya (Private)

    def paise_nikalo(self):
        # ABSTRACTION: User ko bas ye function dikh raha hai
        # Andar ki checking user ko nahi dikhegi
        pin_check = input("Pin batao: ")
        
        if pin_check == self.__pin:
            print("Ye lo paise! 💵")
        else:
            print("Galat Pin! ❌")

my_atm = ATM()

my_atm.paise_nikalo()  #<-- Ye chalega (Public Interface)
# print(my_atm.__pin)    <-- Ye ERROR dega! Kyunki Encapsulation ne protect kiya hai.