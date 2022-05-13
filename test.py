import smtplib
import ssl

# port = 25  # For SSL
# smtp_server = "192.168.50.210"
# sender_email = "me@me.com"  # Enter your address
# receiver_email = "konradchw@gmail.com"  # Enter receiver address
# # password = input("Type your password and press enter: ")
# password = ""
# message = """\
# Subject: Hi there
#
# This message is sent from Python."""
#
# with smtplib.SMTP(smtp_server, port) as server:
#     # server.login(sender_email, password)
#     server.sendmail(sender_email, receiver_email, message)

with smtplib.SMTP("192.168.50.210", 25) as smtp:
    smtp.noop()
