#!/usr/bin/python
import smtplib

class GmailTransport:
    def __init__(self):
        smtpAgent = smtplib.SMTP('smtp.gmail.com', 587)
        smtpAgent.ehlo()
        smtpAgent.starttls()
        smtpAgent.login('ajimenez78@gmail.com', 'vkpukwbzksqfcujt')
        self.smtpAgent = smtpAgent

    def sendMeHelloMail(self):
        from_address = 'ajimenez78@gmail.com'
        to_address = from_address
        msg_subject = 'Hello world!'
        msg_body = 'This is only a test mail body.'
        msg = 'Subject: ' + msg_subject + '\n' + msg_body
        
        self.smtpAgent.sendmail(from_address, to_address, msg)

    def __del__(self):
        try:
            self.smtpAgent.quit()
        except Exception as err:
            pass

myTransport = GmailTransport()
myTransport.sendMeHelloMail()

