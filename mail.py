import os
import datetime
import smtplib, ssl
import configparser
from email.message import EmailMessage

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
    smtp.login(MAILUSER, password)
    smtp.send_message(content)
    smtp.quit()


def getStatusFileContent():
    with open(STATUSFILE) as fp:
        msg = EmailMessage()
        msg.set_content(fp.read())

    now = datetime.datetime.now()
    currentdate = now.strftime("%Y-%m-%d %H:%M:%S")

    msg['To'] =  STATUSMAILADDRESS 
    msg['From'] = STATUSMAILADDRESS 
    msg['Subject'] = f"Subject: Restic Log for {currentdate}"
    print(msg)
    return msg

