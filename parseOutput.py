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

def getFilesByStatus(status, statusSymbol, outputJsons):
    statusFiles = ""
    for jsonPart in outputJsons:
        outputJson = json.loads(jsonPart)
        if outputJson['action'] == status:
            statusFiles = statusSymbol + " " + outputJson['item'] + " (size: " + outputJson['data_size'] + ")\n"
    return statusFiles


def parseBackupOutput(standardOutJson):
    backupOutputString = ""
    standardOutJsons = standardOutJson.split()
    for jsonPart in standardOutJsons:
        outputJson = json.loads(jsonPart)
        json_formatted_str = json.dumps(outputJson, indent=4)
        if outputJson['message_type'] == "summary":
            backupOutputString = f"Summary: {json_formatted_str}\n"
    
    backupOutputString = backupOutputString + getFilesByStatus("new", "+", standardOutJsons)
    backupOutputString = backupOutputString + getFilesByStatus("changed", "o", standardOutJsons)

    #print(outputJson)



    
