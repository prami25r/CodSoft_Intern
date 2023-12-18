import random

lower="abcdefghijklmnopqrstuvwxyz"
upper="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
num="1234567890"
symbols="!@#$%^&*()_+=-.<>?/;:[}{]"
string=lower+upper+num+symbols
length=int(input("Enter the length of the password:"))
password="".join(random.sample(string,length))
print(password)