"""
File: linkedbst.py
Author: Abid Jeem
This is a self-balancing BST which is a little logic intensive. Ideally, this should execute all BST operations with O(logN) time complexity
"""
import math
from utils.abstractcollection import AbstractCollection
from utils.bstnode import BSTNode
from utils.linkedstack import LinkedStack
from utils.linkedqueue import LinkedQueue

# in-order and some other order code is going to be identitical
# will have to verify that the code is working manually

# start with in-order and then move over to preOrder
# another hint: implementing inorder and preorder: note that a stack has an opposite iteration. What you put in most recently is going
# to come out first
# in pre order: push right first, then left and then data
# keep in mind the nuanced implementation with stacks


class LinkedBST(AbstractCollection):
    """An link-based binary search tree implementation."""

    def __init__(self, sourceCollection=None):
        """Sets the initial state of self, which includes the
        contents of sourceCollection, if it's present."""
        self._root = None
        AbstractCollection.__init__(self, sourceCollection)

    # Accessor methods
    def __str__(self):
        """Returns a string representation with the tree rotated
        90 degrees counterclockwise."""
        def recurse(node, level):
            s = ""
            if node != None:
                s += recurse(node.right, level + 1)
                s += "| " * level
                s += str(node.data) + "\n"
                s += recurse(node.left, level + 1)
            return s
        return recurse(self._root, 0)

    def __iter__(self):
        """Supports a preorder traversal on a view of self."""
        return self.preorder()

# ==========================================Traversal methods================================================================#
    def preorder(self):
        """Supports a preorder traversal on a view of self."""
        # lyst = list()
        # def recurse(node):
        #     if node != None:
        #         lyst.append(node.data)
        #         recurse(node.left)
        #         recurse(node.right)
        # recurse(self._root)
        # return iter(lyst)
        """        
        Stack Tree Traversal 
        Benefit: Yield items as they are visited in the tree
        Hint: Note that a stack has an opposite iteration. What you put in most recently is going
        to come out first
        """
        stack = LinkedStack()
        probe = self._root
        while True:
            if probe != None:
                stack.push(probe)
                yield probe.data
                probe = probe.left
            elif not stack.isEmpty():
                probe = stack.pop()
                probe = probe.right
            else:
                break

    def inorder(self):
        """Supports an inorder traversal on a view of self."""
        """        
        Recursive Tree Traversal 
        Issue: Each build a list from the tree and return an iterator on this list
        Consquence: Wastes running time and memory, does NOT catch tree mutation attempts
        with respect to traversal
        
        """
        # lyst = list()
        # def recurse(node):
        #     if node != None:
        #         recurse(node.left)
        #         lyst.append(node.data)
        #         recurse(node.right)
        # recurse(self._root)
        # return iter(lyst)

        """        
        Stack Tree Traversal 
        Benefit: Yield items as they are visited in the tree
        Hint: Note that a stack has an opposite iteration. What you put in most recently is going
        to come out first
        """
        stack = LinkedStack()
        probe = self._root
        while True:
            if probe != None:
                stack.push(probe)
                probe = probe.left
            elif not stack.isEmpty():
                probe = stack.pop()
                yield probe.data
                probe = probe.right
            else:
                break

    def postorder(self):
        """Supports a postorder traversal on a view of self."""
        lyst = list()

        def recurse(node):
            if node != None:
                recurse(node.left)
                recurse(node.right)
                lyst.append(node.data)
        recurse(self._root)
        return iter(lyst)
# pg301

    def levelorder(self):
        """Supports a levelorder traversal on a view of self."""
        q = LinkedQueue()
        lyst = list()
        if not self._root:
            return iter(lyst)

        q.add(self._root)
        while not q.isEmpty():
            node = q.pop()
            lyst.append(node.data)
            if node.left != None:
                q.add(node.left)
            if node.right != None:
                q.add(node.right)

        return iter(lyst)
