# Fortnite Hotfix Tool made by: Leaks station#3384 / @leaks_station / @GrenadeBR

from requests import get
import json
import time
import colorama
from colorama import Fore
colorama.init(autoreset=True)

# REMOVED TWITTER SUPPORT FOR NOW #

def Bot():
    data = get("https://fortnitecentral.genxgames.gg/api/v1/hotfixes?lang=en").json()[""]
    Odata = open("oldhotfixes.json", "r+")
    olddata = json.load(Odata)

    if data == {} or data is None:
        print(f"{Fore.RED} API is Empty, Checking Delayed!".title())
    elif data == olddata:
        print(f"{Fore.LIGHTGREEN_EX}>>> Searching For New Hotfix!")
    else:
        ReadfortweetNew = "New Hotfixes: \n"
        generated_data = {"new_hotfixes": [], "modified_hotfixes": []}

        print(f"{Fore.CYAN}-> New Hotfix Detected !!!")
        for i in data:
            if i not in olddata:
                print(f"New Hotfix : {Fore.LIGHTYELLOW_EX}-> ID :{i}")
                dataget = data[i]
                ReadfortweetNew = ReadfortweetNew + f"• {dataget}\n"
                generated_data["new_hotfixes"].append({"ID": i, "Hotfix": dataget})

        # To print every single one
        if len(ReadfortweetNew) > 280:
            for i in data:
                ReadfortweetNew = "New Hotfixes: \n"
                if i not in olddata:
                    dataget = data[i]
                    ReadfortweetNew = ReadfortweetNew + f"• {dataget}\n"
                    print(f"New Hotfix : {Fore.LIGHTYELLOW_EX}-> ID :{i}")
                    generated_data["new_hotfixes"].append({"ID": i, "Hotfix": dataget})

        # Here will make sure if it's Equal or Less than the Limit, if less than the limit, It will print it all
        elif len(ReadfortweetNew) <= 280:
            print(ReadfortweetNew)
            
# Scrolling through Source code huh? Cheeky boy ;)

        # Here Checking for new Modification Of any Hotfix :D
        for i in data:
            if i in olddata:
                if olddata[i] != data[i]:
                    print(f"{Fore.LIGHTCYAN_EX}-> Hotfix Modification Detected !!!\n ID : {i}\n"
                          f"{Fore.LIGHTYELLOW_EX}-> OLD : {olddata[i]}\n{Fore.YELLOW}-> NEW : {data[i]}")
                    generated_data["modified_hotfixes"].append({"ID": i, "Old": olddata[i], "New": data[i]})

       # NEWLY ADDED: Save generated data to a new file
        with open("generated_data.json", "w") as generated_file:
            json.dump(generated_data, generated_file, indent=3)

        Odata = open("oldhotfixes.json", "w+")
        json.dump(data, Odata, indent=3)

if "HI" == "HI":
    while True:
        try:
            Bot()
        except:
            print(f"{Fore.LIGHTRED_EX}-> ERROR [INTERNET PROBLEM/ELSE (the bot will stop detecting until the error stops)]")
        time.sleep(10)  # Changed to a 10-second loop