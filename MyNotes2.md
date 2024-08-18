
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