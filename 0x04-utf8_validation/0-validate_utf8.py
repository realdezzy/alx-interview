#!/usr/bin/python3
"""Utf-8 validation
"""
from typing import List


def validUTF8(data: List[int]) -> bool:
    """ Validate utf8 passed in as a list of integers.

    Args:
        data (List[int]): List of integers

    Returns:
        bool: True or False
    """
    num_bytes_to_follow = 0
    
    for byte in data:
        # Check if the byte starts with the correct UTF-8 pattern
        if num_bytes_to_follow == 0:
            if (byte >> 7) == 0b0:
                num_bytes_to_follow = 0
            elif (byte >> 5) == 0b110:
                num_bytes_to_follow = 1
            elif (byte >> 4) == 0b1110:
                num_bytes_to_follow = 2
            elif (byte >> 3) == 0b11110:
                num_bytes_to_follow = 3
            else:
                return False
        else:
            # Check if the byte follows the correct continuation pattern
            if (byte >> 6) != 0b10:
                return False
            num_bytes_to_follow -= 1

    # If all bytes are valid, there should be no remaining bytes to follow
    return num_bytes_to_follow == 0
