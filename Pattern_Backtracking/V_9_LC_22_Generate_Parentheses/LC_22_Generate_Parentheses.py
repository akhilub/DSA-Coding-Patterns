#Approach:Recursive 
#Starting from top n==n
#I prefer this, Write this in interviews

class Solution:
    def generateParenthesis(self, n):
        ans = []
        def dfs(l: int, r: int, path: list[str]) -> None:
            if l==0 and r==0:
                ans.append(''.join(path))
            if l>0:
                dfs(l-1,r,path+['('])
            if l<r:
                dfs(l,r-1,path+[')'])
                
        dfs(n,n,[])
        return ans
    

    
    










































    
#Approach:Recursive 
#Starting from bottom n==0

'''
DFS + Pruning
The range of n in the problem is [1,8], so we can directly solve this problem through "brute force search + pruning".

We design a function dfs(l,r,t), where l and r represent the number of left and right brackets respectively, and t represents the current bracket sequence. 

Then we can get the following recursive structure:

• If l>n or r>n or l<r, then the current bracket combination t is invalid, return directly;
• If l==n and r==n, then the current bracket combination t is valid, add it to the answer array ans, and return directly;
• We can choose to add a left bracket, and recursively execute dfs(l + 1, r, t + "(");
• We can also choose to add a right bracket, and recursively execute dfs(l, r + 1, t + ")").

The time complexity is O(2²ⁿ x n), and the space complexity is O(n).
'''

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def dfs(l:int, r:int, t:str)->None:
            if l > n or r > n or l < r:
                return
            if l == n and r == n:
                ans.append(t)
                return
            dfs(l + 1, r, t + '(')
            dfs(l, r + 1, t + ')')

        ans = []
        dfs(0, 0, '')
        return ans