import random
import string
import os
import time
import requests
import threading
import ctypes
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
class title:
    gen = 0
    to_gen = 0
    thing='menu'
    def set():
        if title.to_gen == title.gen:
            title.reset()
        while True:
            ctypes.windll.kernel32.SetConsoleTitleW(f"code gen - {title.thing} {f'- made {title.gen}/{title.to_gen}' if title.thing != 'menu' else ''}")
    def reset():
        title.gen = 0
        title.to_gen = 0
        title.thing = 'menu'
def amazon():
    
    title.thing = ('amazon')
    printf("""
╔═╗╔╦╗╔═╗╔═╗╔═╗╔╗╔
╠═╣║║║╠═╣╔═╝║ ║║║║
╩ ╩╩ ╩╩ ╩╚═╝╚═╝╝╚╝
""")
    try:
        amount = int(input("How many amazon gift codes to generate: "))
        title.to_gen += amount
        f = open('./output/amazoncodes.txt', 'a+')
        for i in range(amount):
            title.gen += 1
            first = ("".join(random.choices(string.ascii_uppercase + string.digits, k = 4)))
            second = ("".join(random.choices(string.ascii_uppercase + string.digits, k = 5)))
            third = ("".join(random.choices(string.ascii_uppercase + string.digits, k = 5)))
            code = f'{first}-{second}-{third}'
            printf(f"[green]new code: {code}")
            f.write(f'{code}\n')
        input("Press enter to go back to the main menu")
        clear()
        main()
    except ValueError:
        printf("[bold red]ERROR: please enter a valid number next time")
        sleep(3)
        clear()
        fortnite()
def fortnite(): 
    title.thing = ('fortnite')
    printf("""
╔═╗╔═╗╦═╗╔╦╗╔╗╔╦╔╦╗╔═╗
╠╣ ║ ║╠╦╝ ║ ║║║║ ║ ║╣ 
╚  ╚═╝╩╚═ ╩ ╝╚╝╩ ╩ ╚═╝
""")
    try:
        amount = int(input("How many fortnite gift codes to generate: "))
        title.to_gen += amount
        f = open('./output/fortnitecodes.txt', 'a+')
        for i in range(amount):
            title.gen += 1
            first = ("".join(random.choices(string.ascii_uppercase + string.digits, k = 16)))
            code = f'{first}'
            printf(f"[green]new code: {code}")
            f.write(f'{code}\n')
        input("Press enter to go back to the main menu")
        clear()
        main()
    except ValueError:
        printf("[bold red]ERROR: please enter a valid number next time")
        sleep(3)
        clear()
        fortnite()
def steam():
    
    title.thing = ('steam')
    printf("""
╔═╗╔╦╗╔═╗╔═╗╔╦╗
╚═╗ ║ ║╣ ╠═╣║║║
╚═╝ ╩ ╚═╝╩ ╩╩ ╩
""")
    try:
        amount = int(input("How many steam gift codes to generate: "))
        title.to_gen += 1
        f = open('./output/steamcodes.txt', 'a+')
        for i in range(amount):
            title.gen += 1
            first = ("".join(random.choices(string.ascii_uppercase + string.digits, k = 5)))
            second = ("".join(random.choices(string.ascii_uppercase + string.digits, k = 5)))
            third = ("".join(random.choices(string.ascii_uppercase + string.digits, k = 5)))
            code = f'{first}-{second}-{third}'
            printf(f"[green]new code: {code}")
            f.write(f'{code}\n')
        input("Press enter to go back to the main menu")
        clear()
        main()
    except ValueError:
        printf("[bold red]ERROR: please enter a valid number next time")
        sleep(3)
        clear()
        steam()
def roblox():
    
    title.thing = ('roblox')
    printf("""
[#808080]╦═╗╔═╗╔╗ ╦  ╔═╗═╗ ╦
╠╦╝║ ║╠╩╗║  ║ ║╔╩╦╝
╩╚═╚═╝╚═╝╩═╝╚═╝╩ ╚═[/#808080]
""")
    try:
        amount = int(input("How many roblox gift codes to generate: "))
        title.to_gen += amount
        f = open('./output/robloxcodes.txt', 'a+')
        for i in range(amount):
            title.gen += 1
            first = ("".join(random.choices(string.ascii_uppercase + string.digits, k = 4)))
            second = ("".join(random.choices(string.ascii_uppercase + string.digits, k = 4)))
            third = ("".join(random.choices(string.ascii_uppercase + string.digits, k = 4)))
            fourth = ("".join(random.choices(string.ascii_uppercase + string.digits, k = 4)))
            code = f'RI-{first}-{second}-{third}-{fourth}'
            printf(f"[green]new code: [gray]{code}[/gray]")
            f.write(f'{code}\n')
        input("Press enter to go back to the main menu")
        clear()
        main()
    except ValueError:
        printf("[bold red]ERROR: please enter a valid number next time")
        sleep(3)
        clear()
        roblox()
