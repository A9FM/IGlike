import os
from time import sleep

try:
    import colorama
except:
    os.system("pip3 install colorama -y")
    import colorama

try:
    import wget
except:
    os.system("pip3 install wget -y")
    import wget

try:
    from instagram_private_api import Client, ClientCompatPatch
except:
    os.system("pip3 install git+https://git@github.com/ping/instagram_private_api.git@1.6.0")

users = ["5791701778", "460563723", "26669533", "7719696", "247944034", "173560420", "18428658" ,"6380930", "232192182", "12281817", "305701719", "427553890", "12331195", "5457896418", "325734299", "212742998", "407964088", "7555881", "177402262", "19596899", "181306552", "1506607755", "184692323", "11830955", "25025320"]

# Color
yellow = "\033[1;33m"
red = "\033[1;31m"
green = "\033[1;32m"

# Requirements
logs = f"{yellow}LOGS |"
good = f"{green}Good"
fail = f"{red}Fail"
version = "V:1.1"

def start():
    run = 666
    while run != 1:
        os.system('cls' if os.name == 'nt' else 'clear')
        print(f"""{red}
$$$$$$\  $$$$$$\  $$\ $$\ $$\                 
\_$$  _|$$  __$$\ $$ |\__|$$ |                
  $$ |  $$ /  \__|$$ |$$\ $$ |  $$\  $$$$$$\  
  $$ |  $$ |$$$$\ $$ |$$ |$$ | $$  |$$  __$$\ 
  $$ |  $$ |\_$$ |$$ |$$ |$$$$$$  / $$$$$$$$ |
  $$ |  $$ |  $$ |$$ |$$ |$$  _$$<  $$   ____|
$$$$$$\ \$$$$$$  |$$ |$$ |$$ | \$$\ \$$$$$$$\ 
\______| \______/ \__|\__|\__|  \__| \_______|

-=-=-=-=-=-=-=-=-=( {version} )=-=-=-=-=-=-=-=-=-=-

       [YT] - www.youtube.com/c/A9FM_top
       [IG] - @a9fm_official
       [TG] - @a9_fm

-=-=-=-=-=-=-=-=-=( {version} )=-=-=-=-=-=-=-=-=-=-
{yellow}
[1] - Start Script
[2] - Update
[9] – Exit
""")
        action = input(f"{red}>> {yellow}")
        if action == "1" or action == "2" or action == "9":
            run = 1
        else:
            print(f"{logs} {red}[x] Not found")
            sleep(1)

    if action == "1":
        cookies = input(f"{logs} {red}Use cookies? (default N) [y/n] >>{yellow} ")
        if cookies == "y" or cookies == "Y":
            try:
                loginn = open("login.txt", "r")
                login = loginn.read()
                passwd = open("password.txt", "r")
                password = passwd.read()
            except:
                login = input(f"{logs} {red}Enter you username >>{yellow} ")
                password = input(f"{logs} {red}Enter you password >>{yellow} ")
        else:
            login = input(f"{logs} {red}Enter you username >>{yellow} ")
            password = input(f"{logs} {red}Enter you password >>{yellow} ")

        api = Client(login, password)

        my_file = open("login.txt", "w")
        text_for_file = login
        my_file.write(text_for_file)
        my_file.close()
        my_file = open("password.txt", "w")
        text_for_file = password
        my_file.write(text_for_file)
        my_file.close()
        try:
            script = 0
            while script == 0:
                for user in users:
                    try:
                        api.friendships_create(user)
                        result = good
                        time = 5
                    except:
                        result = fail
                        time = 30
                    sleep(time)
                    print(f"{logs} {result} |   Subs [ID: {user}]. Sleep {str(time)} sec")
                sleepError()

                # AutoFollow
                for user in users:
                    try:
                        api.friendships_destroy(user)
                        result = good
                        time = 5
                    except:
                        result = fail
                        time = 30
                    print(f"{logs} {result} | UnSubs [ID: {user}]. Sleep {str(time)} sec")
                    sleep(time)
                sleepError()
        except KeyboardInterrupt:
            script = 1

    if action == "2":
        os.remove("main.py")
        print(f"{logs} {red}Updating...")
        wget.download("https://raw.githubusercontent.com/A9FM/IGlike/main/main.py", "main.py", bar=False)
        print(f"{logs} {red}Update succesfull! Shutdown...")
        quit()
    if action == "9":
        goodbye()


def sleepError():
    print(f"{logs} \033[33mSleep 2 min...")
    sleep(120)

def goodbye():
    print(f"{logs} \033[32m[√] Bye Bye!")
    quit()

while True:
    try:
        start()
    except KeyboardInterrupt:
        goodbye()