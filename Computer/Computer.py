import random
from random import randint
import string
import uuid
import os
import time 
from time import sleep
from colorama import Fore
import sys
###########
print("\n"*10)
print("""\033[32m
  ____ ___  __  __ ____  _   _ _____ _____ ____
 / ___/ _ \|  \/  |  _ \| | | |_   _| ____|  _ \
| |  | | | | |\/| | |_) | | | | | | |  _| | |_) |
| |__| |_| | |  | |  __/| |_| | | | | |___|  _ <
 \____\___/|_|  |_|_|    \___/  |_| |_____|_| \_\
\033[32m""") 
soheil = """
\033[41m[1]\33[1;0m  \033[32m Banner Computer1
\033[41m[2]\33[1;0m  \033[32m Banner Computer2
\033[41m[2]\33[1;0m  \033[32m Banner Computer3

"""
for i in soheil:
	sleep(0.05)
	print(i,end='',flush=True)
print()

shah = int(input(Fore.CYAN+"     \033[41m[?]\33[1;0m"+"\33[1; \033[31mSelect\033[32m◈─━─━─━─━\033[34m❯❯❯  \033[93m"+Fore.RED+""))
#
if(str(shah) == "1"):
  os.system("cd Computer1&&bash install.sh")
#
if(str(shah) == "2"):
  os.system("cd Computer2&&bash install.sh")
#
if(str(shah) == "3"):
  os.system("cd Computer3&&bash install.sh") 
