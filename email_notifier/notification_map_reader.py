import json

from email_notifier.notifications import Notification, NotificationGarbage

class NotificationMapReader:
    def __init__(self, notification_map: dict, logger) -> None:
        self._logger = logger
        try:
            self._notification_map = notification_map
            all_elements = [self._parse_notification_type_to_class(i) for i in self._notification_map]
            self._all_elements = [i for i in all_elements if i is not None]  
            self._logger.debug("Sucessfully parsed all notification configurations")         
        except Exception as e:
            self._logger.error(f"Error while reading notification_map.json: {e}")
            raise e

    def _parse_notification_type_to_class(self, elements: dict) -> Notification:
        notification_type = elements["message_type"]
        if notification_type == "garbage":
            self._logger.debug(f"Found a type of notification for {notification_type}: NotificationGarbage")
            return NotificationGarbage(elements)
        else:
            self._logger.warning("Did not get the type of notification from notification_map for: {notification_type}")
            return None

    def get_all_elements(self):
        return self._all_elements
