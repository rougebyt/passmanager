
# 🔐 Simple Password Manager CLI

A lightweight, **command-line password manager** written in Python.  
It securely stores your credentials using **Fernet** symmetric encryption (from the `cryptography` library).

Perfect for learning purposes or personal use on a single trusted device.

## Features

- AES-128 encryption in CBC mode + HMAC (via Fernet)
- Stores usernames and encrypted version of passwords
- Automatic key generation & storage (single key file)
- Simple text-file based storage (human-readable encrypted format)

## Important Security Notes

⚠️ **This is NOT production-grade software**  
Use it only for learning or very low-risk personal credentials.

Current limitations / known trade-offs:

- Single encryption key stored in plain file (`.secret.key`)
- No master password / key derivation
- No salt / key stretching
- File-based storage (not resistant to physical access)
- Very basic — no categories, search, copy-to-clipboard, etc.

## Installation

1. Make sure you have Python 3.7+ installed
2. Install the only required dependency:

```bash
pip install cryptography
```

3. Clone the repository:

```bash
git clone https://github.com/rougebyt/passmanager.git
cd passmanager
```

4. (Optional) Create a virtual environment:

```bash
python -m venv venv
source venv/bin/activate    # Linux/Mac
venv\Scripts\activate       # Windows
```

## Usage

```bash
python passmanager.py
```

Commands:

```
(a)dd   →  Add new username + password
(v)iew  →  Show all saved credentials (decrypted)
(q)uit  →  Exit the program
```

Example flow:

```
→ a
User Name: henrycreel
Password: mindflayer2026!

→ v

**************USER CREDENTIALS**************
username:henrycreel, password:mindflayer2026!
********************************************
```

## Project Structure

```
simple-password-manager/
├── passmanager.py              
├── .secret.key          # generated encryption key (do NOT commit!)
├── passwords.txt        # encrypted credentials
└── README.md
```


## How It Works (Quick Overview)

1. Generates (or loads) a Fernet key → stored in `.secret.key`
2. Each credential is encrypted separately → `username|encrypted_password`
3. Uses `cryptography.fernet.Fernet` for encryption/decryption
4. Very straightforward implementation — great for learning symmetric encryption basics

## Future Improvement Ideas

- Add master password + PBKDF2 key derivation
- Better key management (environment variable, keyring, etc.)
- Search/filter credentials
- Categories / tags
- Copy password to clipboard
- Export/Import functionality

## License

MIT License — feel free to use, modify, and learn from this code!

Made with curiosity & coffee ☕  
Happy (secure) coding! 🐦‍⬛

```

