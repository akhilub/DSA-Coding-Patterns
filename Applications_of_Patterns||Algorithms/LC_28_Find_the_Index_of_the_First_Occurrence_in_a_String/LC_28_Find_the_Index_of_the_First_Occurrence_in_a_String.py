#Approach1:Traversal
'''
We compare the string needle with each character of the string haystack as the starting point. 
If we find a matching index, we return it directly.

Assuming the length of the string haystack is n and the length of the string needle is m, 
the time complexity is O((n-m)•m), and the space complexity is O(1).
'''
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        n, m = len(haystack), len(needle)
        for i in range(n - m + 1):
            if haystack[i : i + m] == needle:
                return i
        return -1
















#Solution 2:Rabin-Karp String Matching Algorithm
'''
The Rabin-Karp algorithm essentially uses a sliding window combined with a hash function to compare the hashes of fixed-length strings,
which can reduce the time complexity of comparing whether two strings are the same to O(1).


Assuming the length of the string haystack is n and the length of the string needle is m, 
the time complexity is O(n+m), and the space complexity is O(1).
'''



#Solution 3: KMP String Matching Algorithm
'''

Assuming the length of the string haystack is n and the length of the string needle is m, the time complexity is 

O(n+m), and the space complexity is O(m).
'''