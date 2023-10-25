"""
Name: Abid Jeem
File: abstractCollection.py
This is a class that is a collection of methods that all other classes inherit from. This does NOT do anything when run
"""

class AbstractCollection(object):
    
    """Represents an abstract collection for all collection types."""

    # Constructor
    def __init__(self, sourceCollection = None):
        """Sets the initial state of self, which includes the contents of sourceCollection, if it's present."""
        self._size = 0
        if sourceCollection:
            for item in sourceCollection:
                self.add(item)
        
    def isEmpty(self):
        """Returns True if len(self) == 0, or False otherwise."""
        return len(self) == 0
    
    def __len__(self):
        """Will copy items to self from sourceCollection
        if it's present."""
        return self._size

    def __add__(self, other):
        """Returns a new bag containing the contents
        of self and other."""
        result = type(self)(self)
        for item in other:
            result.add(item)
        return result

    def count(self, target):
        """Counts the amount of targets currently contained in self."""
        counter = 0
        for item in self:
            if item == target:
                counter += 1         
        return counter
    