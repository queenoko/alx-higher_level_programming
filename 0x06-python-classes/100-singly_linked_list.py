#!/usr/bin/python3
# 100-singly_linked_list.py
"""Module for singly linked list"""


class Node:
    """Defines Node"""

    def __init__(self, data, next_node=None):
        """Initialize Node with instance variable"""

        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Gets the data attribute"""

        return (self.__data)

    @data.setter
    def data(self, value):
        """Sets the data attribute:"""

        if not isinstance(value, int):
            raise TypeError('data must be an integer')
        self.__data = value

    @property
    def next_node(self, value):
        """sets the value for the next node"""

        if (value is not None and not isinstance(value, None)):
            raise TypeError('next_node must be a Node object')

        self.__next_node = value


class SinglyLinkedList:
    """defines singly linked list"""

    def __init__(self):
        """initialize singly linked list"""

        self.head = None

    def __str__(self):
        """make printable list"""

        printsll1 = ""
        location = self.head
        while location:
            printsll1 += str(location.data) + "\n"
            location = location.next_node
        return printsll1[:-1]

    def sorted_insert(self, value):
        """insert in a sorted fasion
        Arg:
        value: what is the value that would be on the node
        """
        new = Node(value)
        if not self.head:
            self.head = new
            return
        if value < self.head.data:
            new.next_node = self.head
            self.head = new
            return
        location = self.head
        while location.next_node and location.next_node.data < value:
            location = location.next_node
        if location.next_node:
            new.next_node = location.next_node
        location.next_node = new
