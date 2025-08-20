#Approach 1:BFS

# We can use the BFS method to solve this problem. First, enqueue the root node, then continuously perform the following operations until the queue is empty:
# Traverse all nodes in the current queue, store their values in a temporary array `t`, and then enqueue their child nodes.
# Store the temporary array `t` in the answer `ans` array.
# Finally, return the answer `ans` array.

# The time complexity is O(n) and the space complexity is O(n).Here, n is the number of nodes in the binary tree.


# Definition for a binary tree node.
from typing import Optional,List
from collections import deque
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans =[]
        if root is None:
            return ans
        q = deque([root])
        while q:
            t = []                      #t-traversal order
            for _ in range(len(q)):     #len(q) -  Number of nodes at the current level
                node = q.popleft()
                t.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            ans.append(t)
        return ans
    
    
    
    
    
    #To Print Each Level of binary tree
    '''
    Replace

    `ans.append(t)`

    with

    `print(" ".join(map(str,t)))`
    '''
    
    
    def print_levels(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return None
        q = deque([root])
        while q:
            l = []
            for i in range(len(q)):
                # Dequeue the front node
                node = q.popleft()
                l.append(node.val)
                # Enqueue child nodes
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

            # Print the current level
            print(' '.join(map(str,l)))
        return

def bfs()





    
    
if __name__ == "__main__":
    # Creating a sample binary tree
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(7)
    
    
    print('Level Order Traversal')
    print(Solution().levelOrder(root))

    print("Levels of Binary Tree:")
    Solution().print_levels(root)