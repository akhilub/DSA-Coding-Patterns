# LONGEST SUBSTRING WITH CHARACTER COUNT OF AT LEAST K VIA BRUTEFORCE ALGORITHM
# We can bruteforce each substrings in O(N^2) time and then check each substring to see if it satisfies the requirement: i.e 
# each character appears at least K times O(N) time. The overall time complexity is O(N^3) and the space complexity is O(N) as we are using a Counter object.


class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        n = len(s)
        for l in range(n):
            for r in range(l,n):
                x = s[l:r+1]
                c = Counter(x)
                if min(c.values())>=k:
                    ans = max(ans,r-l+1)

        return ans


# LONGEST SUBSTRING WITH CHARACTER COUNT OF AT LEAST K VIA DIVIDE AND CONQUER ALGORITHM
# If a character appears less than K times, then it must not be included in the longest satisified substring. 
# Thus, we can use the invalid character to split the string into several groups and recursively conquer it. The longest substring each character appears at least K times should then be from group of strings split by the invalid character.

class Solution:
    def longestSubstring(self, s, k):
        cnt = Counter(s)
        for ch, count in cnt.items():
            if count < k:
                return max(self.longestSubstring(x, k) for x in s.split(ch))
        return len(s) # If no character with a count less than k is found, return the length of the string

# The time complexity is O(N). The space complexity is O(N) from the Counter and the stack.