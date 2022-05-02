import os
import smtplib, ssl
import configparser

config = configparser.ConfigParser()
config.read('/home/pi/restic-backup/config.cfg')

STATUSMAILADDRESS = config['MAIL']['STATUSMAILADDRESS']
MAILSERVER = config['MAIL']['MAILSERVER']


def sendMail(message):

    port = 465  # For SSL
    password = os.environ["MAIL_PW"]

    # Create a secure SSL context
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(MAILSERVER, 465, context=context) as server:
        server.login(STATUSMAILADDRESS, password)
        server.sendmail(STATUSMAILADDRESS, STATUSMAILADDRESS, message)