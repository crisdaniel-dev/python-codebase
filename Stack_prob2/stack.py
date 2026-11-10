from node import Node

class Stack:

    def __init__(self):
        self.__top = None

    def push(self, data):
        node = Node(data)
        node.next = self.__top
        self.__top = node

    def pop(self):
        if self.is_empty():
            return None

        top = self.__top.data
        self.__top = self.__top.next
        return top

    def peek(self):
        if self.is_empty():
            return None

        return self.__top.data

    def is_empty(self):
        return self.__top is None

    def clear(self):
        self.__top = None