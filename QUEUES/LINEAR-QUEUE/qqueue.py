from node import Node

class Queue:
    
    def __init__(self):
        self.__front = self.__rear = None
        
    def enqueue(self, data):
        node = Node(data)
        if not self.__front:
            self.__front = self.__rear = node
        else:
            self.__rear.next = node
            self.__rear = node
            
    def dequeue(self):
        assert self.__front, "Queue is empty"
        front = self.__front.data
        self.__front = self.__front.next
        
        if not self.__front:
            self.__rear = None
        return front