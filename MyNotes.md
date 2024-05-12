- In DSA for FAAANG Always learn the best algorithmic solution for a coding problem

# In Python


## Python Data Structure

[] is a list, and is mutable, in that its size can vary.

() is a tuple. Tuples are immutable, in that their sizes cannot vary. Immutable objects can be hashed, which is an important property. You can concatenate tuples, but it returns a new tuple, not the same one. Extending / appending to a list returns the same list object.

{} is a set, in that it contains unique, immutable objects. {} is also used to create a dictionary, where the dictionary has a set of keys.



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