# ==========================================Traversal methods================================================================#

    def __contains__(self, item):
        """Returns True if target is found or False otherwise."""
        return self.find(item) != None

    def find(self, item):
        """If item matches an item in self, returns the
        matched item, or None otherwise."""
        def recurse(node):
            if node is None:
                return None
            elif item == node.data:
                return node.data
            elif item < node.data:
                return recurse(node.left)
            else:
                return recurse(node.right)
        return recurse(self._root)

    # Mutator methods
    def clear(self):
        """Makes self become empty."""
        self._root = None
        self.resetSizeAndModCount()

    def add(self, item):
        """Adds item to the tree."""

        # Helper function to search for item's position
        def recurse(node):
            # New item is less, go left until spot is found
            if item < node.data:
                if node.left == None:
                    node.left = BSTNode(item)
                else:
                    recurse(node.left)
            # New item is greater or equal,
            # go right until spot is found
            elif node.right == None:
                node.right = BSTNode(item)
            else:
                recurse(node.right)
            # End of recurse

        # Tree is empty, so new item goes at the root
        if self.isEmpty():
            self._root = BSTNode(item)
        # Otherwise, search for the item's spot
        else:
            recurse(self._root)
        self._size += 1
        self.incModCount()

    def remove(self, item):
        """Precondition: item is in self.
        Raises: KeyError if item is not in self.
        postcondition: item is removed from self."""
        if not item in self:
            raise KeyError("Item not in tree.""")

        # Helper function to adjust placement of an item
        def liftMaxInLeftSubtreeToTop(top):
            # Replace top's datum with the maximum datum in the left subtree
            # Pre:  top has a left child
            # Post: the maximum node in top's left subtree
            #       has been removed
            # Post: top.data = maximum value in top's left subtree
            parent = top
            currentNode = top.left
            while not currentNode.right == None:
                parent = currentNode
                currentNode = currentNode.right
            top.data = currentNode.data
            if parent == top:
                top.left = currentNode.left
            else:
                parent.right = currentNode.left

        # Begin main part of the method
        if self.isEmpty():
            return None

        # Attempt to locate the node containing the item
        itemRemoved = None
        preRoot = BSTNode(None)
        preRoot.left = self._root
        parent = preRoot
        direction = 'L'
        currentNode = self._root
        while not currentNode == None:
            if currentNode.data == item:
                itemRemoved = currentNode.data
                break
            parent = currentNode
            if currentNode.data > item:
                direction = 'L'
                currentNode = currentNode.left
            else:
                direction = 'R'
                currentNode = currentNode.right

        # Return None if the item is absent
        if itemRemoved == None:
            return None

        # The item is present, so remove its node

        # Case 1: The node has a left and a right child
        #         Replace the node's value with the maximum value in the
        #         left subtree
        #         Delete the maximium node in the left subtree
        if not currentNode.left == None \
           and not currentNode.right == None:
            liftMaxInLeftSubtreeToTop(currentNode)
        else:

            # Case 2: The node has no left child
            if currentNode.left == None:
                newChild = currentNode.right

        # Case 3: The node has no right child
            else:
                newChild = currentNode.left

        # Case 2 & 3: Tie the parent to the new child
            if direction == 'L':
                parent.left = newChild
            else:
                parent.right = newChild

        # All cases: Reset the root (if it hasn't changed no harm done)
        #            Decrement the collection's size counter
        #            Return the item
        self._size -= 1
        self.incModCount()
        if self.isEmpty():
            self._root = None
        else:
            self._root = preRoot.left
        return itemRemoved

    def replace(self, item, newItem):
        """Precondition: item == newItem.
        Raises: KeyError if item != newItem.
        If item is in self, replaces it with newItem and
        returns the old item, or returns None otherwise."""
        if item != newItem:
            raise KeyError("Items must be equal")
        probe = self._root
        while probe != None:
            if probe.data == item:
                oldData = probe.data
                probe.data = newItem
                return oldData
            elif probe.data > item:
                probe = probe.left
            else:
                probe = probe.right
        return None


# task-3

    def height(self):
        """Returns the height of the tree (the length of the longest path
        from the root to a leaf node).
        When len(t) < 2, t.height() == 0."""
        def recurse(node):
            if node is None:
                return 0
            left_height = recurse(node.left)
            right_height = recurse(node.right)
            return 1+max(left_height, right_height)
        return recurse(self._root)


# one line of code
    def isBalanced(self):
        """Returns True if the tree is balaned or False otherwise.
        t is balanced iff t.height() < 2 * log2(len(t) + 1) - 1."""
        return self.height() < 2 * math.log2(len(self) + 1) - 1


# algorithm is in the slide and the in the book
# rebalance strategy already given just implement it
    def rebalance(self):
        """Rebalances the tree."""
        sorted_tree_list=[]
        for i in self.inorder():
            sorted_tree_list.append(i)
        temp_size= len(sorted_tree_list)
        self.clear()
        self._root=self._rebuild(sorted_tree_list)
        self._size= temp_size

    def _rebuild(self,lyst):
        #When the list has no values
        if len(lyst)==0:
            return None
        mid_index= len(lyst)//2
        newNode= BSTNode(lyst[mid_index])
        #When the list has only one value (leaf node)
        if len(lyst)==1:
            newNode.data=lyst[0]
            newNode.left=None
            newNode.right= None
        #When the list has 2 values, one parent || one child
        if len(lyst)==2:
            newNode.data=lyst[1]
            #this looks more natural
            #but both will give a balanced outcome wherever I place it
            newNode.left=self._rebuild(lyst[:1])
            self.right=None
        #Final case: any amount of values larger than 2
        else:

            left_side= lyst[:mid_index]
            right_side= lyst[mid_index+1:]

            newNode.data= lyst[mid_index]
            newNode.left= self._rebuild(left_side)
            newNode.right=self._rebuild(right_side)
        return newNode
    


    


    
