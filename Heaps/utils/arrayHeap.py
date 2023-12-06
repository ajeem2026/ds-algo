"""
File: arrayHeap.py
Author: Abid Jeem

This is an array heap implementation.
"""

from .arrayList import ArrayList
from .abstractHeap import AbstractHeap


class ArrayHeap(AbstractHeap):
   """An array-based implementation of a heap."""
   
   DEFAULT_SIZE = 10
   
   def __init__(self, sourceCollection = None):
      """Initialization of a heap."""
      self._heap = ArrayList()      
      AbstractHeap.__init__(self,sourceCollection)
   
   def add(self, item):
      """Adds item to the end of the array and then walks it up to the top,
         stopping when parent is less than the new item"""
         
      self._size += 1
      self._heap.append(item)
      curPos = len(self._heap) - 1
      
      while curPos > 0:
         parent = (curPos - 1) // 2
         parentItem = self._heap[parent]
         if parentItem <= item:
            break
 
         else:
            self._heap[curPos] = self._heap[parent]
            self._heap[parent] = item
            curPos = parent
   
   def pop(self):
      """Swaps the top element with the last element, then walks the top
         element down until both children are larger than the current node."""
      if self.isEmpty():
         raise KeyError("The heap is empty.")
         
      self._size -= 1
      topItem = self._heap[0]
      bottomItem = self._heap.pop(len(self._heap) - 1)
      
      if len(self._heap) == 0:
         return bottomItem
             
      self._heap[0] = bottomItem
      lastIndex = len(self._heap) - 1
      curPos = 0
   
      while True:
         leftChild = curPos * 2 + 1
         rightChild = curPos * 2 + 2
         
         if leftChild > lastIndex:
            break
         
         if rightChild > lastIndex:
            maxChild = leftChild
            
         else:
            leftItem  = self._heap[leftChild]
            rightItem = self._heap[rightChild]
            if leftItem < rightItem:
               maxChild = leftChild
               
            else:
               maxChild = rightChild
               
         maxItem = self._heap[maxChild]
         
         if bottomItem <= maxItem:
            break
         
         else:
            self._heap[curPos] = self._heap[maxChild]
            self._heap[maxChild] = bottomItem
            curPos = maxChild
            
      return topItem
   
   def _getRoot(self):
      """Should return the root"""
      return 0
   
   def _getParent(self, index):
      """Returns access to the parent from the index."""
      return (index-1)//2
   
   def _getLeftChild(self, index):
      """Returns access to the left child from the index."""
      return index*2+1
   
   def _getRightChild(self, index):      
      """Returns access to the right child from the index."""
      return index*2+2
   
   def _getData(self, index):
      """Returns the data from the index."""
      return self._heap[index]
   
   def _insideTree(self, index):
      """Returns True if the index is within the tree."""
      if 0<=index<len(self._heap):
         return True
   

   



