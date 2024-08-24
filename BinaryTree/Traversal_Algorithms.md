# Binary Tree

## Validity
To check whether a binary tree is a full binary tree we need to test the following cases:-

- If a binary tree node is NULL then it is a full binary tree. 
- If a binary tree node does have empty left and right sub-trees, then it is a full binary tree by definition. 
- If a binary tree node has left and right sub-trees, then it is a part of a full binary tree by definition. In this case recursively check if the left and right sub-trees are also binary trees themselves. 
- In all other combinations of right and left sub-trees, the binary tree is not a full binary tree.


## Defination

I: [1,2,3,4,5,6,null]

- Complete Binary Tree

```
class TreeNode:
    def __init__(self,val=0,left=None,right=None):
        self.val = val
        self.left = left
        self.right = right
```

```
           1                                       
         /    \                                         
        2      3                                            
       /  \   /                                             
      4    5  6                                             
```


- Given a Binary Tree, we can visit the nodes in a particular order – which is called Tree Traversal.

## BINARY TREE PRE-ORDER TRAVERSAL ALGORITHM
- We visit the Node first then Recursively traverse the Left Tree and then Right Tree i.e. NLR.

```
def preOrder(root):
    if root is None:
        return
    print(root.val) # visit Node
    preOrder(root.left)
    preOrder(root.right)
```
- The NLR of above tree is: 1,2,4,5,3,6



## BINARY TREE IN-ORDER TRAVERSAL ALGORITHM
- We recursively traverse the left tree, and then visit the node, and then traverse recursively the right tre i.e. LNR.
```
def inOrder(root):
    if root is None:
        return
    inOrder(root.left)
    print(root.val) # visit Node
    inOrder(root.right)
```
- The LNR of above tree is: 4,2,5,1,6,3




## POST ORDER TRAVERSAL ALGORITHM FOR BINARY TREE
The post-order traversal visits the nodes in LRN order, which is recursively visiting left tree, then right tree, and visit the node last.
```
def postOrder(root):
    if root is None:
        return
    postOrder(root.left)
    postOrder(root.right)
    print(root.val) # visit Node
```
- The LRN of above tree is: 4,5,2,6,null,3,1


## BINARY TREE REVERSE IN-ORDER TRAVERSAL ALGORITHM
The reverse in-order visits the nodes in RNL that is recursively traversing right tree, then visit node, then recursively traversing the left tree.
```
def reverseInorder(root):
    if root is None:
    reverseInOrder(root.right)
    print(root.val) #visit node
    reverseInOrder(root.left)
```
- The RNL of above tree is: 3,6,1,4,2,5




## Level-By-Level Traversal or BFS traversal
It traverses the binary tree in level by level order, and each level from left to right..The implementation of a BFS is usually based on queue:

```
def bfs(root):                                                      
    if root is None:                                                
        return
    q = deque([root])
    while q:
        p = q.popleft()
        print(node.val) #visit node
        if p.left:
            q.append(p.left)
        if p.right:
            q.append(p.right)
```
- The BFS or Level-By-Level of above tree is: 1,2,3,4,5,6

- Just Another way of implementation Using a stack/basically a list

```
def bfs(root):
    if root is None:
        return
    q = [root]
    while q:
        p = pop(0)
        print(node.val) #visit node
        if p.left:
            q.append(p.left)
        if p.right:
            q.append(p.right)

```


### All Binary Tree Traversal Algorithms run at O(N) time and O(N) space (due to recursion/stack or queue).





### Some Useful Definations related to Binary Trees

- A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.



- The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.



- The length of a path between two nodes is represented by the number of edges between them.













