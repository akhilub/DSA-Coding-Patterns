
## How to sort a hashmap/dictionary in python based on value?

```
arr = [3,1,2]

x ={ 0:3 , 1:1, 2:2 }   # {idx:ele}

sort_x = sorted(x.items(), key = lambda item:item[1],reverse=False)

>>> [(1, 1), (2, 2), (0, 3)]
```

- **Reference :**   https://stackoverflow.com/questions/613183/how-do-i-sort-a-dictionary-by-value