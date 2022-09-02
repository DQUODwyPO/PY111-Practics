"""
My little Queue
"""
from typing import Any


class Queue:
    def __init__(self):
        self.__data = list()  # todo для очереди можно использовать python list

    def enqueue(self, elem: Any) -> None:
        """
        Operation that add element to the end of the queue

        :param elem: element to be added
        :return: Nothing
        """
        self.__data.append(elem)
        return None

    def dequeue(self) -> Any:
        """
        Return element from the beginning of the queue. Should return None if no elements.

        :return: dequeued element
        """
        try:
            answ = self.__data[0]
            self.__data.remove(answ)
            return answ
        except IndexError:
            return None

    def peek(self, ind: int = 0) -> Any:
        """
        Allow you to see at the element in the queue without dequeuing it

        :param ind: index of element (count from the beginning)
        :return: peeked element
        """
        print(ind)
        try:
            return self.__data[ind]
        except IndexError:
            return None

    def clear(self) -> None:
        """
        Clear my queue

        :return: None
        """
        self.__data.clear()
        return None
