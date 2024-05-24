# Reverse a positive integer

- Given n is a positive integer i.e <span>n ∈ ℤ<sup>+</sup></span> return its reverse integer

```
def reverse(n):
    ans = 0
    while n!=0:
        r = n%10
        ans= ans*10+r
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
reverseList = lambda arr: arr[::-1]
OR
def reverseList(arr:List):
    n = len(arr)
    for i in range(n//2):       #<------- Note we need to traverse till the middle (n//2) because we can swap elements around it , 
      arr[i],arr[n-1-i] = arr[n-1-i],arr[i]        #do not got till n otherwise we will swap them back 
    return arr


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


- Given an m x m 2D matrix , modify the input 2D matrix directly in-place to find its transpose

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
    return False
  # if n&1 == 1, then num is odd
  else:
    return True

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

