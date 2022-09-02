"""
Priority Queue

Queue priorities are from 0 to 10
"""
from typing import Any


class PriorityQueue:
    def __init__(self):
        self.__data = list()  # todo для очереди можно использовать python dict

    def enqueue(self, elem: Any, priority: int = 0) -> None:
        """
        Operation that add element to the end of the queue

        :param elem: element to be added
        :return: Nothing
        """
        if len(self.__data) == 0:
            self.__data.append((priority, elem))
        else:
            idx = 0
            size = len(self.__data)
            while priority >= self.__data[idx][0]:
                idx += 1
                if idx == size:
                    break
            self.__data.insert(idx, (priority, elem))
        return None

    def dequeue(self) -> Any:
        """
        Return element from the beginning of the queue. Should return None if not elements.

        :return: dequeued element
        """
        try:
            answ = self.__data[0]
            self.__data.remove(answ)
            return answ[1]
        except IndexError:
            return None

    def peek(self, ind: int = 0, priority: int = 0) -> Any:
        """
        Allow you to see at the element in the queue without dequeuing it

        :param ind: index of element (count from the beginning)
        :return: peeked element
        """
        try:
            return self.__data[ind][1]
        except IndexError:
            return None

    def clear(self) -> None:
        """
        Clear my queue

        :return: None
        """
        self.__data.clear()
        return None
