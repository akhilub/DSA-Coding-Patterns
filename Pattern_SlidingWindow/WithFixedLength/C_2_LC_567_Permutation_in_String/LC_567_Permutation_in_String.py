#Approach:Sliding Window Technique:Fixed_Size , Using Two Pointers
#TC : O(|s1|+|s2|)
#SC:  O(128) = O(1)

'''
1.Check if s1 is longer than s2: 
If s1 is longer, it cannot be a permutation of any substring in s2.

2.Create character count dictionaries: 
Use Counter to create dictionaries for both strings, counting the occurrences of each character in s1 and the first len(s1) characters of s2.

3.Slide the window: 
Iterate through s2, maintaining a window of size len(s1).

4.Compare counts: 
At each position, check if the character counts in the window match the counts in s1. If they match, you've found a permutation.

5.Update counts:
Add the new character entering the window to the count and remove the character leaving the window.
'''

from collections import Counter
class Solution:
    def checkInclusion(self,s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        n1, n2 = len(s1),len(s2)
        
        cnt1 = Counter(s1)
        cnt2 = Counter(s2[:n1])

        for i in range(n1, n2):
            if cnt1 == cnt2:
                return True
            
            cnt2[s2[i]] += 1
            cnt2[s2[i - n1]] -= 1
            
            if cnt2[s2[i - n1]] == 0:
                del cnt2[s2[i - n1]]

        return cnt1 == cnt2
    
    
    



#Another Way of Writing Sliding Window (I prefer this)
#Optimised,No need to worry About delettin the character for hashmap of s2

from collections import Counter
class Solution:
    def checkInclusion(self,s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        n1 , n2 = len(s1),len(s2)
        cnt1 = Counter(s1)
        cnt2 = Counter(s2[:n1])
        
        if cnt1 ==cnt2:
            return True
        
        for i in range(n1,n2):
            cnt2[s2[i]]+=1
            cnt2[s2[i-n1]]-=1
            
            if cnt1 ==cnt2:
                return True
        return False
            