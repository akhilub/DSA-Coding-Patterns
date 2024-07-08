The "Top K Elements" coding pattern is a common algorithmic pattern used to find the top or bottom K elements in a collection of elements. It's particularly useful when you need to extract the K largest or smallest elements from an array, a list, or any other data structure.


# Here's a general outline of the Top K Elements pattern:

1. **Priority Queue (Heap):** The most common approach to solve Top K Elements problems involves using a Priority Queue, often implemented as a heap data structure.
Priority Queues allow efficient retrieval of the highest (or lowest) priority element in the collection.

2. **Selecting K Elements:**  Depending on the problem statement, you may need to find the top K elements (K largest) or the bottom K elements (K smallest). The approach remains similar, but the priority queue's ordering may need to be adjusted accordingly.

3. **Iterating Through the Collection:** Start by iterating through the collection of elements. For each element, perform the following steps:
a). If the priority queue contains fewer than K elements, add the current element to the priority queue.

b). If the priority queue already contains K elements, compare the current element with the smallest (or largest) element in the priority queue. If the current element is greater (or smaller, depending
on the requirement), remove the smallest (or largest) element from the priority queue and add the current element.

4. **Finalizing the Result:** After processing all elements, the priority queue will contain the top K elements. Depending on the problem statement, you may need to return these elements in a particular order or format.

