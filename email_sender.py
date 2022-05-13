import os
import smtplib
import ssl
from pathlib import Path

from dotenv import load_dotenv

dotenv_path = Path('./.env.local')
load_dotenv(dotenv_path=dotenv_path)


class EmailSender:
    port = int(os.getenv("SMTP_PORT"))
    smtp_server = os.getenv("SMTP_SERVER")
    sender_email = os.getenv("SMTP_SENDER")
    receiver_email = os.getenv("SMTP_RECEIVER")
    password = os.getenv("SMTP_PASSWORD")

    def __init__(self, message):
        self.message = message

    def send_email(self):
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL(self.smtp_server, self.port, context=context) as server:
            server.login(self.sender_email, self.password)
            try:
                server.sendmail(self.sender_email, self.receiver_email, self.message)
                print("Sending email")
            except:
                print("Fail to send email")

            server.quit()
