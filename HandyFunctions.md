# Get digits of a positive Integer

- Given n is a positive integer i.e <span>n ∈ ℤ<sup>+</sup></span> return its digits in order and reverse order simultaneously

```
def getDigits(n):
    lst = []  # Define the list inside the function
    while n > 0:
        r = n % 10
        lst.append(r)
        n = n // 10
    return lst

print(getDigits(123))  #[3,2,1]
```
OR 

```
getDigits = lambda n: list(map(int, str(n)))

print(getDigits(12345))  #[5, 4, 3, 2, 1]

Explanation
str(n): Converts the number to its string representation, allowing us to iterate over each digit.
map(int, ...): Converts each character back to an integer.
list(...): Converts the map object to a list.
```

- To get the digits of a positive integer
```
def getDigits(n):
    lst = []
    while n > 0:
        r = n % 10
        lst.append(r)
        n = n // 10
    return lst[::-1]  # Reverse the list before returning

print(getDigits(123))  #[1,2,3]
```
OR

```
getDigits = lambda n: list(map(int, str(n)))[::-1]
```

print(getDigits(12345))  # Expected: [1, 2, 3, 4, 5]


# Factorial


# Reverse a positive integer

- Given n is a positive integer i.e <span>n ∈ ℤ<sup>+</sup></span> return its reverse integer

```
def reverse(n):
    ans = 0
    while n!=0:
        r = n%10
        ans= ans*10 + r
        n = n//10
    return ans
```
OR
```
reverse = lambda n: int(str(n)[::-1])
```


# Reverse a String

- Given a string s reverse it in place,.
  I:s = 'Hello World'   O:'dlroW olleH'

```
def reverseString(s:str):
    chars = list(s)         #list of characters
    l , r = 0 , len(chars)-1
    while l < r:
        chars[l] ,chars[r] = chars[r] , chars[l]
        l+=1
        r-=1
    return ''.join(chars)
```
- Strings are immutable in python
OR
```
def reverseString(s:str):
    return s[::-1]
```
OR
reverseString = lambda s:s[::-1]


# Reverse words in a sentence

- Given a 




# Reverse a List/Array

```
def reverseList(arr:List):
    l,r = 0,len(arr)-1
    while l<r:
        arr[l],arr[r]=arr[r],arr[l]
        l+=1
        r-=1
    return arr
```
OR 
```
def reverseList(arr:List):
    return arr[::-1]
```
or
```
reverseList = lambda arr: arr[::-1]
```
OR
```
def reverseList(arr:List):
    n = len(arr)
    for i in range(n//2):       #<------- Note we need to traverse till the middle (n//2) because we can swap elements around it , 
      arr[i],arr[n-1-i] = arr[n-1-i],arr[i]        #do not got till n otherwise we will swap them back 
    return arr
```

# Transpose of Matrix/Grid

- Given an m x n 2D matrix where m ≠ n , return its transpose 

```
def transpose(grid:List[List[int]]):
    m , n = len(grid),len(grid[0])
    T = [[0]*m for _ in range(n)]
    for i in range(m):
        for j in range(n):
            T[j][i] = matrix[i][j]

    return T
```
OR
```
def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
    return list(zip(*matrix))
```
OR 
```
transpose = lambda matrix:list(zip(*matrix))
```

### Given an m x m 2D matrix , modify the input 2D matrix directly in-place to find its transpose

```
def transposeInPlace(grid:List[List[int]]):
      m = len(grid)
      for r in range(m):
          for c in range(r):  #<------- Note we need to traverse till the diagonal of each row (r) because we can swap elements around the diagonal in one pass ,    
              grid[r][c] , grid[c][r] = grid[c][r], grid[r][c]
```
      
# Rotate an image 

```
def rotated(array_2d):
    list_of_tuples = zip(*array_2d[::-1])
    return [list(row) for row in list_of_tuples]
    # return map(list, list_of_tuples)
```
OR
```
def rotateImage(matrix):
    rotated = [list(tupleRow) for tupleRow in zip(*matrix[::-1])]
    return rotated
```






# Function To Check if all character are unique in a string:

```
def checkUniqueCharacter(s:str):
    len(s) == len(set(s))

TC:O(N)
```


# Function to Check if a number is even or odd

- Given n is a positive integer i.e <span>n ∈ ℤ<sup>+</sup></span> return whether it is odd or even

- Using Bitwise AND operator (&)

If we observe the binary representation of a number we will know that the rightmost bit of every odd number is 1 for even numbers it is 0. Bitwise AND (&) operator gives 1 only for (1&1) otherwise it gives 0. So, knowing this we are going to evaluate the bitwise AND of a number with 1 and if the result is 1 number is odd, and if it is 0 number is even

```
def isEvenOdd(n):
 
  # if n&1 == 0, then num is even
  if n & 1:
    return 'odd'
  # if n&1 == 1, then num is odd
  else:
    return 'even'

```

- Using Modulus Operator (%)

The % sign is like division only it checks for the remainder, so if the number divided by 2 has a remainder of 0 it's even otherwise odd.

Or reverse them for a little speed improvement, since any number above 0 is also considered "True" you can skip needing to do any equality check:

```
def isEvenOdd(n):
 
  # if n%2 == 0, then num is even
  if n%2:
    return False
  # if n%2 == 1, then num is odd
  else:
    return True

```

