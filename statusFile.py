
import datetime
import configparser


config = configparser.ConfigParser()
config.read('config.cfg')


STATUSFILE = config['BACKUP']['STATUSFILE']

f = open(STATUSFILE, "w")


def initOutputFile():
    now = datetime.datetime.now()
    currentdate = now.strftime("%Y-%m-%d %H:%M:%S")
    timeStamp = f"Starting backup: {currentdate}"

    f.write(timeStamp + "\n")


def writeToFile(statusText):
    f.write(statusText + "\n")


def close():
    f.close()