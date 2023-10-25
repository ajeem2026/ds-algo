"""
    Name: Abid Jeem
    Filename: linkedSet.py

"""


from linkedBag import LinkedBag
from abstractSet import AbstractSet

class LinkedSet(LinkedBag, AbstractSet):
    
    def __init__(self, sourceCollection=None):
        LinkedBag.__init__(self, sourceCollection)
        
    def add(self,item):
        if item not in self:
            super().add(item)