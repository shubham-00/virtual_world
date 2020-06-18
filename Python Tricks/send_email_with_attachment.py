import smtplib
from pathlib import Path
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.utils import COMMASPACE, formatdate
from email import encoders
from getpass import getpass


def send_mail(send_from, send_to, subject, message,
              files=[], server="localhost", port=587,
              username='', password='', use_tls=True):

    msg = MIMEMultipart()
    msg['From'] = send_from
    msg['To'] = COMMASPACE.join(send_to)
    msg['Date'] = formatdate(localtime=True)
    msg['Subject'] = subject

    msg.attach(MIMEText(message))

    for path in files:
        part = MIMEBase('application', "octet-stream")
        with open(path, 'rb') as file:
            part.set_payload(file.read())
        encoders.encode_base64(part)
        part.add_header('Content-Disposition',
                        'attachment; filename="{}"'.format(Path(path).name))
        msg.attach(part)

    smtp = smtplib.SMTP(server, port)

    if use_tls:
        smtp.starttls()

    smtp.login(username, password)
    smtp.sendmail(send_from, send_to, msg.as_string())
    smtp.quit()


_username = input("Enter username: ")
_password = getpass("Enter password: ")
_send_to = input("Send to: ")
_subject = input("Enter Subject: ")
_message = input("Enter message: ")
_file = input("Enter file path: ")

send_mail(_username,
          [_send_to],    # this is where mail will be send
          _subject, _message,
          files=[_file],
          server="smtp.gmail.com", port=587,
          username=_username,
          password=_password,
          use_tls=True)

print('Email sent...')