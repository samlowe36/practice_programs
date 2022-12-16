from email.message import EmailMessage
from email_confidential import *
import ssl
import smtplib

email_sender = sender
email_password = password

email_receiver = receiver

email_subject = subject
email_body = body

em = EmailMessage()
em["From"] = email_sender
em["To"] = email_receiver
em["subject"] = email_subject
em.set_content(email_body)

context = ssl.create_default_context()

with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as smtp:
    smtp.login(email_sender, email_password)
    smtp.sendmail(email_sender, email_receiver, em.as_string())

