#Approach : DFS Recursion
#We can follow the same DFS approach and additionally, track the element of the given sequence that we should match with the current node. Also, we can return false as soon as we find a mismatch between the sequence and the node value.

#TC:O(n)
#SC:O(n)
class Solution:
    def isValidSequence(self, root: TreeNode, arr: List[int]) -> bool:
        ans = []
        def dfs(root,path):
            if not root:
                return 

            path.append(root.val)

            if not root.left and not root.right:
                ans.append(path[:])
        
            dfs(root.left,path)
            dfs(root.right,path)
            path.pop()

        dfs(root,[])
        return True if arr in ans else False



#Approach : DFS Recursion
#TC:O(n)
#SC:O(n) The space complexity of this algorithm will be O(n) in the worst case. This space will be used to store the recursion stack. The worst case will happen when the given tree is a linked list

#class TreeNode:
#  def __init__(self, val, left=None, right=None):
#    self.val = val
#    self.left = left
#    self.right = right

class Solution:
  def isValidSequence(self, root, sequence):
    def dfs(root,idx):
      if not root:
        return False

      #logic for matching the sequence ele with root node within the idx
      if idx<len(sequence) and root.val!=sequence[idx]:
        return False

      #reached leaf node
      if root.left is None and root.right is None:
        if idx == len(sequence)-1: #Apply question condition
          return True
      
      #traverse the trees path
      return dfs(root.left,idx+1) or dfs(root.right,idx+1)
      
    return dfs(root,0)




#Approach : DFS Recursion
#TC:O(n)
#SC:O(h)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidSequence(self, root: TreeNode, arr: List[int]) -> bool:
        def dfs(root, idx):
            if root is None or root.val != arr[idx]:
                return False
            if idx == len(arr) - 1:
                return root.left is None and root.right is None
            return dfs(root.left, idx + 1) or dfs(root.right, idx + 1)

        return dfs(root, 0)
