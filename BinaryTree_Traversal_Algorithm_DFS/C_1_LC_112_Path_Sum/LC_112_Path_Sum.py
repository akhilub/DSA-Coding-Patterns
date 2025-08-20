#Approach: DFS Recursion

#Starting from the root node, recursively traverse the tree and update the value of the node to the path sum from the root node to that node. 
#When you traverse to a leaf node, determine whether this path sum is equal to the target value. If it is equal, return true, otherwise return false.

#TC:O(n) where n is the number of nodes in the binary tree. Each node is visited once.
#SC: O(h) h is the height of the binary tree

#In the worst case, h=n when each node in binary tree has only one child or O(LogN) when the given binary tree is highly balance: the different between any child nodes is no more than one.

class Solution:
    def hasPathSum(self,nums):

        def dfs(root,curSum):
            if root is None:
                return False
            
            #adding the path node value in curSum
            curSum+=root.val

            #check if reached leaf node
            if root.left is None and root.right is None:
                if curSum == targetSum:
                    return True

            #traverse the tree revcursively on left or right branches with their path sum
            return dfs(root.left,curSum) or dfs(root.right,curSum) 

        return dfs(root,0)


#Approach :DFS Iterative

#Approach :BFS

#No need to do them they are covered in other problems and topics 