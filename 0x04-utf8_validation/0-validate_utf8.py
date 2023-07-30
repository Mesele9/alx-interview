#!/usr/bin/python3
""" 0-validate_utf8.py """


def validUTF8(data):
    """ a method that determines if a given data set represents a valid UTF-8
    encoding
    """
    def countLeadingOnes(byte):
        mask = 1 << 7
        count = 0
        while byte & mask:
            count += 1
            mask >>= 1
        return count

    i = 0
    while i < len(data):
        byte = data[i]
        length = countLeadingOnes(byte)

        if length == 0:
            i += 1
        else:
            if length < 2 or length > 4:
                return False

            if i + length > len(data):
                return False

            for j in range(i + 1, i + length):
                if (data[j] >> 6) != 0b10:
                    return False

            i += length

    return True

