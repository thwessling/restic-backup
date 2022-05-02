
import os, os.path
import subprocess
import configparser
import time


config = configparser.ConfigParser()
config.read('config.cfg')
REPOSITORY = config['BACKUP']['REPOSITORY']
DIRECTORY_TO_BACKUP = config['BACKUP']['DIRECTORY_TO_BACKUP']

def isGoogleMounted():
    numOfFiles = len(os.listdir('/home/pi/mnt/gdrive/'))
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
    time.sleep(30)

def backupFiles():
    output = subprocess.run(["restic", "-r", REPOSITORY, "--verbose=2", "backup", "--json", DIRECTORY_TO_BACKUP], capture_output=True)
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
    
