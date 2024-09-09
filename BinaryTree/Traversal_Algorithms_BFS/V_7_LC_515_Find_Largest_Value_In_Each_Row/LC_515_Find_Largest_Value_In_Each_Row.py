# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []

        ans = []
        q = deque([root])
        while q:
            path = []                       #mx = -math.inf
            for _ in range(len(q)):
                node = q.popleft()
                path.append(node.val)       #mx = max(mx,node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            ans.append(max(path))           #ans.append(mx)
        return ans