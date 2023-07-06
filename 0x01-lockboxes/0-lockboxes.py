#!/usr/bin/env python3
"""
    Lockboxes
"""


def canUnlockAll(boxes: list) -> bool:
    """Checks if all boxes can be unlocked

    Args:
        boxes (list): list of boxes to check

    Returns:
        bool: boolean indicating whether all boxes can be unlocked
    """
    new_boxes: list = []
    box_length = len(boxes)

    for box in range(box_length):
        if box + 1 == box_length:
            break
        if box + 1 in boxes[box]:
            new_boxes.append(True)
        else:
            new_boxes.append(False)

    return all(new_boxes)
