import math
from typing import Sequence, Optional


def binary_search(elem: int, arr: Sequence) -> Optional[int]:
    """
    Performs binary search of given element inside of array

    :param elem: element to be found
    :param arr: array where element is to be found
    :return: Index of element if it's presented in the arr, None otherwise
    """
    size = len(arr)
    idx = round(size / 2)
    n = 1
    t = round(math.log2(size)) + 1
    while 1:
        a = arr[idx]
        try:
            a2 = arr[idx - 1]
        except IndexError:
            a2 = None
        if a == elem and a2 != elem:
            return idx
        else:
            if elem > a:
                n += 1
                idx += round(size / (2 ** n))
            else:
                n += 1
                idx -= round(size / (2 ** n))
        if n == t:
            return None
