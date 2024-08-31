#Approach : Backtracking or Recursion or DFS
#TC:O(n4^n)
#SC:O(4^n)


# Meta(Lucas) asked me this on 29 Aug 2024 with a slight variation
from typing import List ,Dict
class Solution:
    def letterCombinations(self, digits: str, mapping:Dict) -> List[str]:
        if not digits:
            return []
                
        ans = []
        def dfs(i:int , path:List[str]): # i - no of digit() in digits
            
            if i ==len(digits):
                ans.append(''.join(path))
                return
            
            for ch in mapping[digits[i]]:
                dfs(i+1,path+[ch])
                    
        dfs(0,[])
        return ans 
            
            
if __name__=="__main__":
    
    digits = "23"
    
    mapping = {'2':"abc",'3':"def"}
    
    expected_output = ["ad","ae","af","bd","be","bf","cd","ce","cf"]
    
    actual_output = Solution().letterCombinations(digits,mapping)
    
    print('Test Case1',actual_output)



'''    
mapping = {'2':"abc",'3':"def"}

print(mapping.items()) // return list of tuples(key,value)

// dict_items([('2', 'abc'), ('3', 'def')])
            
print(mapping.keys())  // return list of keys
// dict_keys(['2', '3'])

print(mapping.values()) // return list of values
// dict_values(['abc', 'def'])
'''