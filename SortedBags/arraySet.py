"""
    Name: Abid Jeem
    Filename: arraySet.py

"""

from arrayBag import ArrayBag
from abstractSet import AbstractSet

class ArraySet(ArrayBag, AbstractSet):
    
    def __init__(self, sourceCollection=None):
        ArrayBag.__init__(self, sourceCollection)
        
    def add(self,item):
        if self._size == 0:
            super().add(item)
        else: 
           if item not in self:
                super().add(item)
            
    
    
    