"""
File: arrayQueue.py
Author: Abid Jeem

In collaboration with Rihards and TAs
"""

from .arrays import Array
from .abstractCollection import AbstractCollection

class ArrayQueue(AbstractCollection):
    """An array-based queue implementation."""

    # Simulates a circlular queue within an array

    # Class variable
    DEFAULT_CAPACITY = 10

    # Constructor
    def __init__(self, sourceCollection = None):
        """Sets the initial state of self, which includes the
        contents of sourceCollection, if it's present."""
        self._front=self._rear=-1
        self._items= Array(ArrayQueue.DEFAULT_CAPACITY)
        super().__init__(sourceCollection)
    # Scene:1 => F<=R: do stuff
    # Scene:2 => F> R: Two loops: First loop goes from Front to len(self._items), second loop goes from 0 to R
    # Scene:3 => F=R: We only have one element in the list, yield self.items[self.front]
    #Approach 2 (WRAP around or MODULO approach):
    #Start cursor at 0 and iterate cursor over length of logical size of Q (this is the number of times you want to yield into Q, NOT array)
    #while cursor <len(self): i yield[cursor+front]; but you will go out of range when it reaches the end [edge case] 
    # so we can wrap aournd yield[cursor+front]%len(self.items)
    # Accessor methods
    def __iter__(self):
        """Supports iteration over a view of self."""
        # Same as an iterator for an arrayBag, only using modulo inside self._items access
        #  to wrap the cursor around the end of the array
        if self._front == -1:
            return 
        # Same as an iterator for an arrayBag, only using modulo inside self._items access
        cursor=self._front 
        #to wrap the cursor around the end of the array
             #logical size: len(self)
             #physical size: len(self._items)
        while True:
            yield self._items[cursor]
            if cursor == self._rear:
                break
            #returning an iterable object each time the while is run
            cursor += 1
            cursor %= len(self._items)

    
    def peek(self):
        """Returns the item at the front of the queue.
        Precondition: the queue is not empty.
        Raises: KeyError if queue is empty."""
        
        if self.isEmpty():
            raise KeyError("Attempt to peek from empty queue")
        return self._items[self._front]

    # Mutator methods
    def clear(self):
        """Makes self become empty."""
        self.resetSizeAndModCount()
        self._items = Array(ArrayQueue.DEFAULT_CAPACITY)   
        

    def resize(self, sizeFactor):
        # Only shrink if we're not too small
        if len(self._items)*sizeFactor >= ArrayQueue.DEFAULT_CAPACITY:
            temp = Array(round(len(self._items)*sizeFactor))
            
            cursor = self._front
            for new in range(len(self)):
                temp[new]=self._items[cursor]
                cursor+=1
                cursor%=len(self._items)
                
            self._items=temp
            self._front=0
            self._rear= self._front+ self._size-1 if self._size!=0 else -1
    #only add and pop need resize and that's just an additional if condition 
    
    def add(self, item):
        """Inserts item at rear of the queue."""
        
        if len(self)== len(self._items):
            self.resize(2)
    
        if self.isEmpty():
            self._front=self._rear=0
            
        else: #if the queue is full
            #Wrapping around with modulo
            self._rear+=1
            self._rear%=len(self._items)
        
        #adding functionality:
        #Adds item to the rear pointer
        self._items[self._rear]=item
        #increases size by 1 
        self._size+=1
        
    def pop(self):
        """Removes and returns the item at the front of the queue.
        Precondition: the queue is not empty.
        Raises: KeyError if queue is empty.
        Postcondition: the front item is removed from the queue."""
        
        #Checking if queue is empty
        if self.isEmpty():
            raise KeyError("Attempt to pop from empty queue")
        
        data= self._items[self._front]
        self._size-=1
        
        if self.isEmpty():
            self._front= self._rear=-1
        else: 
            self._front+=1
            self._front%=len(self._items)
        
        #Resize array here if necessary
        if self._size < len(self._items) // 4:
            self.resize(0.5)  # Resize the array to half of its current size

        return data
         
