# Approach :Sliding Window (Two Pointers + HashTable )

'''
To solve this problem, we'll use a sliding window approach with two pointers. 
We'll maintain a dictionary to keep track of the characters we need and their frequencies.

We'll move the right pointer to expand the window until we have all the required characters. 
Then, we'll move the left pointer to shrink the window while maintaining the required characters.

We'll update the minimum window whenever we find a valid window. 
This process continues until we've examined all characters in s.

The time complexity of this solution is O(m + n), where m is the length of s and n is the length of t.
'''


from collections import Counter
import math
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        #Count characters in t
        cnt = Counter(t)
        
        
        #Initialize variables
        l,minL=0,0
        min_len=inf                             #float('inf') or math.inf
        required = len(cnt)                     #required no of characters 
        
        for r in range(len(s)):
            #Expand the window
            if s[r] in cnt:
                cnt[s[r]]-=1
                if cnt[s[r]]==0:
                    required-=1
                    
            #Shrink the window if all characters are found
            while required==0:
                #Update minimum window
                if r-l+1<min_len:
                    min_len = r-l+1
                    minL = l
                    
                #Remove left character from the window
                if s[l] in cnt:
                    cnt[s[l]]+=1
                    if cnt[s[l]]>0:
                        required+=1
                    
                l+=1
        
        #Return the minimum window substring
        return s[minL:minL+min_len] if min_len!=inf else ""