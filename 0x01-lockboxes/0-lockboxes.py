#!/usr/bin/python3
'''
Define canUnlockAll function
'''


def canUnlockAll(boxes):
    '''
    Check if all boxes can be unlocked.

    Args:
        boxes int[[]]: the boxes

    Return:
        True if all boxes can be unlocked, otherwise false
    '''
    keys = set()
    keys.add(0)
    i = 0

    for box in boxes:
        for key in box:
            if key != i:
                keys.add(key)
        i += 1

    for i in range(len(boxes)):
        if i not in keys:
            return False

    return True
