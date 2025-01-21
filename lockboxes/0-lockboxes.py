#!/usr/bin/python3

def canUnlockAll(boxes):
    """
    Determines if all the boxes can be opened.
    A list of lists is given where each inner list represents a box and contains keys to other boxes.
    The function returns True if all boxes can be opened, otherwise returns False.
    Parameters:
    boxes (list of list of int): A list of lists where each inner list contains keys to other boxes.
    Returns:
    bool: True if all boxes can be opened, False otherwise.
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

