import json
import os
import sys
from email.message import EmailMessage

sys.path.insert(0, os.path.abspath(os.path.join(__file__, os.pardir, os.pardir)))

from email_notifier.email_sending.email_sender import EmailSender


class TestEmailSender:
    def test_send_email(self):

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

        with EmailSender(EMAIL, passw) as emailSender:
            emailSender.send_email(EMAIL, msg)


testEmailSender = TestEmailSender()
testEmailSender.test_send_email()
