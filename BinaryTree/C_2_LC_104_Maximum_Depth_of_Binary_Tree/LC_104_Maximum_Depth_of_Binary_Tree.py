#Approach: Recursion(DFS)

#Recursive Algorithm
#If the tree is None return 0, 
#otherwise it will be the max of left the right tree value respectively plus 1  which we can recursively to get the value
 
#TC: O(N) where N is the number of nodes in BT, since each node is traversed only once in the recursion.
#SC: O(N) due to recursion

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        left = self.maxDepth(root.left)
        right = self.maxDepth(root.right)

        return 1+ max(left,right)


#Approach:BFS
#TC:O(N)
#SC:O(N)
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        ans = 0
        q = deque([root])
        while q:
            ans+=1
            for _ in range(len(q)):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
        return ans
        