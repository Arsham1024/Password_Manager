from cryptography.fernet import Fernet

'''
def write_key():
    key = Fernet.generate_key()
    # WB = write in bites
    # fernet generates a key in keyfile.
    with open("key.key", "wb") as key_file:
        key_file.write(key)
'''

def load_key():
    # Reading bytes mode =rb
    file = open("key.key", "rb")
    key = file.read()
    file.close()
    return key


master_pwd = input("Enter the master password: ")
key = load_key() + master_pwd.encode()
fer = Fernet(key)

def view():
    print("Here are the passwords:")
    with open("passwords.txt", "r") as r:
        for line in r:
            data = line.rstrip()
            user, passw = data.split("|")
            print("" + fer.decrypt(passw.encode()).decode() + "\n")
    print()

def add():
    name = input("Account name: ")
    pwd = input("password: ")

    with open("passwords.txt", 'a') as f:
        f.write(name + "|" + fer.encrypt(pwd.encode()).decode() + "\n")
    print()

while True:
    mode = input("What would you like to do?\n"
                 "1. add\n"
                 "2. view\n"
                 "3. quit\n")
    if mode == "3":
        print("Goodbye")
        break
    if mode == "2":
        print("--View Mode--\n")
        view()
    elif mode == "1":
        print("--Add Mode-- \n")
        add()
    else:
        print("--invalid mode--")
        continue
