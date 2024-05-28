#Approach: Recursion

#When thinking about the classic routine of recursion problems in binary trees, we consider:

# 1) Termination condition (when to terminate recursion)
# 2) Recursively process the left and right subtrees
# 3) Merge the calculation results of the left and right subtrees


#For this problem, we design a function `dfs(root)`, which returns the maximum path sum of the binary tree with `root` as the root node.

#The execution logic of the function `dfs(root)` is as follows:

#If `root` does not exist, then returns 0;

#Otherwise, we recursively calculate the maximum path sum of the left and right subtrees of `root`, denoted as `left` and `right`

#If `left` is less than 0, then we set it to 0 , similarly, if `right`is less than 0, then we set it to 0.

#Then, we update the answer with  `root.val+left+right`.Finally, the function returns `root.val + max(left,right)`.

#In the main function, we call dfs(root) to get the maximum path sum of each node, and the maximum value among them is the answer.

#The time complexity is O(n), and the space complexity is O(n). Here, n is the number of nodes in the binary tree.

class Solution:
    def maxPathSum(root):
       ans = -math.inf
        def dfs(root):
            if root is None:
                return 0

            left = max(0,dfs(root.left))

            right = max(0,dfs(root.right))

            nonlocal ans
            
            ans = max(ans,root.val+left+right)

            return root.val + max(left,right)

        dfs(root)
        return ans