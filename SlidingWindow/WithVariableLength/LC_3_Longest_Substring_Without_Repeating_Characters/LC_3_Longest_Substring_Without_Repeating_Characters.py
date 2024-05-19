#Approach 1: Sliding window flexible longest
#We can keep tracking a current window, and use two pointer to apply the sliding window algorithms. We can expand the window to the right greedily as long as the character is not existent in the current window. Otherwise, we need to move the left pointer and erase the corresponding characters at left pointer out of the window until the current character at the right pointer is no longer in the window.

#If we don’t move the left pointer (shrink the window), the substring is not valid no matter how we move the right pointer.

#The time complexity is O(N) as the left and right pointers both move towards the right – and the space complexity is O(N) as we need a hash set to store the elements in the current window.


#) Using Set
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ans = 0
        l = 0
        n = len(s)
        win = set()
        for r in range(n):
            while s[r] in win: #invalid window condition or window condition is broken
                win.remove(s[l]) #remove the outgoing element
                l+=1
            win.add(s[r]) #add the incoming element
            w_len = r-l+1 #current window length
            ans = max(ans,w_len)

        return ans

#) Using Dictionary
import collections
class Solution:
    def lengthOfLongestSubstring(self,s):
        ans = 0
        l = 0
        n = len(s)
        win = collections.Counter() #window , a hastable of characters with their count(values)

        for r in range(n):
            win[s[r]]+=1 #add the count of the incoming element 
            while win[s[r]]>1:    #window condition is broken when the same character repeat i.e count of that element/character becomes greater than 1
                win[s[l]]-=1 # remove outging element from left by decrementing its count by 1 in dictionary(win)
                l+=1
            w_len = r - l +1 
            ans = max(ans,w_len)
        return ans


#Approach 2:Brute Force
#O(N^3)