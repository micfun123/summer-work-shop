import requests
import json
import sys
import smtplib
import email
from email.message import EmailMessage
import os
import ssl
import time

fromuser = ""
PASSWORD = ""

def send_mail(recipient_email):
    pdf = "receipt.pdf"

    password = os.environ["GMAIL_PASSWORD"]
    fromuser = os.environ["GMAIL_USER"]
    touser = recipient_email  

    subject = "your receipt"
    body = "Your pc parts"
    filepdf = "receipt.pdf"
    em = EmailMessage()
    em.set_content(body)
    em['From'] = fromuser
    em['To'] = recipient_email
    em['Subject'] = subject 
    
    with open(filepdf, 'rb') as f:
        file_data = f.read()
    em.add_attachment(file_data, maintype="application", subtype="pdf", filename=filepdf)



    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login(fromuser, password)
        server.send_message(em)
        print("Email sent")
        server.quit()  
        #update every 30 minutes 
        time.sleep(1800)
