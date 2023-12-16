"""
File: testGraph.py

Abid Jeem

"""

from modules.graph.graph import LinkedDirectedGraph
from modules.graph.pathEntry import PathEntry
from modules.stack.linkedStack import LinkedStack
from modules.queue.linkedQueue import LinkedQueue
from modules.utils.grid import Grid
from modules.utils.arrays import Array
from modules.math.infinity import *


#showProcess: boolean is just a parameter to show you the movement 
def traverseFromVertex(graph, startVertex, showProcess, collection = LinkedStack()):
    # Exercise
    graph.clearVertexMarks()
    collection.add(startVertex)
    while collection:
        vertex= collection.pop()
        if not vertex.isMarked():
            vertex.setMark()
            if showProcess:
                print(vertex)
            #go over each connection it is connecting to
            for node in vertex.neighboringVertices():
                #check if neighbouring vertices are marked or not before adding
                if not node.isMarked():
                    collection.add(node)

    

def depthFirstTraverse(graph, startVertex, showProcess):
    # Exercise
    traverseFromVertex(graph, startVertex, showProcess)
    

def breadthFirstTraverse(graph, startVertex, showProcess):
    # Exercise
    traverseFromVertex(graph, startVertex, showProcess, LinkedQueue())
    


          
def main():
        
    # Create a directed graph using an adjacency list
    graph = LinkedDirectedGraph()
    
    # Exercise: Add vertices with appropriate labels and print the graph
    for label in ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]:
        graph.addVertex(label)
    
    print("\nThe graph: \n" + str(graph))
    
    # Exercise: Insert edges with weights and print the graph
    graph.addEdge("A","I",8)
    graph.addEdge("A","J",1)
    graph.addEdge("A","B",3)
    graph.addEdge("J","B",1)
    graph.addEdge("J","H",6)
    graph.addEdge("H","B",2)
    graph.addEdge("H","E",1)
    graph.addEdge("B","C",2)
    graph.addEdge("C","E",4)
    graph.addEdge("C","G",2)
    graph.addEdge("G","D",1)
    graph.addEdge("G","F",1)
    graph.addEdge("D","I",1)
    

    print("\nThe graph: \n" + str(graph))
    
    # Print the vertices adjacent to vertex A
    print("\nExpect vertices adjacent to A:")
    print(", ".join(list(map(str,graph.getVertex("A").neighboringVertices()))))
    
    # Print the edges incident to A
    print("Expect edges incident to A:")
    print(", ".join(list(map(str,graph.getVertex("A").incidentEdges()))))
    
    # Exercise
    print("\nTraverse from vertex A:")
    traverseFromVertex(graph, graph.getVertex("A"), True)

    # Exercise
    print("\nDepth first traversal:")
    depthFirstTraverse(graph, graph.getVertex("A"), True)
    
    # Exercise
    print("\nBreadth first traversal:")
    breadthFirstTraverse(graph, graph.getVertex("A"), True)
    

if __name__ == '__main__':
    main()