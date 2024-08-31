#Approach: HashMap
#TC:(O(n))
#SC:(O(n))

#Method1 :Using Built-in HashMap

class Solution:
    def firstUniqChar(self, s: str) -> int:
        cnt = Counter(s)
        for i, c in enumerate(s):
            if cnt[c] == 1:
                return i
        return -1


#Method 2 : Creating HashMap/HashTable
class Solution:
    def firstUniqChar(self, s: str) -> int:
        cnt = {}
        for ch in s:
            cnt[ch] = cnt.get(ch,0)+1
            
        for i in range(len(s)):
            if cnt[s[i]]==1:
                return i
            
        return -1
            

#Variation : To find first non-repeating character just update the condition `if cnt[c] != 1:`