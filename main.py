import random
import string
import os
import time
import requests
from time import sleep
from os import system
from rich import print as printf
def clear():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')
try:
    os.mkdir('output')
except FileExistsError:
    pass
banner = """
[red]╔═╗╦╔═╗╔╦╗  ╔═╗╔═╗╔╦╗╔═╗  ╔═╗╔═╗╔╗╔╔═╗╦═╗╔═╗╔╦╗╔═╗╦═╗[/red]
[red]║ ╦║╠╣  ║   ║  ║ ║ ║║║╣   ║ ╦║╣ ║║║║╣ ╠╦╝╠═╣ ║ ║ ║╠╦╝   [/red]
[red]╚═╝╩╚   ╩   ╚═╝╚═╝═╩╝╚═╝  ╚═╝╚═╝╝╚╝╚═╝╩╚═╩ ╩ ╩ ╚═╝╩╚═ [/red]
"""
def psn():
    system('title menu code gen - psn')
    printf("""
[cyan]╔═╗╔═╗╔╗╔  ╔═╗╔═╗╔╦╗╔═╗  ╔═╗╔═╗╔╗╔╔═╗╦═╗╔═╗╔╦╗╔═╗╦═╗                       
╠═╝╚═╗║║║  ║  ║ ║ ║║║╣   ║ ╦║╣ ║║║║╣ ╠╦╝╠═╣ ║ ║ ║╠╦╝                       
╩  ╚═╝╝╚╝  ╚═╝╚═╝═╩╝╚═╝  ╚═╝╚═╝╝╚╝╚═╝╩╚═╩ ╩ ╩ ╚═╝╩╚═ [/cyan]
""")
    try:
        amount = int(input("How many psn gift codes to generate: "))
        f = open('./output/psncodes.txt', 'a+')
        for i in range(amount):
            first = ("".join(random.choices(string.ascii_uppercase + string.digits, k = 4)))
            second = ("".join(random.choices(string.ascii_uppercase + string.digits, k = 4)))
            third = ("".join(random.choices(string.ascii_uppercase + string.digits, k = 4)))
            printf(f"[green]new code: [cyan]{first} {second} {third}[/cyan]")
            f.write(f'{first} {second} {third}\n')
        print("press enter to go back to the menu")
        input()
        clear()
    except KeyboardInterrupt:
        clear()
    except ValueError:
        printf("[bold red]ERROR: please enter a valid number next time")
        sleep(3)
        clear()
        psn()
def xbox():
    system('title menu code gen - xbox')
    printf("""
[green]═╗ ╦╔╗ ╔═╗═╗ ╦  ╔═╗╔═╗╔╦╗╔═╗  ╔═╗╔═╗╔╗╔╔═╗╦═╗╔═╗╔╦╗╔═╗╦═╗                  
╔╩╦╝╠╩╗║ ║╔╩╦╝  ║  ║ ║ ║║║╣   ║ ╦║╣ ║║║║╣ ╠╦╝╠═╣ ║ ║ ║╠╦╝                  
╩ ╚═╚═╝╚═╝╩ ╚═  ╚═╝╚═╝═╩╝╚═╝  ╚═╝╚═╝╝╚╝╚═╝╩╚═╩ ╩ ╩ ╚═╝╩╚═                  [/green]
""")
    try:
        amount = int(input("How many xbox gift codes to generate: "))
        a = open('./output/xboxcodes.txt', 'a+')
        for i in range(amount):
            first = ("".join(random.choices(string.ascii_uppercase + string.digits, k = 5)))
            second = ("".join(random.choices(string.ascii_uppercase + string.digits, k = 5)))
            third = ("".join(random.choices(string.ascii_uppercase + string.digits, k = 5)))
            fourth = ("".join(random.choices(string.ascii_uppercase + string.digits, k = 5)))
            fifth = ("".join(random.choices(string.ascii_uppercase + string.digits, k = 5)))
            printf(f"[green]new code: [cyan]{first}-{second}-{third}-{fourth}-{fifth}[/cyan]")
            a.write(f'{first}-{second}-{third}-{fourth}-{fifth}\n')
        print("press enter to back to the main menu")
        input()
        clear()
    except KeyboardInterrupt:
        clear()
    except ValueError:
        printf("[bold red]ERROR: please enter a valid number next time")
        sleep(3)
        clear()
        xbox()
