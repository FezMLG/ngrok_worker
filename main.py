import sched
import time
from pathlib import Path
import ngrok
from dotenv import load_dotenv
import os

from email import Email

dotenv_path = Path('./.env.local')
load_dotenv(dotenv_path=dotenv_path)

global lastAddress
global client


def do_something(sc):
    global lastAddress
    print("Doing stuff...", time.strftime('%X %x'))
    for t in client.tunnels.list():
        url = t.public_url
        print(url)
        if url != lastAddress:
            lastAddress = url
            Email(url).sendEmail()

    sc.enter(5, 1, do_something, (sc,))


if __name__ == '__main__':
    lastAddress = ""
    client = ngrok.Client(os.getenv('API_KEY'))
    s = sched.scheduler(time.time, time.sleep)
    s.enter(1, 1, do_something, (s,))
    s.run()
