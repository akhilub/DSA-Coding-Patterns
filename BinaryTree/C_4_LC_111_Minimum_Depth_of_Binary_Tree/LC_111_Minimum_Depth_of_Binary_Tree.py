#Approach:BFS

#Use a queue to implement breadth-first search, initially adding the root node to the queue. 
#Each time, take a node from the queue. If this node is a leaf node, directly return the current depth. If this node is not a leaf node, add all non-null child nodes of this node to the queue. Continue to search the next layer of nodes until a leaf node is found.

#The time complexity is O(n), and the space complexity is O(n). Here, n is the number of nodes in the binary tree.

class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        ans = 0
        q = deque([root])
        while q:
            ans+=1 # update 
            for _ in range(len(q)):
                node = q.popleft()

                #apply here what's is said in question i.e check if this is a leaf node
                #leaf nodes Note: A leaf is a node with no children that is why `and`
                if node.left is None and node.right is None:
                    return ans

                #traversing the tree by insert the children of current node in the queue
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)



#Approach: DFS

                

                



