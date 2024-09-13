#Approach 1: Sliding window flexible longest

'''
To solve this problem, we'll use a sliding window approach with a dictionary. We'll keep track of the characters we've seen and their count.

We'll move the right pointer of our window, adding characters to the dictionary. If we find a repeating character, we'll move the left pointer to the right of the last occurrence of that character.

We'll update the maximum length of the substring as we go.

The time complexity of this solution is O(n), where n is the length of the input string.
'''


#) Using Two pointers + Hash Table(Dictionary)
from collections import Counter
class Solution:
    def lengthOfLongestSubstring(self,s):
        ans = 0
        l = 0
        n = len(s)
        cnt = Counter() #window , a hastable of characters with their count(values)

        for r in range(n):
            cnt[s[r]]+=1 #add/increment the count of the incoming element 
            
            while cnt[s[r]]>1:    #window condition is broken when the same character repeat i.e count of that element/character becomes greater than 1
                cnt[s[l]]-=1 # remove outging element from left by decrementing its count by 1 in dictionary(win)
                l+=1
            w_len = r - l + 1 
            ans = max(ans,w_len)
        return ans



#Sliding Window Algorithm
'''
1.We can keep tracking a current window, and use two pointer to apply the sliding window algorithms. 
2.We can expand the window to the right greedily as long as the character is not existent in the current window.
3.Otherwise, we need to move the left pointer and erase the corresponding characters at left pointer out of the window until the current character at the right pointer is no longer in the window.

4.If we don’t move the left pointer (shrink the window), the substring is not valid no matter how we move the right pointer.

•The time complexity is O(N) as the left and right pointers both move towards the right – 
and the space complexity is O(N) as we need a hash set to store the elements in the current window.
'''




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





#Approach 2:Brute Force
#O(N^3)