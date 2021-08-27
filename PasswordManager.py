from cryptography.fernet import Fernet


master_pwd = input("Enter the master password: ")

def view():
    print("Here are the passwords:")
    with open("passwords.txt", "r") as r:
        for line in r:
            print("" + line.rstrip())
    print()

def add():
    name = input("Account name: ")
    pwd = input("password: ")

    with open("passwords.txt", 'a') as f:
        f.write(name + "|" + pwd + "\n")
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
