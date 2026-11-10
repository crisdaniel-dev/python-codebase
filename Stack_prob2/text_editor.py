from stack import Stack

class TextEditor:

    def __init__(self):
        self.undo_stack = Stack()
        self.current_text = ""

    def type_text(self, text):
        self.undo_stack.push(self.current_text)
        self.current_text += text

    def delete_last_character(self):
        if not self.current_text:
            print("No text to delete.")
            return

        self.undo_stack.push(self.current_text)
        self.current_text = self.current_text[:-1]

    def undo(self):
        if self.undo_stack.is_empty():
            print("Nothing to undo.")
            return

        self.current_text = self.undo_stack.pop()

    def show_text(self):
        if not self.current_text:
            print("Editor is empty.")
            return

        print("Current Text:", self.current_text)