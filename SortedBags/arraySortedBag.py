"""
Name: Abid Jeem
File: arraySortedBag.py

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
    
    # def add(self, item):
    #     """Adds item to self"""
    #     if len(self._items) == len(self):
    #         self.resize(2)  # Increase array size by a factor of 2 if it's full

    #     #If empty or the last item, we call ArrayBag.add
    #     if self.isEmpty():
    #         ArrayBag.add(self,item)
        
    #     # elif self.size==1: 
    #     #     if item> self._items[0]:
    #     #         temp= self._items[0]
    #     #         self._items[0]= item
    #     #         self._items[1]= temp
    #     else:
    #         #Resize the array if it is full here
    #         #Search for first item >= new item
    #         targetIndex=0 
    #         for i in range(self._size):
    #             if self._items[i] >= item:
    #                 targetIndex=i
    #                 break
    #         for j in range(self._size, targetIndex, -1):
    #             self._items[j]=self._items[j-1]
            
    #         self._items[targetIndex]= item
        #     while item> self._items[targetIndex]:
        #         targetIndex+=1 
        #     #Open a hole for the new item
        #     for i in range(len(self)-1, targetIndex, -1):
        #         self._items[i]= self._items[i-1]
        #     #Insert item and update size
        #     self._items[targetIndex]=item
            # self._size+=1
        
        # """Adds item to self."""
        # # Check array memory here and increase it if necessary
        # # len(self._items) gives you physical size
        # # len(self) gives you the logical size

        # if len(self._items) == len(self):
        #     self.resize(2)  # Increase array size by a factor of 2 if it's full

        # self._items[len(self)] = item
        # self._size += 1

        # # Check array memory here and decrease it if necessary
        # if len(self._items) >= 4 * len(self):
        #     self.resize(0.5)  # Decrease array size by a factor of 0.5 if it's too empty
    def add(self, item):
        """Adds item to self"""
        #If empty or the last item, we call ArrayBag.add
        if self.isEmpty() or item>= self._items[len(self)-1]:
            ArrayBag.add(self,item)
        else:
            #Resize the array if it is full here
            if len(self._items) == len(self):
                self.resize(2)  # Increase array size by a factor of 2 if it's full
            #Search for first item >= new item
            targetIndex=0 
            while item> self._items[targetIndex]:
                targetIndex+=1 
            #Open a hole for the new item
            for i in range((self._size), targetIndex, -1):
                self._items[i]= self._items[i-1]
            #Insert item and update size
            self._items[targetIndex]=item
            self._size+=1
        
    
            