def psn():
    
    title.thing = ('psn')
    printf("""
[cyan]╔═╗╔═╗╔╗╔  ╔═╗╔═╗╔╦╗╔═╗  ╔═╗╔═╗╔╗╔╔═╗╦═╗╔═╗╔╦╗╔═╗╦═╗                       
╠═╝╚═╗║║║  ║  ║ ║ ║║║╣   ║ ╦║╣ ║║║║╣ ╠╦╝╠═╣ ║ ║ ║╠╦╝                       
╩  ╚═╝╝╚╝  ╚═╝╚═╝═╩╝╚═╝  ╚═╝╚═╝╝╚╝╚═╝╩╚═╩ ╩ ╩ ╚═╝╩╚═ [/cyan]
""")
    try:
        amount = int(input("How many psn gift codes to generate: "))
        title.to_gen += amount
        f = open('./output/psncodes.txt', 'a+')
        for i in range(amount):
            title.gen += 1
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
    
    title.thing = ('xbox')
    printf("""
[green]═╗ ╦╔╗ ╔═╗═╗ ╦  ╔═╗╔═╗╔╦╗╔═╗  ╔═╗╔═╗╔╗╔╔═╗╦═╗╔═╗╔╦╗╔═╗╦═╗                  
╔╩╦╝╠╩╗║ ║╔╩╦╝  ║  ║ ║ ║║║╣   ║ ╦║╣ ║║║║╣ ╠╦╝╠═╣ ║ ║ ║╠╦╝                  
╩ ╚═╚═╝╚═╝╩ ╚═  ╚═╝╚═╝═╩╝╚═╝  ╚═╝╚═╝╝╚╝╚═╝╩╚═╩ ╩ ╩ ╚═╝╩╚═                  [/green]
""")
    try:
        amount = int(input("How many xbox gift codes to generate: "))
        title.to_gen += amount
        a = open('./output/xboxcodes.txt', 'a+')
        for i in range(amount):
            title.gen += 1
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
    
    title.thing = ('nitro')
    printf("""[#5865F2]
╔╗╔╦╔╦╗╦═╗╔═╗  ╔═╗╔═╗╔╦╗╔═╗  ╔═╗╔═╗╔╗╔╔═╗╦═╗╔═╗╔╦╗╔═╗╦═╗
║║║║ ║ ╠╦╝║ ║  ║  ║ ║ ║║║╣   ║ ╦║╣ ║║║║╣ ╠╦╝╠═╣ ║ ║ ║╠╦╝
╝╚╝╩ ╩ ╩╚═╚═╝  ╚═╝╚═╝═╩╝╚═╝  ╚═╝╚═╝╝╚╝╚═╝╩╚═╩ ╩ ╩ ╚═╝╩╚═[/#5865F2]
""")
    try:
        amount = int(input("How many nitro codes to generate: "))
        title.to_gen += amount
        for i in range(amount):
            title.gen += 1
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
    
    title.thing = ('roblox')
    printf("""[yellow]
╔═╗╔═╗╔═╗╔═╗╦  ╔═╗  ╔═╗╦  ╔═╗╦ ╦  ╔═╗╔═╗╔╦╗╔═╗  ╔═╗╔═╗╔╗╔╔═╗╦═╗╔═╗╔╦╗╔═╗╦═╗
║ ╦║ ║║ ║║ ╦║  ║╣   ╠═╝║  ╠═╣╚╦╝  ║  ║ ║ ║║║╣   ║ ╦║╣ ║║║║╣ ╠╦╝╠═╣ ║ ║ ║╠╦╝
╚═╝╚═╝╚═╝╚═╝╩═╝╚═╝  ╩  ╩═╝╩ ╩ ╩   ╚═╝╚═╝═╩╝╚═╝  ╚═╝╚═╝╝╚╝╚═╝╩╚═╩ ╩ ╩ ╚═╝╩╚═[/yellow]
""")
    try:
        amount = int(input("How many google play gift codes to generate: "))
        title.to_gen += amount
        c = open('./output/googlecodes.txt', 'a+')
        for i in range(amount):
            title.gen += 1
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
    threading.Thread(target=title.set).start()
    title2 = 'Please choose a gift code type to generate: '
    options = ['xbox', 'psn', 'nitro', 'google play', 'roblox', 'steam', 'fortnite', 'amazon', 'exit']
    option, index = pick(options, title2, indicator='>>')
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
    elif option == 'steam':
        clear()
        steam()
    elif option == 'fortnite':
        clear()
        fortnite()
    elif option == 'amazon':
        clear()
        amazon()
    elif option == 'exit':
        clear()
        os._exit(1)

main()

