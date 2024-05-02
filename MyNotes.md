# In Python

- To split a string into a list of characters?

```
"foobar"    →    ['f', 'o', 'o', 'b', 'a', 'r']
```
Using list Constructor
>>> list("foobar")

Using List Comprehension
>>> str = 'foobar'
>>> [ch for ch in str]

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
Output: C = 'BAB'
```

>>> map(lambda ch: if "B" ch =="A" else "A", C)