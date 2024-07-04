import sys
import traceback

from typing import Any

from src.INRCoinSense.logger import logging


def error_message_detail(error: Any, error_detail: sys) -> str:
    """
    This function is used to get the error message details.

    Args:
        error: Error caught by the base Exception class.
        error_detail: system level details of the error.

    Returns:
        str: Formatted error message with details:
            1. File name where the error occurred.`
            2. Line number where the error occurred.
            3. Error message.
    """
    _, _, exc_traceback = error_detail.exc_info()
    frame = traceback.extract_tb(exc_traceback)[-1]
    file_name, line_number = frame.filename, frame.lineno
    error_message = (
        f"Error occurred in script: [{file_name}], line number: [{line_number}], error message: [{str(error)}]"
    )

    return error_message


class CustomException(Exception):
    """
    This class is used to raise custom exceptions.
    """
    def __init__(self, error_message: Any, error_detail: sys):
        """
        This function is used to initialize the CustomException class.
        Args:
            error_message: Error message caught by the base Exception class.
            error_detail: system level details of the error.
        """
        super().__init__(error_message)
        self.error_message = error_message_detail(error_message, error_detail=error_detail)
        logging.error(self.error_message)

    def __str__(self) -> str:
        """
        This function is used to return the error message.

        Returns:
            str: Error message.
        """
        return self.error_message


if __name__ == '__main__':
    try:
        a = 1/0
    except Exception as e:
        logging.error('Divide by zero error! more info below:')
        raise CustomException(e, sys)
