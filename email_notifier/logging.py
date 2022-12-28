from datetime import datetime

class Logger:
    class LogMessage:
        def __init__(self, level, file_name, time, message) -> None:
            self._level = level
            self._file_name = file_name
            self._time = time
            self._message = message

        def __str__(self) -> str:
            return f"{self._level} {self._file_name} {self._time}: {self._message}"

    _DATETIME_FORMAT = "%Y-%m-%d %H:%M:%S"

    def __init__(self) -> None:
        self._message_stack = []

    def info(self, message: str, file_name: str = "") -> None:
        now = datetime.now().strftime(self._DATETIME_FORMAT)
        logMessage = self.LogMessage("INFO", file_name, now, message)
        self._message_stack.append(str(logMessage))

    def error(self, message: str, file_name: str = "") -> None:
        now = datetime.now().strftime(self._DATETIME_FORMAT)
        logMessage = self.LogMessage("ERROR", file_name, now, message)
        self._message_stack.append(str(logMessage))

    def warning(self, message: str, file_name: str = "") -> None:
        now = datetime.now().strftime(self._DATETIME_FORMAT)
        logMessage = self.LogMessage("WARNING", file_name, now, message)
        self._message_stack.append(str(logMessage))

    def debug(self, message: str, file_name: str = "") -> None:
        now = datetime.now().strftime(self._DATETIME_FORMAT)
        logMessage = self.LogMessage("DEBUG", file_name, now, message)
        self._message_stack.append(str(logMessage))

    def get_message_stack_as_str(self) -> str:
        return "\n".join(self._message_stack) + "\n"
