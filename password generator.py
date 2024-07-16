import random

upletters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
loletters = upletters.lower();
num = "0123456789"
symbols = "!@\\#$%|^&*()/*+-"
passchar = upletters+loletters+num+symbols

length = int(input("Enter the length of the password = "))

for i in range(3):
    password = ''.join(random.sample(passchar,length))
    print(password)