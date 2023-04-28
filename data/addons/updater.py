import requests, os, webbrowser
from colorama import *
os.system('title Checking For Updates..')

update = f'''{Fore.LIGHTBLUE_EX}
                                 █    ██  ██▓███  ▓█████▄  ▄▄▄     ▄▄▄█████▓▓█████ 
                                 ██  ▓██▒▓██░  ██▒▒██▀ ██▌▒████▄   ▓  ██▒ ▓▒▓█   ▀ 
                                ▓██  ▒██░▓██░ ██▓▒░██   █▌▒██  ▀█▄ ▒ ▓██░ ▒░▒███   
                                ▓▓█  ░██░▒██▄█▓▒ ▒░▓█▄   ▌░██▄▄▄▄██░ ▓██▓ ░ ▒▓█  ▄ 
                                ▒▒█████▓ ▒██▒ ░  ░░▒████▓  ▓█   ▓██▒ ▒██▒ ░ ░▒████▒
                                ░▒▓▒ ▒ ▒ ▒▓▒░ ░  ░ ▒▒▓  ▒  ▒▒   ▓▒█░ ▒ ░░   ░░ ▒░ ░
                                ░░▒░ ░ ░ ░▒ ░      ░ ▒  ▒   ▒   ▒▒ ░   ░     ░ ░  ░
                                 ░░░ ░ ░ ░░        ░ ░  ░   ░   ▒    ░         ░   
                                   ░                 ░          ░  ░           ░  ░ 
                                   
                                   '''


web = "https://bypasstool.xyz"
version = "V3.1"
lookingforup = requests.get(web)
content = lookingforup.content.decode('utf-8')
if version in content:
    os.system('title No Update Found')
    pass
else:
    os.system('title Update Found')
    print(update)
    input(f"{Fore.LIGHTBLUE_EX}[{Fore.WHITE}>{Fore.LIGHTBLUE_EX}]{Fore.WHITE}: Version: {version} is Outdated, Press {Fore.LIGHTBLUE_EX}ENTER{Fore.WHITE} to Install it.")
    webbrowser.open('https://bypasstool.xyz')
    exit()
