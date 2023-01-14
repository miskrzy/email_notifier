import json
import os

from datetime import datetime, date
from email.message import EmailMessage

from email_notifier.email_logging import EmailLogger
from email_notifier.email_sender import EmailSender
from email_notifier.garbage_scrapper import GarbageScrapper
from email_notifier.mail_crafting import craft_garbage_mails
from email_notifier.notification_map_reader import NotificationMapReader, NotificationGarbage


LOGS_EMAIL = os.environ["host_email"]

def create_log_message(logger: EmailLogger) -> EmailMessage:
    email_msg = EmailMessage()
    email_msg['Subject'] = f'log stack from {date.today()}'
    email_msg['From'] = LOGS_EMAIL
    email_msg['To'] = LOGS_EMAIL
    email_msg.set_content(logger.get_message_stack_as_str())
    return email_msg

def run():
    logger = EmailLogger()
    logger.info(f"Coordinator ran at {datetime.now()}")
    notification_map = os.environ['notification_map']
    notification_map_dict = json.loads(notification_map)
    logger.debug("Successfully read the notification_map from config")
    notification_map_reader = NotificationMapReader(notification_map=notification_map_dict, logger=logger)
    garbage_scrapper = GarbageScrapper(logger=logger)
    passw = os.environ["gmail_app_pass"]

    garbage_notifications = []
    other_notifications = []
    for notification in notification_map_reader.get_all_elements():
        if isinstance(notification, NotificationGarbage):
            garbage_notifications.append(notification)
        else:
            other_notifications.append(notification)
    
    garbage_notifications_with_content = craft_garbage_mails(notifications=garbage_notifications, garbage_scrapper=garbage_scrapper, logger=logger)
    other_notifications_with_content = []
    all_notifications = garbage_notifications_with_content + other_notifications_with_content    
    
    with EmailSender(email=LOGS_EMAIL, passw=passw, logger=logger) as email_sender:
        for notification in all_notifications:
            email_sender.send_email(notification.get_recepient(), notification.get_email_msg())

        email_sender.send_email(receiver=LOGS_EMAIL, msg=create_log_message(logger))
