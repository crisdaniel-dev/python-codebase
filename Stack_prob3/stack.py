from node import Node

class Stack:
    
    def __init__(self):
        self.__top = None
        
    def push(self, data):
        node = Node(data)
        node.next = self.__top
        self.__top = node
        
    def pop(self):
        assert self.__top, "Stack is empty"
        top = self.__top.data
        self.__top = self.__top.next
        return top
        
    def peek(self):
        assert self.__top, "Stack is empty"
        return self.__top.data
    
    def is_empty(self):
        if self.__top:
            return False
        else:
            return True
        
    def clear(self):
        self.__top = None