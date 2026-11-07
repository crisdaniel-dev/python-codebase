from node import Node

class Stack:
    
    def __init__(self):
        self.__top = None
        
    def push(self, data):
        node = Node(data)
        node.next = self.__top
        self.__top = node
        