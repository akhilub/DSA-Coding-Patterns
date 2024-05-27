
matrix = [[1,2,3],[4,5,6],[7,8,9]]

list(zip(*matrix[::-1]))


In Python 3 zip() returns an iterator, so we need to enclose the whole thing in list() to get an actual list back out, so as of 2020 it's actually:

```
list(zip(*matrix[::-1]))
```

Here's the breakdown:

**[::-1]** - makes a shallow copy of the original list in reverse order. Could also use reversed() which would produce a reverse iterator over the list rather than actually copying the list (more memory efficient).

"*" - makes each sublist in the original list a separate argument to zip() (i.e., unpacks the list)

**zip()** - takes one item from each argument and makes a list (well, a tuple) from those, and repeats until all the sublists are exhausted. This is where the transposition actually happens.
list() converts the output of zip() to a list.

So we have this:
```
[ [1, 2, 3],
  [4, 5, 6],
  [7, 8, 9] ]
```
We first get this (shallow, reversed copy):

```
[ [7, 8, 9],
  [4, 5, 6],
  [1, 2, 3] ]
```
Next each of the sublists is passed as an argument to zip:

```
zip([7, 8, 9], [4, 5, 6], [1, 2, 3])
```

zip() repeatedly consumes one item from the beginning of each of its arguments and makes a tuple from it, until there are no more items, resulting in (after it's converted to a list):

```
[(7, 4, 1), 
 (8, 5, 2), 
 (9, 6, 3)]
```