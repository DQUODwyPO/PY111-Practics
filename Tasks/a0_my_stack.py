"""
My little Stack
"""
from typing import Any


class Stack:
    def __init__(self):
        self.__data = list()  # todo для стека можно использовать python list

    def push(self, elem: Any) -> None:
        """
        Operation that add element to stack

        :param elem: element to be pushed
        :return: Nothing
        """
        self.__data.append(elem)
        print(elem)
        return None

    def pop(self) -> Any:
        """
        Pop element from the top of the stack. If not elements - should return None.

        :return: popped element
        """
        try:
            return self.__data.pop()
        except IndexError:
            return None

    def peek(self, ind: int = 0) -> Any:
        """
        Allow you to see at the element in the stack without popping it.

        :param ind: index of element (count from the top, 0 - top, 1 - first from top, etc.)
        :return: peeked element or None if no element in this place
        """
        print(ind)
        try:
            return self.__data[-ind - 1]
        except IndexError:
            return None

    def clear(self) -> None:
        """
        Clear my stack

        :return: None
        """
        self.__data.clear()
        return None
