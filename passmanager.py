
FILE = "testpass.txt"

def add():

    uname = input("User Name: ")
    passwd = input("Password: ")

    with open(FILE, 'a') as f:
        f.write(f"{uname}|{passwd}\n")

def view():
    
    print("**************USER CREDENTIALS**************\n")
    with open(FILE, 'r') as f:
            
            for line in f.readlines():

                credential = line.rstrip()
                uname, passwd = credential.split("|")
                
                print(f"username:{uname}, password:{passwd}")
            
        
        
    print(44*"*", "\n")



while True:

    mode = input("\n(v) to view or (a) to add password (q) to quit: ").lower()

    if mode == "q":

        break

    elif mode == "a":

        add()
    
    elif mode == "v":

        view()

    else:
        print("Invalid input...")
        continue

