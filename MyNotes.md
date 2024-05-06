# In Python

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