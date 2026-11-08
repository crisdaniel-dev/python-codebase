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
    
    def peek(self):
        assert self.__front, "Queue is empty"
        return self.__front.data
    
    def is_empty(self):
        if self.__front:
            return False
        else:
            return True
        
    def get_size(self):
        if not self.__front:
            return 0
        count = 0
        current = self.__front
        while current:
            count += 1
            current = current.next
        return count
    
    def display(self):
        assert self.__front, "Queue is empty"
        current = self.__front
        output = ""
        while current:
            output += str(current.data) + " "
            current = current.next
        return output.strip()