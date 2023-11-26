import configparser
from os.path import isdir

config_dict = configparser.ConfigParser()
config_dict.read("config.ini", encoding="UTF-8")

# PATHs to files and save
LOCALPATH = config_dict["PATH"]["LOCALPATH"]

if isdir(LOCALPATH):
    PATH = LOCALPATH
else:
    raise Exception("PATH is not accessible!")
