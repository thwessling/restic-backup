import subprocess
import re

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
        statusString = statusString + "\n\n" + backupOutput
    return statusString 



def parseBackupOutput(backupOutput):
    backupOutputStringLines = backupOutput.decode("utf-8").split("\n")

    filteredLines = [line for line in backupOutputStringLines if re.match("unchanged.*", line) != None]

    return "\n".join(filteredLines)


    
