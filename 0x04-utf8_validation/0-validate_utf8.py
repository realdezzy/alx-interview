#!/usr/bin/env python3
"""Utf-8 validation
"""
import unicodedata
from typing import List 


def validUTF8(data: List[int]) -> bool:
    """Validate utf8 string

    Args:
        data (List[int]): list of integer representing the UTF-8 value

    Returns:
        bool: True if all values are valid
    """
    try:
        for i in data:
            unicodedata.name(chr(i))
        return True

    except:
        return False
