'''
Problem is indirectly asking to use property of BST i.e so use the below properties to 
optimise your solution by searching only in feasible region

Properties of BST
left subtree child node values will always be less than its parent/root node
right subtree child node values will always be greater than its parent/root node
'''

#Approach:BFS
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        if not root:
            return 0
        ans = 0
        q = deque([root])
        
        while q:
            
            node = q.popleft()
            
            
            #Feasible Region
            if low<=node.val<=high:
                ans+=node.val
                
            #Applying Feasibilty Cuts
            if node.val>low and node.left:  # Explore left subtree only if current node's value is greater than low
                q.append(node.left)
            
            if node.val<high and node.right:    # Explore right subtree only if current node's value is less than high
                q.append(node.right)
        return ans  












#Approach: DFS
#Note:Observe How we have get rid of `nonlocal` `ans` using `self.ans`

class Solution:
    def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:
        def search(node):
            if not node:
                return
            #to capture required node values
            if low <= node.val <= high:
                self.ans += node.val
                search(node.left)
                search(node.right)
            #applying feasilbilty cuts by asking/forcing dfs function to search only in BST feasible region
            elif node.val < low:
                search(node.right)
            elif node.val > high:
                search(node.left)

        self.ans = 0
        search(root)
        return self.ans