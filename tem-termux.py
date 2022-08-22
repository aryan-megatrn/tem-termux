#aryan
#love atnam♥❣️
import os
import random
from random import randint
import string
import uuid
import time 
from time import sleep
from colorama import Fore
import sys
###########
print("\n"*10)
print("""\033[31m
 __  __ _____ ____    _  _____ ____  _   _
|  \/  | ____/ ___|  / \|_   _|  _ \| \ | |
| |\/| |  _|| |  _  / _ \ | | | |_) |  \| |
| |  | | |__| |_| |/ ___ \| | |  _ <| |\  |
|_|  |_|_____\____/_/   \_\_| |_| \_\_| \_|\033[32m""")
soheil = """
\033[41m[1]\33[1;0m  \033[32m Flower
\033[41m[2]\33[1;0m  \033[32m skeleton
\033[41m[3]\33[1;0m  \033[32m Computer
\033[41m[4]\33[1;0m  \033[32m parrot"""
#
for i in soheil:
	sleep(0.05)
	print(i,end='',flush=True)
print()
################
shah = int(input(Fore.CYAN+"     \033[41m[?]\33[1;0m"+"\33[1; \033[31mType number \033[32m◈─━─━─━─━\033[34m❯❯❯  \033[93m"+Fore.RED+""))
################################## 
if(str(shah) == "1"):
  os.system("cd Flower&&bash install.sh")
###############################
if(str(shah) == "2"):
  os.system("cd اسکلت&&bash install.sh")
###############################
if(str(shah) == "3"):
  os.system("cd Computer&&python Computer.py")
###############################
if(str(shah) == "4"):
  os.system("cd parrot&&bash install.sh")
  
