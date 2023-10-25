"""
Author: Abid Jeem
Filename: arraybag.py
This is an array-based implementation of a bag data structure.  
The purpose of the code is to demonstrate the functionality of this arrayBag, showcasing how it adds and retrieves objects 
in the order they were added.
"""

from arrays import Array
from abstractBag import AbstractBag

class ArrayBag(AbstractBag):
    """An array-based bag implementation."""

    # Class variable
    DEFAULT_CAPACITY = 10

    # Constructor
    def __init__(self, sourceCollection = None):
        """Sets the initial state of self, which includes the
        contents of sourceCollection, if it's present."""
        self._items = Array(ArrayBag.DEFAULT_CAPACITY)
        super().__init__(sourceCollection)

    # Accessor methods

    def __iter__(self):
        """Supports iteration over a view of self."""
        cursor = 0
        while cursor < len(self):
            yield self._items[cursor]
            cursor += 1

    
    def resize (self, sizeFactor):
        if len(self._items) *sizeFactor >= ArrayBag.DEFAULT_CAPACITY:
            temp= Array(round(len(self._items)*sizeFactor))
            for i in range(len(self)):
                temp[i] = self._items[i]
            self._items= temp
    
    # Mutator methods
    def clear(self):
        """Makes self become empty."""
        self._size = 0
        self._items = Array(ArrayBag.DEFAULT_CAPACITY)
            
    def add(self, item):
        """Adds item to self."""
        # Check array memory here and increase it if necessary
        #len(self._items) gives you physical size
        #len(self) gives you the logical size
        
        if len(self._items)== len(self):
            self.resize(2)
        self._items[len(self)] = item
        self._size += 1

    def remove(self, item):
        """Precondition: item is in self.
        Raises: KeyError if item in not in self.
        Postcondition: item is removed from self."""
        # Check precondition and raise exception if necessary
        if not item in self:
            raise KeyError(str(item) + " not in bag")
        # Search for the index of the target item
        targetIndex = 0
        for targetItem in self:
            if targetItem == item:
                break
            targetIndex += 1
        # Shift items to the left of target up by one position
        for i in range(targetIndex, len(self) - 1):
            self._items[i] = self._items[i + 1]
        # Decrement logical size
        self._size -= 1
        # Check array memory here and decrease it if necessary
        if len(self._items) >= 4*(len(self)):
            self.resize(0.5)
        
