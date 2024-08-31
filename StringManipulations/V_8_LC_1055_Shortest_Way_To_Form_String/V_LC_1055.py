#Meta(Lucas) asked me on 29 Aug 2024

'''
Given Two Strings src and tgt.
Return minimum no of src strings required to make the tgt strings
'''

from math import *
from collections import Counter
class Solution:
    def shortestWay(self, source: str, target: str) -> int:
        cnt_src = Counter(source)
        cnt_tgt = Counter(target)
        
        print(cnt_src,cnt_tgt)
        ans = 0 # count how many of src are required to make tgt
        for ch,fq in cnt_tgt.items():
            if ch in cnt_src.keys():
                curr_letter_cnt = ceil(fq/cnt_src[ch])
                ans = max(ans,curr_letter_cnt)      #max letter count
        return ans
    
#TC:O(N)
#SC:O(N) 
#where N is size of max hashmap (cnt_src,cnt_tgt)
                
if __name__=="__main__":
    source = "facebook" 
    target = "foo"
    expected_output = 1
    
    actual_output = Solution().shortestWay(source,target)
    print('Test Case1',actual_output)
    
    source = "facebook"
    target = "fee"
    expected_output = 2
    
    actual_output = Solution().shortestWay(source,target)
    print('Test Case2',actual_output)