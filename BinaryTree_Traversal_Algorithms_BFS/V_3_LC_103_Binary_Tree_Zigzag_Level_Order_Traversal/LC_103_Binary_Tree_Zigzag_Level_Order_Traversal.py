#Approach: BFS

# To implement zigzag level order traversal, we need to add a flag `left` on the basis of level order traversal. This flag is used to mark the order of the node values in the current level. If left is true, the node values of the current level are stored in the result array ans from left to right. If left is false, the node values of the current level are stored in the result array ans from right to left.

# The time complexity is O(n), and the space complexity is O(n) Here, n is the number of nodes in the binary tree.

class Solution:
    def zigzagLevelOrder(self,root):
        ans = []
        if not root:
            return ans
        q = deque([root])
        left = True
        while q:
            cur = []
            for _ in range(len(q)):
                node = q.popleft()
                cur.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

            ans.append(cur if left else cur[::-1])
            left = (not left)

        return ans
                











#Another logic 
#For the Zig-Zag, we can just reverse the rows of the even numbers in the ans Using Bitwise AND operator to check whether the row is odd or even
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans = []
        if not root:
            return ans
        q = deque([root])
        while q:
            cur =[]
            for _ in range(len(q))
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            
            #problem logic
            if len(ans)&1: #odd <----- if the next row is even number, we reverse it
                ans.append(cur[::-1])
            else:
                ans.append(cur)
            
        return ans


