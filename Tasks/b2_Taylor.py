"""
Taylor series
"""
from math import factorial
from typing import Union


def ex(x: Union[int, float]) -> float:
    """
    Calculate value of e^x with Taylor series

    :param x: x value
    :return: e^x value
    """
    ex_ = 1
    ix = x
    for i in range(1, 10):
        ex_ += ix / factorial(i)
        ix *= x
    return ex_


def sinx(x: Union[int, float]) -> float:
    """
    Calculate sin(x) with Taylor series

    :param x: x value
    :return: sin(x) value
    """
    sinx_ = 0
    ix = x
    for i in range(1, 10, 2):
        if i % 4 == 1:
            sinx_ += ix / factorial(i)
        else:
            sinx_ -= ix / factorial(i)
        ix *= x ** 2
    return sinx_
