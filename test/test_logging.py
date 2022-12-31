import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(__file__, os.pardir, os.pardir)))

from email_notifier.logging import Logger


class TestLogger:
    def test_info(self):
        MESSAGE = "some message"
        logger = Logger()
        logger.info(message=MESSAGE, file_name=__file__)
        
        message_to_check = logger._message_stack[0]
        assert "INFO" in message_to_check
        assert __file__ in message_to_check
        assert MESSAGE in message_to_check
        assert len(message_to_check) == len(MESSAGE + __file__ + "INFO" + "9999-99-99 99:99:99" +":   ")

    def test_error(self):
        MESSAGE = "some message"
        logger = Logger()
        logger.error(message=MESSAGE, file_name=__file__)
        
        message_to_check = logger._message_stack[0]
        assert "ERROR" in message_to_check
        assert __file__ in message_to_check
        assert MESSAGE in message_to_check
        assert len(message_to_check) == len(MESSAGE + __file__ + "ERROR" + "9999-99-99 99:99:99" +":   ")

    def test_warning(self):
        MESSAGE = "some message"
        logger = Logger()
        logger.warning(message=MESSAGE, file_name=__file__)
        
        message_to_check = logger._message_stack[0]
        assert "WARNING" in message_to_check
        assert __file__ in message_to_check
        assert MESSAGE in message_to_check
        assert len(message_to_check) == len(MESSAGE + __file__ + "WARNING" + "9999-99-99 99:99:99" +":   ")

    def test_debug(self):
        MESSAGE = "some message"
        logger = Logger()
        logger.debug(message=MESSAGE, file_name=__file__)
        
        message_to_check = logger._message_stack[0]
        assert "DEBUG" in message_to_check
        assert __file__ in message_to_check
        assert MESSAGE in message_to_check
        assert len(message_to_check) == len(MESSAGE + __file__ + "DEBUG" + "9999-99-99 99:99:99" +":   ")

    def test_get_message_stack_as_str(self):
        MESSAGE_INFO = "some info"
        MESSAGE_ERROR = "some error"
        logger = Logger()
        logger.info(message=MESSAGE_INFO, file_name=__file__)
        logger.error(message=MESSAGE_ERROR, file_name=__file__)
        
        message_to_check = logger.get_message_stack_as_str()
        assert "INFO" in message_to_check
        assert "ERROR" in message_to_check
        assert __file__ in message_to_check
        assert MESSAGE_INFO in message_to_check
        assert MESSAGE_ERROR in message_to_check
        assert message_to_check.count("\n") == 2
