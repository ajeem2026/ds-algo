"""
Name: Abid Jeem
Filenme: arraySortedSet.py

Array-based implementation of sorted set
"""

from arraySortedBag import ArraySortedBag
from abstractSet import AbstractSet

class ArraySortedSet(ArraySortedBag, AbstractSet):
    
    def __init__(self, sourceCollection=None):
        ArraySortedBag.__init__(self, sourceCollection)    
        
    def add(self,item):
        if not item in self:
            ArraySortedBag.add(self, item)