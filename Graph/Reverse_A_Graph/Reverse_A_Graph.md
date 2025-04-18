# Reverse a Graph (Adjacency List)

Given a directed graph represented as an adjacency list, return its reverse so if an edge goes from A to B, it now goes from B to A.

Each list in the adjacency list should be sorted in ascending order.

Example 1
```
Input

graph = [
    [1],
    [2],
    []
]
```

```
Output
[
    [],
    [0],
    [1]
]
```

Explanation
In this example the nodes start off 0 -> 1 -> 2 and then become 0 <- 1 <- 2.

```
    1 ←---- 0               then becomes      1 ---→ 0
    |       ↑                                 ↑      ↑
    |       |                                 |      |
    ↓       ↓                                 |      ↓ 
    2       3                                 2      3
```

Constraints
0 ≤ n, m ≤ 250 where n is the number of rows and m is the maximum number of columns in graph

