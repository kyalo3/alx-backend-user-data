#!/usr/bin/env python3
"""
Regex-ing
"""

import re


def filter_datum(fields, redaction, message, separator):
    """
    function should use a regex to replace
    occurrences of certain field values
    """
    return re.sub(
        '|'.join(
            f'(?<={re.escape(separator)}{field}=)[^{re.escape(separator)}]*' for field in fields),
        redaction,
        message
    )
