import unittest
from queue_1 import Queue

class TestQueue(unittest.TestCase):
    
    def setUp(self):
        # Initialize a queue for testing
        self.queue = Queue()

    def test_initialize(self):
        # Test if a new queue is empty
        self.assertTrue(self.queue.isEmpty(), "New queue should be empty")

    def test_enqueue(self):
        # Enqueue an item and check if the queue is no longer empty
        self.queue.enqueue(1)
        self.assertFalse(self.queue.isEmpty(), "Queue should not be empty after enqueueing an item")
        
        # Check if the front item is the same as the enqueued item
        self.assertEqual(self.queue.front(), 1, "Front item should be 1 after enqueueing 1")

    def test_dequeue(self):
        # Enqueue items and then dequeue one
        self.queue.enqueue(2)
        self.queue.enqueue(3)
        
        dequeued_item = self.queue.dequeue()
        
        # Ensure the dequeued item is the one that was enqueued first
        self.assertEqual(dequeued_item, 2, "Dequeued item should be 2")
        
        # Check if the front item is now the next in line (3)
        self.assertEqual(self.queue.front(), 3, "Front should be 3 after dequeuing 2")

    def test_front(self):
        # Enqueue multiple items and check if front returns the first enqueued item
        self.queue.enqueue(4)
        self.queue.enqueue(5)
        
        # Front should return the first enqueued item (4)
        self.assertEqual(self.queue.front(), 4, "Front should return 4")
        
        # After dequeuing, the front should update to the next item
        self.queue.dequeue()
        self.assertEqual(self.queue.front(), 5, "Front should return 5 after dequeuing 4")

    def test_isEmpty(self):
        # Initially, the queue should be empty
        self.assertTrue(self.queue.isEmpty(), "Queue should be empty initially")
        
        # Enqueue an item and check if the queue is no longer empty
        self.queue.enqueue(6)
        self.assertFalse(self.queue.isEmpty(), "Queue should not be empty after enqueueing an item")
        
        # Dequeue the item and check if the queue is empty again
        self.queue.dequeue()
        self.assertTrue(self.queue.isEmpty(), "Queue should be empty after dequeuing the last item")

if __name__ == '__main__':
    unittest.main()
