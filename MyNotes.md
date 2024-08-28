- In DSA for FAAANG Always learn the best algorithmic solution for a coding problem

# In Python


## Python Data Structure

[] is a list, and is mutable, in that its size can vary.

() is a tuple. Tuples are immutable, in that their sizes cannot vary. Immutable objects can be hashed, which is an important property. You can concatenate tuples, but it returns a new tuple, not the same one. Extending / appending to a list returns the same list object.

{} is a set, in that it contains unique, immutable objects. {} is also used to create a dictionary, where the dictionary has a set of keys.


#### There are four collection data types in the Python programming language:

- List is a collection which is ordered and changeable. Allows duplicate members.
- Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
- Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
- Dictionary is a collection which is ordered** and changeable. No duplicate members.



## To split a string into a list of characters?

```
"foobar"    →    ['f', 'o', 'o', 'b', 'a', 'r']
```

Using list Constructor
```
>>> list("foobar")
['f', 'o', 'o', 'b', 'a', 'r']
```

Using List Comprehension
```
>>> str = 'foobar'
>>> [ch for ch in str]
['f', 'o', 'o', 'b', 'a', 'r']
```
- Syntax of lambda function

```
lambda arguments : expression

```

- Syntax of map() with lambda function


```
map(lambda item: item[] expression, iterable)

```

- it returns the manipulated item within a map object


```
Input : C = 'ABA' 
Output: 'BAB'
```
```
>>> C = 'ABA'
>>> map(lambda ch: "B" if ch =="A" else "A", C)
<map object at 0x102d9eac0>
>>>list(map(lambda ch: "B" if ch =="A" else "A", C))
['B', 'A', 'B']
>>>''.join(['B', 'A', 'B'])
'BAB'
```



## String manipulation?

- To convert string into uppercase,lowercase 
```
>>> string = "A man, a plan, a canal: Panama"
>>> string.upper()
'A MAN, A PLAN, A CANAL: PANAMA'
>>> string.lower()
'a man, a plan, a canal: panama'
```

- To remove all non alphanumeric characters from the string
```
>>>string = "A man, a plan, a canal: Panama"
>>>import re
>>>re.sub(r'[^a-zA-Z0-9]','',string)
'AmanaplanacanalPanama'
```


# Counter()

- count of missing values is 0
```
>>>c = Counter(['eggs', 'ham'])
>>>c['bacon']                              # count of a missing element is zero
0
```

- 


# To get Quotient & Remainder in Python 

```
divmod(dividend,divisor)
>>> divmod(17,3)
(5, 2)
```

- using the floor Division operator '//’ one can derive the quotient
```
q = dividend//divisor
>>> 17//3
5
```

- using the modulus operator '%' one can derive the remainder
```
r = dividend % divisor
>>>17%3
2
```


# To reverse a string 

### Using Slicing
Slice notation takes the form [start:stop:step]. In this case, we omit the start and stop positions since we want the whole string. We also use step = -1, which means, "repeatedly step from right to left by 1 character".

- Faster Way
```
>>> s = 'hello world'
>>>s[::-1]
'dlrow olleh'
```
### Using str.join
- Readable
```
>>> s = 'hello world'
>>> ''.join(reversed(s))
'dlrow olleh'
```


### zip_longest()

```
Syntax:

zip_longest( iterable1, iterable2, fillval)

```

```
>>>from itertools import zip_longest
>>> word1 = "ab"
>>> word2 = "pqrs"
>>> print(*(zip_longest(word1,word2,fillvalue = "")))
('a', 'p') ('b', 'q') ('', 'r') ('', 's')
```





# Break Statement in Python

- break statement terminates the loop containing it.

```
>>> for num in range(0,10):
...     if num == 5:
...             break
...     print(f'Iteration: {num}')
... 
Iteration: 0
Iteration: 1
Iteration: 2
Iteration: 3
Iteration: 4
>>> 
```

# Continue Statement in Python

- continue statement is used to skip the remaining code inside a loop for the current iteration only.

```
>>> for num in range(0,10):
...     if num == 5:
...             continue
...     print(f'Iteration: {num}')
... 
Iteration: 0
Iteration: 1
Iteration: 2
Iteration: 3
Iteration: 4
Iteration: 6
Iteration: 7
Iteration: 8
Iteration: 9
>>> 
```

# Python  bisect_right(list, element)

Syntax

```
import bisect
bisect.bisect_right(list, element)
```

Parameters
- list: Contains a list of sorted integers.
- element: Provides an element that needs to be inserted into the sorted list.

Return value
- The bisect_right() method is provided by the bisect module, which returns the **right-most index to insert the given element while maintaining the sorted order**.

Example

```
#import the module
>>>import bisect
>>>bisect.bisect_right([1,3,5,7,10,25,49,55],25)
6
```


# Python bisect_left(list,element)

The syntax of the bisect_left() function is given below:

Syntax


```
import bisect
bisect.bisect_left(list, element, lo=0, hi=len(list), key=None)

```

Parameters
- list: This contains a list of sorted integers.
- element: This provides an element that needs to be inserted into the sorted list.
- lo (Optional): Default is 0. It defines the starting position within the list for the search.
- hi (Optional): Default is len(list). It defines the ending position within the list for the search.
- key (Optional): If the key parameter is None, the elements are compared directly without invoking any key function.



