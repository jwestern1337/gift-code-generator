import random
import string
import os
import time
import requests
from time import sleep
from os import system
from pick import pick
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

def roblox():
    system('title code gen - roblox')
    printf("""
[grey]╦═╗╔═╗╔╗ ╦  ╔═╗═╗ ╦
╠╦╝║ ║╠╩╗║  ║ ║╔╩╦╝
╩╚═╚═╝╚═╝╩═╝╚═╝╩ ╚═[/grey]
""")
    try:
        amount = int(input("How many roblox gift codes to generate: "))
        f = open('./output/robloxcodes.txt', 'a+')
        for i in range(amount):
            first = ("".join(random.choices(string.ascii_uppercase + string.digits, k = 4)))
            second = ("".join(random.choices(string.ascii_uppercase + string.digits, k = 4)))
            third = ("".join(random.choices(string.ascii_uppercase + string.digits, k = 4)))
            fourth = ("".join(random.choices(string.ascii_uppercase + string.digits, k = 4)))
            code = f'RI-{first}-{second}-{third}-{fourth}'
            printf(f"[green]new code: [grey]{code}[/grey]")
            f.write(code)
        input("Press enter to go back to the main menu")
        clear()
        main()
    except ValueError:
        printf("[bold red]ERROR: please enter a valid number next time")
        sleep(3)
        clear()
        roblox()
def psn():
    system('title code gen - psn')
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
        main()
    except ValueError:
        printf("[bold red]ERROR: please enter a valid number next time")
        sleep(3)
        clear()
        psn()
def xbox():
    system('title code gen - xbox')
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
        main()
    except ValueError:
        printf("[bold red]ERROR: please enter a valid number next time")
        sleep(3)
        clear()
        xbox()
def quickChecker():
    nitro = ("".join(random.choices(string.ascii_uppercase + string.digits + string.ascii_lowercase, k = 16)))
    b = open('./output/nitrocodes.txt', 'a+')
    url = f"https://discordapp.com/api/v9/entitlements/gift-codes/{nitro}?with_application=false&with_subscription_plan=true"
    response = requests.get(url)

    if response.status_code == 200:
        printf(f"[green]Valid[/green] | https://discord.gift/{nitro}")
        b.write(f'https://discord.gift/{nitro}\n')
    else:
        printf(f"[red]Invalid[/red] | https://discord.gift/{nitro}")

def nitro():
    system('title code gen - nitro')
    printf("""[#5865F2]
╔╗╔╦╔╦╗╦═╗╔═╗  ╔═╗╔═╗╔╦╗╔═╗  ╔═╗╔═╗╔╗╔╔═╗╦═╗╔═╗╔╦╗╔═╗╦═╗
║║║║ ║ ╠╦╝║ ║  ║  ║ ║ ║║║╣   ║ ╦║╣ ║║║║╣ ╠╦╝╠═╣ ║ ║ ║╠╦╝
╝╚╝╩ ╩ ╩╚═╚═╝  ╚═╝╚═╝═╩╝╚═╝  ╚═╝╚═╝╝╚╝╚═╝╩╚═╩ ╩ ╩ ╚═╝╩╚═[/#5865F2]
""")
    try:
        amount = int(input("How many nitro codes to generate: "))
        for i in range(amount):
            quickChecker()
        print("Press enter to go back to the menu")
        input()
        clear()
        main()
    except ValueError:
        printf("[bold red]ERROR: please enter a valid amount next time")
        sleep(3)
        clear()
        nitro()
def google():
    system('title code gen - google play')
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
        main()
    except ValueError:
        printf("[bold red]ERROR: please enter a valid number next time")
        sleep(3)
        clear()
        google()

def main():
    system('title code gen - menu')
    title = 'Please choose a gift code type to generate: '
    options = ['xbox', 'psn', 'nitro', 'google play', 'roblox', 'exit']
    option, index = pick(options, title, indicator='>>')
    if option == 'xbox':
        clear()
        xbox()
    elif option == 'psn':
        clear()
        psn()
    elif option == 'nitro':
        clear()
        nitro()
    elif option == 'google play':
        clear()
        google()
    elif option == 'roblox':
        clear()
        roblox()
    elif option == 'exit':
        clear()
        os._exit(1)


        
main()
