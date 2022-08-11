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
    subject = f"receipt for {recipient_email}"
    body = "your mail"

    em = EmailMessage()
    em.set_content(body)
    em['From'] = fromuser
    em['To'] = recipient_email
    em['Subject'] = subject 

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login(fromuser, PASSWORD)
        server.send_message(em)
        print("Email sent")
        server.quit()  
        #update every 30 minutes 
        time.sleep(1800)
