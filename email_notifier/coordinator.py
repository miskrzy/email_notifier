import os

from datetime import datetime, date
from email.message import EmailMessage

from email_notifier.email_logging import EmailLogger
from email_notifier.email_sender import EmailSender
from email_notifier.garbage_scrapper import GarbageScrapper
from email_notifier.mail_crafting import craft_garbage_mails
from email_notifier.notification_map_reader import NotificationMapReader, NotificationGarbage


NOTIFICATION_MAP_PATH = os.path.abspath(os.path.join(__file__, os.pardir, "notification_map.json"))
LOGS_EMAIL = "schedumail.skr@gmail.com"

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
    notification_map_reader = NotificationMapReader(path=NOTIFICATION_MAP_PATH, logger=logger)
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
    
    with EmailSender(email="schedumail.skr@gmail.com", passw=passw, logger=logger) as email_sender:
        for notification in all_notifications:
            email_sender.send_email(notification.get_recepient(), notification.get_email_msg())

        email_sender.send_email(receiver=LOGS_EMAIL, msg=create_log_message(logger))
