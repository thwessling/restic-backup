import os
import smtplib, ssl
import configparser

config = configparser.ConfigParser()
config.read('/home/pi/restic-backup/config.cfg')

config = configparser.ConfigParser()
config.read('/home/pi/restic-backup/config.cfg')



STATUSFILE = config['BACKUP']['STATUSFILE']

STATUSMAILADDRESS = config['MAIL']['STATUSMAILADDRESS']
MAILSERVER = config['MAIL']['MAILSERVER']
MAILUSER = config['MAIL']['MAILUSER']


def sendMail():
    content = getStatusFileContent()
    port = 465  # For SSL
    password = os.environ["MAIL_PW"]

    # Create a secure SSL context
    context = ssl.create_default_context()
    smtp = smtplib.SMTP(MAILSERVER, port='587')
    smtp.ehlo()  
    smtp.starttls()
    print(STATUSMAILADDRESS)
    print(password)
    smtp.login(MAILUSER, password)
    smtp.sendmail(STATUSMAILADDRESS, STATUSMAILADDRESS, content)
    smtp.quit()


def getStatusFileContent():
    x = open(STATUSFILE)
    content = x.read()
    x.close()
    print(content)
    return content

