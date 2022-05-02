import os, os.path
import subprocess
import configparser
import time
import parseOutput
import statusFile
import mail

config = configparser.ConfigParser()
config.read('/home/pi/restic-backup/config.cfg')
REPOSITORY = config['BACKUP']['REPOSITORY']
DIRECTORY_TO_BACKUP = config['BACKUP']['DIRECTORY_TO_BACKUP']

def isGoogleMounted():
    numOfFiles = len(os.listdir('/home/pi/mnt/gdrive/'))
    if numOfFiles > 0:
        print("Google drive mounted with " + str(numOfFiles) + " files")
        statusFile.writeToFile("Google drive mounted with " + str(numOfFiles) + " files", includeTime=True)
        return True
    else:
        print("Google Drive not mounted")
        statusFile.writeToFile("Google Drive not mounted", includeTime=True)
        return False

def mountGoogleDrive():
    output = subprocess.run(["rclone", "mount", "--allow-other", "GoogleDrive:", "/home/pi/mnt/gdrive/", "--daemon"], capture_output=True)
    print("Google Drive mounting ")
    print(output)
    statusFile.writeToFile("Google Drive mouting:", includeTime=True)
    statusFile.writeToFile(output + "\n")
    time.sleep(30)

def backupFiles():
    output = subprocess.run(["restic", "-r", REPOSITORY, "--verbose=2", "backup", "--tag", "automatic", DIRECTORY_TO_BACKUP], capture_output=True)
    print(output)
    return output

def pruneBackups():
    output = subprocess.run(["restic", "-r", REPOSITORY, "--verbose=2", "forget", "--keep-daily", "7", "--keep-weekly", "4", "--keep-monthly", "12", "--prune"], capture_output=True)
    print(output)
    return output


if __name__ == "__main__":
    statusFile.initOutputFile(REPOSITORY, DIRECTORY_TO_BACKUP)
    if not isGoogleMounted():
        mountGoogleDrive()
    if isGoogleMounted():
        print("Google drive is mounted, proceed...\n\n")
        statusFile.writeToFile("Google drive is mounted, proceed...\n", includeTime=True)
    else:
        print("Abort.")
        statusFile.writeToFile("Abort.", includeTime=True)
        #TODO: Abort
    output=backupFiles()
    statusString = parseOutput.parseProcessStatusOutput(output)
    statusFile.writeToFile(statusString)

    output = pruneBackups()
    statusString = parseOutput.parseProcessStatusOutput(output)
    statusFile.writeToFile(statusString)
    statusFile.close()
    content = statusFile.getStatusFileContent()
    mail.sendMail(content)

