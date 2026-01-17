from cryptography.fernet import Fernet
from os import path


PASS_FILE = "testpass.txt"
KEY_FILE = "key.key"


def write_key():
    try:
        key = Fernet.generate_key()
        with open(KEY_FILE, "wb") as key_file:
            key_file.write(key)

    except Exception as e:
        print("Couldn't write key: ",e)

def load_key():
        try:
            if not path.exists(KEY_FILE):
                write_key()
                with open(KEY_FILE, 'rb') as key_file:
                    key = key_file.read()
                return key

            else:
                with open(KEY_FILE, 'rb') as key_file:
                    key = key_file.read()
                return key
            
        except Exception as e:
            print("Couldn't load key because: ", e)


fer = Fernet(load_key())

def add():
    try:
        uname = input("User Name: ")
        passwd = input("Password: ")

        if uname != "" and passwd !="":
            with open(PASS_FILE, 'a') as f:
                encrypted_uname = fer.encrypt(uname.encode()).decode()
                encrypted_pass = fer.encrypt(passwd.encode()).decode()
                f.write(f"{encrypted_uname}|{encrypted_pass}\n")
        else:
            print("Invalid username or password")
            
    except Exception as e:
        print("Unable to add credentials due to: ", e)
     

def view():
    
    print("**************USER CREDENTIALS**************\n")
    with open(PASS_FILE, 'r') as f:
            
            for line in f.readlines():

                credential = line.rstrip()
                encrypted_uname, encrypted_pass = credential.split("|")

                uname = fer.decrypt(encrypted_uname.encode()).decode()
                passwd = fer.decrypt(encrypted_pass.encode()).decode()
                print(f"username:{uname}, password:{passwd}")
            
        
        
    print(44*"*", "\n")


def main():
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


if __name__ == '__main__':
    main()