"""

HELLO HACKERS THIS CODE IS FOR BRUTE FORCE PASSWORD GANERATER SCRIPT THAT WILL HELPS TO CREATE PASSWORS TO DO Dictionary attack

SO LETS IMPORT RANDAM
FOR RANDAM PASSWORD GENERATION

SO LETS IMPORT TERMCOLOR
FOR COLORING THE CODE
LIKE A PRO

A SMALL CODE BY SAI KAMESH SHARMA

"""
import random
import termcolor
import time
from time import strftime
import hashlib
import os
def banner():
    os.system('clear')
    os.system('figlet Hash BruteForce Genereter [!] | lolcat')
t = strftime("%H:%M:%S", time.localtime())
char = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789`~!@#$%^&*()-_+="
caplistchar = list(char)
os.system('clear')
os.system('figlet Program is starting [=]|lolcat')
time.sleep(10)
os.system('figlet [======///////////]|lolcat')
time.sleep(5)
os.system('figlet [=========////////]|lolcat')
time.sleep(15)
os.system('figlet [===========//////]|lolcat')
time.sleep(2)
os.system('figlet [=================]|lolcat')
banner()
hash = input(termcolor.colored("[!] Enter the MD5 hash [+] ",color="blue"))
pwd = input(termcolor.colored("[!] Enter the max lenth of password [+] example : kala@50,hello etc [!]  ",color="red"))
sample_pwd = ''
try:
        for num in range(1,500000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000):
          sample_pwd = random.choices(caplistchar,k=len(pwd))
          sample_pwd = str(sample_pwd).replace('[','').replace(']','').replace(',','').replace("'","")
          save = open("brute.txt", 'w').write(str(sample_pwd))
          hash_open = open("brute.txt","r").read().strip()

          print(termcolor.colored("<============[" + str(hash_open) + "]========  " + "[START TIME] " + str(t) + " [CURRENT TIME] " + strftime("%H:%M:%S") + " ======>   "+" [Password Serial number] "+ str(num) +"  [KALA@185 KNONE AS SAI KAMESH ]",color="green"))

          hash_word = hash_open.encode('UTF-8')
          hash_encode = hashlib.md5(hash_word)
          digiest = hash_encode.hexdigest()
          if digiest == hash:
              print(termcolor.colored(f"[+] [ Password cracked ][PASSWORD IS  {hash_open} ] [ Password sereal number {num} ] [START TIME {t} ] [ END TIME {strftime('%H:%M:%S')} ]", color='blue'))
              break
except KeyboardInterrupt as e:
        print(termcolor.colored("[+] THANKS FOR USING MY TOOL [+]",color="blue"))
        print(termcolor.colored("Made by sai kamesh sharma ",color="blue"))
