#!/usr/bin/env python3
"""
Regex-ing
"""

import re
from typing import List
import logging
import mysql.connector
import os


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
