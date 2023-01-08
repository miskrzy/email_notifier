import json

from email_notifier.notifications import Notification, NotificationGarbage

class NotificationMapReader:
    def __init__(self, path, logger) -> None:
        self._logger = logger
        try:
            with open(path) as json_file:
                self._notification_map = json.load(json_file)
            self._logger.debug("Successfully read the notification_map.json")
            all_elements = [self._parse_notification_type_to_class(i) for i in self._notification_map]
            self._all_elements = [i for i in all_elements if i is not None]           
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
