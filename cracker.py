#password cracker
from random import*
import os
u_pwd= input('Enter Password: ')
pwd=[' ','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','u','v','w','x','z',0,1,2,3,4,5,6,7,8,9]
pw=''
while (pw!=u_pwd):
    pw=''
    for letters in range(len(u_pwd)):
        guess_pwd=pwd[randint(0,6)]
        pw=str(guess_pwd)+str(pw)
        print(pw)
        print('Cracking pasword...Please Wait')
        os.system('cls')
print('Your password is :',pw)