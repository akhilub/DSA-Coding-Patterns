#Approach: DFS(Stick to DFS only)
#TC:O(n)
#SC:O(h)

'''
To find total no of edges , we calculate the height/depth of the left & right subtrees
'''

# #Defination of binary TreeNode
# class TreeNode:
#     def __init__(self,val=0,left=None,right=None):
#         self.val = val
#         self.left =left
#         self.right =right
        
class Solution:
    def diameterOfBinaryTree(self,root):
        
        def maxDepth(node):
            if node is None:
                return 0
            
            L = maxDepth(node.left)
            R = maxDepth(node.right)
            
            nonlocal ans
            ans = max(ans,L+R)
            
            return 1 + max(L,R)         
        
        ans = 0
        maxDepth(root)
        return ans
    
    

#Variation :When asked give the length of the longest path between any two nodes in a tree pasing through root
'''
ans = max(ans,L+R+1)
'''