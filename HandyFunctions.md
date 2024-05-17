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
