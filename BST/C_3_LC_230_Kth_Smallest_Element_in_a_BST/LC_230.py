'''
We can leverage the properties of a binary search tree (BST).
A binary search tree has the property that an in-order traversal (left -> root -> right) will yield the node values in sorted order.

we can find the kth smallest element directly during the traversal.

Optimized Approach
By performing an in-order traversal and stopping as soon as we reach the kth smallest element, we can reduce space complexity and time complexity.


Algorithm:
1.Perform an in-order traversal of the tree.
2.Keep a counter that increments/decrements each time we visit a node.
3.Once the counter equals k/0, return that node's value as the result.
'''
#TC:O(H+k), where 𝐻 is the height of the tree
#SC:O(H)






# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        self.k = k
        self.ans = None
        
        def inOrder(node):
            if not node:
                return
            # Traverse left subtree
            inOrder(node.left)
            
            # Process the current node
            self.k -= 1
            if self.k == 0:
                self.ans = node.val
                return
            
            # Traverse right subtree
            inOrder(node.right)
        
        inorder(root)
        return self.ans
    
    
#Another Way 
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        ans = []
        def inorder(node):
            if not node:
                return
            inorder(node.left)              # Traverse left subtree
            ans.append(node.val)            # Process the current node
            inorder(node.right)             # Traverse right subtree
        inorder(root)
        return ans[k-1]
    
    
    



#Approach:Max-Heap
#TC:O(Nlog(k)),N-nodes
#SC:O(k+H)    ,H-height
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        self.pq = []
        def dfs(root):
            if root is None:
                return
            
            dfs(root.left)
            
            
            heappush(self.pq,-root.val)
            if len(self.pq)>k:
                heappop(self.pq)
            
            
            dfs(root.right)
        
        
        dfs(root)    
        
        return -self.pq[0]