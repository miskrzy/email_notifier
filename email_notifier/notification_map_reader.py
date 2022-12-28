import json
from datetime import date


class Notification:
    def __init__(self, elements: dict) -> None:
        self._today = date.today().strftime("%d-%m-%Y")
        self._recipient = elements["email_address"]
        self._subject = "dummy subject"
        self._content = None

    def set_content(self, content: str) -> None:
        self._content = content

    def get_recipient(self) -> str:
        return self._recipient

    def get_subject(self) -> str:
        return self._subject

    def get_content(self) -> str:
        return self._content


class NotificationGarbage(Notification):
    def __init__(self, elements: dict) -> None:
        super().__init__(elements)
        self._street = elements["specifics"]["street_name"]
        self._number = elements["specifics"]["number"]
        self._subject = f"Garbage schedule for: {self._street} {self._number} on: {self._today}"


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
            self._logger.debug(f"Found a type of notification: {notification_type}")
            return NotificationGarbage(elements)
        else:
            self._logger.warning("Did not get the type of notification from notification_map")
            return None

    def get_all_elements(self):
        return self._all_elements
