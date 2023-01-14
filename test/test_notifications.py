import os
import sys

from datetime import date
from email.message import EmailMessage

sys.path.insert(0, os.path.abspath(os.path.join(__file__, os.pardir, os.pardir)))

from email_notifier.notifications import Notification, NotificationGarbage

class TestNotification():
    def test_get_email_msg(self):
        dummy_content = "dummy_content"
        elements = {
            "email_address": "dummy@dummail.com",
            "message_type": "garbage",
            "specifics": {
                "street_name": "Dummy Street",
                "number": "123"
            }
        }
        dummy_subject = "dummy subject"
        notification = Notification(elements)
        notification.set_content(dummy_content)
        msg = notification.get_email_msg()
        assert isinstance(msg, EmailMessage)
        assert msg['Subject'] == dummy_subject
        assert msg['To'] == elements['email_address']
        assert msg.get_content() == dummy_content + "\n"

class TestNotificationGarbage():
    def test_get_email_msg(self):
        dummy_content = "dummy_content"
        elements = {
            "email_address": "dummy@dummail.com",
            "message_type": "garbage",
            "specifics": {
                "street_name": "Dummy Street",
                "number": "123"
            }
        }
        subject = f"Garbage schedule for: {elements['specifics']['street_name']} {elements['specifics']['number']} on: {date.today().strftime('%d-%m-%Y')}"
        notification = NotificationGarbage(elements)
        notification.set_content(dummy_content)
        msg = notification.get_email_msg()
        assert isinstance(msg, EmailMessage)
        assert msg['Subject'] == subject
        assert msg['To'] == elements['email_address']
        assert msg.get_content() == dummy_content + "\n"
