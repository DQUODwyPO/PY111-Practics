from typing import Optional, List


def _prefix_fun(prefix_str: str) -> List[int]:
    """
    Prefix function for KMP

    :param prefix_str: dubstring for prefix function
    :return: prefix values table
    """
    size = len(prefix_str)
    table = [0] * size
    cnt = 0
    for i in range(1, size):
        if prefix_str[cnt] == prefix_str[i]:
            cnt += 1
            table[i] = cnt
        else:
            cnt = 0
            if prefix_str[cnt] == prefix_str[i]:
                cnt += 1
                table[i] = cnt
    return table


def kmp_algo(inp_string: str, substr: str) -> Optional[int]:
    """
    Implementation of Knuth-Morrison-Pratt algorithm

    :param inp_string: String where substr is to be found (haystack)
    :param substr: substr to be found in inp_string (needle)
    :return: index where first occurrence of substr in inp_string started or None if not found
    """
    k = 0
    A = []
    p = _prefix_fun(substr + inp_string)
    for i in range(len(inp_string)):
        while k > 0 and inp_string[i] != substr[k]:
            k = p[k]
        if inp_string[i] == substr[k]:
            k = k + 1
        if k == len(substr):
            A = A + [i - len(substr) + 1]
            A = A + [i]
            k = p[k]

    if A != []:
        return A[0]
    else:
        return None