Return value
- The bisect_left() method is provided by the bisect module, which returns the **left-most index to insert the given element**, while maintaining the sorted order.

Example

```
#import the module
>>>import bisect
>>>bisect.bisect_left([1,3,5,7,10,25,49,55],25)
5
```



```
#import the module
import bisect

#given sorted list of numbers
nums = [1,3,5,7,10,25,49,55]

#given element to be inserted into the list
ele = 50

#get index where to insert the element
idx = bisect.bisect_left(nums, ele, lo=4, hi=len(nums))

#print the index
print(f"Insert element {ele} at index {idx} in nums list to maintain sorted order.")
```






# Python sorted() vs sort()


```
sorted() returns a new sorted list, leaving the original list unaffected. list.sort() sorts the list in-place, mutating the list indices, and returns None (like all in-place operations).

sorted() works on any iterable, not just lists. Strings, tuples, dictionaries (you'll get the keys), generators, etc., returning a list containing all elements, sorted.

Use list.sort() when you want to mutate the list, sorted() when you want a new sorted object back. Use sorted() when you want to sort something that is an iterable, not a list yet.

For lists, list.sort() is faster than sorted() because it doesn't have to create a copy. For any other iterable, you have no choice.

No, you cannot retrieve the original positions. Once you called list.sort() the original order is gone.

```



# Python String join()

- The string `join()` method returns a string by joining all the elements of an iterable (list, string, tuple), separated by the given separator.

Syntax
```
string.join(iterable)
```

### Example
```
# .join() with lists
numList = ['1', '2', '3', '4']
separator = ', '
print(separator.join(numList))
# 1, 2, 3, 4


# .join() with tuples
numTuple = ('1', '2', '3', '4')
separator = ', '
print(separator.join(numTuple))
#1, 2, 3, 4



>>> s1 = 'abc'
>>> s2 = '123'
>>> print('s1.join(s2):', s1.join(s2))
s1.join(s2): 1abc2abc3

# each element of s2 is separated by s1
# '1'+ 'abc'+ '2'+ 'abc'+ '3'


>>> print('s2.join(s1):', s2.join(s1))
s2.join(s1): a123b123c

# each element of s1 is separated by s2
# 'a'+ '123'+ 'b'+ '123'+ 'b'

```


## Python Bitwise Right-Shift >> Operator

The Python bitwise right-shift operator x >> n shifts the binary representation of integer x by n positions to the right. It inserts a 0 bit on the left and removes the right-most bit. For example, if you right-shift the binary representation 0101 by one position, you’d obtain 0010. Semantically, the bitwise right-shift operator is the same as performing integer division by 2**n.

Here’s a minimal example:

```
print(8 >> 1)
# 4
print(8 >> 2)
# 2
print(-3 >> 1)
# -2
```
## Mutable and Immutable objects in Python


Mutable Objects	    Immutable Objects
Lists	                Numbers
Dictionaries	        Strings
Sets	                Tuples


## Python list Shallow Copy vs Deep Copy

Shallow Copy: Copies the list, but not the objects inside the list. If the list contains mutable objects, changes to those objects will be reflected in both the original and the copied list.



1) arr[:]
- This creates a shallow copy of the entire list.
- It's a slicing operation where the start and end indices are not specified, which defaults to copying the entire list.


```
>>>arr = [1, 2, 3, 4, 5]
>>>copy_arr = arr[:]
>>>copy_arr
[1, 2, 3, 4, 5]
```
Note:Integers are immutable in python


2) arr[::]

- This also creates a shallow copy of the entire list.
- This slicing operation includes the step parameter, which is not specified here, thus defaults to 1, effectively copying the entire list.

```
>>>arr = [1, 2, 3, 4, 5]
>>>copy_arr = arr[::]
>>>copy_arr
[1, 2, 3, 4, 5]
```

3) arr.copy()

- This creates a shallow copy of the entire list using the list's built-in copy method.
- This method is explicit and directly conveys the intention of copying the list.

```
>>>arr = [1, 2, 3, 4, 5]
>>>copy_arr = arr.copy()
>>>copy_arr
[1, 2, 3, 4, 5]
```

All three methods (arr[:], arr[::], arr.copy()) achieve the same result of creating a shallow copy of the list.

Deep Copy: Copies the list and the objects inside it. Changes made to original list will not be reflected upon the copied list

```
>>>import copy
>>>arr = [[1, 2], [3, 4]]
>>>deep_copy_arr = copy.deepcopy(arr)
[[1, 2], [3, 4]]
```



# Truthy & Falsy Value in Python

We use "truthy" and "falsy" to differentiate from the bool values True and False. A "truthy" value will satisfy the check performed by if or while statements. As explained in the documentation, all values are considered "truthy" except for the following, which are "falsy":

```
None
False

- Numbers that are numerically equal to zero, including:

0
0.0
0j
decimal.Decimal(0)
fraction.Fraction(0, 1)

- Empty sequences and collections, including:
[] - an empty list
{} - an empty dict
() - an empty tuple
set() - an empty set
'' - an empty str
b'' - an empty bytes
bytearray(b'') - an empty bytearray
memoryview(b'') - an empty memoryview
an empty range, like range(0)


- objects for which
obj.__bool__() returns False
obj.__len__() returns 0, given that obj.__bool__ is undefined

```



# To Get maximum/minimum values and keys in Python dictionaries

- https://note.nkmk.me/en/python-dict-value-max-min/