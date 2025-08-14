# a stack is filo
# a stack initialized as empty
# we can add on top =add
# we can pop
class Stack:
    def __init__(self):
        self.stack = []
    def push(self, item):
        self.stack.append(item)
    def pop(self):
        return self.stack.pop()
    def peek(self):
        return self.stack[-1]

s = Stack()
s.push(1)
s.pop()
print(s.stack)



