#Approach : Sliding Window Fixed Length
#Stick to this approach, easy to visulize
#TC:O(n)
#SC:O(26)=O(1)

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        ans = []
        l = R = len(p)
        n = len(s)
        cnt_p = Counter(p)
        cnt_s = Counter(s[:l])
        
        if cnt_p==cnt_s:
            ans.append(R-l)
        
        while R<n:
            cnt_s[s[R]]+=1
            cnt_s[s[R-l]]-=1
            if cnt_s[s[R-l]]==0:
                del cnt_s[s[R-l]]
            if cnt_p == cnt_s:
                ans.append(R-l+1)
            R+=1

        return ans
    



















#Approach: Sliding Window

#TC:O(n)
#SC:O(26)
'''
The problem asks us to find all the anagrams of the string p in the string s. In other words, we need to find all the substrings in s that have the same letters as p, but in a different order.

For example, if s = "cbaebabacd" and p = "abc", the solution should be [0, 6], because the substrings "cba" and "bac" in s are anagrams of p.

To solve this problem, we can use a technique called a "sliding window". Here's how it works:

1)Create two arrays (or hash maps) to store the frequency of each letter in p and in the current substring of s that we're considering.
2)Iterate through s, and for each iteration, consider the substring of s that starts from the current index and has a length equal to the length of p.
3)Compare the frequency arrays (or hash maps) of the current substring in s and p. If they are the same, it means that the current substring is an anagram of p.
add the start index of the current substring to the output list.
4)Move the "sliding window" one step to the right by removing the first character of the current substring and adding the next character to the end.
5)Repeat steps 3-5 until we reach the end of s.

By using a sliding window, we only need to update the frequency arrays (or hash maps) when moving the window one step to the right, instead of computing the arrays (or hash maps) from scratch for every substring of s. This makes the solution more efficient.
'''


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        m , n = len(s) , len(p)
        if m<n:
            return ans
        
        ans = []
        cnt1= Counter(p)
        cnt2 = Counter()
        l = 0
        
        for r in range(len(s)):
            cnt2[s[r]]+=1
            
            while cnt2[s[r]]>cnt1[s[r]]:  ## If number of characters `s[r]` is more than our expectation
                cnt2[s[l]]-=1
                l+=1
                
            if r-l+1 ==len(p):
                ans.append(l)
                
        return ans
        
        
        
#Write this in interviews        
#Approach2: Sliding Window

'''
Firstly, we count the number of characters needed in p string.
Then we sliding window in the s string:
Let l control the left index of the window, r control the right index of the window (inclusive).
Iterate r in range [0..n-1].
When we meet a character c = s[r], we decrease the cnt[c] by one by cnt[c]--.
If the cnt[c] < 0, it means our window contains char c with the number more than in p, which is invalid.
So we need to slide left to make sure cnt[c] >= 0.
If r - l + 1 == p.length then we already found a window which is perfect match with string p. WHY? 
Because window has length == p.length and window doesn't contains any characters which is over than the number in p.

'''

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        ans = []
        l = 0
        cnt1 = Counter(p)
        for r in range(len(s)):
            cnt1[s[r]]-=1
            
            while cnt1[s[r]]<0: # If number of characters `c` is more than our expectation
                cnt1[s[l]]+=1   # Slide left until cnt[c] == 0
                l+=1
            
            if r-l+1 ==len(p):
                ans.append(l)
                
        return ans
    
    

    
                
                