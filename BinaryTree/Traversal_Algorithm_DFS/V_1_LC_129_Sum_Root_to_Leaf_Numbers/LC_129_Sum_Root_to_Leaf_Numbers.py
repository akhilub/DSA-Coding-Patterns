#Approach: DFS Recursion

# We can design a function `dfs(root,s)`, which represents the sum of all path numbers from the current node to the leaf nodes, given that the current path number is `s`. 
# The answer is `dfs(root,0)`.

# The calculation of the function dfs(root,s) is as follows:

# If the current node is null, return 0.
# Otherwise, add the value of the current node to s, i.e. s = s*10 + root.val.
# If the current node is a leaf node, return s.
# Otherwise, return dfs(root.left,s) + dfs(root.right,s).

# The time complexity is O(n), and the space complexity is log(n). Here, n is the number of nodes in the binary tree.


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        def dfs(root,s):
            #terminate dfs
            if not root:
                return 0
            
            #logic for making the number of the node down the path 
            s=s*10+root.val
            
            #reached leaf node 
            if not root.left and not root.right:
                return s
            
            #traverse the left branch & right branch when finished exploring add up both the subtrees total
            return dfs(root.left,s) + dfs(root.right,s)
            
        
        return dfs(root,0)


# Another way of writing
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        ans = []
        def dfs(root,path):
            #terminate dfs
            if not root:
                return 
            
            #logic for making the number of the node down the path 
            path.append(str(root.val))
            
            #reached leaf node 
            if not root.left and not root.right:
                ans.append(int(''.join(path[:])))
            
            #traverse the left subtress & right subtress
            dfs(root.left,path)
            dfs(root.right,path)
            path.pop()
            
        dfs(root,[])
        return sum(ans)