def quickChecker(nitro:str):
    b = open('./output/nitrocodes.txt', 'a+')
    url = f"https://discordapp.com/api/v9/entitlements/gift-codes/{nitro}?with_application=false&with_subscription_plan=true"
    response = requests.get(url)

    if response.status_code == 200:
        printf(f"[green]Valid[/green] | https://discord.gift/{nitro}")
        b.write(f'https://discord.gift/{nitro}\n')
    else:
        printf(f"[red]Invalid[/red] | https://discord.gift/{nitro}")

def nitro():
    system('title menu code gen - nitro')
    printf("""[#5865F2]
╔╗╔╦╔╦╗╦═╗╔═╗  ╔═╗╔═╗╔╦╗╔═╗  ╔═╗╔═╗╔╗╔╔═╗╦═╗╔═╗╔╦╗╔═╗╦═╗
║║║║ ║ ╠╦╝║ ║  ║  ║ ║ ║║║╣   ║ ╦║╣ ║║║║╣ ╠╦╝╠═╣ ║ ║ ║╠╦╝
╝╚╝╩ ╩ ╩╚═╚═╝  ╚═╝╚═╝═╩╝╚═╝  ╚═╝╚═╝╝╚╝╚═╝╩╚═╩ ╩ ╩ ╚═╝╩╚═[/#5865F2]
""")
    try:
        amount = int(input("How many nitro codes to generate: "))
        for i in range(amount):
            code = ("".join(random.choices(string.ascii_uppercase + string.digits + string.ascii_lowercase, k = 16)))
            quickChecker(code)
        print("Press enter to go back to the menu")
        input()
        clear()
    except KeyboardInterrupt:
        clear()
    except ValueError:
        printf("[bold red]ERROR: please enter a valid amount next time")
        sleep(3)
        clear()
        nitro()
def google():
    system('title menu code gen - google play')
    printf("""[yellow]
╔═╗╔═╗╔═╗╔═╗╦  ╔═╗  ╔═╗╦  ╔═╗╦ ╦  ╔═╗╔═╗╔╦╗╔═╗  ╔═╗╔═╗╔╗╔╔═╗╦═╗╔═╗╔╦╗╔═╗╦═╗
║ ╦║ ║║ ║║ ╦║  ║╣   ╠═╝║  ╠═╣╚╦╝  ║  ║ ║ ║║║╣   ║ ╦║╣ ║║║║╣ ╠╦╝╠═╣ ║ ║ ║╠╦╝
╚═╝╚═╝╚═╝╚═╝╩═╝╚═╝  ╩  ╩═╝╩ ╩ ╩   ╚═╝╚═╝═╩╝╚═╝  ╚═╝╚═╝╝╚╝╚═╝╩╚═╩ ╩ ╩ ╚═╝╩╚═[/yellow]
""")
    try:
        amount = int(input("How many google play gift codes to generate: "))
        c = open('./output/googlecodes.txt', 'a+')
        for i in range(amount):
            first = ("".join(random.choices(string.ascii_uppercase + string.digits, k = 4)))
            second = ("".join(random.choices(string.ascii_uppercase + string.digits, k = 4)))
            third = ("".join(random.choices(string.ascii_uppercase + string.digits, k = 4)))
            fourth = ("".join(random.choices(string.ascii_uppercase + string.digits, k = 4)))
            fifth = ("".join(random.choices(string.ascii_uppercase + string.digits, k = 4)))
            printf(f"[green]new code: [cyan]{first} {second} {third} {fourth} {fifth}[/cyan]")
            c.write(f'{first} {second} {third} {fourth} {fifth}\n')
             
        print("press enter to back to the main menu")
        input()
        clear()
    except KeyboardInterrupt:
        clear()
def main():
    try:
        system('title menu code gen - menu')
        printf(banner)
        printf("""
1. xbox gift code generator
2. psn gift code generator
3. nitro gift code generator
4. google play gift code generator
        """)
        choice = int(input("> "))
    except ValueError:
        printf("[bold red]ERROR: please enter a valid option next time")
        sleep(3)
        clear()
        main()
    except KeyboardInterrupt:
        clear()
        main()
    if choice == 1:
        clear()
        xbox()
        main()
    elif choice == 2:
        clear()
        psn()
        main()
    elif choice == 3:
        clear()
        nitro()
        main()
    elif choice == 4:
        clear()
        google()
        main()
        
main()
