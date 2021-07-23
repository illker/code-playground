#!/usr/bin/python3
""" locked boxes """


def canUnlockAll(boxes):
    """ method that determines if all the boxes can be opened """
    keys = [x for x in range(1, len(boxes))]
    for i in range(len(boxes)):
        for key in boxes[i]:
            if key in keys and key != i:
                keys.remove(key)
    return len(keys) == 0
