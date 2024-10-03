# Problem Statement

Given a string, find the minimum number of characters that we can remove to make it a palindrome.

OR

Given a string, Find minimum number of deletions required to convert a string into a palindrome.

Example 1:
```
Input: "abdbca"
Output: 1
Explanation: By removing "c", we get a palindrome "abdba".
```

Example 2:
```
Input: = "cddpd"
Output: 2
Explanation: Deleting "cp", we get a palindrome "ddd".
```

Example 3:
```
Input: = "pqr"
Output: 2
Explanation: We have to remove any two characters to get a palindrome, e.g. if we 
remove "pq", we get palindrome "r".
```

**Constraints:**

- 1 <= st.length <= 1000
- st consists only of lowercase English letters.
