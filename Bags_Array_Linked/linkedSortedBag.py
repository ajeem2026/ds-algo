"""
Name: Abid Jeem
File: linkedSortedBag.py
Code implementation for linkedSortedBag 

"""
from node import Node
from linkedBag import LinkedBag

class LinkedSortedBag(LinkedBag):
    """A link-based bag implementation."""

    # Constructor
    def __init__(self, sourceCollection = None):
        """Sets the initial state of self, which includes the
        contents of sourceCollection, if it's present."""
        LinkedBag.__init__(self, sourceCollection)

    # Accessor methods
    def __add__(self, other):
        """Returns a new bag containing the contents
        of self and other."""
        result = LinkedBag(self)
        for item in other:
            result.add(item)
        return result

    def __eq__(self, other):
        """Returns True if self equals other,
        or False otherwise."""
        
        #Check if self is and others are the same object in memory 
        if self is other: return True
        
        #Check if self and other have different types or lengths
        if type(self) != type(other) or len(self) != len(other):
            return False
        
        #Here we initialize probes to iterate through the internal linked structure
        probe1=self._items
        probe2=other._items
        
        while probe1 and probe2:
            #Iterate through elements of self and other
            if probe1.data != probe2.data:
                return False
            
            probe1=probe1.next
            probe2=probe2.next
        #if one object is longer than the other, they cannot be equal
        if probe1 or probe2:
            return False
        
        #if PASS all, objects are equal 
        return True

    # Mutator methods

    def add(self, item):
        """Adds item to self in sorted order"""
        # Special case for the empty or first node
        if self.isEmpty() or item < self._items.data:
            self._items = Node(item, self._items)
            self._size += 1
        else:
            # Search for the node before the point of insertion
            probe = self._items
            while probe.next is not None and item > probe.next.data:
                probe = probe.next
            probe.next = Node(item, probe.next)
            self._size += 1
        
        
