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
 ____  ____  ____      _    ____  ___  _   _
|  _ \|  _ \|  _ \    / \  / ___|/ _ \| \ | |

| | | | | | | |_) |  / _ \| |  _| | | |  \| |
| |_| | |_| |  _ <  / ___ \ |_| | |_| | |\  |
|____/|____/|_| \_\/_/   \_\____|\___/|_| \_|
\033[32m""")
soheil = """
\033[41m[1]\33[1;0m  \033[32m Banner Dragon1
\033[41m[2]\33[1;0m  \033[32m Banner Dragon2
"""
for i in soheil:
	sleep(0.05)
	print(i,end='',flush=True)
print()

shah = int(input(Fore.CYAN+"     \033[41m[?]\33[1;0m"+"\33[1; \033[31mSelect\033[32m◈─━─━─━─━\033[34m❯❯❯  \033[93m"+Fore.RED+""))
#
if(str(shah) == "1"):
  os.system("cd Dragon1&&bash install.sh")
#
if(str(shah) == "2"):
  os.system("cd Dragon2&&bash install.sh") 
