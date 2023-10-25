"""
Name: Abid Jeem
File: arraySortedBag.py

Code implementation for arraySortedBag in collaboration with Rihards and Sarp, and, of course, Dr. Lambert

"""
from arrayBag import ArrayBag

class ArraySortedBag(ArrayBag):
    """This is an array-based sorted bag implementation"""
    
    #Constructor
    def __init__(self,sourceCollection= None):
        """Sets the initial state of self, which includes the contents of sourceCollection, if it's present."""
        ArrayBag.__init__(self,sourceCollection)
    
    def __eq__(self, other):
        """Returns True if self equals other,
        or False otherwise."""
        if self is other: return True
        if type(self) != type(other) or \
           len(self) != len(other):
            return False
        for i in range(len(self)):
            if self._items[i] != other._items[i]:
                return False
        return True
    
    #Accesor methods 
    def __contains__(self, item):
        """Returns True if item is in self, or False otherwise."""
        left=0
        right= len(self)-1
        while left<=right:
            midPoint=(left+right)//2
            if self._items[midPoint]==item:
                return True
            elif self._items[midPoint] > item:
                right = midPoint-1
            else:
                left = midPoint+1
        return False
    
    def __add__(self, other):
        """Returns a new bag with the contents of self and other."""
        result= ArraySortedBag(self)
        for item in other:
            result.add(item)
        return result 
    
    def add(self, item):
        """Adds item to self"""
        #If empty or the last item, we call ArrayBag.add
        if self.isEmpty() or item>= self._items[len(self)-1]:
            ArrayBag.add(self,item)
        else:
            #Resize the array if it is full here
            #Search for first item >= new item
            targetIndex=0 
            while item> self._items[targetIndex]:
                targetIndex+=1 
            #Open a hole for the new item
            for i in range(len(self), targetIndex, -1):
                self._items[i]= self._items[i-1]
            #Insert item and update size
            self._items[targetIndex]=item
            self._size+=1
    
            


