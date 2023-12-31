"""
File: linkedHeap.py
Name: Abid Jeem

This is a linked implementation of heap, we have established the adding and popping
functions while maintaining "heap"-ness and elucidated the algorithm using our
walk_up and walk_down helper methods.
"""


from .abstractHeap import AbstractHeap
from .bstNode import BSTNode
import math


class LinkedHeap(AbstractHeap):
   """A link-based implementation of a heap."""
   
   def __init__(self, sourceCollection = None):
      """Initialization of a heap."""
      self._heap = None
      super().__init__(sourceCollection)

   def _getRoot(self):
      """Helper for AbstractHeap"""
      return self._heap
   
   def _getParent(self, node):
      """Helper for AbstractHeap"""
      return node.parent 
   
   def _getLeftChild(self, node):
      """Helper for AbstractHeap"""
      return node.left 
   
   def _getRightChild(self, node):
      """Helper for AbstractHeap"""
      return node.right 
   
   def _getData(self, node):
      """Helper for AbstractHeap"""
      return node.data 

   def _insideTree(self, node):
      """Helper for AbstractHeap"""
      return node is not None

   
   def _walkUp(self, node):
      """Walks node's data upwards through its parents while
         it is smaller than the parent."""
      #Will only walk up if node exists and it's smaller than the parent
      while node is not None and node.parent is not None and node.data < node.parent.data:
         #making the swap
         temp= node.data
         node.data = node.parent.data
         node.parent.data= temp
         #walking up after each deduction
         node= node.parent
   
   
   def _walkDown(self, node):
      """Walks node's data downwards through its children while
         it is larger than a child."""
      while True:
        #Set the current node as the smallest in the very beginning
        smallest_node = node
        #Check both children for larger nodes
        if node.left and node.left.data < smallest_node.data:
            smallest_node = node.left
        if node.right and node.right.data < smallest_node.data:
            smallest_node = node.right
         #If the smallest node is the current node after the checks, then it is in the correct heap position
        if smallest_node==node:
            break

        # Swap the data to achieve walking down when the node is NOT in correct position
        temp=node.data
        node.data=smallest_node.data
        smallest_node.data=temp
        #Setting the current node as the smallest child for continuing the walk down 
        node = smallest_node

   def add(self, item):
      """Adds item to the end of the array and then walks it up to the top,
         stopping when parent is less than the new item"""
      # increase size by one so that finding the last node points to
      #  the node BEYOND the last node
      
      self._size += 1
      path = self._findPathToLastNode()
      
      # Start at the top
      parentPointer = self._heap
      
      # If there is no path, we have an empty tree      
      if len(path) == 0:
         self._heap = BSTNode(item)
         
      # Otherwise, follow the path to one before the end
      else:
         # Use slicing to stop one early, could also use range(len(path) - 1)
         for choice in path[:-1]:
            # Go the directions
            if choice == "left":
               parentPointer = parentPointer.left
            else:
               parentPointer = parentPointer.right
         
         # If our last direction choice is left, place new node there
         #  and walk it up the heap
         if path[-1] == "left":
            parentPointer.left = BSTNode(item, None, None, parentPointer)
            self._walkUp(parentPointer.left)
         
         # Otherwise, right and walk
         else:
            parentPointer.right = BSTNode(item, None, None, parentPointer)
            self._walkUp(parentPointer.right)
        
      
   def pop(self):
      """Swaps the top element with the last element, then walks the top
         element down until both children are larger than the current node."""
      if self.isEmpty():
         raise KeyError("The heap is empty.")
      
      # Find the path to the actual last node
      path = self._findPathToLastNode()
      
      # Start at the top
      parentPointer = self._heap
      
      # If there is no path, we have only one item in the heap
      if len(path) == 0:
         removedNode = self._heap
         self._heap = None
      
      # Follow directions
      else:
         # Stop one early using slicing, could also use range(len(path)-1)
         for choice in path[:-1]:
            # Go left
            if choice == "left":
               parentPointer = parentPointer.left
            # Go right
            else:
               parentPointer = parentPointer.right
         
         # Replace the top based on the last choice, remove the last item
         if path[-1] == "left":
            removedNode = parentPointer.left
            removedNode.data, self._heap.data = self._heap.data, removedNode.data
            parentPointer.left = None
            
         else:
            removedNode = parentPointer.right
            removedNode.data, self._heap.data = self._heap.data, removedNode.data
            parentPointer.right = None
         
         # Walk down the new top item
         self._walkDown(self._heap)
            
      # Decrease size now and return value popped
      self._size -= 1
      
      return removedNode.data
      

   def _findPathToLastNode(self):
      """Calculates the path to the last node in a linked
         heap based on the total number of items stored."""
         
      #The list will be empty if the len(self) is 1
      
      n = len(self)
      path = []
      
      total = math.floor(math.log(n, 2)) + 1
      
      for i in range(total - 2, -1, -1):
         if (n // math.pow(2, i)) % 2 == 0:
            path.append("left")
         else:
            path.append("right")
      
      # Return list of directions
      return path

   
