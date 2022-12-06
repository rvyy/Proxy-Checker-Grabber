import requests,colorama,ctypes,threading,os,vlc
from os import system
from ctypes import windll
from colorama import Fore


system('mode 80,23')


C,A = Fore.LIGHTCYAN_EX,Fore.LIGHTWHITE_EX

st = f'{A}[{C} - {A}]'

colorama.init()

stop_thread = threading.Event()

proxies = []

good = 0
bad = 0


def grab():
    u1 = "https://api.proxyscrape.com/v2/?request=getproxies&protocol=http&timeout=10000&country=all&ssl=all&anonymity=all"

    r = requests.get(u1)
    count = r.text.count(":")
    rr = r.text.replace("\n","")
    open('proxies.txt','a').write(f'{rr}')
    print(f'{st} Grabbed {count} Proxies And Saved in proxies.txt',end='');input();exit()
def check():
    global good,bad
    while True:
        proxy = proxyf.readline().split('\n')[0]
        windll.kernel32.SetConsoleTitleW(f'Good Proxies : {good} , Bad Proxies : {bad}')
        try:
            req = requests.get(u,proxies={'http':f'http://{proxy}','https':f'http://{proxy}'}, timeout=3)
            good += 1
            open('good.txt','a').write(f'{proxy}\n')
        except:
            bad += 1
        if stop_thread.is_set():
              break
        if (proxy == ''):
            stop_thread.set()
            print(f'{st} Checked All Proxies, Good Proxies Saved in good.txt',end='');input();exit()
print(f'''

    {A}- Proxies {C}Grabber {A}& {C}Checker
    {A}- {A}Made by {C}@rv.y{A}


''')

print(f'{st} Grabber == {C}1{A} // Checker == {C}2{A} > ',end='')
ch = int(input())
if ch == 1:
    grab()
if ch == 2:
    proxyf = open('proxies.txt')
    print(f'{st} Website Link ? : ',end='')
    u = input()
    threads = []
    for i in range(25):
        t = threading.Thread(target=check).start()
