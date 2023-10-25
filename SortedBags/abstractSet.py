"""
Name: Abid Jeem
Filename: abstractSet.py
This is an abstract set class that all other sets inherit from. This does NOT do anything when run
"""
class AbstractSet(object):
    
    def __or__(self, other):
        return self + other
    
    def __and__(self, other):
        intersection= self.__class__()
        for item1 in self:
            for item2 in other:
                if item1 == item2:
                    intersection.add(item1)
        
        return intersection
    
    def __sub__(self, other):
        newSub= type(self.__class__())
        for item1 in self:
            if item1 not in other:
                newSub.add(item1)
        return newSub