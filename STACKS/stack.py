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
    
    def is_empty(self):
        if self.__top:
            return False
        else:
            return True
        
    def is_palindrome(self, word):
        if not isinstance(word, str):
            raise ValueError("Word must be a string")
        
        if not word.strip():
            raise ValueError("Word cannot be empty")
        
        s = Stack()
        word = word.upper()
        count = 0
  
        for ch in word:
            s.push(ch)
            count += 1
            
        if count < 3:
            return None
            
        for ch in word:
            if ch != s.pop():
                return False
            
        return True
    
    def display(self):
        assert self.__top, "Stack is empty"
        current = self.__top
        output = ""
        while current:
            output += str(current.data) + " "
            current = current.next
        return output.strip()