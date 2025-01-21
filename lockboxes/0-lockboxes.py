#!/usr/bin/python3
"""
    You have n number of locked boxes in front of you.
    Each box is numbered sequentially from 0 to n - 1 and
    each box may contain keys to the other boxes.
"""

def canUnlockAll(boxes):
    """
    Determines if all boxes can be opened.

    :param boxes: List of lists where each inner list contains keys to other boxes
    :return: True if all boxes can be opened, otherwise False
    """
    if not isinstance(boxes, list):
        return False
    
    n = len(boxes)
    opened = [False] * n
    opened[0] = True
    keys = set(boxes[0])

    while keys:
        key = keys.pop()

        if 0 <= key < n and not opened[key]:
            opened[key] = True
            keys.update(boxes[key])
    
    return all(opened)

