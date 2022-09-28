from typing import List


def partition(container: List[int], l: int, h: int) -> int:
    avg = container[(l + h) // 2]
    i = l
    j = h
    while 1:
        while container[i] < avg:
            i += 1
        while container[j] > avg:
            j -= 1
        if i >= j:
            return container, j
        a = container[i]
        container[i] = container[j]
        container[j] = a
        i += 1
        j -= 1


def quick_sort_rec(container: List[int], l: int, h: int) -> List[int]:
    if l < h:
        container, p = partition(container, l, h)
        container = quick_sort_rec(container, l, p)
        container = quick_sort_rec(container, p + 1, h)
    return container


def sort(container: List[int]) -> List[int]:
    """
    Sort input container with quick sort

    :param container: container of elements to be sorted
    :return: container sorted in ascending order
    """
    container = quick_sort_rec(container, 0, len(container) - 1)
    return container
