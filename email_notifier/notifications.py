from datetime import date

from email.message import EmailMessage


class Notification:
    def __init__(self, elements: dict) -> None:
        self._today = date.today().strftime("%d-%m-%Y")
        self._recipient = elements["email_address"]
        self._subject = "dummy subject"
        self._content = None

    def set_content(self, content: str) -> None:
        self._content = content

    def get_recepient(self) -> str:
        return self._recipient

    def get_email_msg(self) -> EmailMessage:
        msg = EmailMessage()
        msg['Subject'] = self._subject
        msg['To'] = self._recipient
        msg.set_content(self._content)
        return msg


class NotificationGarbage(Notification):
    def __init__(self, elements: dict) -> None:
        super().__init__(elements)
        self._street = elements["specifics"]["street_name"]
        self._number = elements["specifics"]["number"]
        self._subject = f"Garbage schedule for: {self._street} {self._number} on: {self._today}"

    def get_street(self):
        return self._street

    def get_number(self):
        return self._number
