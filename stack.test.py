# Stack unit tests
import unittest
from stack import Stack

class TestStack(unittest.TestCase):
    def setUp(self):
        # Initialize a stack with a max size of 5 for testing isFull
        self.stack = Stack()
    
    def test_initialize(self):
        # Test if a new stack is empty
        self.assertTrue(self.stack.isEmpty(), "New stack should be empty")
    
    def test_push(self):
        # Push an item onto the stack and check if it is no longer empty
        self.stack.push(1)
        self.assertFalse(self.stack.isEmpty(), "Stack should not be empty after pushing an item")
        
        # Check if the top item is the same as the pushed item
        self.assertEqual(self.stack.top(), 1, "Top item should be 1 after pushing 1")
    
    def test_pop(self):
        # Push an item and then pop it
        self.stack.push(2)
        popped_item = self.stack.pop()
        
        # Ensure the popped item is the one that was pushed
        self.assertEqual(popped_item, 2, "Popped item should be 2")
        
        # Check if the stack is empty after the pop
        self.assertTrue(self.stack.isEmpty(), "Stack should be empty after popping the only item")
    
    def test_top(self):
        # Push multiple items and check if top returns the last pushed item without removing it
        self.stack.push(3)
        self.stack.push(4)
        
        # Top should return the last pushed item (4)
        self.assertEqual(self.stack.top(), 4, "Top should return 4")
        
        # The stack should still contain 4 after calling top
        self.assertFalse(self.stack.isEmpty(), "Stack should not be empty after calling top")
    
    def test_isEmpty(self):
        # Initially, the stack should be empty
        self.assertTrue(self.stack.isEmpty(), "Stack should be empty initially")
        
        # Push an item and check if the stack is no longer empty
        self.stack.push(5)
        self.assertFalse(self.stack.isEmpty(), "Stack should not be empty after pushing an item")
        
        # Pop the item and check if the stack is empty again
        self.stack.pop()
        self.assertTrue(self.stack.isEmpty(), "Stack should be empty after popping the last item")
    
    def test_push_pop_order(self):
        # Test if stack follows Last In First Out (LIFO) order
        self.stack.push(1)
        self.stack.push(2)
        self.stack.push(3)
        
        # The first pop should return 3, then 2, then 1
        self.assertEqual(self.stack.pop(), 3, "Pop should return 3")
        self.assertEqual(self.stack.pop(), 2, "Pop should return 2")
        self.assertEqual(self.stack.pop(), 1, "Pop should return 1")

if __name__ == '__main__':
    unittest.main()