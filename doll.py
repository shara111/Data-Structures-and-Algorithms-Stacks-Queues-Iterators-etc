class DoublyLinkedList():
    class Node:
        def __init__(self, data, next=None, prev=None):
            self.data = data
            self.next = next
            self.prev = prev

        def _init_(self):
            self.front = self.Node(None)
            self.back = self.Node(None)

            self.front.next = self.back
            self.back.prev = self.front

        def insert(self, data):
            new_node = self.Node(data)

            if self.front.next == self.back:
                self.front.next = new_node
                self.back.prev = new_node

                new_node.prev = self.front
                new_node.next = self.back
            else:
                curr = self.front.next

                while curr != self.back and curr.data < data:
                    curr = curr.next

                #insert our value
                new_node.next = curr
                new_node.prev = curr.prev

                curr.prev.next = new_node
                curr.prev = new_node
        
        