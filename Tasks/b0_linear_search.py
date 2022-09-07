"""
This module implements some functions based on linear search algo
"""
from typing import Sequence


def min_search(arr: Sequence) -> int:
    """
    Function that find minimal element in array

    :param arr: Array containing numbers
    :return: index of first occurrence of minimal element in array
    """
    size = len(arr)
    try:
        min = arr[0]
        idx = 0
        for i in range(1, size):
            if min > arr[i]:
                idx = i
                min = arr[i]
        return idx
    except IndexError:
        return -1
