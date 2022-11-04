##chars > 8 and chars <=16
##at least one capital letter (ASKSLD)
##at least one number (0-9)
##at least one lower letter
import random
CapitalLetter = ('A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z')
LowercaseLetter = ('a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z')
numbers = ('0','1','2','3','4','5','6','7','8','9')
password = ""
CharsList = (CapitalLetter,LowercaseLetter,numbers)
passwordRange = ('9','10','11','12','13','14','15','16')
for i in range(int(random.choice(passwordRange))):
    Char = random.choice(CharsList)
    password = password + random.choice(Char)

#print(password)    
if(any(chr.isdigit() for chr in password) and any(chr.isupper() for chr in password) and any(chr.islower() for chr in password) and len(password)>8 and len(password)<=16):
    print(password)
else:
    print("not valid password")