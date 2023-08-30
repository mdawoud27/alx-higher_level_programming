#!/usr/bin/python3

"""This class defines a node of a single linked list."""


class Node:
    def __init__(self, data, next_node=None):
        """Instantiation with data and next_node.

        Args:
            data (int): node data.
            next_node (Node): new node.
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Return the data of the current node."""
        return self.__data

    @data.setter
    def data(self, value):
        """Set the node data.

        Args:
            value (int): node data.
        """
        if not isinstance(value, int):
            raise TypeError('data must be an integer')
        self.__data = value

    @property
    def next_node(self):
        """Return next node."""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """Set the next node.

        Args:
            value (Node or None): Next node or None.
        """
        if not isinstance(value, (Node, type(None))):
            raise TypeError('next_node must be a Node object')
        self.__next_node = value


class SinglyLinkedList:
    def __init__(self):
        """Initialize an empty linked list."""
        self.__head = None

    def sorted_insert(self, value):
        """Insert a node in its correct position.

        Args:
            value (int): node data to be inserted.
        """
        new = Node(value)

        if not self.__head or value < self.__head.data:
            new.next_node = self.__head
            self.__head = new
            return

        ptr = self.__head
        while ptr.next_node and ptr.next_node.data < value:
            ptr = ptr.next_node

        new.next_node = ptr.next_node
        ptr.next_node = new

    def __str__(self):
        """Return the string representation."""
        node_str = ""
        ptr = self.__head

        while ptr:
            node_str += str(ptr.data)
            if ptr.next_node:
                node_str += '\n'
            ptr = ptr.next_node

        return node_str
