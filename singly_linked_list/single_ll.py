from Node import Node
from typing import Generic, TypeVar

T = TypeVar('T')
"""
Singly Linked List
----------

Each node contains a value and a link to the next node. It supports operations to set and get its element as well as operations to set and get the element it is linked to.

The Singly Linked List will contain Nodes from the Node class which you have created. It supports operations to get the first and last element, check before and after a particular node, insert an element before or after a particular node, remove a node, check size of list and also check if the list is empty.

Note: Although creating a doubly linked list data structure will fulfil the requirements for this task, it is best to try and create a singly linked list data structure for your learning purposes.
"""


class Single_ll(Generic[T]):

    _size: int
    _front: Node[T]
    _back: Node[T]
    """
    Single_ll Class
    Holds nodes, where each node in the Single_ll has a next Node, unless it is the end node
    where the next Node is None.
    
    
    """


    def __init__(self, first_node: Node[T]) -> None:
        """
        The initialisation of the List with the first and back being the Node being the Node in the argument.
        Size is the number of nodes in the list.
        :param size: The number of nodes in the list
        :param front: First Node of the Linked List
        :param back: Last Node of the Linked List
        """
        self._size = 1
        self._front = first_node
        self._back  = first_node

    def first(self) -> Node[T]:
        """
        Returns the first node in the singly linked list
        :return: The node at the front of the list
        """

        # TODO implement me.
        return self._front

    def last(self) -> Node[T]:
        """
        Returns the last node in the singly linked list
        :return: The node at the back of the list
        """
        
        # TODO implement me.
        return self._back
    
    def after(self, p: Node[T]) -> Node[T]:
        """
        Returns the node immediately after node p.
        If p is None return None.
        :return: The node after p
        """

        # TODO implement me.
        if p is None:
            return None
        return p._next

    def insert_after(self, p: Node[T], e: Node[T]) -> None:
        """
        Inserts the node e immediately after node p. If p is None then add e at the first position of 
        the list. 
        :param p: Node object which Node e is to be inserted after If None then add e to first pos
        :param e: Node object to be inserted
        """

        # TODO implement me.
        if p is None: # Adding e to front of linked list
            if self._size == 0:
                self._back = e
            self._size += 1
            e.set_next(self.first()) 
            self._front = e
        else: # Adding e immediately after p in linked list
            e.set_next(p.get_next())
            p.set_next(e)
            self._size += 1
            # If p was at the end now e will be
            if self.last() == p:
                self._back = e


    def remove(self, p: Node[T]) -> Node[T]:
        """
        Removes node p from list and joins the node previous from p to the node next to p. If p is 
        first node then just remove p and change first accordingly.
        If p is None return None. 
        :param p: Node object that is to be removed
        :return: The node that was removed
        """

        # TODO implement me.
        if p == None:
            return None
        cur_node = self._front
        if cur_node == p:
            if self._front == self._back:
                self._front = None
                self._back = None
            else:
                self._front = p.get_next()
            
        else:
            while cur_node.get_next() != p:
                cur_node = cur_node.get_next()
            if p == self._back:
                self._back = cur_node
            cur_node.next = p.get_next()
        self._size -= 1
        return p

            
    
    def size(self) -> int:
        """
        Returns the size of the singly linked list
        :return: size of the list
        """

        # TODO implement me.
        return self._size

    def is_empty(self) -> bool:
        """
        Returns if the singly linked list is empty of not.
        :return: True or False depending if list is empty or not.
        """

        # TODO implement me.
        return self._front is None
   

