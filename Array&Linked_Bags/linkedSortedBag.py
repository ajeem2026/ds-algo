"""
Name: Abid Jeem
File: linkedSortedBag.py
Code implementation for linkedSortedBag in collaboration with Rihards and Sarp, and, of course, Dr. Lambert

"""
from node import Node
from linkedBag import LinkedBag
class LinkedSortedBag(object):
    """A link-based bag implementation."""

    # Constructor
    def __init__(self, sourceCollection = None):
        """Sets the initial state of self, which includes the
        contents of sourceCollection, if it's present."""
        self._items = None
        self._size = 0
        if sourceCollection:
            for item in sourceCollection:
                self.add(item)

    # Accessor methods
    def isEmpty(self):
        """Returns True if len(self) == 0, or False otherwise."""
        return len(self) == 0
    
    def __len__(self):
        """-Returns the number of items in self."""
        return self._size

    def __str__(self):
        """Returns the string representation of self."""
        return "{" + ", ".join(map(str, self)) + "}"

    def __iter__(self):
        """Supports iteration over a view of self."""
        cursor = self._items
        while not cursor is None:
            yield cursor.data
            cursor = cursor.next

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
    
    def count(self, target):
        """Counts the amount of targets currently contained in self."""
        counter = 0
        for item in self:
            if item == target:
                counter += 1         
        return counter

    # Mutator methods
    def clear(self):
        """Makes self become empty."""
        self._size = 0
        self._items = None

    def add(self, item):
        """Adds item to self."""
        self._size += 1
        current_node = self._items
        if current_node is None or current_node.data> item:
            self._items = Node(item, self._items)
            return
        while current_node.next is not None and current_node.next.data< item:
            current_node= current_node.next
        
        new_node= Node(item, current_node.next)
        current_node.next=new_node

    def remove(self, item):
        """Precondition: item is in self.
        Raises: KeyError if item in not in self.
        Postcondition: item is removed from self."""
        # Check precondition and raise exception if necessary
        if not item in self:
            raise KeyError(str(item) + " not in bag")
        # Search for the node containing the target item
        # probe will point to the target node, and trailer
        # will point to the one before it, if it exists
        probe = self._items
        trailer = None
        for targetItem in self:
            if targetItem == item:
                break
            trailer = probe
            probe = probe.next
        # Unhook the node to be deleted, either the first one or one
        # thereafter
        if probe == self._items:
            self._items = self._items.next
        else:
            trailer.next = probe.next
        # Decrement logical size
        self._size -= 1