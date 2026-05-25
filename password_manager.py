from cryptography.fernet import Fernet

'''
def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)
        '''

def load_key():
    file = open("key.key", "rb")
    key = file.read()
    file.close()
    return key

master_pwd = input("Enter Your Master Password")
key = load_key() + master_pwd.bytes
fer = Fernet(key)



def add():
    name = input("Account Name: ")
    pwd = input("Password: ")

    with open('password.txt','a') as f:
        f.write(name + "|" + pwd +'\n')


    


def view():
    with open('password.txt') as f:
        for line in f.readlines():
            data = line.strip()
            user, passw = data.split("|")
            print(f"Username is {user} \nPassword is {passw} ")

def main():
    
    while True:
        mode = input("Type 1 to view your passwords \nType 2 to add new passwords \nType 3 for Quiting ")

        if mode.isdigit():
            mode = int(mode)
            if mode == 1:
                view()
                continue

            elif mode == 2:
                add()
                continue

            elif mode ==3:
                quit()

            else:
                print("Invalid Number")
            break
        else:
            print("Not a Choise")
            continue
    



main()