# Binary Tree


## Defination

I: [1,2,3,4,5,6,null]

- Complete Binary Tree
```
           1                                        class TreeNode:
         /    \                                         def __init__(self,val=0,left=None,right=None):
        2      3                                            self.val = val
       /  \   /                                             self.left = left
      4    5  6                                             self.right = right
```


- Given a Binary Tree, we can visit the nodes in a particular order – which is called Tree Traversal.

## BINARY TREE PRE-ORDER TRAVERSAL ALGORITHM
- We visit the Node first then Recursively traverse the Left Tree and then Right Tree i.e. NLR.

```
def preOrder(root):
    if root is None:
        return
    print(root.val) # visit Node
    preOrder(root.right)
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
It traverses the binary tree in level-by-level order.The implementation of a BFS is usually based on queue:

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

- Just Another way of implementation Using a stack or basically a list
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








# Binary Search Tree

## Defination 

L<N<R

Input : [2,1,3,0,1.5,2.5,4]

```
               2
            /     \
          1        3
        /  \      /  \
       0   1.5   2.5  4
```

In a BST 
### preorder traversal    i.e NLR   

### inorder traversal     i.e LNR  0,1,1.5,2,2.5,3,4
- gives elements in sorted order from smallest to largest

### postorder traversal   i.e RLN

### reverseInorder traversal i.e RNL 4,3,2.5,2,1.5,1
- gives elements in reverse sorted order from largest to smallest 
