# Reverse a positive integer

- Given n is a positive integer i.e <span>n ∈ ℤ<sup>+</sup></span> return its reverse integer

```
def reverse(n):
    ans = 0
    while n!=0:
        r = n%10
        y = y*10+r
        n = n//10
    return ans
```