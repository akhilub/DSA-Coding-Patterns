#Approach:Recursion(Stick to DFS for LCA in interviews)

#Idea
'''
The LCA of two nodes `p` and `q` in a binary tree is the lowest node in tree `T` that has both `p` and `q` as descendants (where we allow a node to be a descendant of itself).

The idea behind the solution is to recursively search for the nodes `p` and `q` in the left and right subtrees. 
There are a few cases to consider:

•If either `p` or `q` matches the current node, this node must be part of the LCA.
•If `p` and `q` are found in different subtrees of a node, this node is their LCA.
•If `p` and `q` are found in the same subtree, continue searching in that subtree for the LCA.

Base Case: If the current node is None, or if it matches either p or q, return the current node. This means we have found one of the nodes we’re looking for, or we’ve reached the end of a path without finding either, in which case we return None.

Recursive Search: The function recursively searches the left and right subtrees for `p` and `q`.

Identifying LCA:
If both left and right search calls return non-null values, it means we’ve found `p` and `q` in different subtrees of the current node. Hence, the current node is the LCA.
If only one of the search calls returns a non-null value, it means both `p` and `q` are located in the same subtree, or only one of the nodes was found. Return the non-null result.
'''


#Implementation
'''
We recursively traverse the binary tree:

If the current node is null or equals to p or q, then we return the current node;

Otherwise, we recursively traverse the left and right subtrees, and record the returned results as left and right.
If both left and right are not null, it means that p and q are in the left and right subtrees respectively, so the current node is the nearest common ancestor; 
If only one of left and right is not null, we return the one that is not null.

The time complexity is O(n), and the space complexity is ~~O(n)~~ O(h). 
Here, n is the number of nodes in the binary tree & h is the height of the binary tree.
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root is None: #if not root
            return None  #root
        
        if root ==p or root==q:
            return root
        
        left = self.lowestCommonAncestor(root.left,p,q)
        right = self.lowestCommonAncestor(root.right,p,q)
        
        if left is None: #if not left
            return right
        
        if right is None:#if not right
            return left
        
        return root


#Explanation
'''
If the root value is either p or q, then it must be the common ancestor of both p and q. Otherwise, we check recursively if the common ancestor if it is at the left tree, or if it is at right tree, otherwise, current node will be the common ancestor.
Recursive algorithm above to find the common ancestor takes O(N) time as we need to traverse the binary tree and there are N nodes. The space complexity is O(H) as we are implicitly using stack due to recursion and H in the worst case is N – considering a binary tree highly degraded/imblanced to a linked list.
'''
