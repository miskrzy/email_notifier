import json
import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(__file__, os.pardir, os.pardir)))

from email_notifier.notification_map_reader import NotificationMapReader, Notification
from email_notifier.email_logging import EmailLogger


class TestNotificationMapReader:

    _LOCAL_SETTINGS_JSON = os.path.abspath(os.path.join(__file__, os.pardir, os.pardir, "local.settings.json"))

    def test_get_all_elements(self):
        logger = EmailLogger()
        print(f'before_read: {self._LOCAL_SETTINGS_JSON}')
        with open(self._LOCAL_SETTINGS_JSON) as local_settings:
            print(f'after read: {local_settings}')
            notification_map = json.load(local_settings)['Values']['notification_map']
            notification_map_dict = json.loads(notification_map)
            print(type(notification_map_dict))
            print(notification_map_dict[0])
            print(notification_map_dict[0]['email_address'])
        notificationMapReader = NotificationMapReader(notification_map_dict, logger)
        notifications = notificationMapReader.get_all_elements()
        for i in notifications:
            assert isinstance(i, Notification)
