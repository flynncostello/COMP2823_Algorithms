from Node import Node
from typing import Generic, TypeVar

T = TypeVar('T')

"""
Doubly Linked List
----------

This class will represent your Doubly Linked List and will contain Nodes from the Node class which you have created.
It supports operations to get first and last element, get elements before and after a particular node, insert
nodes, remove a node, return the size of the doubly linked list and also check if list is empty.
"""


class DoublyLinkedList(Generic[T]):
    _size: int
    _front: Node[T]
    _back: Node[T]

    """
    DoublyLinkedList Class
    Holds nodes, where each node in the DoublyLinkedList has a next Node and a prev Node.
    If the node is the start node, prev should be None and vice versa for the end node.

    Each node in the tree is type <class Node>[T] defined in 'node.py'.
    """

    def __init__(self, front: Node[T] = None) -> None:
        """
        The initialisation of the DoublyLinkedList sets the first node of the structure 
        :param front: The first node of the doubly linked list.
        """
        self._size = 1 if front else 0
        self._front = front
        self._back = front

    def first(self) -> Node[T]:
        """
        Returns the first node in the doubly linked list
        :return: The node at the front of the list.
        """

        return self._front

    def last(self) -> Node[T]:
        """
        Returns the last node in the doubly linked list
        :return: The node at the back of the list.
        """

        return self._back

    def before(self, p: Node[T]) -> Node[T]:
        """
        Returns the node immediately before node p and returns None if there are no nodes prior.
        :param p: The node whose previous node we are after.
        :return: The node immediately prior to p or None if there are no nodes after.
        """

        return p.get_prev() if p else None

    def after(self, p: Node[T]) -> Node[T]:
        """
        Returns the node immediately after node p and returns None if there are no nodes after.
        :param p: The node to get the next node after.
        :return: The node immediately after p or None if there are no nodes after.
        """

        return p.get_next() if p else None

    def insert_before(self, p: Node[T], e: Node[T]) -> None:
        """
        Inserts the node e immediately before the node p.
        If the list is empty and p is None, insert e at the front of the list.
        Otherwise, if the list is not empty and p is None, return None.
        :param p: The node we want to insert e before.
        :param e: The node to insert.
        """

        if(not e):
            return
        elif(not p and self._size):
            return
        elif(not p):
            self._front = e
            self._back = e
            self._size = 1
            return

        e.set_next(p)
        e.set_prev(p.get_prev())
        if(p.get_prev()):
            p.get_prev().set_next(e)
        p.set_prev(e)

        if p == self.first():
            self._front = e

        self._size += 1

    def insert_after(self, p: Node[T], e: Node[T]) -> None:
        """
        Inserts the node e immediately after the node p.
        If the list is empty and p is None, insert e at the front of the list.
        Otherwise, if the list is not empty and p is None, return None.
        :param p: The node we want to insert e after.
        :param e: The node to insert.
        """

        if(not e):
            return
        elif(not p and self._size):
            return
        elif(not p):
            self._front = e
            self._back = e
            self._size = 1
            return

        e.set_next(p.get_next())
        e.set_prev(p)
        if(p.get_next()):
            p.get_next().set_prev(e)
        p.set_next(e)

        if p == self.last():
            self._back = e

        self._size += 1

    def remove(self, p: Node[T]) -> Node[T]:
        """
        Removes the node p from the doubly linked list and returns it.
        If p is not valid, return None.
        :param p: The position of the node remove.
        :return: The node that was removed.
        """
        if(not p):
            return None

        if(p == self._front and p == self._back):
            self._front = None
            self._back = None
            self._size = 0
        elif(p == self._front):
            self._front = p.get_next()
            self._front.set_prev(None)
            self._size -= 1
        elif(p == self._back):
            self._back = p.get_prev()
            self._back.set_next(None)
            self._size -= 1
        else:
            p.get_prev().set_next(p.get_next())
            p.get_next().set_prev(p.get_prev())
            self._size -= 1

        return p

    def size(self) -> int:
        """
        Returns the size of the singly linked list
        :return: The size of the list.
        "D

        return self._size

    def is_empty(self) -> bool:
        """
        Returns if the singly linked list is empty of not.
        :return: True if the list is empty, false otherwise.
        """

        return not self._size