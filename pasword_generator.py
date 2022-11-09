import random
run = True
newList = []
tupla = ""
FILE_NAME = 'Passwords.txt'

def generate_password():
    CapitalLetter = ('A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z')
    LowercaseLetter = ('a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z')
    numbers = ('0','1','2','3','4','5','6','7','8','9')
    password = ""
    CharsList = (CapitalLetter,LowercaseLetter,numbers)
    for i in range(random.randint(8,16)):
        Char = random.choice(CharsList)
        password = password + random.choice(Char)

    #print(password)    
    if(any(chr.isdigit() for chr in password) and any(chr.isupper() for chr in password) and any(chr.islower() for chr in password) and len(password)>8 and len(password)<=16):
        #print(password)
        return password
    else:
        print("not valid password")

def register_password(name_app, password):
    password_list = {"Application": name_app, "Password": password}
    newList.append(password_list)
    print(password_list)
    file = open(FILE_NAME, 'w')
    file.write(str(newList))
    return password_list    

def get_tuple(tuple):
    file = open(FILE_NAME, 'r')
    print(file.read())
    file.close()

while run:    
    print("MENU")
    print("1. Generate Password")
    print("2. Get Password")
    print("3. Exit\n")
    user_option = input("Select your option: ")

    if user_option == "1":
        app_name = input("Enter the application name: ")
        print("Your password is:")
        pass_text = str(generate_password())
        print(pass_text)
        print("\n")
        tupla = register_password(app_name,pass_text)        
    
    if user_option == "2":
        get_tuple(tupla)   

    if user_option == "3":
        print("Finish program")
        run = False