- If the problem requires finding all permutations or combinations , we can use **backtracking** or BFS or DFS.

- If the problem has input as **sorted** array,list or matrix we can use **Two pointer** or **Binary Search**.

- If the problem requires performing an operation that needs faster search in O(1), we can use **Set** or a **Map**.

- If the problem revolves around iterating an array, and takes O(N²) time complexity, O(1) space complexity then we can use a HashMap/HashSet. It makes the algorithm faster with O(N) time complexity but takes more space with O(N) space complexity.

- If the problem revolves around iterating an array and takes O(N²) time complexity, and O(1) space complexity then we can **sort** the array. It makes the algorithm faster with O(N log N) time complexity and O(1) space complexity.

- If the problem requires optimization around the recursive the solution, there could be a possibility that dynamic programming can be used.

- If the problem has a recursive solution but it's hard to visualize/code, try using a **Stack** data structure with a loop.

- If the problem has input in the form of a Tree or Graph, then most of the time can be solved by applying Tree Traversals or Graph Traversals algorithms called Breadth First Search (BFS) and Depth First Search (DFS)