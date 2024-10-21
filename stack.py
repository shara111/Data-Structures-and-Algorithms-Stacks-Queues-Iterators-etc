class Stack:
    def __init__(self):
        self.stack = []
    
    def push(self, value):
       return self.stack.append(value)
    
    def pop(self):
        return self.stack.pop()
    
    def isEmpty(self):
        return len(self.stack) == 0
    
    def top(self):
       return self.stack[-1]