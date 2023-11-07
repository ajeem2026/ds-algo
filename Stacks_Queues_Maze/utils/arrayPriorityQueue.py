"""
File: arrayPriorityQueue.py
Author: Abid Jeem

In collaboration with Rihards and TAs
"""

from .node import Node
from .arrayQueue import ArrayQueue

class ArrayPriorityQueue(ArrayQueue):
    """A link-based priority queue implementation."""


    def __init__(self, sourceCollection = None):
        """Sets the initial state of self, which includes the
        contents of sourceCollection, if it's present."""
        super().__init__(sourceCollection)


    def add(self, item):
        """Adds item to its proper place in the queue."""
       
    # Resize array if full
        if  len(self._items) == self._size:
            self.resize(2)

        # If it's empty or we have the worst priority in the queue, add to the end
        if self.isEmpty() or item >= self._items[self._rear]:
            super().add(item)
            return
        # Otherwise, find the correct position and insert.
        else:  
            cursor = self._front
            # Search for first item >= new item
            while item >= self._items[cursor]:
                cursor += 1
                cursor %= len(self._items)
            # Open a hole for new item
            for i in range(self._rear, cursor - 1, -1):
                nextIndex = (i + 1) % len(self._items)
                self._items[nextIndex] = self._items[i]
            # Insert item and update size
            self._items[cursor] = item
            self._rear = (self._rear + 1) % len(self._items)
            self._size += 1
            
