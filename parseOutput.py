from sqlite3 import Timestamp
import subprocess
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
        statusString = statusString + "\n" + backupOutput
    return statusString 

def parseBackupOutput(standardOutJson):
    standardOutJsons = standardOutJson.split()
    for jsonPart in standardOutJsons:
        outputJson = json.loads(jsonPart)
        if outputJson['message_type'] == "summary":
            return f"Summary: {outputJson}"
    
    #print(outputJson)



    
