class iterators():
    def __init__(self, start, end):
        self.current = start
        self.end = end

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.current < self.end:
            current_value = self.current
            self.current += 1
            return current_value
        else:
            raise StopIteration
        
for num in iterators(1, 5):
    print(num)