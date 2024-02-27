"""
Singly Linked List Node
----------

This node represents an item in a doubly linked list. 
Each node contains a value and a link to the next node as well as to the previous node. 
It supports operations to set and get its element as well as 
operations to set and get the elements it is linked to.
"""

from typing import Generic, TypeVar

T = TypeVar('T')


class Node(Generic[T]):
    _value: T
    _next: 'Node[T]'
    _prev: 'Node[T]'

    """
    Node Class
    - Init: Sets the basic information such as the value it holds and linked elements.
    - Getters: Returns the value held by the node and the elements it is linked to.
    - Setters: Sets the value held by the node and the elements it is linked to.
    """

    def __init__(self, value: T, next: 'Node[T]' = None, prev: 'Node[T]' = None) -> None:
        """
        The initialisation of the node sets the value held by the node
        as well as the elements it is linked to.
        :param value: The value of the node.
        :param next: The next element after the node.
        :param prev: The previous element connected to the node.
        """
        self._value = value
        self._next = next
        self._prev = prev

    def get_value(self) -> T:
        """
        Getter method for the value of the node
        :return: The value of the node.
        """

        # TODO implement me.
        return self._value

    def set_value(self, value: T) -> None:
        """
        Setter method for the value of the node
        :param value: The value to set the node to.
        """

        # TODO implement me.
        self._value = value

    def get_next(self) -> 'Node[T]':
        """
        Returns the next node linked to the current node.
        :return: Node which follows this given node.
        """

        # TODO implement me.
        return self._next

    def set_next(self, next: 'Node[T]') -> None:
        """
        Sets the next node linked to the current node.
        :param next: The node that comes after the current one.
        """

        # TODO implement me.
        self._next = next

    def get_prev(self) -> 'Node[T]':
        """
        Returns the previous node linked to the current node.
        :return: Node which comes before this given node.
        """

        # TODO implement me.
        return self._prev

    def set_prev(self, prev: 'Node[T]') -> None:
        """
        Sets the previous node linked to the current node.
        :param prev: The node that comes before the current one.
        """

        # TODO implement me.
        self._prev = prev


