#!/usr/bin/python3


def canUnlockAll(boxes):
    keys = set([0])

    for i in range(len(boxes)):
        if i in keys:
            keys.update(boxes[i])

    return len(keys) == len(boxes)
