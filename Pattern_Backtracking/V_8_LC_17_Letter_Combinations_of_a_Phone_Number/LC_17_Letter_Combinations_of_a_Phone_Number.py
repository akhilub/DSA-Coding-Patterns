#Approach : Backtracking or Recursion or DFS
#TC:O(n4^n)
#SC:O(4^n)

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        
        digitsToLetter = ['','','abc','def','ghi','jkl','mno','pqrs','tuv','wxyz']
        
        ans = []
        def dfs(i:int , path:List[str]): # i - no of character in each string
            
            if i ==len(digits):
                ans.append(''.join(path))
                return
            
            for ch in digitsToLetter[ord(digits[i])- ord('0')]:
                dfs(i+1,path+[ch])
                    
        dfs(0,[])
        return ans 
            
            
            
            
            












































#Using HashTable
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        
        digitsToChar = {'2':'abc','3':'def','4':'ghi','5':'jkl','6':'mno','7':'pqrs','8':'tuv','9':'wxyz'}
        
        ans = []
        def dfs(s:int , path:List[str]):            # s - start index
            
            if s ==len(digits):
                ans.append(''.join(path))
                return
            
            for ch in digitsToChar[digits[s]]:
                dfs(s+1,path+[ch])
                    
        dfs(0,[])
        return ans 



            
            
        