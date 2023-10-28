#!/usr/bin/python3
"""Define classed for a singly_linked list"""


class Node:
    """Represents a Node in a singly_linked list"""

    def __init__(self, data, next_node=None):
        """Initializes the new Node.

        Args:
            data (int): The data of the new Node.
            next_node (Node): The nwxt Node of the new Node
        """

        self.data = data
        self.next_node = next_node

        @property
        def data(self):
            """Get and set the data of thw Node"""
            return (self.__data)

        @data.setter
        def data(self, value):
            if not isinstance(value, int):
                raise TypeError("data must be an integer")
            self.__data = value

        @property
        def next_node(self):
            """Get/set the next node of the Node"""
            return (self.__next_node)

        @next_node.setter
        def next_node(self, value):
            if not isinstance(value, Node) and value is not None:
                raise TypeError("next_node must be a Node Object")
            self.__next_node = value

            
