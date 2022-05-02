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
    smtp = smtplib.SMTP(MAILSERVER, port='465')
    smtp.ehlo()  
    smtp.starttls()
    smtp.login(STATUSMAILADDRESS, password)
    smtp.sendmail(STATUSMAILADDRESS, STATUSMAILADDRESS, message)
    smtp.quit()
