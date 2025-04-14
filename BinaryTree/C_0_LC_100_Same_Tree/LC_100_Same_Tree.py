#Approach:DFS
#TC:O(n)
#SC:O(h)

'''
We can use the DFS recursive method to solve this problem.

First, determine whether the root nodes of the two binary trees are the same. 
If both root nodes are null, then the two binary trees are the same. 
If only one of the root nodes is null, then the two binary trees are definitely different. 
If both root nodes are not null, then determine whether their values are the same. 
If they are not the same, then the two binary trees are definitely different. 
If they are the same, then determine whether the left subtrees of the two binary trees are the same and whether the right subtrees are the same.
The two binary trees are the same only when all the above conditions are met.

The time complexity is O(min(m,n)), and the space complexity is O(min(m,n)). Here, 
m and n are the number of nodes in the two binary trees, respectively. 

The space complexity mainly depends on the number of layers of recursive calls, which will not exceed the number of nodes in the smaller binary tree.

'''




# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p==q:                                                                        #Step 3
            return True 
        if not p or not q or p.val!=q.val:                                              #Step 2
            return False
        return self.isSameTree(p.left,q.left) and self.isSameTree(p.right,q.right)      #Step 1


#Another way of writing DFS
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        if not p or not q:
            return False
        if p.val!=q.val:
            return False
        return self.isSameTree(p.left,q.left) and self.isSameTree(p.right,q.right)



#Another way of writing DFS
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p or not q:
            return p==q # covers: p=none and q!=none, q=none and p!=none, both none
        return p.val==q.val and self.isSameTree(p.left,q.left) and self.isSameTree(p.right,q.right)
    































































































    
#Appoach BFS
#Lengthy ,dont go for it not required, 
#Writing just for the sake of completness

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p is None:                  #if not p:
            return q is None               #return not q

        if q is None:                  #if not q:
            return p is None                #return not p

        q1 = deque([p])                 #stk1 = [p]
        q2 = deque([q])                 #stk2 = [q]

        while q1 and q2:                #while stk1 and stk2:
            node1 = q1.popleft()            #node1 = stk1.pop()
            node2 = q2.popleft()            #node2 = stk2.pop()

            if node1 is None and node2 is None:
                continue
            elif node1 is None or node2 is None:
                return False
            elif node1.val != node2.val:
                return False

            q1.append(node1.left)           #stk1.append(node1.left)
            q2.append(node2.left)           #stk2.append(node2.left)

            q1.append(node1.right)          #stk1.append(node1.right)
            q2.append(node2.right)          #stk2.append(node2.right)

        return not q1 and not q2        #return not stk1 and not stk2