#Approach BFS

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

#TC:O(n)
#SC:O(n)
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        ans = []
        q = deque([root])
        while q:
           cur = [] #current level
            for _ in range(len(q)):
                node = q.popleft()
                cur.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            ans.append(sum(cur)/len(cur))
        return ans


#TC:O(n)
#SC:O(1)
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        ans = []
        q = deque([root])
        while q:
            s , n = 0 , len(q) #levelSum,levelSize
            for _ in range(n):
                node = q.popleft()
                s+=node.val
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            ans.append(s/n)
        return ans




