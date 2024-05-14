# Reverse a positive integer

- Given x is a positive integer i.e <p>x ∈ ℤ<sup>+</sup></p> return its reverse integer

```
def reverse(x):
    y = 0
    while x!=0:
        r = x%10
        y = y*10+r
        x = x//10
    return y
```