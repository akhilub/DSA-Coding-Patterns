## WHAT IS DYNAMIC PROGRAMMING ALGORITHM?

Dynamic Programming aka DP, is a popular technique to optimise the algorithms. The main purpose of DP is avoid re-calculating the intermediate results. For example, if you are given 5 apples, and some minutes later, you are given another one, you know you have 5+1 apples in total without needing to re-count the 5 apples. In computer, we can save the known solutions in a cache i.e. memoization.

There are usually two types of Dynamic Programming: The Top Down and the Bottom-up.

## TOP DOWN DYNAMIC PROGRAMMING ALGORITHM: RECURSION WITH MEMOIZATION
The Top Down DP is usually implemented via Recursion with Memoization. For example, we know the Fibonacci Numbers are calculated via the following Recursion:

1) Recursion
```
def f(n):
  if n == 0 or n == 1:
    return n
  return f(n - 1) + f(n - 2)
```

The recursion is simple to implement, however the time complexity for above is O(2^n) exponential. As the intermediate Fibonacci numbers are calculated over and over again. For example, in the following, the F(2) are calculated multiple times.

```
    f(4)
    / \
  f(3) f(2)
  /\
f(2)f(1)

```
We can easily fix this by bringing a hash table to remember the values that we have calculated:

2) Recusion + Memomization
```
def f(n, nb = {}):
  if n == 0 or n == 1:
    return n
  if n in nb:
    return nb[n]  # return known values
  val = f(n - 1) + f(n - 2)
  nb[n] = val  # remember it
  return val
```

This brings down the time complexity to O(N) – as each Fibonacci number is calculated only once thanks to the cache.

In Python, we can easily cache the function values by using the following Least-Recently-Used Cache aka LRU:

```
@lru_cache(maxsize=None)                            |@cache(maxsize=None) 
def f(n):                                           |def f(n):
  if n == 0 or n == 1:                              |   if n == 0 or n == 1:
    return n                                        |       return n
  return f(n - 1) + f(n - 2)                        |   return f(n - 1) + f(n - 2)
```

The above Fibonacci Number Algorithm via The Top Down DP calculates F(N) in top-down manner: in order to calculate F(N), we need to calculate F(N-1), F(N-2) and so on.

## BOTTOM-UP DYNAMIC PROGRAMMING ALGORITHM
The Bottom-up Dynamic Programming reverses the calculation. Given the same Fibonacci Numbers, we can calculate F(0), F(1) and then F(2) until we reach the value F(N):

3) Bottom-Up No memory DP
```
def f(n):
  f0, f1 = 0, 1
  for _ in range(n):
    f0, f1 = f1, f0 + f1
  return f1
```

We simply use iteration – bottom-up and this results in a O(N) linear Dynamic Programming Algorithm.


4) Bottom Up DP Tabulation
```
def fn(n: int) -> int:
    dp = [0,1]
    for i in range(2,n+1):
        newVal = dp[i-1] + dp[i-2]
        dp.append(newVal)
    return dp[-1]
```

TC: O(N)
SC: O(N)
