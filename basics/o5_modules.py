# make a search bar for your system
import os 
'''
check the dir in / 
as well as print os name 
different computer have different os name 
'''
# path = "/"
# dir_list = os.listdir(path) 
# print("Files and directories in '", path, "' :") 
# for dir in dir_list:
#     print(dir)

# print("name of os")
# print(os.name)

'''
searching of file in your system
here is the code
we use os.walk()
it help to check all the drive floder 
it always check :
root: Abhi hum kis folder mein khade hain.
dirs: Yahan aur kaunse folders hain.
files: Yahan kaunsi files padi hain.
'''

print ("welcome to search system bar:~ ")
user = input('enter your file name : ')
print("searching your file....")
drives = ["C:\\", "D:\\", "E:\\"]
flag = False

try:
    for drive in drives:
        for root ,dirs , files in os.walk(drive):
            for file in files :
                name = file.split(".")[0]
                if user == name :
                    location = os.path.join(root ,  user)
                    print(location)
                    flag = True
                    break
except:
    print("something wrong try!")

if flag == False:
    print("this file is not in your system:~")
else:
    print( "\n done checking")