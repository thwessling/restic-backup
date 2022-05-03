import subprocess
import re

def parseProcessStatusOutput(completedProcess):
    '''
    Return status information about process in pretty string and the status code in a tuple:
    (statusString, statusCode)
    '''
    statusCode = completedProcess.returncode

    statusString = (
        f"Process {completedProcess.args} has completed "
        f"with statuscode {statusCode}. "
    )

    if statusCode != 0:
        statusString = statusString + f". STDERR: {completedProcess.stderr}"
    else:
        statusString = statusString + "\n\n"
    return (statusString,statusCode)



def parseBackupOutput(backupCommandOutput):
    statusParse = parseProcessStatusOutput(backupCommandOutput)
    statusText = statusParse[0]
    statusCode = statusParse[1]
   
    if statusCode == 0:
        backupOutput = backupCommandOutput.stdout
        backupOutputStringLines = backupOutput.decode("utf-8").split("\n")
        filteredLines = [line for line in backupOutputStringLines if re.match("unchanged.*", line) == None]
        statusText = statusText + "\n".join(filteredLines)

    return statusText


    
