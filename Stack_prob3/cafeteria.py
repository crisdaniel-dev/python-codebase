from stack import Stack

class CafeteriaTraySystem:
    
    def __init__(self):
        self.tray_stack = Stack()
        
    def return_tray(self, tray_id):
        self.tray_stack.push(tray_id)
    
    def wash_tray(self):
        if self.tray_stack.is_empty():
            print("No trays to wash.")
            return
        top = self.tray_stack.pop()
        print("Washed tray:",top)
        
    def peek_tray(self):
        if self.tray_stack.is_empty():
            print("No trays are waiting.")
            return
        print("Top tray:",self.tray_stack.peek())
        
    def display_trays(self):
        if self.tray_stack.is_empty():
            print("No tray available.")
            return
        current = self.tray_stack._Stack__top
        while current:
            print(current.data)
            current = current.next
            
    def is_empty(self):
        if self.tray_stack.is_empty():
            return True
        else:
            return False