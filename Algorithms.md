##Dutch National Flag 


**Pseudocode**
The following pseudocode for three-way partitioning which assumes zero-based array indexing was proposed by Dijkstra himself.[2] It uses three indices i, j and k, maintaining the invariant that i ≤ j ≤ k.

- Entries from 0 up to (but not including) i are values less than mid,
- entries from i up to (but not including) j are values equal to mid,
- entries from j up to (and including) k are values not yet sorted, and
- entries from k + 1 to the end of the array are values greater than mid.


`procedure` three-way-partition(A : array of values, mid : value):
    i ← 0
    j ← 0
    k ← size of A - 1

    `while` j <= k:
        `if` A[j] < mid:
            `swap` A[i] and A[j]
            i ← i + 1
            j ← j + 1
        `else if` A[j] > mid:
            `swap` A[j] and A[k]
            k ← k - 1
        `else`:
            j ← j + 1

```
__`procedure`__ three-way-partition(A : array of values, mid : value):
    i ← 0
    j ← 0
    k ← size of A - 1

    __`while`__ j <= k:
        __`if`__ A[j] < mid:
            __`swap`__ A[i] and A[j]
            i ← i + 1
            j ← j + 1
        __`else if`__ A[j] > mid:
            swap A[j] and A[k]
            k ← k - 1
        __`else`__:
            j ← j + 1
```