from stack import Stack

class BrowserHistory:
    
    def __init__(self):
        self.back_stack = Stack()
        self.forward_stack = Stack()
        self.current_page = None
        
    def visit(self, page):
        if self.current_page is not None:
            self.back_stack.push(self.current_page)
            
        self.current_page = page
        self.forward_stack.clear()
        
    def back(self):
        if self.back_stack.is_empty():
            print("No previous page.")
            return
        self.forward_stack.push(self.current_page)
        self.current_page = self.back_stack.pop()
        
    def forward(self):
        if self.forward_stack.is_empty():
            print("No next page.")
            return
        self.back_stack.push(self.current_page)
        self.current_page = self.forward_stack.pop()
        
    def show_current_page(self):
        if self.current_page is None:
            print("No page is open.")
            return
        print("Current Page:",self.current_page)