import requests
import json
from pick import pick
import os
import sys

version = "1.0.0"


# ------------------------------- Installation ------------------------------- #
try: 
    from colorama import Fore, Style, init
except ModuleNotFoundError:
    os.system(f'{sys.executable} "pip install colorama"')

try: 
    from pathlib import Path
except ModuleNotFoundError:
    os.system(f'{sys.executable} "pip install path"')

# ---------------------------------- Colors ---------------------------------- #

b = Style.BRIGHT
w = b+Fore.WHITE
c = b+Fore.CYAN

# ---------------------------- Custom Err Messages --------------------------- #
def printLog(err, reason):
    if err.lower() == 'err':
        color=b+Fore.RED
        symbol='-'
    else:
        color=b+Fore.CYAN
        symbol='+'
    
    print(f"{color}[{w}{symbol}{color}] {err} -> {w}{reason}")

def exitInput(reason):
    print(f"{c}[{w}+{c}] Exit -> {w}Create github issue: {reason}")
    input('')

def newline():
    print('\n')

# ---------------------- Creating Files / Checking Files --------------------- #
def ConfCreate():
    try: 
        if not os.path.isfile('config.json'):
            with open('config.json', "w") as f:
                f.write('''
{
    "player_id": 0,
    "offer_item_ids": [],
    "request_item_ids": [],
    "request_tags": [],
    "cookie": ""
}
                ''')
                f.close()
            printLog('Success', f'Made config file')
    except:
        printLog('Err', f'Failed to create config file')
        main()

ConfCreate()

# ------------------------------- Configuration ------------------------------ #
CONFIG = json.load(open("config.json"))

__player_id__ = CONFIG["player_id"]
__offer_item_ids__ = CONFIG["offer_item_ids"]
__request_item_ids__ = CONFIG["request_item_ids"]
__request_tags__ = CONFIG["request_item_ids"]
__cookie__ = CONFIG["cookie"]

if  "{__player_id__}".isdigit() != True:
    print("Please change your player_id to ")

def is_windows():
    return os.name == "nt"
def is_linux():
    return os.name == "posix"

# ------------------------------- Begin Options ------------------------------ #
def main():
    width = os.get_terminal_size().columns
    os.system(f"title ROLIMONS BYPASSER [{version}]")
    os.system('cls')
    print("")
    print("{Fore.BLUE}")
    print("██████╗  ██████╗ ██╗     ██╗    ████████╗██████╗  █████╗ ██████╗ ███████╗    ██████╗  ██████╗ ████████╗".center(width))
    print("██╔══██╗██╔═══██╗██║     ██║    ╚══██╔══╝██╔══██╗██╔══██╗██╔══██╗██╔════╝    ██╔══██╗██╔═══██╗╚══██╔══╝".center(width))
    print("██████╔╝██║   ██║██║     ██║       ██║   ██████╔╝███████║██║  ██║█████╗      ██████╔╝██║   ██║   ██║   ".center(width))
    print("██╔══██╗██║   ██║██║     ██║       ██║   ██╔══██╗██╔══██║██║  ██║██╔══╝      ██╔══██╗██║   ██║   ██║   ".center(width))
    print("██║  ██║╚██████╔╝███████╗██║       ██║   ██║  ██║██║  ██║██████╔╝███████╗    ██████╔╝╚██████╔╝   ██║   ".center(width))
    print("╚═╝  ╚═╝ ╚═════╝ ╚══════╝╚═╝       ╚═╝   ╚═╝  ╚═╝╚═╝  ╚═╝╚═════╝ ╚══════╝    ╚═════╝  ╚═════╝    ╚═╝   ".center(width))
    print(f"{version}\n\n".center(width))
    print(f"Developed by Scope")

# --------------------------- Main Options & Checks -------------------------- #

    title = 'Choose your option (Arrow keys to navigate)'
    options = ['Change Cookie','Change User ID', 'Change Requesting', 'Change Offer', 'START']
    option, index = pick(options, title)
    
    if option == "Change Cookie":
        print('Coming Soon')
    elif option == "Change User ID":
        print('Coming Soon')
    if option == "Change Requesting":
        print('Coming Soon')
    if option == "Change Offer":
        print('Coming Soon')
    if option == 'START':
        option2, index = pick(['Change Timing', 'Start'], 'Choose your option (Arrow keys to navigate)')

        if option2 == "Change Timing":
            print('Coming Soon')
        if option2== "Start":
            
            url='https://www.rolimons.com/tradeapi/create'
            headers={
            "origin": "https://www.rolimons.com",
            "referer": "https://www.rolimons.com/tradeadcreate",
            "cookie": "{__cookie__}",
            "accept": "application/json, text/javascript, */*; q=0.01",
            "content-type": "application/json",
            "sec-ch-ua-platform": "Windows",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36",
            "x-requested-with": "XMLHttpRequest"
            }
            body={
                "player_id": __player_id__,
                "offer_item_ids": __offer_item_ids__,
                "request_item_ids": __request_item_ids__,
                "request_tags": __request_tags__
            }

            request = requests.post(url,data=json.dumps(body),headers=headers)
            data = request.json()
            print(data)
    else:
        main()

main()
