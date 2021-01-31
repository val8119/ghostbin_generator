# Name: Ghostbin Generator
#
# Author: https://github.com/val8119
#
# Description: Generate random ghostbin URLs and check if any of them are valid,
# saves the valid URLs in a text file.


import requests
import random
import string


def fprint(status, text):
    pre = {
        "valid": f"{colors.green}[+]",
        "invalid": f"{colors.red}[-]",
        "neutral": f"{colors.yellow}[=]"
    }

    print(f" {pre[status]} {colors.white}{text}")


class colors:
    white = "\033[39m"
    yellow = "\033[33m"
    green = "\033[32m"
    red = "\033[31m"


alphabet = string.ascii_lowercase + string.digits
valids = 0

print(f"""{colors.yellow}
     ________               __  __    _          ______                           __            
    / ____/ /_  ____  _____/ /_/ /_  (_)___     / ____/__  ____  ___  _________ _/ /_____  _____
   / / __/ __ \/ __ \/ ___/ __/ __ \/ / __ \   / / __/ _ \/ __ \/ _ \/ ___/ __ `/ __/ __ \/ ___/
  / /_/ / / / / /_/ (__  ) /_/ /_/ / / / / /  / /_/ /  __/ / / /  __/ /  / /_/ / /_/ /_/ / /    
  \____/_/ /_/\____/____/\__/_.___/_/_/ /_/   \____/\___/_/ /_/\___/_/   \__,_/\__/\____/_/     
""")

total = int(input(f" {colors.yellow}Enter number of URLs to check: {colors.white}"))

print("")

for number in range(1, total + 1):
    url_mid = "".join(random.choice(alphabet) for i in range(5))

    url = f"https://ghostbin.co/paste/{url_mid}"

    response = requests.get(url)

    if response:
        fprint("valid", f"{number}/{total}: Valid ghostbin: {colors.green}{url}")
        print(url, file=open("ghostbins.txt", "a"))
        valids += 1
    else:
        fprint("invalid", f"{number}/{total}: Invalid ghostbin: {colors.red}{url}")

print("")

fprint("neutral", f"Finished checking {colors.yellow}{total}{colors.white} URLs and found {colors.green}{valids}{colors.white} valid URLs")

input("")

quit()
