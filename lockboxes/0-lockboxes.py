#!/usr/bin/python3

def canUnlockAll(boxes):
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

