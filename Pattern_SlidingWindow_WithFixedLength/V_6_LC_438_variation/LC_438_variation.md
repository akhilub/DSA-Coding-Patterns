# Problem Statement

## Given two strings s0 and s1, return the number of substrings where s1 contains any anagram of s0.

**Constraints**
- n ≤ 100,000 where n is the length of s0
- m ≤ 100,000 where m is the length of s1

**Example 1**
```
Input
s0 = “abc”
s1 = “bcabxabc”
Output
3
Explanation
The substrings “bca”, “cab” and “abc” of s0 are permutations of “abc”.
```

**Hints**:
Sliding window, what could change between each successive window?