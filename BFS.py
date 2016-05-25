import numpy as np

'''
Breadth-First Search

Inputs:
-------
numNodes - Number of nodes in graph
Adjacency Matrix (A[n,n]) - maps Node's adjacent nodes

Outputs:
-------
p - predecessor node
d - distance to source node

Description:
-----------
This script employs Breadth First Search to determine
the shortest distance from a source node to the goal node

The algorithm traverses a graph structure and processes each adjacent
node from a queue. Nodes visited but not yet processed are kept in the
open list (OpenList) and those that are visited and processed are kept
in the closed list (ClosedList)

Outputs of the algorithm are each Node's predecessor nodes from a breadth
traversal of the graph and the distance from the particular node to the
source node.

'''

'''
Class queue is a queue-like data structure that allows the user
to populate a dynamic array and pop out elements that were placed
first (i.e., obeys FIFO - First In First Out procedures)
'''


class queue:
    def __init__(self):
        self.data = []

    def push(self, x=None):
        self.data.append(x)

    def popQueue(self):
        del self.data[0]


# Nodes in graph
numNodes = 5

# Adjacency Matrix - Manual Inputs
A = np.zeros([numNodes, numNodes])

'''
Graph Schematic:

  A-B-C
  |   |
  D---E

Distance between each node is unity.

'''

A[0, 1] = 1
A[0, 3] = 1

A[1, 0] = 1
A[1, 2] = 1

A[2, 1] = 1
A[2, 4] = 1

A[3, 0] = 1
A[3, 4] = 1

A[4, 2] = 1
A[4, 3] = 1

# Instantiate Open/Closed List objects
openList = queue()
closedList = queue()

# List of distances from source node
# Source node has zero distance from itself
# Initialize to zero
d = np.zeros(numNodes)

# List of Predecessor Nodes
# Source node has no predecessors, i.e., the first
# element will be kept as None (NULL)
p = [None] * 5

# Put source node in open list
openList.push(0)

# Start Breadth-First Search Algorithm
while openList.data:  # Break once open list is empty

    for i in range(numNodes):  # Traverse the adjacency matrix

        # If there is an adjacent node and it is not already in the open/closed lists then process
        if ((A[openList.data[0], i] == 1) and (i not in closedList.data) and (i not in openList.data)):
            openList.push(i)

            d[i] = d[openList.data[0]] + 1

            p[i] = openList.data[0]

    closedList.push(openList.data[0])  # Add processed Node to closed list

    # Prevent dequeueing data from an empty list
    if (openList.data is not []):
        openList.popQueue()  # Dequeue processed Node from open list







