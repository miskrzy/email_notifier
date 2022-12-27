import logging
import os
import smtplib

from email.message import EmailMessage

class EmailSender:
    def __init__(self, email: str, passw: str) -> None:
        self._email = email
        self._passw = passw
        self._server = smtplib.SMTP_SSL('smtp.gmail.com', 465)

    def __enter__(self):
        self._server.login(self._email, self._passw)
        return self
    
    def __exit__(self, *args):
        self._server.quit()

    def send_email(self, receiver: str, msg: EmailMessage):
        self._server.send_message(msg, self._email, receiver)
