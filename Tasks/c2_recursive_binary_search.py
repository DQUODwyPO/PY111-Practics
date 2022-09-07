import math
from typing import Sequence, Optional


def recursive(elem: int, arr: Sequence, idx: int, n: int, t: int) -> int:
    if t == n:
        return None
    size = len(arr)

    try:
        a = arr[idx]
        a2 = arr[idx - 1]
    except IndexError:
        return None

    if elem == arr[idx] and a2 != elem:
        return idx
    else:
        if elem > arr[idx]:
            return recursive(elem, arr, idx + round(size / (2 ** n)), n + 1, t)
        else:
            return recursive(elem, arr, idx - round(size / (2 ** n)), n + 1, t)

def binary_search(elem: int, arr: Sequence) -> Optional[int]:
    """
    Performs binary search of given element inside of array (using recursive way)

    :param elem: element to be found
    :param arr: array where element is to be found
    :return: Index of element if it's presented in the arr, None otherwise
    """
    idx = round(len(arr) / 2)
    t = round(math.log2(len(arr))) + 2
    return recursive(elem, arr, idx, 2, t)
