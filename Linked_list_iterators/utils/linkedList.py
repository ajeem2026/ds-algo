"""
File: linkedList.py
Author: Abid Jeem

In collaboration with TAs and half of our class (Michael, Teddy, Sarp, Jonathan, Rihards, and Elizabeth)
"""

from node import TwoWayNode
from abstractList import AbstractList

class LinkedList(AbstractList):
    """A link-based list implementation."""

    def __init__(self, sourceCollection = None):
        """Sets the initial state of self, which includes the
        contents of sourceCollection, if it's present."""
        # Uses a circular linked structure with a dummy header node
        self._head = TwoWayNode()
        self._head.previous = self._head.next = self._head
        super().__init__(sourceCollection)

    # Helper method returns node at position i
    def _getNode(self, i):
        """Helper method: returns a pointer to the node at position i."""
        if i == (len(self) - 1):
            return self._head.previous
        
        probe = self._head.next
        while i > 0:
            probe = probe.next
            i -= 1
        return probe

    #Accessor methods
    def __iter__(self):
        """Supports iteration over a view of self."""
        cursor = self._head.next
        modCount = self.getModCount()
        while cursor != self._head:
            yield cursor.data
            if modCount != self.getModCount():
                raise AttributeError("Mutations not allowed in a for loop")
            cursor = cursor.next

    def __getitem__(self, i):
        """Precondition: 0 <= i < len(self)
        Returns the item at position i.
        Raises: IndexError."""
        if i < 0 or i >= len(self):
            raise IndexError("List index out of range")
        return self._getNode(i).data

    # Mutator methods
    def clear(self):
        self._head.previous = self._head.next = self._head
        self.resetSizeAndModCount()
    
    def __setitem__(self, i, item):
        if i < 0 or i >= len(self):
            raise IndexError("List index out of range")
        self._getNode(i).data = item
    
    def insert(self, i, item):
        if i < 0: i = 0
        elif i > len(self): i = len(self)
        
        probe = self._getNode(i)
        newNode = TwoWayNode(item, probe.previous, probe)
        probe.previous.next = newNode
        probe.previous = newNode
        
        self._size += 1
        self.incModCount()
        
    
    def pop(self, i = None):
        """
        Removes item from ith position and returns the Node's data;
        Calling pop() without an arguemnt will return in pos=None, in which case remove and return the item at end of list;
        
        Raise an IndexError if the list is empty, or if pos is NOT in range [0,len(list)-1]
        Raise a Typeerror if pos is NOT an integer 
        
        pop(0) must be O(1)
        
        :param post: the position (index) of the item to be popped
        :return: the data item in the node
        
        """
        
        #1) Check that pos parameter is valid
        if i == None: i = len(self) - 1
        if i < 0 or i >= len(self):
            raise IndexError("List index out of range")
        if not isinstance(i, int):
            raise TypeError("i is not an integer")
        
        #2) Searching step, get to where you need to pop (_getnode) does this for you
        #walk the list with curr and prev the pos number of items. 
        #Count the steps you take 
        probe= self._getNode(i)
        item= probe.data
        
        # #removing the head
        # if probe is self._head:
        #     probe.next = self._head
        
        # #removing the tail
        # if probe is self:
        #     probe.previous = self.tail
        
        # else:
        probe.previous.next= probe.next
        probe.next.previous=probe.previous
        self.incModCount()

        #3)remove and return the item
        return item
        
    def listIterator(self):
        return LinkedList.ListIterator(self)
        
        
        
    
    # Use _getNode wherever possible to support access to the ith node
    class ListIterator(object):
        """Represents a list iterator for LinkedList."""

        def __init__(self, backingStore):
            """Sets the initial state of the list iterator."""
            self._backingStore = backingStore
            self._modCount = backingStore.getModCount()
            self.first()

        def first(self):
            """Returns the cursor to the beginning of the backing store.
            lastItemPos is undefined."""
            self._cursor = self._backingStore._head.next
            self._lastItemPos = None

        def hasNext(self):
            """Returns True if the iterator has a next item or False otherwise."""
            return self._cursor.data != None
        def next(self):
            """Preconditions: hasNext returns True
            The list has not been modified except by this iterator's mutators.
            Returns the current item and advances the cursor to the next item.
            Postcondition: lastItemPos is now defined.
            Raises: ValueError if no next item.
            AttributeError if illegal modification of the backing store."""
            if not self.hasNext():
                raise ValueError("There is no next item")
            if self._modCount != self._backingStore.getModCount():
                raise AttributeError("Illegal modification of the backing store")
            self._lastItemPos = self._cursor
            self._cursor = self._cursor.next
            return self._lastItemPos.data

        def last(self):
            """Moves the cursor to the end of the backing store."""
            self._cursor = self._backingStore._head
            self._lastItemPos = None

        def hasPrevious(self):
            """Returns True if the iterator has a previous item or False otherwise."""
            return self._cursor.previous.data != None

        def previous(self):
            """Preconditions: hasPrevious returns True
            The list has not been modified except by this iterator's mutators.
            Returns the current item and moves the cursor to the previous item."""
            if not self.hasPrevious():
                raise ValueError("No previous item in list iterator")
            if self._modCount != self._backingStore.getModCount():
                raise AttributeError("Illegal modification of backing store")
            
            self._cursor = self._cursor.previous
            self._lastItemPos=self._cursor
            return self._cursor.data

        def replace(self, item):
            """Preconditions: the current position is defined.
            The list has not been modified except by this iterator's mutators.
            Replaces the items at the current position with item."""
            if self._lastItemPos is None:
                raise AttributeError("The current position is undefined.")
            if self._modCount != self._backingStore.getModCount():
                raise AttributeError("List has been modified illegally.")
            self._lastItemPos.data = item

        def insert(self, item):
            """Preconditions:
            The list has not been modified except by this iterator's mutators.
            Adds item to the end if the current position is undefined, or
            inserts it at that position."""
            if self._modCount != self._backingStore.getModCount():
                raise AttributeError("List has been modified illegally.")
            new_node = TwoWayNode(item, self._cursor.previous, self._cursor)
            self._cursor.previous.next = new_node
            self._cursor.previous = new_node
            self._backingStore.incModCount()
            self._modCount += 1

        def remove(self):
            """Preconditions: the current position is defined.
            The list has not been modified except by this iterator's mutators.
            Pops the item at the current position."""
            if self._lastItemPos is None:
                raise AttributeError("The current position is undefined.")
            if self._modCount != self._backingStore.getModCount():
                raise AttributeError("List has been modified illegally.")
            
            probe= self._lastItemPos
            probe.previous.next= probe.next
            probe.next.previous=probe.previous
            self._backingStore.incModCount()
            self._modCount+=1
           


