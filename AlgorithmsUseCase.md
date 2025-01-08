1) If the coding problem requires performing an operation that needs faster **search in O(1)**, try to use **Set or a Map**.

2) If the coding problem requires **finding/manipulating/dealing** with the **top, bottom, maximum, minimum, closest, and farthest** *"K"* elements among given *"N"* elements, try to use a **Heap**.

3) If the coding problem has **input** as a **sorted Array, List, or Matrix**, try to use **Two Pointer strategy** or try to use **Binary Search**.

4) If the problem requires finding all **permutations or combinations** , we can use **backtracking(DFS)** or **BFS**.

5) If the coding problem has **input** in the form of a *Tree* or *Graph*, then most of the time can be *solved* by applying *Tree Traversals* or *Graph Traversals* algorithms called **Breadth First Search (BFS)** and **Depth First Search (DFS)**.

6) If the coding problem is around a **Singly Linked List**, and If you are stuck in traversals logic, then try to use either **Two Pointers** or **Slow/Fast Pointers**.

7) If the coding problem has a **recursive solution** but it's **hard to visualize/code**, try using a **Stack** data structure with a **loop**.

8) If the coding problem revolves around iterating an array, and takes O(N²) time complexity, O(1) space complexity then try to use a **HashMap/HashSet**. It makes the algorithm faster with O(N) time complexity but takes more space with O(N) space complexity.

9) If the coding problem revolves around iterating an array and takes O(N²) time complexity, and O(1) space complexity then try to **sort** the array. It makes the algorithm faster with O(N log N) time complexity and O(1) space complexity.


11)  If the coding problem requires **optimization**(e.g., maximization or minimization) around the **recursive the solution**, there could be a possibility that **dynamic programming** can be used.

12)  If the coding problem has a **group of strings** or **some manipulation/find/storing** needs to be done around the **substring**, there is a high possibility that either **Tries or HashMap** can be used.


## Observations 

1) Collectively 8 and 9 suggests

- For a problem involving arrays, if there exists a solution in O(n^2) time and O(1) space, there must exist two other solutions :

    - a) Using a HashMap or a Set for O(n) time and O(n) space,
    - b) Using sorting for O(n log n) time and O(1) space.

2) Every recursive solution can be converted to an iterative solution using a Stack.

3) If we need to try all combinations (or permutations) of the input, we can either use recursive Backtracking or iterative Breadth-First Search


## Data Structures Use Case

- The best data structure that comes to mind to find the smallest number among a set of ‘K’ numbers is a Heap.

- If we need to find some common substring among a set of strings, we will be using a HashMap or a Trie.

- If we need to search/manipulate a bunch of strings, Trie will be the best data structure.

- 



## Problem Solving Techniques

**1.Two Pointer Technique:** This technique is commonly applied on sorted arrays or linked lists to find pairs or reverse elements. It is an ideal strategy when managing elements with pair relationships.


**2.Sliding Window:** This pattern is used to track a subset of data within a larger dataset. It's particularly useful in array or string problems when you need to maintain a 'window' of elements satisfying a certain condition.


**3.Fast & Slow Pointer:** Used in linked list or array problems, this pattern is ideal for detecting cycles or finding a midpoint.


**4.Merge Intervals:** Use this pattern to deal with overlapping intervals, helping to create a more organized and efficient structure.


**5.Cyclic Sort:** Employed when you need to sort numbers within a defined range, it provides a neat way to ensure ordered data.


**6.In-place Reversal of a Linked List:** If you need to reverse a linked list in-place, this is the pattern to use.


**7.Tree Breadth First Search:** Perfect for traversing a tree level-by-level, providing a comprehensive overview of all nodes.


**8.Tree Depth First Search:** This pattern allows you to traverse a tree or graph using depth as the main factor.


**9.Two Heaps:** Ideal when dealing with situations that require access to both the smallest and largest elements simultaneously.


**10.Subset Pattern (Backtracking):** Useful in solving problems related to permutations and combinations.


**11.Modified Binary Search:** An adaptation of the binary search for situations where a standard binary search doesn't apply.


**12.Top 'K' Elements:** This pattern is beneficial for problems that require identifying the top or bottom 'k' elements in a set.


**13.K-way Merge:** Employ this pattern to merge K sorted lists or arrays efficiently.


**14.0/1 Knapsack (Dynamic Programming):** This dynamic programming pattern is often used for optimization problems.


**15.Topological Sort (Graph):** Useful in finding a linear ordering of vertices in a directed acyclic graph (DAG).


**16.Floyd's Cycle Detection Algorithm:** Ideal for finding cycles in data structures such as linked lists or arrays.


**17.Kadane’s Algorithm (Dynamic Programming):** It's an optimal solution for the maximum subarray problem.


**18.Longest Common Subsequence/ Substring (Dynamic Programming):** This pattern is handy when finding the longest common subsequence or substring in two strings or arrays.


**19.Union Find (Disjoint Set):** A data structure used to maintain disjointed sets and is useful for network connectivity problems.


**20.Trie (Prefix Tree):** Ideal for efficient retrieval of keys in a dataset of strings. It's commonly used for features like autocomplete or spell check.