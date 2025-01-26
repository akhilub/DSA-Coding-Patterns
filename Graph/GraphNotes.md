# Graph Data Structure

- A graph consists of Vertices (V) and Edges (E). Each edge can have a weight or not. If it is weighted, we call it a weighted graph otherwise it is unweigted.

- Edges in the Graph G can also have directions. If the edges are directed, we call the Graph directed Graph, otherwise it is undirected Graph.

- For number of incoming edges, we call it the incoming degree, and for number of outgoing edges for a vertex, we call it the outgoing degree.

- A complete Graph is a graph that each vertice contains all possible edges to other vertices. An empty Graph is basically an empty set of G(V, E).

- A Connected Graph is a Graph that each vertice is connected from or connected to any other vertices and Dis-connected graph is otherwise.

- In theory, a tree is also a Graph (special case). Two trees (disjoint) are also graphs (sometimes they are called forest). A linked list is also a graph.


## STORING THE GRAPH USING ADJACENT MATRIX

We can use the 2 dimesnional array to store the Vertices and Edges: for example

```
G = [
  [0, 1, 0], # edges from vertex 0
  [1, 0, 1], # edges from vertex 1
  [0, 1, 0]  # edges from vertex 2
]
```
which represents the following Graph:

```
(0) <--> (1) <--> (2)
```

This data structure can be used to store weighted, unweights, directed and undirected Graphs.

## STORING THE GRAPH USING ADJACENT LINKED LIST

If the edge number is small compared to vertice number, the above data structure is not space efficient, we can store, however, the Graph using the below Adjacent Linked List data structure:

```
G = {
  "A": ["B"],
  "B": ["A", "C"],
  "C": ["B"]
}
```

This represents the following Graph:

```
(A) <--> (B) <--> (C)
```

We can also store the weights by using the tuples:
```
G = {
  "A": [("B", 1)],
  "B": [("A", 2), ("C", 3)],
  "C": [("B", 4)]
}
```

We can also change slightly to use the dictionary/hash map to store the edges as well:
```
G = {
  "A": {"B": 1},
  "B": {"A": 2, "C": 3},
  "C": {"B": 4}
}
```

Algorithm-wise, we can perform Depth First Search, or Breadth First Search Algorithms on it e.g. to find the shortest distance etc.



<p>&nbsp;</p>

## [4 Types of Graph Input](https://www.linkedin.com/posts/neetcodeio_4-graph-input-types-in-a-coding-interview-activity-7281335068680228864-1iCk)

<p>&nbsp;</p>





## 𝗚𝗿𝗮𝗽𝗵 - 𝗠𝗮𝘁𝗿𝗶𝘅 𝗕𝗙𝗦

Breadth-first search can also be applied when given a matrix as an input.
To do this, we make use of a queue, which allows us to explore a node's neighbors. This is shown in the animation.

### 𝗜𝗺𝗽𝗹𝗲𝗺𝗲𝗻𝘁𝗮𝘁𝗶𝗼𝗻

1. Start at source
2. Add neighbors to queue
3. Mark positions visited to avoid infinite loop
4. Continue until target is reached


### 𝗨𝘀𝗲 𝗖𝗮𝘀𝗲𝘀

1. Shortest Path in an unweighted graph - LC 127 Word Ladder

2. Kahn's algorithm for topological sort - LC 207 Course Schedule
   
3. Connected components - LC 200 Number of Islands

### 𝗧𝗶𝗺𝗲 𝗮𝗻𝗱 𝗦𝗽𝗮𝗰𝗲

**Time**: O(n*m) where n and m are the dimensions of the grid.
**Space**: O(n*m)




<p>&nbsp;</p>




## 𝗚𝗿𝗮𝗽𝗵 - 𝗠𝗮𝘁𝗿𝗶𝘅 𝗗𝗙𝗦 𝗕𝗮𝗰𝗸𝘁𝗿𝗮𝗰𝗸𝗶𝗻𝗴

DFS is a common graph traversal algorithm. In a matrix, we can use it to move in all four directions (up, down, left, right) and count the number of unique paths from the top-left cell to the bottom-right cell.


### 𝗜𝗺𝗽𝗹𝗲𝗺𝗲𝗻𝘁𝗮𝘁𝗶𝗼𝗻

1. Use a hash set to track visited coordinates.
2. Add the current cell to the hash set and initialize count as 0.
3. Recursively perform DFS in all four directions.
4. If we go out of bounds, or a cell has already been visited or is blocked (1), no path exists: return 0.
5. If we are at the bottom right cell, we have reached the destination: return 1 and increment count.
6. After exploring all four directions of a cell, remove the cell's coordinates from the hash set to backtrack and explore other unique paths.
7. Finally, return the total number of unique paths found from all four directions.

### 𝗨𝘀𝗲 𝗖𝗮𝘀𝗲𝘀

1. Number of Islands 

2. Max Area of Island 

3. Pacific Atlantic Water Flow 

4. Surrounded Regions 

### 𝗧𝗶𝗺𝗲 𝗮𝗻𝗱 𝗦𝗽𝗮𝗰𝗲

**Time:** O(4^n.m), in the worst case, each cell can have four recursive calls
**Space:** O(n.m), where n represents number of rows and m represents the number of columns