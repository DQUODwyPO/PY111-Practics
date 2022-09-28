from typing import List


def sort(container: List[int]) -> List[int]:
    """
    Sort input container with bubble sort

    :param container: container of elements to be sorted
    :return: container sorted in ascending order
    """
    size = len(container)
    for i in range(size):
        change = False
        for j in range(size - i - 1):
            if container[j] > container[j + 1]:
                a = container[j + 1]
                container[j + 1] = container[j]
                container[j] = a
                change = True
        if not change:
            break
    return container
