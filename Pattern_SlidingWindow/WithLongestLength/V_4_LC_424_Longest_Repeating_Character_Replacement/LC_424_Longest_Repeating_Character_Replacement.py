#Approach:HashTable+SlidingWindow

#TC:O(n)
#SC:O(1)


from collections import Counter
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        ans = 0 
        count = Counter() #window, a hashtable to store the frequencies of characters like this {A:1,B:1,....}
        maxCount = 0      # to store the frequncy of maximum character count
        l = 0
        for r in range(len(s)):
            count[s[r]]+=1                    #expand the window i.e add the count of incoming character in window
            maxCount = max(maxCount,count[s[r]]) 
                                            
            while (r-l+1) - maxCount > k:     #window condition broken or invalid window condition , when length of window (r-l+1) minus maxCharacterCount becomes more than the k (the character can be replaced)
                                              #meaning we can only expand the window until we consume the provided characters count
                count[s[l]]-=1                #shrink the window 
                l+=1                          #slide the window
        
            ans = max(ans,r-l+1)

        return ans 