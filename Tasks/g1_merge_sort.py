from typing import List


def merge_rec(con1: List[int], con2: List[int]) -> List[int]:
    size1 = len(con1)
    if size1 > 1:
        con1 = merge_rec(con1[:size1 // 2], con1[size1 // 2:])
    size2 = len(con2)
    if size2 > 1:
        con2 = merge_rec(con2[:size2 // 2], con2[size2 // 2:])
    i = 0
    j = 0
    cnt = 0
    con = list()
    while cnt < size1 + size2:
        if i != size1:
            if j != size2:
                if con1[i] <= con2[j]:
                    con.append(con1[i])
                    i += 1
                else:
                    con.append(con2[j])
                    j += 1
            else:
                con.append(con1[i])
                i += 1
        else:
            con.append(con2[j])
            j += 1
        cnt += 1
    return con


def merge(container: List[int]) -> List[int]:
    size = len(container)
    container = merge_rec(container[:size // 2], container[size // 2:])
    return container


def sort(container: List[int]) -> List[int]:
    """
    Sort input container with merge sort

    :param container: container of elements to be sorted
    :return: container sorted in ascending order
    """
    container = merge(container)
    return container
