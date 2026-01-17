import os
from cryptography.fernet import Fernet, InvalidToken

PASS_FILE = "passwords.txt"      
KEY_FILE = ".secret.key"         

def load_or_create_key() -> bytes:
    if not os.path.exists(KEY_FILE):
        print("No key found. Generating new one...")
        key = Fernet.generate_key()
        with open(KEY_FILE, "wb") as f:
            f.write(key)
       
        if os.name != 'nt':
            os.chmod(KEY_FILE, 0o600)
        print("New encryption key created.")
        return key

    with open(KEY_FILE, "rb") as f:
        return f.read()


def add_password():
    fer = Fernet(load_or_create_key())

    uname = input("Username / Email / Service: ").strip()
    if not uname:
        print("Username cannot be empty.")
        return

    passwd = input("Password: ").strip()
    if not passwd:
        print("Password cannot be empty.")
        return

    encrypted = fer.encrypt(passwd.encode()).decode()

    with open(PASS_FILE, "a", encoding="utf-8") as f:
        f.write(f"{uname}|{encrypted}\n")

    print("Credential saved.")


def view_passwords():
    if not os.path.exists(PASS_FILE) or os.stat(PASS_FILE).st_size == 0:
        print("\nNo passwords stored yet.\n")
        return

    fer = Fernet(load_or_create_key())

    print("\n" + "═"*50)
    print("      STORED CREDENTIALS")
    print("═"*50)

    try:
        with open(PASS_FILE, encoding="utf-8") as f:
            for line in f:
                line = line.rstrip()
                if not line or '|' not in line:
                    continue

                uname, enc_pass = line.split("|", 1)
                try:
                    password = fer.decrypt(enc_pass.encode()).decode()
                    print(f" {uname:24} :  {password}")
                except InvalidToken:
                    print(f" {uname:24} :  [DECRYPTION FAILED - wrong key?]")
    except Exception as e:
        print(f"Error reading/decrypting file: {e}")

    print("═"*50 + "\n")


def main():
    while True:
        print("\n" + "─"*40)
        print("  (a)dd   (v)iew   (q)uit")
        print("─"*40)
        choice = input("→ ").strip().lower()

        if choice in ("q", "quit", "exit"):
            print("Goodbye!\n")
            break
        elif choice == "a":
            add_password()
        elif choice == "v":
            view_passwords()
        else:
            print("Invalid choice. Use a/v/q")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nInterrupted. Bye! 👋")