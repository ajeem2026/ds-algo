"""
Author: Abid Jeem
Filename: testList.py
This file will test all my lists

In collaboration with TAs and half of our class (Michael, Teddy, Sarp, Jonathan, Rihards, and Elizabeth)
"""

#1. Points awarded based on how robust my test is 
#Questions to think about:
#When programming INSERT> what happens if you insert at start of array? in the middle? in the end?
#at index less than 0? at an index greater than the last index?

from arrayList import ArrayList
from linkedList import LinkedList

def testList(listType):
    print(f"Testing {listType.__name__}:")

    try:
        # Create an empty list
        lyst = listType()

        # Test basic list operations
        print(f"List is Empty, expect True: {(lyst.isEmpty())}")
        lyst.add(1)
        lyst.add(2)
        lyst.add(3)
        print("Items added: 1 2 3")
        print(f"Length, expect 3 : {len(lyst)}")
        print(f"3 in list, expect True", 3 in lyst) 
        print(f"Initial List: {lyst}")
        
        #Test iter
        print("Each element in the list are (in separate lines):")
        for i in lyst:
            print(i)
        
        #Test PLUS
        other_lyst= listType()
        other_lyst.add(4)
        other_lyst.add(5)
        other_lyst.add(6)
        print(f"Another List:", other_lyst)
        print(f"Merged List, expect Initial List and Another List combined: ", lyst+other_lyst)
        
        #Test EQUALITY
        lyst_twin= listType()
        lyst_twin.add(1)
        lyst_twin.add(2)
        lyst_twin.add(3)
        print(f"List Twin: {lyst_twin}")
        print("List is equal to its twin, expect True:", lyst_twin==lyst)

        # Test insert at various positions
        lyst.insert(0, 0)  # Insert at the start
        lyst.insert(2, 2.5)  # Insert in the middle
        lyst.insert(5, 5)  # Insert at the end
        print("Items inserted: 0 @ 0, 2.5 @ 2, 5 @ 5")
        print(f"List after insertions: {lyst}")

        # Test pop at various positions
        lyst.pop(0)  # Pop at the start
        lyst.pop(3)  # Pop in the middle
        lyst.pop()  # Pop at the end (default)
        print(f"Popped items: 0, 3 and 5 (last item)")
        print(f"List after popping: {lyst}")

        # Test clear
        lyst.clear()
        print(f"List after clear, expect []: {lyst}")

        print(f"{listType.__name__} Woohooooooo everything worksss!")

    except Exception as e:
        print(f"{listType.__name__} tests failed: {str(e)}")

def testListIterator(listType):
    print(f"Testing {listType.__name__} ListIterator:")

    try:
        # Create a list
        lyst = listType()
        lyst.add(1)
        lyst.add(2)
        lyst.add(3)
        lyst.add(4)


        # Instantiate list iterator
        iterator = lyst.listIterator()

        # Test hasNext and next
        while iterator.hasNext():
            item = iterator.next()
            print(f"Next item: {item}")
            

        # Test hasPrevious and previous
        while iterator.hasPrevious():
            item = iterator.previous()
            print(f"Previous item: {item}")

        # Test replace
        iterator.first()
        iterator.next()
        iterator.replace(4)
        print(f"List after replace, expect 1 to be replaced by 4: {lyst}")

        # Test insert and remove
        iterator.last()
        iterator.insert(5)
        iterator.first()
        iterator.insert(5)
        print(f"List after insert, expect 5 added to both ends: {lyst}")
        iterator.next()
        iterator.remove()
        print(f"List after remove, expect removal of the replaced 4: {lyst}")
        
        #Test removing all items in the list
        print("Removing all items from the list, expect [] in next line")
        iterator.first()
        while iterator.hasNext():
            iterator.next()
            iterator.remove()
        print(lyst)    
        
        #Test adding back different items to the list
        print("Adding back different items to the list:")
        for i in range(2002, 2024):
            iterator.insert(i)
        print(lyst)
        iterator.first()
        
       
        print(f"{listType.__name__} ListIterator tests passed, let's gooooo!")

    except Exception as e:
        print(f"{listType.__name__} ListIterator tests failed: {str(e)}")



if __name__ == "__main__":
    #testList(ArrayList)
    testList(LinkedList)
    #testListIterator(ArrayList)
    testListIterator(LinkedList)
