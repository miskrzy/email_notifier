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

        EMAIL = "schedumail.skr@gmail.com"
        CONFIG_PATH = os.path.abspath(os.path.join(__file__, os.pardir, os.pardir, "local.settings.json"))
        with open(CONFIG_PATH) as config_file:
            config_dict = json.load(config_file)
        passw = config_dict["Values"]["gmail_app_pass"]

        msg = EmailMessage()
        msg['Subject'] = 'test'
        msg['From'] = EMAIL
        msg['To'] = EMAIL
        msg.set_content("test")

        with EmailSender(EMAIL, passw, logger) as emailSender:
            emailSender.send_email(EMAIL, msg)


testEmailSender = TestEmailSender()
testEmailSender.test_send_email()
