import smtplib

HOST = "www.gmail.com"
SUBJECT = "Test email from Python"
TO = "sgarain1001@gmail.com"
FROM = "sgarain1001@gmail.com"
text = "blah blah blah"
BODY = "\r\n".join((
    f"From: {FROM}",
    f"TO: {TO}",
    f"Subject: {SUBJECT}",
    "",
    text)
)
server = smtplib.SMTP(HOST)
server.sendmail(From,[TO], BODY)
server.quit()