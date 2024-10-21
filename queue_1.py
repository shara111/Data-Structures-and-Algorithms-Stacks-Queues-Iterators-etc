class Queue:
    def __init__(self):
        self.queue = []
    def enqueue(self, value):
        return self.queue.append(value)
    def dequeue(self):
        return self.queue.pop(0)
    def front(self):
        return self.queue[0]
    def isEmpty(self):
        return len(self.queue) == 0