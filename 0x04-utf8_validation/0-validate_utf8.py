#!/usr/bin/python3
"""
UTF-8 validation
"""


def validUTF8(data):
    """
    Determine whether or not [data] is a UTF-8 encoding
    """
    num_bytes = 0

    for num in data:
        byte = num & 0xFF

        if num_bytes == 0:
            # Determine how many bytes to expect for the current character
            if (byte >> 7) == 0b0:
                num_bytes = 0
            elif (byte >> 5) == 0b110:
                num_bytes = 1
            elif (byte >> 4) == 0b1110:
                num_bytes = 2
            elif (byte >> 3) == 0b11110:
                num_bytes = 3
            else:  # Invalid leading byte, hence cannot be UTF-8
                return False
        else:
            # Expect additional byte
            if (byte >> 6) != 0b10:
                return False
            num_bytes -= 1

    return num_bytes == 0