import requests
import random
from colorama import Fore
import threading

with open('data/member_ids.txt') as f:
    member_ids = f.read().splitlines()
with open('data/tokens.txt') as f:
    tokens = f.read().splitlines()

CHANNEL_ID = input(f"{Fore.LIGHTBLUE_EX}[{Fore.WHITE}>{Fore.LIGHTBLUE_EX}]: {Fore.WHITE}Channel ID ?: ")
MESSAGE = input(f"{Fore.LIGHTBLUE_EX}[{Fore.WHITE}>{Fore.LIGHTBLUE_EX}]: {Fore.WHITE}Message ?: ")
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
        emojilist = ['😀', '😁', '😂', '🤣', '🫥', '😎', '🤑', '🤢', '🥶']
        ezem = random.sample(emojilist, 2)
        emmen = " ".join([f" {em}" for em in ezem])
        member_ids_selected = random.sample(member_ids, 6)
        members_mentioned = " ".join([f"<@{id}>" for id in member_ids_selected])
        message_with_member_id = f'{members_mentioned} {message} {emmen}'

        data = {'content': message_with_member_id}
        response = requests.post(url, headers=headers, json=data)
        print(response.text)

threads = []
for token in tokens:
    thread = threading.Thread(target=send_message, args=(token,))
    thread.start()
    threads.append(thread)

for thread in threads:
    thread.join()
