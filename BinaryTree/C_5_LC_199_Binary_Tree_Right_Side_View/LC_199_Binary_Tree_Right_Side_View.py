#Approach 1:BFS
#We use the queue (aka deque in Python) to implement the BFS (Breadth First Search Algorithm). 
#We deque (pop) all elements in current queue at once and push their kids back to the queue, 
#thus we know at any time, the nodes in the queue belong to the same level.


#RIGHT SIDE VIEW OF A BINARY TREE USING BREADTH FIRST SEARCH ALGORITHMS

#We take the rightmost (right side view) aka q[-1] and push to the answer.


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        if root is None:
            return ans
        
        q = deque([root])
        while q:
            ans.append(q[-1].val)           # add last node of previous level traversal results
            for _ in range(len(q)):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
        return ans


    

#Left SIDE VIEW OF A BINARY TREE USING BREADTH FIRST SEARCH ALGORITHMS

#We take the rightmost (right side view) aka q[0] and push to the answer.

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
       
        if not root:
            return []
         ans = []
        q = deque([root])
        while q:
            ans.append(q[0].val)   #logic Left Side View
            for _ in range(len(q)):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
        return ans




#Approach 2:DFS