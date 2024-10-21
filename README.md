
1. Stacks 
A stack is a linear data structure that follows the Last In, First Out (LIFO) principle. This means the last element added to the stack is the first one to be removed. A stack is analogous to a stack of plates: you can only add (push) or remove (pop) a plate from the top.

Common operations:

push(item): Adds an item to the top of the stack.
pop(): Removes and returns the item at the top of the stack.
peek(): Returns the item at the top without removing it.
isEmpty(): Checks if the stack is empty.
Time complexity:

Push: O(1)
Pop: O(1)
Peek: O(1)
Space complexity: O(n) where n is the number of elements in the stack.
Example of stack implementation in Python using a list:

python
Copy code
class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if not self.is_empty():
            return self.stack.pop()

    def peek(self):
        if not self.is_empty():
            return self.stack[-1]

    def is_empty(self):
        return len(self.stack) == 0
2. Queues
A queue is a linear data structure that follows the First In, First Out (FIFO) principle. This means the first element added to the queue will be the first one to be removed.

Common operations:

enqueue(item): Adds an item to the rear of the queue.
dequeue(): Removes and returns the item at the front.
peek(): Returns the item at the front without removing it.
isEmpty(): Checks if the queue is empty.
Time complexity:

Enqueue: O(1)
Dequeue: O(1)
Peek: O(1)
Space complexity: O(n) where n is the number of elements in the queue.
Example of queue implementation in Python using collections.deque:

python
Copy code
from collections import deque

class Queue:
    def __init__(self):
        self.queue = deque()

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.queue.popleft()

    def peek(self):
        if not self.is_empty():
            return self.queue[0]

    def is_empty(self):
        return len(self.queue) == 0
3. Iterators
An iterator in Python is an object that allows you to iterate over a sequence (like lists, tuples, etc.). It implements two methods: __iter__() and __next__().

iter(): This returns the iterator object itself.
next(): This returns the next value from the iterator. If no more elements are available, it raises the StopIteration exception.
Time complexity: Accessing the next element using __next__() is O(1).

Example of an iterator class:

python
Copy code
class MyRange:
    def __init__(self, start, end):
        self.current = start
        self.end = end

    def __iter__(self):
        return self

    def __next__(self):
        if self.current < self.end:
            current = self.current
            self.current += 1
            return current
        else:
            raise StopIteration
4. Constructors
A constructor in Python is a special method called __init__(). It is automatically invoked when an object of the class is created. It is used to initialize the object's attributes.

Example of a constructor in a Python class:

python
Copy code
class MyClass:
    def __init__(self, value):
        self.value = value  # Constructor initializing the attribute 'value'

    def get_value(self):
        return self.value
In this example, when an instance of MyClass is created, the __init__() method will be called to initialize the value attribute.

Time Complexity and Space Complexity
Time Complexity:
This is a measure of the time an algorithm takes to run as a function of the size of its input.

O(1): Constant time — the operation does not depend on the input size (e.g., accessing an element from a stack).
O(n): Linear time — the operation time increases linearly with the size of the input (e.g., traversing a list).
O(log n): Logarithmic time — the operation time increases logarithmically (e.g., binary search).
O(n²): Quadratic time — the operation time grows proportionally to the square of the input size (e.g., bubble sort).
Space Complexity:
This measures the amount of memory an algorithm uses relative to its input size.

O(1): Constant space — the space used does not depend on the input size.
O(n): Linear space — the space used grows linearly with the input size.
