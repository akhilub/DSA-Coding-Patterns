#Approach:Sliding Window
#TC:O(N)
#SC:O(N)
from collections import Counter
class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str,k:int) -> int:
        cnt = Counter() # or, cnt = defaultdict(int) # window, a hashtable of characters with their count (values)
        ans = l = 0
        for r in range(len(s)):
            cnt[s[r]] += 1 # add the count of the incoming element
            while len(cnt) > k: # window condition is broken when the number of unique characters exceeds k
                cnt[s[l]] -= 1 # remove outgoing element from left by decrementing its count
                if cnt[s[l]] == 0:   #pitfall notice it is the count of outgoing character not the len(cnt)
                    cnt.pop(s[l]) #or del cnt[s[l]]  # remove character from window if its count becomes 0
                l += 1
            ans = max(ans, r - l + 1)
        return ans


if __name__=="__main__":
    sol =Solution()
    s = "eceba" 
    k = 2
    expectedOutput = 3
    #Explanation: T is "ece" which its length is 3.
    actualOutput = sol.lengthOfLongestSubstringTwoDistinct(s,k)
    print('Test case1 passed',actualOutput==expectedOutput)


