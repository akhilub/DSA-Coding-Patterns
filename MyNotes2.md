
## How to sort a hashmap/dictionary in python based on value?

```
arr = [3,1,2]

x ={ 0:3 , 1:1, 2:2 }   # {idx:ele}

sort_x = sorted(x.items(), key = lambda item:item[1],reverse=False)

>>> [(1, 1), (2, 2), (0, 3)]
```

- **Reference :**   https://stackoverflow.com/questions/613183/how-do-i-sort-a-dictionary-by-value




- **[Python List extend()](https://www.programiz.com/python-programming/methods/list/extend)**
```
The extend() method takes a single argument.
    • iterable - such as list, tuple, string, or dictionary
The extend() doesn't return anything; it modifies the original list.
```



- **[left shift](https://processing.org/reference/leftshift.html)**

Memonic (<< resembles to L)
```
>>> 1 << 3       # 1 << 3 = 1*(2^3)
8

>>> 2 << 3       # 2 << 3 = 2*(2^3) = 2*(8) =16
16
```


- **[right shift](https://processing.org/reference/rightshift.html)**


Memonic (>> resembles to R)
```
>>> 8 >> 3     # 8 >> 3 =8 //(2^3) = 1
1

>>> 256 >> 6   # 256 // 2^6 = 256//64 = 4
4
```


### Python Operators

- **[Operators](https://www.w3schools.com/python/python_operators.asp)**
  

- '/' is the division operator
- '//' is the quotient operator aka floor division
- '%' is the remainder operator aka modulus 

```
>>> 5/2
2.5
>>> 5/3
1.6666666666666667
```

```
>>> 5//2
2
>>> 5//3
1
>>> 
```

```
>>> 5%3
2
```

#### **[divmod()](https://www.toppr.com/guides/python-guide/references/methods-and-functions/methods/built-in/divmod/python-divmod/)**
- using the in-built python divmod function, you can find the remainder and the quotient of any two numbers given as the input. 


```
>>> divmod(5,2)
(2, 1)
 
>>> divmod(5,3)
(1, 2)
```


#### pairwise

```
>>> from itertools import pairwise
>>> a = ['a','b','c']
>>> pairwise(a)
<itertools.pairwise object at 0x108458730>
>>> list(pairwise(a))
[('a', 'b'), ('b', 'c')]

# same as pairwise()
>>> zip(a, a[1:])
[('a', 'b'), ('b', 'c')]
```