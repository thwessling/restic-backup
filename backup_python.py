
from asyncio import open_unix_connection
import os, os.path
import subprocess
import configparser
import time
import parseOutput
import statusFile


config = configparser.ConfigParser()
config.read('config.cfg')
REPOSITORY = config['BACKUP']['REPOSITORY']
DIRECTORY_TO_BACKUP = config['BACKUP']['DIRECTORY_TO_BACKUP']

def isGoogleMounted():
    numOfFiles = len(os.listdir('/home/pi/mnt/gdrive/'))
    if numOfFiles > 0:
        print("Google drive mounted with " + str(numOfFiles) + " files")
        statusFile.writeToFile("Google drive mounted with " + str(numOfFiles) + " files")
        return True
    else:
        print("Google Drive not mounted")
        statusFile.writeToFile("Google Drive not mounted")
        return False

def mountGoogleDrive():
    output = subprocess.run(["rclone", "mount", "--allow-other", "GoogleDrive:", "/home/pi/mnt/gdrive/", "--daemon"], capture_output=True)
    print("Google Drive mounting ")
    print(output)
    statusFile.writeToFile("Google Drive mouting:")
    statusFile.writeToFile(output)
    time.sleep(30)

def backupFiles():
    output = subprocess.run(["restic", "-r", REPOSITORY, "--verbose=2", "backup", DIRECTORY_TO_BACKUP], capture_output=True)
    print(output)
    return output



if __name__ == "__main__":
    statusFile.initOutputFile()
    if not isGoogleMounted():
        mountGoogleDrive()
    if isGoogleMounted():
        print("Proceed.")
        statusFile.writeToFile("Proceed")
    else:
        print("Abort.")
        statusFile.writeToFile("Abort.")
        #TODO: Abort
    output=backupFiles()
    #statusString = parseOutput.parseProcessStatusOutput(output)
    statusFile.writeToFile(output.stdout.decode("utf-8") )
    statusFile.close()

