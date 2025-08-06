import sys
from networksecurity.logging.logger import logger

class NetworkSecurityException(Exception):
    def __init__(self, error_message, error_details: sys):
        self.error_message = str(error_message)
        _, _, exc_tb = error_details.exc_info()

        if exc_tb:
            self.lineno = exc_tb.tb_lineno
            self.file_name = exc_tb.tb_frame.f_code.co_filename
        else:
            self.lineno = None
            self.file_name = None

    def __str__(self):
        return f"Error occurred in python script name [{self.file_name}] line number [{self.lineno}] error message: [{self.error_message}]"

