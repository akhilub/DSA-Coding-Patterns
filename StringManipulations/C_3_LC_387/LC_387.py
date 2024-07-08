#TC:(O(n))
#SC:(O(n))
class Solution:
    def firstUniqChar(self, s: str) -> int:
        cnt = Counter(s)
        for i, c in enumerate(s):
            if cnt[c] == 1:
                return i
        return -1



#Variation : To find first non-repeating character just update the condition `if cnt[c] != 1:`