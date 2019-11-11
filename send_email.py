import smtplib
import os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
from email.message import Message
import base64
import mimetypes
from email.mime.application import MIMEApplication


email_user =  ‘test@gmail.com’
email_send = 'test2@gmail.com'
cc = ['cc1@gmail.com', 'cc2@gmail.com']

subject = 'Daily Report - Order Status'

toaddrs = ['test2@gmail.com', 'test3@gmail.com', 'test4@gmail.com’']

msg = MIMEMultipart()
msg['from'] = email_user
msg['to'] = ', '.join(toaddrs)
msg['subject'] = subject

body = 'body_text_here'
msg.attach(MIMEText(body, 'plain'))
    
filename = r'C:\users\username\Desktop\csvfilename.csv'
attachment = open(filename, "rb")

part = MIMEBase('application', 'octet-stream')
part.set_payload(attachment.read())
encoders.encode_base64(part)
part.add_header('Content-Disposition', 'attachment; filename= %s' % 'csvfilename.csv')
msg.attach(part)

text = msg.as_string()

def send_mail():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(email_user, 'password')
    server.sendmail(email_user, toaddrs, text)
    server.quit()

send_mail()
