#!/usr/bin/python3


def canUnlockAll(boxes):
    """
    a method that determines if all the boxes can be opened
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
