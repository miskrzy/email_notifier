import logging
import os
import smtplib

from email.message import EmailMessage

from email_notifier.email_logging import EmailLogger

class EmailSender:
    def __init__(self, email: str, passw: str, logger: EmailLogger) -> None:
        self._email = email
        self._passw = passw
        self._server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        self._logger = logger

    def __enter__(self):
        try:
            self._server.login(self._email, self._passw)
            self._logger.info("Successfully logged in to smtp server")
        except Exception as e:
            self._logger.error(f"Error while trying to login to smtp server: {e}")
            raise e
        return self
    
    def __exit__(self, *args):
        self._server.quit()

    def send_email(self, receiver: str, msg: EmailMessage) -> bool:
        try:
            self._server.send_message(msg, self._email, receiver)
            self._logger.info(f"Email with subject: {msg['Subject']} was sent to {receiver}")
            return True
        except Exception as e:
            self._logger.warning(f"Error encountered while trying to send email with msg {msg} to {receiver}")
            return False


