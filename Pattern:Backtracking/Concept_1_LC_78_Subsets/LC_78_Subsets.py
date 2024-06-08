#nums = [1,2,3]
#
#           nums[i]
#            /   \
#          pick  skip
#


#Approach
#For each number we have two choices :include or skip in the subset
#Thus the total number of subsets is 2^N for N unique elements
#The following recursion is easy to understans.It takes two parameters the current subset and the ith number we are looking at now.
#The terminal condition of Recursion is that:
#     - when we reach the end (running out of numbers) we have one subset which we can copy to the list of anwsers 
#     - O/w we have two choices include this number or skip it
#And we can call the recursion backtracking respectively.



#As the Python uses Object-References when passing parameters the list (mutable ) is passed by Reference,
#we need to make a deep copy (using copy.deepcopy(cur) or cur[:]) to copy the current subset e.g cur to answer (list of all subsets)

# Syntax of Python Deepcopy
# Syntax: copy.deepcopy(x)

# Syntax of Python Shallowcopy
# Syntax: copy.copy(x)


class Solution:
    def subsets(self,nums):
        ans = []
        n = len(nums)
        def backtrack(cur,i):
            if i == n:
                ans.append(cur[:])     #ans.append(copy.deepcopy(cur))  # cur[:] means shallow copy of cur
                return 
            #pick
            backtrack(cur+[nums[i]],i+1)
            #skip
            backtrack(cur,i+1)

        backtrack([],0)
        return ans
        
#My Approach 2) DFS
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        def dfs(s: int, path: List[int]) -> None:
            ans.append(path)

            for i in range(s, len(nums)):
                dfs(i + 1, path + [nums[i]])

        dfs(0, [])
        
        return ans

# ans = [[],[1],[1,2],[1,2,3],[1,3],[2],[2,3],[3]]
#
#   s=0             path <---[    ]
#                  i=0   /   i=1|   i=2  \      #for loop
#   s=1                [1]     [2]       [3]
#                     / \       |        
#   s=2            [1,2] [1,3] [2,3]      
#                   /      
#   s=3         [1,2,3] 


#Equivalent of above DFS function written in Expanded form
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        def dfs(s,path):
            ans.append(path[:]) 
            
            for i in range(s,len(nums)):
                path.append(nums[i])
                dfs(i+1,path)
                path.pop()
                
        dfs(0,[])
        return ans