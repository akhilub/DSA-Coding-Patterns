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

a) Using a HashMap or a Set for O(n) time and O(n) space,
b) Using sorting for O(n log n) time and O(1) space.

2) Every recursive solution can be converted to an iterative solution using a Stack.

3) If we need to try all combinations (or permutations) of the input, we can either use recursive Backtracking or iterative Breadth-First Search


## Data Structures Use Case

- The best data structure that comes to mind to find the smallest number among a set of ‘K’ numbers is a Heap.

- If we need to find some common substring among a set of strings, we will be using a HashMap or a Trie.

- If we need to search/manipulate a bunch of strings, Trie will be the best data structure.

- 


