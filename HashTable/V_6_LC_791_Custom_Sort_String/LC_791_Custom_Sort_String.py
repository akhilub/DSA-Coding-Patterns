# Approach:HashTable
# TC:O(∣order∣+∣s∣)
# SC:O(26)


class Solution:
    def customSortString(self, order: str, s: str) -> str:
        cnt= Counter(s)
        ans = []
        for ch in order:
            ans.append(ch*cnt[ch])
            cnt[ch] = 0             #critical step
            
        for ch , fq in cnt.items():
            ans.append(ch*fq)
        
        return ''.join(ans)