## Minimum Starting Nodes to Visit Graph 

### Topological Sort, Indegree

Difficulty : **Medium**

#### Description

You are given a two-dimensional list of integers edges representing a connected, directed, acyclic graph. Each element in edges contains [u, v] meaning there is an edge from u to v. Return the minimum list of nodes from which we can visit every node in the graph, sorted in ascending order.

Example 1:
```
Input: edges = [[0,1],[1,2],[3,2]]
Output: [0,3]
```
Example 2:
```
Input: nums = [[1,0],[2,0],[3,2],[4,3]]
Output: [1,4]
```

Constraints:

`0 ≤ n ≤ 100,000` where n is the length of edges