# Sort an Array
- Using Sorting Algorithm





# Merge Two Sorted Array Using Two Pointer 

Given two sorted arrays/lists, if we want to merge it, we can do this optimally using two pointers in O(N+M) where N and M are the sizes of the two sorted array/list respectively.

Algorithm: We can use two pointers to point to the current smallest element, then compare both, move forward the smaller one. Continue until both points reach the their end.

```
I : a = [1,3,4,5,7,9] , b = [2,4,6,8]
O: [1,2,3,4,4,5,6,7,8,9]


def mergeTwoSortedArray(a:List[int],b:List[int]):
    i , j , la , lb = 0 , 0 ,len(a), len(b)
    res = []
    while i<la and j<lb:
      if a[i]<b[j]:
        res+=[a[i]]
        i+=1
      else:
        res+=[b[j]]
        j+=1
    while i<la:
        res+=[a[i]]
        i+=1
    while j<lb:
        res+=[b[j]]
        j+=1
    return res

```

# MergeSort 

- Based on this we can recursive apply merging sorting algorithm to a list. We continuously divide the list into equal two parts. When the partition size is small enough (one element or none), we know it is by natural sorted. Then we start merge these small partitions into bigger partitions until we get the entire list sorted.

```
def sortArray(nums: List[int]) -> List[int]:
    if len(nums) <= 1:
        return nums
    n = len(nums)
    mid  = n//2
    first = sortArray(nums[:mid])
    second = sortArray(nums[mid:])
    return mergeTwoSortedArray(first,second)
```

# Check if a string is Palindrome
```
def isPalindrome(s:str):
    l , r = 0 ,len(s)
    while l<r:
        if s[l]!=s[r]:return False
        l+=1
        r-=1
    return True

print(isPalindrome('racecar'))  #True
print(isPalindrome('Akhil')) #False
```
OR
```
def isPalindrome(s:str):
    return s==s[::-1]
```
OR
```
isPalindrome = lambda s:s==s[::-1]
```

# Reverse a Graph (Adjacency List)

```
def reverseGraph(graph:List[List[int]]):
    n = len(graph)                      #no of vertices
    rev = [[] for _ in range(n)]        #create the graph with just vertices

    for u , v in enumerate(graph):      
        for k in v:                     # iterate over each edge
            res[k].append(u)            # add reversed edge

    return rev
```

# To Convert the graph input into an equivalent adjacency list before using the templates.

There is a bi-directional graph with n vertices, where each vertex is labeled from 0 to n - 1 (inclusive). The edges in the graph are represented as a 2D integer array edges, where each edges[i] = [ui, vi] denotes a bi-directional edge between vertex ui and vertex vi. Every vertex pair is connected by at most one edge, and no vertex has an edge to itself.

```
edges = [[0,1],[1,2],[2,0]]

def convertGraphInput(edges: List[List[int]]):
    #Convert input to equivalent adjacency list
    G = defaultdict(list(int))
    for s,e in edges:
        G[s].append(e)
        G[e].append(s)
    return G

//G is now defaultdict(list[int], {0: [1, 2], 1: [0, 2], 2: [1, 0]}) 
```

## Convert Graph Adjacency Matrix input to Adjacency List output

- I prefer way 2
<table>

<tr>
<th>Way 1</th>
<th>Way 2</th>
</tr>

<tr>
<td>
<pre>
def adj_list(grid):
    G={}
    for i in range(len(grid)):
        neighbors = []
        for j in range(len(grid[i])):
            if grid[i][j]==1 and i!=j: #Exclude self loop           
                neighbors.append(j)
        G[i] = neighbors
    return G

grid = [[1,1,0],[1,1,0],[0,0,1]] //adjacency matrix
G = adj_list(grid)

print(G) //G is now {0: [1], 1: [0], 2: []}
</pre>
</td>


<td>
<pre>
def adj_list(grid):
    G=defaultdict(list)
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j]==1 and i!=j: #Exclude self loop           
                G[i].append(j)
    return G

grid = [[1,1,0],[1,1,0],[0,0,1]] //adjacency matrix
G = adj_list(grid)

print(G) // G is now defaultdict(<class 'list'>, {0: [1], 1: [0]})
</pre>
</td>


</tr>
</table>




# Merge K Sorted Arrays/Lists
```
def mergeKSortedArrays(self, lists: List[List[int]]) -> List[int]:
    pq= [] 
    # Initialize the priority queue with the first element of each sorted list
    for i, arr in enumerate(lists):
        if arr: # Check if the list is not empty
            pq.append((arr[0], i , 0))
    heapify(pq)
    
    merged_list = []
    
    while pq:
        # Extract the smallest element from the heap
        s_val, li, ei = heappop(pq)
        merged_list.append(s_val)
        
        # If there is a next element in the same list, add it to the heap
        n_ei = ei + 1
        if n_ei < len(lists[li]):
            next_val = lists[li][n_ei]
            heappush(pq, (next_val, li, n_ei))
    
    return merged_list
```
OR
**Note**:The heapq.merge function expects the input to be iterables, such as lists or generators. However, ListNode objects are not directly iterable,
```
def mergeKSortedArrays(self, lists: List[List[int]]) -> List[int]:
    return list(heapq.merge(*lists))
```