import numpy as np

'''
Djikstra's Algorithm

Version 1:
---------
Simple implementation of Djikstra's algorithm that traverses
a graph structure and finds the minimum distances of every
node to source

Inputs
------
A - Adjacency Matrix
numNodes - number of nodes in graph

Outputs
-------
distances.data - minimum distances from every node to source node

'''

'''
Class queue
-----------

queue-like data structure that allows the user
to populate a dynamic array and pop out elements that were placed
first (i.e., obeys FIFO - First In First Out procedures)

'''


class queue:
    def __init__(self):
        self.data = []

    def push(self, x=None):
        self.data.append(x)

    def popQueue(self, node=0):
        del self.data[node]


# Number of nodes in graph
numNodes = 9

'''

Graph schematic:

   1-2---3
  /| |\  | \
 0 | 8 \ |  4
  \|/|  \| /
   7-6---5

Weights along edges indicated in
adjacency matrix (A) below

'''

# Adjacency Matrix with Weights
A = np.zeros([numNodes, numNodes])

A[0, 1] = 4
A[0, 7] = 8

A[1, 0] = 4
A[1, 2] = 8
A[1, 7] = 11

A[2, 1] = 8
A[2, 8] = 2
A[2, 3] = 7
A[2, 5] = 4

A[3, 2] = 7
A[3, 4] = 9
A[3, 5] = 14

A[4, 3] = 9
A[4, 5] = 10

A[5, 2] = 4
A[5, 3] = 14
A[5, 4] = 10

A[6, 5] = 2
A[6, 7] = 1
A[6, 8] = 6

A[7, 0] = 8
A[7, 1] = 11
A[7, 6] = 1
A[7, 8] = 7

A[8, 2] = 2
A[8, 6] = 6
A[8, 7] = 7

# Initialize distances from source node
distances = queue()
distances.push(0)  # Source node

# Initialize distances
k = 0
while (k < numNodes - 1):
    distances.push(10e10)
    k += 1

# Shortest Path Set (visited nodes)
spSet = queue()  # List of nodes

# Start Djikstra's Algorithm
while (len(spSet.data) is not numNodes):  # Stop when all nodes have been visited

    # Find minimum distance of the adjacent nodes
    n = max(distances.data) * 10  # Set min node value to something high
    for i in range(numNodes):  # Traverse the nodes that are not in the closed set
        if ((distances.data[i] < n) and (i not in spSet.data)):
            n = distances.data[i]
            minNode = i

    # Push min distance node into spSet if it's not in there already
    if (minNode not in spSet.data):
        spSet.push(minNode)
        spSetDist.push(n)

    # Update distances of adjacent nodes
    for i in range(numNodes):
        if (A[minNode, i] != 0.0):
            d = distances.data[minNode] + A[minNode, i]
            if (d < distances.data[i]):
                distances.data[i] = d








