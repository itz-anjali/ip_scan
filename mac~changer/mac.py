# mac changer project
# Changes made by macchanger are temporary and reset upon reboot.
import subprocess as ss 

print("welcome to mac ~ changer : \n")
print("--------------------------")
print("NEED SUDO POWER !")
print("--------------------------------")

print("select options \n 1)manual \n 2) random")

user1 = int(input())

try :
    ss.run(["ip", "link", "set", "eth0", "down"], check=True)
    if user1 == 1:
        user2 = input("Enter MAC address: ")
        result1 = ss.run(["macchanger", "-m" ,user2 ,"eth0" ], check=True)
        print("done!")
    elif  user1==2:
        result1 = ss.run( ["macchanger", "-r" ,"eth0" ], check=True)
        print("done!")
    else:
        print("INVALID!")
        exit()

    ss.run(["ip", "link", "set", "eth0", "up"], check=True)
    print("MAC address changed successfully")
except Exception as e:
    print("Error:", e)


print("-------------------------------------------------------------")