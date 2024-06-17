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



