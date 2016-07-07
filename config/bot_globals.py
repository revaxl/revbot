#Global variables and functions for the bot
import configparser
import logging
import os

#Print to console and log the data
def log_print(data):
    try:
        print(data)
        logging.info(data)
    #The unfortunate end user is on Windows
    except UnicodeEncodeError:
        data = data.encode("utf-8")
        log_print(data)

#Create a log file and set up the logger for it
def create_log(log_folder, file_name, file_number=0):
    name = os.path.abspath("{0}/{1}_{2}.log"
    .format(log_folder, file_name, str(file_number)))
    if not os.path.isfile(name):
        logging.basicConfig(filename=name, level=logging.INFO, format="%(message)s")
        log_print("Log file {0} created.".format(name))
    else:
        file_number += 1
        create_log(log_folder, file_name, file_number)


version = "v1"

#List of servers the bot is connected to
server_list = []

#Set up the config
config = configparser.ConfigParser()
config.read(os.path.abspath("./config/config.ini"))

#Everyone who has contributed to the bot
contributors = ["Ispira"]

#Load values from config files
#Log settings
log_messages = config.getboolean("log_settings", "log_messages")
log_commands = config.getboolean("log_settings", "log_commands")
display_purges = config.getboolean("log_settings", "display_purges")
#Bot settings
bot_token = config["bot_settings"]["token"]
bot_owner = config["bot_settings"]["bot_owner"]
bot_name = config["bot_settings"]["bot_name"]
#File locations
log_folder = os.path.abspath(config["files"]["log_folder"])

#Botmasters and blacklist
bot_masters = []
with open(os.path.abspath("./config/botmasters.txt")) as bm:
    for line in bm.readlines():
        if line != "\n":
            bot_masters.append(line.rstrip("\n"))
blacklist = []
with open(os.path.abspath("./config/blacklist.txt")) as bl:
    for line in bl.readlines():
        if line != "\n":
            blacklist.append(line.rstrip("\n"))
