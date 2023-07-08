#!/usr/bin/python3
"""
lockboxes unlock method
"""


def canUnlockAll(boxes):
    """
    a method that determines if all the boxes can be opened
    :param: boxes lists of boxes
    :return: True if all boxes can be opened else return False
    """
    keys = [0]

    for box_num, box in enumerate(boxes):
        if not box:
            continue
        for key in box:
            if key < len(boxes) and key not in keys and key != box_num:
                keys.append(key)
    if len(keys) == len(boxes):
        return True
    return False
