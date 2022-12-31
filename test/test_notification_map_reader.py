import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(__file__, os.pardir, os.pardir)))

from email_notifier.notification_map_reader import NotificationMapReader, Notification
from email_notifier.logging import Logger


class TestNotificationMapReader:

    _NOTIFICATION_MAP_PATH = os.path.abspath(os.path.join(__file__, os.pardir, os.pardir, "email_notifier", "notification_map.json"))

    def test_get_all_elements(self):
        TEMP_CONTENT = "abc"
        logger = Logger()
        notificationMapReader = NotificationMapReader(self._NOTIFICATION_MAP_PATH, logger)
        notifications = notificationMapReader.get_all_elements()
        for i in notifications:
            assert isinstance(i, Notification)
            i.set_content(TEMP_CONTENT)
            assert i.get_content() == TEMP_CONTENT
            assert isinstance(i.get_subject(), str)
            assert isinstance(i.get_recipient(), str)
            assert '@' in i.get_recipient()
