import json

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


class Email:
    def __init__(self, from_email, to_email, subject, body):
        password = Email.retrieve_password(from_email)

        self.msg = MIMEMultipart('alternative')
        self.msg['Subject'] = subject
        self.msg['From'] = from_email
        self.msg['To'] = to_email

        mime = MIMEText(body, 'html')
        self.msg.attach(mime)

        try:
            mail = smtplib.SMTP('smtp.gmail.com', 587)
            mail.ehlo()
            mail.starttls()
            mail.login(from_email, password)
            mail.sendmail(from_email, to_email, self.msg.as_string())
            mail.quit()
            print("Email sent!")

        except Exception as ex:
            print("Failed: %s" % ex)

    @staticmethod
    def retrieve_password(email_address):
        with open('credentials.json', 'r') as fp:
            data = json.load(fp)
            password = data.get(email_address, None)

        return password
