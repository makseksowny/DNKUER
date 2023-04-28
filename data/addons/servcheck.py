__web__ = "https://bypasstool.xyz" # Bypass ©
###################################################################################################################################################
import tempfile
import os
import webbrowser
from colorama import Fore
import requests
###################################################################################################################################################
x = requests.get(f'{__web__}')                                                                                                          
if x.status_code == 200:
    pass
else:
    input(f"{Fore.LIGHTRED_EX}[{Fore.WHITE}>{Fore.LIGHTRED_EX}]: {Fore.WHITE}bypasstool.xyz is down right now, contact the dev")
    exit()
###################################################################################################################################################
filename = "joineddd.txt"
temp_file_path = os.path.join(tempfile.gettempdir(), filename)
if os.path.exists(temp_file_path):
    pass
else:
    os.system('title Bypass     ^|     ERROR')
    input(f"{Fore.LIGHTRED_EX}[{Fore.WHITE}!{Fore.LIGHTRED_EX}]: {Fore.WHITE}You Need to Join The Bypass Server to use this Tool, Press ENTER")
    webbrowser.open("https://discord.gg/pXvUmqJhJN")
    with open(temp_file_path, "w") as f:
        f.write("You Joined The Server.\nYou Can use Bypass now. Enjoy ✅")
###################################################################################################################################################