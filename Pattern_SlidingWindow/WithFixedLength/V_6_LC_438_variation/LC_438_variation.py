#Anagram Substrings via Sliding Window Algorithm
'''
We are looking for a fixed-size substring in s1 so that we can use a sliding window and update the Counter. 
When we shift the sliding window by one, the left-most character is removed from the window, and the next character is added.

The time complexity is O(NM) where N is the length of s1 and M is the length of s0. The space complexity is O(M) for keeping the sliding window.
'''


class Solution:
    def countAnagramSubstrings(self, s0, s1):
        ans = 0
        n0 = R = len(s0)
        n1 = len(s1)
        cnt0 =Counter(s0)
        cur = Counter(s1[:n0])
        if cnt0 == cur:
            ans+=1
        
        while R<n1:
            cur[s1[R]]+=1
            cur[s1[R-n0]]-=1
            if cur[s1[R-n0]]==0:
                del cur[s1[R-n0]]
            if cnt0 == cur:
                ans+=1
            R+=1
        return ans