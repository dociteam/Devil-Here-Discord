# Devil @here - @here in Discord Servers Without Permissions!
# Author: DociTeam - https://github.com/DociTeam
# March 25rd, 2022
# Copyright 2022, Doctor

import discord
from discord.ext import commands , tasks
from discord.utils import get
import os
import time
import discum

def clear_console():
    if os.name in ('nt', 'dos'): #Check OS name for using correct command
        try:
            os.system("cls")
        except:
            pass
    else:
        try:
            os.system("clear")
        except:
            pass

def change_title():
    if os.name in ('nt', 'dos'):
        try:
            os.system('title "DociTeam | Devil @here"')
        except:
            pass
    else:
            pass


clear_console()
change_title()

class color : 
    Red = '\033[91m'
    Green = '\033[92m'
    Blue = '\033[94m'
    Cyan = '\033[96m'
    White = '\033[97m'
    Yellow = '\033[93m'
    Magenta = '\033[95m'
    Grey = '\033[90m'
    Black = '\033[90m'
    Default = '\033[99m'



dociteam = color.Cyan+"""
                                     ____             _ _____                    
                                    |  _ \  ___   ___(_)_   _|__  __ _ _ __ ___  
                                    | | | |/ _ \ / __| | | |/ _ \/ _` | '_ ` _ \ 
                                    | |_| | (_) | (__| | | |  __/ (_| | | | | | |
                                    |____/ \___/ \___|_| |_|\___|\__,_|_| |_| |_|
"""

banner =color.Red+ f"""

________              .__.__       _____ .__                          
\______ \   _______  _|__|  |     / ___ \|  |__   ___________   ____  
 |    |  \_/ __ \  \/ /  |  |    / / ._\ \  |  \_/ __ \_  __ \_/ __ \ 
 |    `   \  ___/\   /|  |  |__ <  \_____/   Y  \  ___/|  | \/\  ___/ 
/_______  /\___  >\_/ |__|____/  \_____\ |___|  /\___  >__|    \___  >
        \/     \/                             \/     \/            \/ 
                 

"""


def slowprint(text: str, speed: float, newLine=True):
    for i in text:
        print(i, end="", flush=True)
        time.sleep(speed)
    if newLine:
        print()

print(dociteam)
time.sleep(2)
clear_console()
print(banner)
time.sleep(1)
slowprint(color.Yellow+f"\n\n|---------- Welcome to {color.Red}Devil @here{color.Yellow} ----------|\n",0.07)
slowprint(color.Yellow+"[!] This Project is Education Purpose Only!\n",0.07)
while True:
    TOKEN = str(input(color.Cyan+f"[+] Enter Your Discord Account Token : {color.White}")).strip()
    if len(TOKEN.strip()) == 0:
        print(color.Red+"\n[-] You Should Enter Your Discord Account Token!\n")
    else:
        break
while True:
    CMD_PREFIX = str(input(color.Cyan+f"[+] Enter Command Prefix (Example : !) : {color.White}")).strip()
    if len(CMD_PREFIX.strip()) == 0:
        print(color.Red+"\n[-] You Should Enter Command Prefix!\n")
    if len(CMD_PREFIX) > 6:
        print(color.Red+"\n[-] Invalid Command Prefix! (Max Length = 6)\n")
    else:
        break

bot = discum.Client(token=TOKEN)

clear_console()
print(banner)
slowprint(color.Yellow+f"\n\n[!] For @here just send {color.Red}{CMD_PREFIX}here{color.Yellow} on channel you want mention members!\n",0.07)
time.sleep(1)

intents = discord.Intents.default()
intents.members = True

client = commands.Bot(command_prefix= CMD_PREFIX , self_bot=True , intents=intents)
client.remove_command("help")

@client.event
async def on_ready():
    print(color.Cyan+"|Username : "+color.Green+str(client.user))
    print(color.Cyan+"|Created On  : "+color.Green+str(client.user.created_at))
    print(color.Cyan+"|Servers Joined : "+color.Green+str(len(client.guilds)))
    print(color.Green+f"\n[+] {color.Red}@here{color.Green} Is Ready....\n")


@client.command()
async def here(ctx): #@here!
    await ctx.message.delete()
    def close_after_fetching(resp, guild_id):
        if bot.gateway.finishedMemberFetching(guild_id):
            bot.gateway.removeCommand({'function': close_after_fetching, 'params': {'guild_id': guild_id}})
            bot.gateway.close()
    def get_members_ID(guild_id, channel_id):
        bot.gateway.fetchMembers(guild_id, channel_id, keep="all", wait=1) #Get all user attributes, wait 1 second between requests
        bot.gateway.command({'function': close_after_fetching, 'params': {'guild_id': guild_id}})
        bot.gateway.run()
        bot.gateway.resetSession() #Saves 10 seconds when gateway is run again
        return bot.gateway.session.guild(guild_id).memberIDs
    with open(f'{str(ctx.guild.name)}_memebrs_ID_mention.txt','a', encoding='UTF-8') as members_ID:
        for i in get_members_ID(str(ctx.guild.id) , str(ctx.channel.id)):
            members_ID.writelines(str(f"<@{i}>\n"))
    clear_console()
    print(banner+"\n")
    print(color.Green+f"[+] Members ID Mention has been saved in this path as {color.Red}'{str(ctx.guild.name)}_memebrs_ID_mention.txt'\n")
    print(color.Green+f"[+] You Can Copy/Paste from text file and mention members!\n")
    print(color.Green+"\n.: |Done! :.\n")

try:
    client.run(TOKEN , bot=False)
except:
    print(color.Red+"\n[-] Error! There is problem with your discord account token or network connection!")
    time.sleep(1)
    input(color.Cyan+"\n[+] Press any key to exit..... ")
    exit()