import json
import os
import sys
from email.message import EmailMessage

sys.path.insert(0, os.path.abspath(os.path.join(__file__, os.pardir, os.pardir)))

from email_notifier.email_sender import EmailSender
from email_notifier.email_logging import EmailLogger


class TestEmailSender:
    def test_send_email(self):

        logger = EmailLogger()

        CONFIG_PATH = os.path.abspath(os.path.join(__file__, os.pardir, os.pardir, "local.settings.json"))
        with open(CONFIG_PATH) as config_file:
            config_dict = json.load(config_file)
        passw = config_dict["Values"]["gmail_app_pass"]
        email = config_dict["Values"]["host_email"]

        msg = EmailMessage()
        msg['Subject'] = 'test'
        msg['From'] = email
        msg['To'] = email
        msg.set_content("test")

        with EmailSender(email, passw, logger) as emailSender:
            emailSender.send_email(email, msg)


testEmailSender = TestEmailSender()
testEmailSender.test_send_email()
