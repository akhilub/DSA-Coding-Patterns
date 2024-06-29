## Dutch National Flag 


**Pseudocode**
The following pseudocode for three-way partitioning which assumes zero-based array indexing was proposed by Dijkstra himself.[2] It uses three indices i, j and k, maintaining the invariant that i ≤ j ≤ k.

- Entries from 0 up to (but not including) i are values less than mid,
- entries from i up to (but not including) j are values equal to mid,
- entries from j up to (and including) k are values not yet sorted, and
- entries from k + 1 to the end of the array are values greater than mid.



**procedure** 
```
three-way-partition(A : array of values, mid : value):
    i ← 0
    j ← 0
    k ← size of A - 1
    while j <= k:
        if A[j] < mid:
            swap A[i] and A[j]
            i ← i + 1
            j ← j + 1
        else if A[j] > mid:
            swap A[j] and A[k]
            k ← k - 1
        else:
            j ← j + 1
```



## Binary Search

**procedure**
```
function binary_search(A: array of values, n:last index value, T:target value) is
    L := 0
    R := n − 1
    while L ≤ R do
        m := floor((L + R) / 2)
        if A[m] < T then
            L := m + 1
        else if A[m] > T then
            R := m − 1
        else:
            return m
    return unsuccessful
```

**Hermann Bottenbruch alternative procedure**
- In the above procedure, the algorithm checks whether the middle element (𝑚 {\displaystyle m}) is equal to the target ( 𝑇 {\displaystyle T}) in every iteration. Some implementations leave out this check during each iteration. The algorithm would perform this check only when one element is left (when 𝐿 =𝑅 {\displaystyle L=R}). This results in a faster comparison loop, as one comparison is eliminated per iteration, while it requires only one more iteration on average

```
function binary_search_alternative(A, n, T) is
    L := 0
    R := n − 1
    while L != R do
        m := ceil((L + R) / 2)
        if A[m] > T then
            R := m − 1
        else:
            L := m
    if A[L] = T then
        return L
    return unsuccessful
```

# For Duplicate elements

**Procedure for finding the leftmost element**

```
function binary_search_leftmost(A, n, T):
    L := 0
    R := n
    while L < R:
        m := floor((L + R) / 2)
        if A[m] < T:
            L := m + 1
        else:
            R := m
    return L
```

**Procedure for finding the rightmost element**

```
function binary_search_rightmost(A, n, T):
    L := 0
    R := n
    while L < R:
        m := floor((L + R) / 2)
        if A[m] > T:
            R := m
        else:
            L := m + 1
    return R - 1
```


**Procedure for Merge Sort**

```
function merge_sort(A : array of values ) is
    // Base case. A list of zero or one elements is sorted, by definition.
    if length of A ≤ 1 then
        return A

    // Recursive case. First, divide the list into equal-sized sublists
    // consisting of the first half and second half of the list.
    // This assumes lists start at index 0.
    n := length of A

    mid : = floor(A / 2)
   

    // Recursively sort both sublists.
    left := merge_sort(A[ : mid ])
    right := merge_sort(A[ mid : ])

    // Then merge the now-sorted sublists.
    return merge(left, right)
```




**Procedure for Floyd's Cycle Detection**
- To detect the cycle in a linear Data Structure

floyd(headNode: linear DS):
    tortoise := headNode
    hare := headNode
    foreach:
        if hare == end
            return 'There is No Loop Found.'
        hare := hare.next
        if hare == end
            return 'No Loop Found'
        hare = hare.next
        tortoise = tortoise.next
        if hare == tortoise
            return 'Cycle Detected'


## Divide & Conquer
A divide-and-conquer algorithm recursively breaks down a problem into two or more sub-problems of the same or related type, until these become simple enough to be solved directly. The solutions to the sub-problems are then combined to give a solution to the original problem.