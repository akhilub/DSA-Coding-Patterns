#Approach 1:BFS

#The approach is the same as in 102. Binary Tree Level Order Traversal, just reverse the result in the end.

class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans =[]
        if root is None:
            return ans
        q = deque([root])
        while q:
            t = [] #to capture elements in the current level
            for _ in range(len(q)):
                node = q.popleft()
                t.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            ans.append(t)
        return ans[::-1]