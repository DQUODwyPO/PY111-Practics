import timeit
from typing import Union, Sequence


def stairway_path_rec(cost: Sequence[Union[float, int]], i: int, fin: int):
    cost[i] += min(cost[i - 1], cost[i - 2])
    if i == fin:
        return cost[i]
    else:
        return stairway_path_rec(cost, i + 1, fin)


def stairway_path(stairway: Sequence[Union[float, int]]) -> Union[float, int]:
    """
    Calculate min cost of getting to the top of stairway if agent can go on next or through one step.

    :param stairway: list of ints, where each int is a cost of appropriate step
    :return: minimal cost of getting to the top
    """
    size = len(stairway)
    return stairway_path_rec(stairway, 2, size - 1)


def stairway_path2(stairway: Sequence[Union[float, int]]) -> Union[float, int]:
    """
    Calculate min cost of getting to the top of stairway if agent can go on next or through one step.

    :param stairway: list of ints, where each int is a cost of appropriate step
    :return: minimal cost of getting to the top
    """
    size = len(stairway)
    cost = stairway[:]
    for i in range(2, size):
        cost[i] += min(cost[i-1], cost[i-2])
    return cost[-1]
