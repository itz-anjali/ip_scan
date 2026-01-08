# convert english in secret code
'''

 if the word contains atleast 3 characters,
 remove the first letter and append it at the end
 Decoding:
 if the word contains less than 3 characters, reverse it
 else:
the beginning
now append three random characters at the starting and the end
else:
simply reverse the string
remove 3 random characters from start and end.
 Now remove the last letter and append it to
'''

def encode(user):
        try:
            msg = user.split( )
            new_msg = []
            for i in msg :
                if (len(i) < 3):
                    msg = i[::-1]
                    new_msg.append(msg)

            # slicing ka use hota hai words or   append , pop
            # reverse ye sb keywprd use nhi hota vo list me hota hai
                else:
                    msg = i[1:] + i[0]
                    data = "fgjk" + msg + "jkfg"
                    new_msg.append(data)
            return  " ".join(new_msg)
        except:
            print("something wrong try next time ")
        finally:
                print("your msg is encoded now ")

def decode(user):
        try:
            msg = user.split( )
            new_msg = []
            for i in msg :
                if (len(i) < 3):
                    msg = i[::-1]
                    new_msg.append(msg)
                else:
                    msg = i[4:-4]
                    data = msg[-1] + msg[:-1]
                    new_msg.append(data)
            return  " ".join(new_msg)
        except:
            print("something wrong try next time ")
        finally:
                print("your msg is encoded now ")

while True:  
    print (" welcome to secert coder language translater")
    print("select option \n a) encode \n b) decode")
    option = input("a or b  or q : \n")
    if (option == "a"):
        user = input("enter your decoding msg: " )
        result = encode(user)
        print(result)
    elif (option == "q"):
         print("bye")
         break  
    else:
        user = input("enter your encoding msg : ")
        result = decode(user)
        print(result)
       
        
     