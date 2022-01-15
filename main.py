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

users = ["5791701778", "460563723", "26669533", "7719696", "247944034", "173560420", "18428658" ,"6380930", "232192182", "12281817", "305701719", "427553890", "39426961689", "12331195", "5457896418", "325734299", "212742998", "407964088", "7555881", "177402262", "19596899", "181306552", "1506607755", "184692323", "11830955", "25025320"]

def start():
    run = 666
    while run != 1:
        os.system('cls' if os.name == 'nt' else 'clear')
        print(f"""\033[1;31m
$$$$$$\  $$$$$$\  $$\ $$\ $$\                 
\_$$  _|$$  __$$\ $$ |\__|$$ |                
  $$ |  $$ /  \__|$$ |$$\ $$ |  $$\  $$$$$$\  
  $$ |  $$ |$$$$\ $$ |$$ |$$ | $$  |$$  __$$\ 
  $$ |  $$ |\_$$ |$$ |$$ |$$$$$$  / $$$$$$$$ |
  $$ |  $$ |  $$ |$$ |$$ |$$  _$$<  $$   ____|
$$$$$$\ \$$$$$$  |$$ |$$ |$$ | \$$\ \$$$$$$$\ 
\______| \______/ \__|\__|\__|  \__| \_______|
-=-=-=-=-=-=-=-=-=( V:1.0 )=-=-=-=-=-=-=-=-=-=-
       [YT] - www.youtube.com/c/A9FM_top
       [IG] - @a9fm_official
       [TG] - @a9_fm
-=-=-=-=-=-=-=-=-=( V:1.0 )=-=-=-=-=-=-=-=-=-=-
\033[33m
[1] - Start Script
[2] - Update (NOT WORK)
[9] – Exit
""")
        action = input('>> ')
        if action == "1" or action == "2" or action == "9":
            run = 1
        else:
            print('[x] Not found')
            sleep(1)

    if action == "1":
        cookies = input("Use cookies? (default N) [y/n] >>\033[33m ")
        if cookies == "y" or cookies == "Y":
            try:
                loginn = open("login.txt", "r")
                login = loginn.read()
                passwd = open("password.txt", "r")
                password = passwd.read()
            except:
                login = input("\033[1;31mEnter you username >>\033[33m ")
                password = input("\033[1;31mEnter you password >>\033[33m ")
        else:
            login = input("\033[1;31mEnter you username >>\033[33m ")
            password = input("\033[1;31mEnter you password >>\033[33m ")

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
                good = "\033[32mGood"
                fail = "\033[1;31mFail"
                for user in users:
                    try:
                        api.friendships_create(user)
                        result = good
                    except:
                        result = fail
                    print(f"{result} | Subs [ID: {user}]. Sleep 5 sec")
                    sleep(5)

                # AutoFollow
                print("\033[33mSleep 2 min...")
                sleep(120)
                for user in users:
                    try:
                        api.friendships_destroy(user)
                        result = good
                    except:
                        result = fail
                    print(f"{result} | Unsubs [ID: {user}]. Sleep 5 sec")
                    sleep(5)
        except KeyboardInterrupt:
            script = 1

    if action == "2":
        pass
    if action == "9":
        goodbye()


def goodbye():
    print("\033[32m[√] Bye Bye!")
    quit()

while True:
    try:
        start()
    except KeyboardInterrupt:
        goodbye()