master_pwd = input("Enter the master password: ")

def view():
    pass
def add():
    name = input("Account name: ")
    pwd = input("password: ")

    with open("passwords.txt", 'a') as f:
        f.write(name + "|" + pwd + "\n")

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