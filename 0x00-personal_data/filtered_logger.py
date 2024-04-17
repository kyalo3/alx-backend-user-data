#!/usr/bin/env python3
"""
Regex-ing
"""

import re
from typing import List
import logging
import mysql.connector
import os


PII_FIELDS = ('name', 'email', 'phone', 'ssn', 'password')


def filter_datum(
        fields: List[str],
        redaction: str, message: str, separator: str) -> str:
    """
    function should use a regex to replace
    occurrences of certain field values
    """
    for field in fields:
        message = re.sub(field + '=.*?' + separator,
                         field + '=' + redaction + separator, message)
    return message


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class
        """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        """ init method """
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        NotImplementedError
        message = super(RedactingFormatter, self).format(record)
        redacted = filter_datum(
            self.fields,
            self.REDACTION,
            message,
            self.SEPARATOR)
        return redacted


def get_logger() -> logging.Logger:
    """
    function that takes no arguments
    """
    logger = logging.getLogger("user_data")
    logger.setLevel(logging.INFO)
    logger.propagate = False

    stream_handler = logging.StreamHandler()
    stream_handler.setLevel(logging.INFO)

    formatter = RedactingFormatter(list(PII_FIELDS))

    stream_handler.setFormatter(formatter)
    logger.addHandler(stream_handler)
    return logger;