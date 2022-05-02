
import datetime
import configparser
from os.path import exists
from shutil import copyfile


config = configparser.ConfigParser()
config.read('/home/pi/restic-backup/config.cfg')



STATUSFILE = config['BACKUP']['STATUSFILE']


if exists(STATUSFILE):
    now = datetime.datetime.now()
    currentdate = now.strftime("%Y-%m-%d")
    copyfile(STATUSFILE, STATUSFILE + "-" + currentdate)

f = open(STATUSFILE, "w")


def initOutputFile(repo, directory):
    now = datetime.datetime.now()
    currentdate = now.strftime("%Y-%m-%d %H:%M:%S")

    #f.write("To: info@thwessling.de\n")
    #f.write("From: info@thwessling.de\n")
    f.write("Subject: Restic Log for " + currentdate + "\n\n")



    timeStamp = f"Starting backup: {currentdate} for directory {directory} to repository {repo}\n"
    timeStamp = timeStamp + "------------------------------------------------------\n"

    f.write(timeStamp + "\n")


def writeToFile(statusText, includeTime=False):
    if includeTime:
        now = datetime.datetime.now()
        currentdate = now.strftime("%H:%M:%S")
        f.write(f"{currentdate} {statusText} \n")
    else:
        f.write(statusText + "\n\n")

def close():
    f.close()

def getStatusFileContent():
    with open(STATUSFILE, "r") as x:
        content = x.read()
    return content
