import smtplib
from pathlib import Path
from dotenv import load_dotenv
import os


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
        with smtplib.SMTP(self.smtp_server, self.port) as server:
            # server.login(sender_email, password)
            server.sendmail(self.sender_email,
                            self.receiver_email, self.message)
