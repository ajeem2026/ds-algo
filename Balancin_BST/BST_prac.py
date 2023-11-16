"This is for BST practice only"

"""
This is a wrapper that handles the management of all the node classes.
Encapsulates functionality: provides a simpler, more user friendly interface to underlying complexity. Its like a remote on a complex machine
Abstraction: Abstracts complexities
Extention: Extends functionality of the wrapped entity; Adding extra features to an existing tool without modifying the tool itself
"""
class Node:
    def __init__(self, value=None):
        self.value = value
        self.left_child= None
        self.right_child= None

class binary_search_tree:
    def __init__(self):
        #Setting root is equal to none as we have no elements inside a BST in the beginning
        self.root = None
    
    #First real function we implement is the insert function, which allows you to add elements to the BST
    #For the entire implementation, it is assumed that the values are integers
    def insert(self, value):
        #create a new instance of node class, passing in our value of insert as the value in the constructor
        #then using self.value in constructor, the node class will be saving that value internally
        newNode = Node(value)
        #checking to see if we can insert the new value at the root
        if self.root is None:
            self.root = newNode
            #We're gonna call a private function inside BST
            #However, python does NOT have any TRUE private function so when a user sees an __ function like this,
            #they should just REFRAIN from calling that function OUTSIDE of that class
        else:
            self._insert(self, value)
    
    #the reason for partition insert into 2 separate functions is that the private function is going to be recursive
    #it is easier to carry the recursive logic in a separate function instead of cramming one function with all the logic
    #can't have a function that is sometimes recursive and sometimes NOT recursive
    def _insert(self, value, cur_node):
        if value < cur_node:
            if cur_node.left_child is None:
                cur_node.left_child= cur_node
            else:
                self._insert(self, value, cur_node.left_child)
        
        elif value> cur_node:
            if cur_node.right_child is None:
                cur_node.right_child= cur_node
            else:
                self._insert(self, value, cur_node.right_child)
        else:
            print("Value already in tree!")
    
    #Height function to determind the overall size of our data structure
    #Takes in NO parameters, only returns an integer
    #Partition into private function where private function is recursive
    def height(self):
        if self.root != None:
            return self._height(self.root, 0)
        else:
            return 0
        
    def _height(self, cur_node, cur_height):
        #this acts as the base case for the two recursive calls below
        if cur_node==None: return cur_height
        #keeps traversing the left children of the tree until it reaches a leaf node
        left_height= self._height(cur_node.left_child, cur_height+1)
        #keeps traversing the right children of the tree until it reaches a leaf node
        right_height= self._height(cur_node.right_child, cur_height+1)
        #returns the larger height out of the left and right side
        return max(left_height,right_height)

        
        
        
        
             
        
        
    