from sqlite3 import Timestamp
import subprocess
import datetime
import json

def parseProcessStatusOutput(completedProcess):
    '''
    Return status information about process in pretty string.
    '''
    statusCode = completedProcess.returncode

    statusString = (
        f"Process {completedProcess.args} has completed "
        f"with statuscode {statusCode}. "
    )

    if statusCode != 0:
        statusString = statusString + f". STDERR: {completedProcess.stderr}"
    else:
        backupOutput = parseBackupOutput(completedProcess.stdout)
    return parseProcessStatusOutput 

def parseBackupOutput(standardOutJson):
    outputJson = json.loads(standardOutJson)
    print(outputJson)


def createStatusMail(statusFile, completedProcess):
    now = datetime.datetime.now()
    currentdate = now.strftime("%Y-%m-%d %H:%M:%S")
    timeStamp = f"Starting backup: {currentdate}"
    statusText = parseProcessStatusOutput(completedProcess)

    with open('statusFile', "w") as f:
        f.write(timeStamp + "\n")
        f.write(statusText)


    
