
import os, os.path
from unittest import main
import subprocess


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
    print(output)

if __name__ == "__main__":
    print(os.environ["B2_ACCOUNT_ID"])
    isGoogleMounted()
    
