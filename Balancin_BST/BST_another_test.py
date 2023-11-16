import unittest
import math
from utils.abstractcollection import AbstractCollection
from utils.bstnode import BSTNode
from utils.linkedstack import LinkedStack
from utils.linkedqueue import LinkedQueue
from linkedbst import LinkedBST  # Assuming your class is in linkedbst.py

class TestLinkedBST(unittest.TestCase):


    def test_init(self):
        tree = LinkedBST()
        self.assertIsNone(tree._root)
        self.assertEqual(len(tree), 0)

    def test_add_find(self):
        tree = LinkedBST()
        tree.add(5)
        tree.add(3)
        tree.add(7)
        self.assertTrue(tree.find(5))
        self.assertTrue(tree.find(3))
        self.assertFalse(tree.find(10))

    def test_add_find(self):
        tree = LinkedBST()
        tree.add(5)
        tree.add(3)
        tree.add(7)
        self.assertTrue(tree.find(5))
        self.assertTrue(tree.find(3))
        self.assertFalse(tree.find(10))

    def test_inorder(self):
        tree = LinkedBST()
        elements = [5, 3, 7]
        for e in elements:
            tree.add(e)
        self.assertEqual(list(tree.inorder()), sorted(elements))

    def test_remove(self):
        tree = LinkedBST()
        elements = [5, 3, 7]
        for e in elements:
            tree.add(e)
        tree.remove(3)
        self.assertFalse(tree.find(3))
        self.assertEqual(len(tree), 2)

    def test_height_isBalanced(self):
        tree = LinkedBST()
        tree.add(3)
        tree.add(1)
        tree.add(4)
        self.assertEqual(tree.height(), 2) 
        self.assertTrue(tree.isBalanced())
    

    def test_rebalance(self):
        tree = LinkedBST()
        for i in range(1, 5):
            tree.add(i)
        self.assertFalse(tree.isBalanced())
        tree.rebalance()
        self.assertTrue(tree.isBalanced())

if __name__ == '__main__':
    unittest.main()





