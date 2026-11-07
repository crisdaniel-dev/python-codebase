from stack import Stack

s = Stack()
s.push(1)
print("Push: ", end="")
print(s.display())
s.push(2)
print("Push: ", end="")
print(s.display())
s.push(3)
print("Push: ", end="")
print(s.display())
s.pop()
print("Pop: ", end="")
print(s.display())
s.pop()
print("Pop: ", end="")
print(s.display())
s.pop()
print("Is the stack empty? ", end="")
print(s.is_empty())
word = "Level"
print(f"\nIs the word '{word}' a palindrome? ", end="")
print(s.is_palindrome(word))
parenthesis = "{[()]}"
print(f"Are these brackets '{parenthesis}' balanced? ",end="")
print(s.is_balanced(parenthesis))

