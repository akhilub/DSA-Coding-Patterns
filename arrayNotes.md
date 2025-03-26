# Consider an array: {1,2,3,4}

# Subarray: contiguous non-empty sequence of an elements within an array i.e. {1,2},{1,2,3}

# Subsequence: Need not to be contiguous, but maintains order i.e. # {1,2,4}

# Subset: Same as subsequence except it has empty set i.e. # {1,3},{}

# Given an array/sequence of size n, possible

```
Subarray = n*(n+1)/2
Subseqeunce = (2^n) -1 (non-empty subsequences)
Subset = 2^n
```

# Array Operations Time Complexity

```
-----------------------------------------------------------
|    Operations              |      Time Complexity       |
-----------------------------------------------------------
|  Add or Remove Element     |      O(1)  Amortized       |
|  at the end of Array       |                            |
|                            |                            |
|  Add or Remove Element     |          O(n)              |
|  NOT at the end of Array   |                            |
|                            |                            |
|   Access Element at an     |          O(1)              |
|       Index                |                            |
|                            |                            |
|  Searching Array for an    |          O(n)              |
|       Element              |                            |
|                            |                            |
|  Searching Sorted Array    |          O(log(n))         |
|    for an Element          |      Binary Search         |
|                            |                            |
|     Copying  Array         |          O(n)              |
|                            |                            |
|     Sliding Window         |          O(n)              |
|                            |                            |
|     All Pairs of Array     |          O(n^2)            |
|         Elements           |                            |
|                            |                            |
|                            |                            |
|---------------------------------------------------------|

```
