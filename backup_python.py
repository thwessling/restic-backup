
import os, os.path
from turtle import back
from unittest import main
import subprocess
import configparser

config = configparser.ConfigParser()
config.read('config.cfg')
REPOSITORY = config['REPOSITORY']
DIRECTORY_TO_BACKUP = config['DIRECTORY_TO_BACKUP']

def isGoogleMounted():
    numOfFiles = len([name for name in os.listdir('/home/pi/mnt/gdrive/') if os.path.isfile(name)])
    if numOfFiles > 0:
        print("Google drive mounted with " + str(numOfFiles) + " files")
        return True
    else:
        print("Google Drive not mounted")
        return False

def mountGoogleDrive():
    output = subprocess.run(["rclone", "mount", "--allow-other", "GoogleDrive:", "/home/pi/mnt/gdrive/", "--daemon"], capture_output=True)
    print("Google Drive mouting:")
    print(output)

def backupFiles():
    output = subprocess.run(["restic", "-r", REPOSITORY, "--verbose=2", "backup", "", "--json"], capture_output=True)
    print("Backup output:") 
    print(output)    

if __name__ == "__main__":
    print(os.environ["B2_ACCOUNT_ID"])
    isGoogleMounted()
    mountGoogleDrive()

    if isGoogleMounted():
        print("Proceed.")
    else:
        print("Abort.")
        #TODO: Abort
    backupFiles()
    
