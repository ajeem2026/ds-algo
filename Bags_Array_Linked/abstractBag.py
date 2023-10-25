"""
Name: Abid Jeem
Filename: abstractBag.py 
This is an abstract bag class that all other bags inherit from. This does NOT do anything when run
"""
from abstractCollection import AbstractCollection

class AbstractBag(AbstractCollection):

    # Constructor
    def __init__(self, sourceCollection = None):
        """Sets the initial state of self, which includes the contents of sourceCollection, if it is present."""
        super().__init__(sourceCollection)
    
    #Redundant methods  
    def __str__(self):
        """Returns the string representation of self."""
        return "{" + ", ".join(map(str, self)) + "}"

    def __eq__(self, other):
        """Returns True if self equals other,
        or False otherwise."""
        if self is other: return True
        if type(self) != type(other) or \
           len(self) != len(other):
            return False
        for item in self:
            if self.count(item) != other.count(item):
                return False
        return True
