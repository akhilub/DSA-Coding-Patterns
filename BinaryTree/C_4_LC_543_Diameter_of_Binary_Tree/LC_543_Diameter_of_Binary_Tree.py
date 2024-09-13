#Write this in interviews    
#Optimized Solution
#TC:O(N)
#SC:O(N)

'''
We can calculate both the depth and the diameter in a single traversal of the tree. 
This reduces the time complexity from O(N^2) to O(N), where N is the number of nodes in the tree.
'''

class Solution:
    def diameterOfBinaryTree(self,root):
        def dfs(node):
            if node is None:    #terminal condition/ when to stop tree traversal
                return 0 , 0    #(depth,diameter)
            
            L_depth, L_dia = dfs(node.left)
            R_depth, R_dia = dfs(node.right)
            
            #Current depth
            C_depth = 1+max(L_depth,R_depth)
            
            #Diameter passing through the current node
            C_dia = L_depth + R_depth
            
            #Maximum diameter found so far
            max_dia = max(C_dia,L_dia,R_dia)
            
            return C_depth,max_dia
        
        _ , dia = dfs(root)
        return dia



#Approach2:TLE because TC is O(N^2) since we are calculating depth and dia in two separate traversal of tree

class Solution:
    def diameterOfBinaryTree(self,root):
        def maxDepth(node):
            if node is None:
                return 0
            
            L = maxDepth(node.left)
            R = maxDepth(node.right)            
            
            return 1+max(L,R)
            
        
        def calculateDiameter(node):
            if node is None:    #terminal condition
                return 0
            
            L = maxDepth(node.left)  # left subtree max Depth
            R = maxDepth(node.right) # right subtree max Depth
            
            diameter = L + R        # diameter passing through the current node (`L + R`).
            
            L_dia = calculateDiameter(node.left) # diameter of the left subtree (`L_dia`)
            R_dia = calculateDiameter(node.right) # diameter of the right subtree (`R_dia`)
            
            return max(diameter,L_dia, R_dia)
            
            
        return calculateDiameter(root)





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

#Short Answer       
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





    


            
            